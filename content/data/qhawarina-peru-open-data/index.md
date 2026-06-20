---
title: "Qhawarina — Peru Open Economic Data"
date: 2026-03-01
tags: ["Peru","nowcasting","open data","political risk","inflation","GDP","poverty","price index"]
author: "Carlos César Chávez Padilla"
description: "Daily open data for Peru: a supermarket price index, a news-based political-risk index, a quarterly-GDP nowcast, and a monetary-poverty projection. CC BY 4.0."
summary: "The open datasets behind the Qhawarina nowcasting platform — a daily supermarket price index, a daily news-based political-risk (instability) index for Peru, a GDP nowcast, and a poverty projection — with a full methodology document. Updated daily, CC BY 4.0."
editPost:
    URL: "/qhawarina-methodology.pdf"
    Text: "Methodology (PDF)"

---

---

##### Access

+ [Methodology document (PDF)](/qhawarina-methodology.pdf)
+ [Code and daily data on GitHub](https://github.com/cesarchavezp29/qhawarina)
+ [Project overview](/papers/) and the [Qhawarina project page](/projects/qhawarina/)

---

##### What this is

The open data behind **Qhawarina**, a real-time economic-monitoring platform for Peru. Four indicators are produced and published daily under an open license:

- **Daily price index** — a Billion-Prices-style supermarket inflation index built from 42,000+ products scraped daily, chain-linked with the Jevons formula.
- **Political-risk index** — a daily, news-based measure of the intensity of political instability in Peru, classified from 81 Peruvian news sources with an EPU-style severity weighting. This is the political-instability measure for Peru.
- **GDP nowcast** — a dynamic factor model over 35+ monthly indicators, with regional disaggregation.
- **Monetary-poverty projection** — a monthly department-level estimate combining survey data and nighttime lights.

The `qhawarina-methodology.pdf` documents the formulas, data sources, assumptions, validation, and known limitations for each indicator.

---

##### Sources and license

Built from public sources (BCRP, INEI, MIDAGRI, supermarket VTEX APIs, Peruvian news RSS feeds, VIIRS nighttime lights). Released under **CC BY 4.0**. All code is open at [github.com/cesarchavezp29/qhawarina](https://github.com/cesarchavezp29/qhawarina).

##### Citation

Chávez Padilla, Carlos César. 2026. "Qhawarina — Nowcasting Económico para el Perú (Documento Metodológico), v1.0."
