---
title: "Qhawarina: Real-Time Economic Monitoring for Peru"
date: 2026-02-22
tags: ["nowcasting","dynamic factor models","poverty","inflation","GDP","Peru"]
author: "Carlos César Chávez Padilla"
description: "A comprehensive nowcasting platform for Peru's economy using dynamic factor models, daily price indices, and political risk monitoring."
summary: "Real-time monitoring system for Peru's economic indicators including GDP, inflation, poverty, and political risk using state-of-the-art econometric methods and daily data scraping."
sparkline: "/qhawarina-sparkline.svg"
sparkline_label: "Daily price index"
sparkline2: "/qhawarina-sparkline-gdp.svg"
sparkline2_label: "GDP growth (quarterly)"
cover:
    image: "qhawarina.png"
    alt: "Qhawarina Platform"
    relative: false
showToc: true
disableAnchoredHeadings: false

---

## Overview

Qhawarina is a real-time economic monitoring platform for Peru that provides nowcasts of key macroeconomic variables using dynamic factor models (DFM) and high-frequency data. The platform combines traditional monthly indicators with daily scraped data from supermarkets and news sources to provide up-to-date economic intelligence.

<div class="qh-cards">
  <div class="qh-card"><div class="qh-val">42K+</div><div class="qh-label">Products / day</div><div class="qh-sub">daily supermarket price index</div></div>
  <div class="qh-card"><div class="qh-val">+2.8%</div><div class="qh-label">GDP nowcast</div><div class="qh-sub">year-on-year &middot; beats AR(1) by 31%</div></div>
  <div class="qh-card"><div class="qh-val">2.4%</div><div class="qh-label">Inflation nowcast</div><div class="qh-sub">monthly &middot; bridge R&sup2; 0.81</div></div>
  <div class="qh-card"><div class="qh-val">24.5K</div><div class="qh-label">Articles classified</div><div class="qh-sub">political-risk index &middot; 506 days</div></div>
  <div class="qh-card"><div class="qh-val">25</div><div class="qh-label">Departments</div><div class="qh-sub">monthly poverty nowcast</div></div>
</div>
<p class="qh-note">Built in 2026 and <strong>still updating daily</strong> &mdash; the prices, inflation, GDP, and poverty pipelines refresh every day on <a href="https://github.com/cesarchavezp29/qhawarina">GitHub</a>. Only the political-risk index is paused, since it needs a news classifier to run. The code and methodology are fully open.</p>

### Live demo — daily supermarket price index

Real prices scraped every day across 42,000+ products. Base 100 = February 10, 2026; hover for any day.

<div class="qh-chart-wrap"><canvas id="qhPriceChart"></canvas></div>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script>
(function () {
  fetch('/qhawarina-prices.json').then(function (r) { return r.json(); }).then(function (d) {
    var el = document.getElementById('qhPriceChart');
    if (!el || !window.Chart) return;
    new Chart(el, {
      type: 'line',
      data: { labels: d.dates, datasets: [
        { label: 'All items', data: d.all, borderColor: '#7a1f2b', backgroundColor: 'rgba(122,31,43,0.07)', fill: true, tension: 0.25, pointRadius: 0, borderWidth: 2 },
        { label: 'Food', data: d.food, borderColor: '#1a2c54', fill: false, tension: 0.25, pointRadius: 0, borderWidth: 1.5 }
      ]},
      options: {
        responsive: true, maintainAspectRatio: false,
        interaction: { mode: 'index', intersect: false },
        plugins: { legend: { labels: { boxWidth: 14, font: { size: 12 } } } },
        scales: { x: { ticks: { maxTicksLimit: 8, maxRotation: 0 } }, y: { title: { display: true, text: 'Index (base 100)' } } }
      }
    });
  });
})();
</script>

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
