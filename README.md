📊 Project Overview  
This repository contains the full workflow for constructing the Global Financial Sentiment Index, a synthetic indicator designed to capture global public attention to uncertainty, panic, market stress and financial risk. The index is constructed using Google Trends data and a curated list of financial search terms, to which Principal Component Analysis is applied.
The international financial environment has become increasingly sensitive to geopolitical tensions, commodity market volatility and rapid shifts in public perception. This project provides a fast, flexible and data‑driven tool for monitoring global financial sentiment using online search behavior.

🔍 Key Findings  
The Global Financial Sentiment Index is a PCA‑based indicator constructed from worldwide Google search activity on financial terms. The index relies on a curated list of 23 financial terms selected through correlation filtering and aggregates monthly data for the period February 2004 - June 2026, after applying Principal Component Analysis. The first principal component explains 48% of total variance - unusually high for Google Trends data. Monthly index values are classified into positive and negative shocks. The dynamics of the oil market dominate the evolution of the index, as the PCA loading for the term “oil price” is 0.9963. This is why negative shocks correspond to sharp declines in oil prices, while positive shocks reflect spikes in perceived risk on the oil market. The index successfully identifies major geopolitical and energy‑related shocks.

📁 Repository Structure  
/src – Python scripts for data extraction, correlation matrix, normalization, PCA computation and shock classification.  
/docs – introduction, methodology, empirical results and appendices.

🚀 Reproducibility  
All steps are fully automated in Python.  
The repository includes:  
• complete dataset in CSV format  
• correlation matrix  
• results of the Principal Component Analysis  
• chart with the values of the Global Financial Sentiment Index  
• shock classification tables  
• full codebase.
