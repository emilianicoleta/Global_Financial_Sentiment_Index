from pytrends.request import TrendReq
import pandas as pd
import numpy as np

pytrends = TrendReq(hl='en-US', tz=360)

# Lista completa de termeni
keywords = [
    "economic growth", "recession", "GDP", "inflation", "deflation",
    "unemployment", "interest rate", "exchange rate", "monetary policy", "fiscal policy",
    "financial crisis", "banking crisis", "credit crunch", "liquidity crisis",
    "sovereign debt crisis", "market crash", "stock market crash", "bear market",
    "volatility", "VIX",
    "stock market", "equities", "bonds", "commodities",
    "oil price", "gold price", "exchange rate volatility",
    "geopolitical risk", "war", "terrorism", "sanctions", "oil shock",
    "market sentiment", "investor sentiment", "fear index",
    "panic", "uncertainty", "risk aversion"
]

# Functie pentru impartirea listei in grupuri de cate 5
def chunk_list(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

# DataFrame final gol
df_all = pd.DataFrame()

# Descarcare pe grupuri
for group in chunk_list(keywords, 5):
    pytrends.build_payload(group, timeframe='2004-01-01 2026-06-30')
    data = pytrends.interest_over_time()

    if not data.empty:
        data = data.drop(columns=['isPartial'])
        df_all = pd.concat([df_all, data], axis=1)

# Eliminam duplicatele de index
df_all = df_all.loc[:, ~df_all.columns.duplicated()]

# Salvare rezultat
df_all.to_csv("google_trends_data.csv")
print(df_all.head())
