import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. un DataFrame cu termenii Google Trends
df_trends = pd.read_csv("google_trends_data.csv", parse_dates=["date"], index_col="date")

# 2. Calcularea matricii de corelatie
corr_matrix = df_trends.corr()

# 3. Salvare matrice intr-un CSV
corr_matrix.to_csv("correlation_matrix.csv")
print(corr_matrix)

# 4. Vizualizare profesionala (heatmap) fara cifre
plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=False, cmap="coolwarm", linewidths=0.5) 
plt.title("Correlation Matrix of Google Trends Keywords")
plt.show()