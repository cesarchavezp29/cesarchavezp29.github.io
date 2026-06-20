---
title: "The Construction Club Cartel — Reconstructed Dataset"
date: 2026-06-19
tags: ["Peru","corruption","procurement","collusion","bid-rigging","cartel","open data"]
author: "Carlos César Chávez Padilla"
description: "Tender-and-firm universe of the Peruvian road-procurement bid-rigging cartel, reconstructed from Indecopi Resolución 080-2021/CLC. Firm-level, public-source, CC BY 4.0."
summary: "78 cartelized road tenders, 32 sanctioned firms, firm roles, winners, offer-level bids with the adjudicated colluded/competitive label, fines and illicit benefit, and exposure measures."
editPost:
    URL: "/data/construction-club-cartel.zip"
    Text: "Download (ZIP)"

---

---

##### Download

+ [Dataset (ZIP, ~180 KB)](/data/construction-club-cartel.zip) — CSVs, the QA'd Excel transcription, README, data dictionary, and license.

---

##### What this is

The realized assignment of a procurement cartel, reconstructed from a public antitrust ruling. Indecopi's
**Resolución 080-2021/CLC** (15 November 2021) sanctioned thirty-two construction groups for rigging Ministry of
Transport road tenders between November 2002 and December 2016. This dataset is the tender-and-firm universe
behind the paper [*The Price of Corruption*](/papers/price-of-corruption/).

Most of the collusion-detection literature has to infer which tenders were rigged from bid distributions. Here
the competition authority adjudicated each tender, so the **colluded/competitive label is observed**, which
makes the data useful for validating screens, studying cartel governance, and measuring overcharge.

All tables are **firm-level** and built entirely from the public resolution. No personal data is included.

---

##### Contents

- **78 reconstructed road tenders** with project, year, winning consortium and members, reference and offered values.
- **Firm × process roles** (winning member, cover bidder, uncertain-target cover, participant without support).
- **32 sanctioned economic groups** with RUC, conduct dates, fines (UIT), and remedies.
- **Offer-level bids** (Anexo 2) with the colluded/competitive classification.
- **Illicit benefit and reference values** (Anexo 3) in the QA'd Excel transcription.
- **Exposure measures** (firm- and process-level) and a **SEACE/OCDS validation** crosswalk.
- A `README.md` and `DATA_DICTIONARY.md`.

---

##### Source and license

Derived from Indecopi *Resolución 080-2021/CLC-INDECOPI* (Expediente 001-2020/CLC), which is public. Released
under **CC BY 4.0**.

##### Citation

Chávez Padilla, Carlos César. 2026. "The Construction Club Cartel — Reconstructed Dataset." Derived from
Indecopi Resolución 080-2021/CLC.
