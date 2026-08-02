import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FixedLocator
from sklearn.decomposition import PCA

# 1. Importul datelor din CSV
df = pd.read_csv("google_trends_data.csv", parse_dates=["date"], index_col="date")

# 2. Lista termenilor selectati pentru indexul de sentiment financiar
selected_terms = [
    "GDP",
    "inflation",
    "interest rate",
    "exchange rate",
    "financial crisis",
    "banking crisis",
    "liquidity crisis",
    "market crash",
    "bear market",
    "volatility",
    "stock market",
    "equities",
    "bonds",
    "commodities",
    "oil price",
    "gold price",
    "sanctions",
    "oil shock",
    "uncertainty",
    "risk aversion"
]

# 3. Selecteaza doar coloanele dorite
df_selected = df[selected_terms]
# print(df_selected.head())

# 4. Cum apare data? 27 aprilie 2026 va aparea '2026-04-27'.
# print(df_selected.index)

# 5. Normalizare (z-score) pentru fiecare cuvant cheie (serie de timp)
df_z = (df_selected - df_selected.mean()) / df_selected.std(ddof=1)

# 6. Transformarea în variații procentuale (rate of change)
df_pct = df_z.pct_change().dropna()



# 7. PCA pentru agregarea intr-un singur index
pca = PCA(n_components=1)
sentiment_index = pca.fit_transform(df_pct)

# 8. Convertim rezultatul intr-o serie Pandas
sentiment_index = pd.Series(sentiment_index.flatten(), index=df_pct.index, name="sentiment_index")

# 9. Normalizare finală a indexului (optional, dar recomandat)
sentiment_index = (sentiment_index - sentiment_index.mean()) / sentiment_index.std(ddof=1)

# 10. Salvare rezultat
sentiment_index.to_csv("sentiment_index.csv")
# print(sentiment_index.head())



# 11. Varianta explicata de PCA
print("Explained variance ratio:", pca.explained_variance_ratio_)

# 12. Valorile proprii
print("Eigenvalues:", pca.explained_variance_)

# 13. Vectorul propriu (loadings)
loadings = pd.Series(
    pca.components_[0],
    index=df_pct.columns,
    name="PCA_Loadings"
)
print(loadings)



# 14. Selectare date pentru indexul de sentiment financiar 
index_df = pd.read_csv("sentiment_index.csv")

index_df["date"] = pd.to_datetime(index_df["date"], format="%Y-%m-%d", errors="raise")

index_df = index_df.set_index("date")


# 15. Definirea pragului pentru socuri negative si pozitive

def classify_shock(value):
    # Socuri negative (scaderi ale pretului petrolului, calmarea tensiunilor, revenirea pietelor, cresterea increderii)
    if value < -4:
        return "extreme_shock_positive"
    elif value < -3:
        return "severe_shock_positive"
    elif value < -2:
        return "moderate_shock_positive"

    # Socuri pozitive (razboaie, sanctiuni, crize energetice, tensiuni geopolitice, panica pe pietele de marfuri)
    elif value > 4:
        return "extreme_shock_negative"
    elif value > 3:
        return "severe_shock_negative"
    elif value > 2:
        return "moderate_shock_negative"

    # Zona normala
    else:
        return "normal"


index_df["shock_type"] = index_df["sentiment_index"].apply(classify_shock)
mod_neg = index_df[index_df["shock_type"] == "moderate_shock_negative"]
sev_neg = index_df[index_df["shock_type"] == "severe_shock_negative"]
ext_neg = index_df[index_df["shock_type"] == "extreme_shock_negative"]

mod_pos = index_df[index_df["shock_type"] == "moderate_shock_positive"]
sev_pos = index_df[index_df["shock_type"] == "severe_shock_positive"]
ext_pos = index_df[index_df["shock_type"] == "extreme_shock_positive"]

# print(index_df[["sentiment_index", "shock_type"]].head(5))



### 16. Grafic cu evidentiere automata a socurilor
plt.figure(figsize=(12,5))

# Linia principala
plt.plot(index_df.index, index_df["sentiment_index"], linewidth=2, color="black", label="Financial Sentiment Index")

# Socuri pozitive si moderate
plt.scatter(mod_pos.index, mod_pos["sentiment_index"], color="cornflowerblue", s=20, label="Moderate positive shocks")

# Socuri pozitive si severe
plt.scatter(sev_pos.index, sev_pos["sentiment_index"], color="blue", s=20, label="Severe positive shocks")

# Socuri pozitive si extreme
plt.scatter(ext_pos.index, ext_pos["sentiment_index"], color="darkblue", s=20, label="Extreme positive shocks") 

# Socuri negative si moderate
plt.scatter(mod_neg.index, mod_neg["sentiment_index"], color="yellow", s=20, label="Moderate negative shocks")

# Socuri negative si severe
plt.scatter(sev_neg.index, sev_neg["sentiment_index"], color="orange", s=20, label="Severe negative shocks")

# Socuri negative si extreme
plt.scatter(ext_neg.index, ext_neg["sentiment_index"], color="red", s=20, label="Extreme negative shocks") 

# Etichete pentru socuri pozitive si extreme
for idx, row in ext_pos.iterrows():
    plt.text(idx + pd.Timedelta(days=1),
             row["sentiment_index"],
             f"{row['sentiment_index']:.2f}",
             color="navy", fontsize=10, va="top")

# Etichete pentru socuri negative si extreme
for idx, row in ext_neg.iterrows():
    plt.text(idx + pd.Timedelta(days=1),
             row["sentiment_index"],
             f"{row['sentiment_index']:.2f}",
             color="red", fontsize=10, va="bottom")

# Linie zero
plt.axhline(0, color="gray", linestyle="--", linewidth=0.7)

# Titluri
plt.title("Global Financial Sentiment Index using Principal Component Analysis \nconstructed from Google search activity on financial terms", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Monthly values", fontsize=14)

# Grid discret
plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.7)


## Axa X - o eticheta la 12 luni
# Generarea manuala a tick-urilor in ianuarie pentru fiecare an (primul tick 2004-01-01, desi datele incep cu februarie 2004)
years = np.arange(2004, 2027)  # 2004–2026
ticks = [pd.Timestamp(f"{year}-01-01") for year in years]

# Convertim tick-urile din Timestamp in format numeric Matplotlib
ticks_num = mdates.date2num(ticks)

# Etichete rotite la 45 grade
plt.xticks(rotation=45)

# Setarea manuala a tick-urilor (acum sunt numere, nu Timestamp)
plt.gca().xaxis.set_major_locator(FixedLocator(ticks_num))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%Y'))

# Limitele axei X (ianuarie 2004 - ianuarie 2026)
plt.xlim(pd.Timestamp("2004-01-01"), index_df.index.max())


plt.legend()
plt.tight_layout()

# Afisarea sursei datelor si metodologiei
plt.figtext(0.02, 0.02,
    "Data source: Google Trends. \nMethodology: PCA applied to monthly percentage changes of normalized financial search terms. \nNote: The structure of the PCA loadings indicates a clear dominance of the term “oil price”, suggesting that oil market dynamics represent the main driver of global financial sentiment.",
    ha="left", fontsize=10, transform=plt.gcf().transFigure)

plt.show()
