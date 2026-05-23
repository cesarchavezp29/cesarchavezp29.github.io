---
topic: "Innovation & the Economics Profession"
title: "Automation Is Not a Sufficient Statistic: A Two-Frontier Task Model of Robots, AI, and Inequality"
date: 2026-02-10
layout: rich
math: true
tags: ["automation","AI","inequality","labor economics","technology"]
author: "Carlos César Chávez Padilla"
description: "Two-frontier task model showing why aggregate automation masks opposite skill-premium effects of robots and AI."
summary: "Develops a novel task-based framework showing why aggregate automation hides opposite skill-premium effects of robots and AI."
editPost:
    URL: "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6212859"
    Text: "SSRN"

---

## Abstract

This paper develops a two-frontier task model in which robots and AI displace labor along distinct task continua — a *physical* sector and a *cognitive* sector. Within a nested CES production structure with two skill types and worker mobility across sectors, the partial effects of robot and AI shocks on the skill premium have **opposite signs** under pure displacement, and remain opposite under symmetric reinstatement regimes. Aggregate automation is therefore *not a sufficient statistic* for inequality: any test that lumps robots and AI into a single index masks economically meaningful heterogeneity.

## Setup

Two sectors, *Physical* ($P$) and *Cognitive* ($C$), and two skill types, *High* ($H$) and *Low* ($S$). Each sector uses a nested CES production function with capital, surviving labor, and reinstated labor modules. The within-sector labor aggregator nests skill types with elasticity $\varepsilon_w > 1$.

A **robot shock** is an increase in $I_R$, the physical frontier (holding $I_A$ fixed). An **AI shock** is an increase in $I_A$, the cognitive frontier (holding $I_R$ fixed). Each frontier marks the fraction of its task continuum that has been automated.

## Key Reduction

Wage equalization across sectors and the skill comparative-advantage assumption imply a *constant cross-sector skill ratio*,

$$\frac{r_C}{r_P} = \kappa^{\varepsilon_w - 1},$$

which depends only on the skill comparative-advantage parameter $\kappa$ and the labor elasticity $\varepsilon_w$ — not on automation levels, prices, or output. This collapses the two-dimensional labor-allocation problem $(\lambda_S, \lambda_H)$ to a single dimension, enabling a clean chain-rule decomposition of the skill-premium effects of each frontier.

## Main Result

**Proposition 1 (Opposite Skill Premium Effects).** Under pure displacement ($\delta_R = \delta_A = 0$), inner elasticity $\sigma > 1$, outer elasticity $\rho > 1$, and Cobb-Douglas final aggregation,

$$\frac{\partial \mathcal{P}}{\partial I_R} > 0 \qquad \text{and} \qquad \frac{\partial \mathcal{P}}{\partial I_A} < 0.$$

A robot shock reduces surviving physical-labor productivity $\mathcal{A}_{SP}$, pushing workers *out of* the physical sector — the resulting reallocation **raises** the skill premium. An AI shock reduces surviving cognitive-labor productivity $\mathcal{A}_{SC}$, pushing workers *into* the physical sector — the resulting reallocation **lowers** the skill premium. The opposite-sign result is robust to the nested CES structure (the outer elasticity $\rho$ scales the magnitude but not the sign) and to symmetric reinstatement regimes.

## Calibration

The calibrated configuration is strongly asymmetric across frontiers:

- $\hat{\delta}_R \approx 1.13$ — robots reinstate substantial new physical tasks per task displaced (strong reinstatement)
- $\hat{\delta}_A \approx 0$ — AI displaces cognitive tasks with negligible reinstatement

This asymmetry is illustrated below: in *Panel A* the physical-task identity extends past $1$ (robots create new tasks beyond the surviving range), while in *Panel B* the cognitive labor band is simply compressed with no offsetting task creation. **Drag the sliders to see how each frontier reshapes its task continuum.**

{{< two_frontier_demo >}}

## Implication

Aggregate automation indices conflate two technologically distinct frontiers. Empirical work and policy that treat automation as a single phenomenon will systematically miss the opposite skill-premium responses to robots and AI. The model rationalizes apparent "no effect" findings on composite automation indices: each frontier moves the skill premium, but in opposite directions — the canceled sum looks like nothing happened.
