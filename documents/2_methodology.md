1. Data description

I downloaded monthly data from Google Trends for the period January 2004 – June 2026. The data consist of time series reflecting the relative volume of online searches for various financial terms at the global level. For this scientific study, I selected financial terms formulated in English, relevant for the global perception of financial risk, uncertainty, panic, and volatility. The data are normalized by Google and scaled from 0 to 100, meaning that the values represent a relative interest index, not absolute search volumes on the Google search engine.

The dataset was automatically extracted from Google Trends using the Python programming language. Initially, I tested 39 financial terms using the Pearson correlation, and then retained only 23 keywords for constructing the Global Financial Sentiment Index. For a robust index, it is recommended to use between 15 and 25 terms, combined from all categories of financial interest, allowing the simultaneous capture of public attention toward financial risks, developments in energy markets, and global macroeconomic dynamics. The terms included in the analysis are fully presented in Appendix 1.

2. Selection of financial terms used in constructing the Global Financial Sentiment Index

The correlation analysis of the financial terms in the initial dataset played a crucial role in establishing the robustness of the principal component analysis and in avoiding informational redundancy. Since Google Trends provides normalized series with very different levels of variability across terms, evaluating correlations made it possible to identify the variables that effectively contribute to the common variation of global financial sentiment.

The correlation results highlighted the presence of several terms with very low average correlations (below 0,2), such as “deflation,” “unemployment,” “credit crunch,” “sovereign debt crisis,” “war,” “terrorism,” and “panic.” These terms were removed because they do not exhibit a statistically significant relationship with the other variables and do not contribute to capturing a common latent factor. Terms such as “economic growth” and “recession” generated unstable values after normalization due to extremely low variation, which led to infinite values when computing percentage changes. To maintain the stability of the principal component analysis, these terms were excluded.

The correlation analysis also allowed the identification of highly redundant terms with correlation coefficients above 0,8. For example, “stock market crash” shows a correlation of 0.84 with “market crash,” while “market sentiment” and “investor sentiment” have correlations above 0.9 with “volatility.” In such cases, the terms were removed to avoid duplicating information and over‑representing the same conceptual dimension within the principal component analysis.

Similarly, terms such as “VIX” and “fear index” were excluded because they are technical indicators specific to the U.S. market, with very high correlations relative to keywords such as “interest rate” or “volatility,” which would have introduced a geographic bias into the global index.

Following the filtering process, the final set of variables includes only terms that exhibit relevant correlations, adequate variability, and conceptual significance for analyzing financial sentiment at the global level. This rigorous selection enabled a stable principal component analysis, in which the loading structure clearly highlights the dominance of the term “oil price,” confirming the central role of energy markets in shaping global risk perception.

3. Principal Component Analysis

For each financial term, the monthly values of global interest were collected, then normalized (z‑score) and transformed into percentage changes in order to capture the dynamics of financial sentiment rather than the static level of attention, since this index measures sudden increases in interest for these financial terms.

The principal component analysis was applied to a matrix containing the percentage changes for the 23 financial terms presented in the appendix. This technique reduces data dimensionality, identifies the common latent factor, and extracts the principal component that explains the largest share of variation in the dataset.

The first principal component represents the Global Financial Sentiment Index. Positive values indicate an increase in perceived financial risk (a negative shock), while negative values indicate a risk reduction (a positive shock). Large positive values reflect geopolitical tensions, wars, sanctions, energy crises, and panic in financial and commodity markets. Large negative values correspond to declines in oil prices, easing geopolitical tensions, market recovery, and rising confidence. Small values of the index capture periods of calm and stability. The Global Financial Sentiment Index typically ranges between –2 and +2, which is the most frequently observed interval.

To ensure reproducibility and data consistency, I designed an automated Python workflow that extracted the selected terms from Google Trends, normalized the monthly data, and computed percentage changes. The principal component analysis is applied to the 23 financial terms. The values of the Global Financial Sentiment Index are automatically classified into positive and negative shocks and saved in a report. The chart is generated automatically. The full code is included in the appendix.

The final dataset covers the period February 2004 – June 2026. To identify shocks, the values of the Global Financial Sentiment Index were classified as follows, allowing the association with real events presented in the appendix:  
• moderate positive shock: < –2  
• severe positive shock: < –3  
• extreme positive shock: < –4  
• moderate negative shock: > +2  
• severe negative shock: > +3  
• extreme negative shock: > +4
