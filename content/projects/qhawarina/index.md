---
title: "Qhawarina: Real-Time Economic Monitoring for Peru"
date: 2026-02-22
tags: ["nowcasting","dynamic factor models","poverty","inflation","GDP","Peru"]
author: "Carlos César Chávez Padilla"
description: "A comprehensive nowcasting platform for Peru's economy using dynamic factor models, daily price indices, and political risk monitoring."
summary: "Real-time monitoring system for Peru's economic indicators including GDP, inflation, poverty, and political risk using state-of-the-art econometric methods and daily data scraping."
cover:
    image: "qhawarina.png"
    alt: "Qhawarina Platform"
    relative: false
showToc: true
disableAnchoredHeadings: false

---

## Overview

Qhawarina is a real-time economic monitoring platform for Peru that provides nowcasts of key macroeconomic variables using dynamic factor models (DFM) and high-frequency data. The platform combines traditional monthly indicators with daily scraped data from supermarkets and news sources to provide up-to-date economic intelligence.

---

## Key Features

### GDP Nowcasting
- Dynamic factor model with 35+ monthly indicators
- Regional disaggregation for 25 departments
- Rolling 7-year window to handle structural breaks
- Ridge regression bridge equations (α=1.0)

### Inflation Monitoring
- Daily price index based on Billion Prices Project methodology
- 42,000+ products from Plaza Vea, Metro, and Wong supermarkets
- Jevons bilateral chain-linked index
- 25 monthly series in DFM (BCRP, MIDAGRI, supermarket data)

### Poverty Nowcasting
- GradientBoosting regressor for 24 departments
- Monthly frequency estimates
- NTL (nighttime lights) data integration
- District-level spatial disaggregation

### Political Risk Index
- Daily RSS feed classification using Claude API with keyword fallback
- EPU-style severity-weighted methodology
- Separate political and economic instability indices
- Real-time news monitoring from 81 Peruvian sources

---

## Technical Stack

**Backend**: Python (statsmodels, scikit-learn, pandas, anthropic)
**Scraping**: VTEX API, RSS feeds, BCRP API, MIDAGRI bulletins
**Frontend**: Next.js 14, TypeScript, Tailwind CSS, Recharts
**Deployment**: GitHub Pages (data), Vercel (website)
**Automation**: Windows Task Scheduler (daily updates)

---

## Data Sources

- **BCRP**: 58 national series + 233 departmental series
- **INEI**: GDP (quarterly), CPI (monthly), Poverty (annual)
- **Supermarkets**: Daily prices via VTEX API
- **MIDAGRI**: Wholesale food prices, poultry prices
- **News**: 81 RSS feeds (El Comercio, La República, Gestión, etc.)
- **Satellite**: VIIRS nighttime lights (monthly, 2012-2024)

---

## Methodology

**DFM Specification**: Based on Giannone et al. (2008), Stock & Watson (2002)
- EM algorithm for factor extraction with PCA fallback
- Handles ragged edge via truncation (50% threshold)
- COVID-exclusion filter (2020-2021) for post-pandemic stability

**Price Index**: Cavallo & Rigobon (2016) Billion Prices Project
- Geometric mean of price ratios (Jevons formula)
- Chain-linking with daily base updates
- Extreme ratio filter: 0.5 < ratio < 2.0

**Poverty Model**: Change-prediction approach
- Predict Δpoverty_t = poverty_t - poverty_{t-1}
- GBR with dept-specific features from panel
- Beats AR(1) benchmark (Rel.RMSE=0.953)

---

## Performance

**GDP Nowcast**: RMSE=1.41pp (pre-COVID), Rel.RMSE=0.69 vs AR(1)
**Inflation Nowcast**: RMSE=0.319% vs AR(1)=0.322% (3-month MA target)
**Poverty Nowcast**: RMSE=2.54pp vs AR(1)=2.65pp
**Daily Price Index**: 12 days of data, -0.57% cumulative since Feb 10
**Political Index**: 417 days, 24,541 articles classified

---

## Links

- **Live Platform**: [qhawarina.vercel.app](https://qhawarina.vercel.app) *(placeholder - update with actual URL)*
- **GitHub**: [cesarchavezp29/qhawarina](https://github.com/cesarchavezp29/qhawarina)
- **Data Exports**: JSON files updated daily

---

## Future Work

- Incorporate commodity prices (copper, gold, zinc)
- Add employment nowcast using job postings data
- Implement MIDAS regression for mixed-frequency models
- Expand to other Latin American countries
- Add forecast evaluation dashboard

---

## References

- Cavallo & Rigobon (2016). "The Billion Prices Project", *MIT*
- Giannone, Reichlin & Small (2008). "Nowcasting", *ECB Working Paper*
- Stock & Watson (2002). "Forecasting Using Principal Components", *JASA*
