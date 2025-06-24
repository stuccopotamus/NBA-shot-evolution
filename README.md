# 📊 How Statisticians Ruined Basketball  
### The NBA 3-Pointer Revolution

---

## Overview

The rise in 3-point shots over the last two decades is explained by a simple mathematical calculation. Consider a prolific shooter:

- A 2-point mid-range jumper typically converts at a **50%** rate, yielding an expected return of **1.0 point per attempt** (0.5 × 2).
- A 3-point shot, even at a lower **40%** accuracy, has an average value of **1.2 points** (0.4 × 3).

This marginal efficiency gain has **fundamentally reshaped shot selection**, offensive strategies, and defensive systems across the NBA.

This project explores how **shot selection has evolved** in the NBA over the last **21 seasons**, from 2004 to 2024.

---

## Data Overview

### Data Source

The primary dataset consists of NBA shot logs from **2004 to 2024**, capturing every shot attempted in official NBA games.

> [Download the dataset on Kaggle](https://www.kaggle.com/datasets/mexwell/nba-shots?resource=download&select=NBA_2005_Shots.csv)

---

### Initial Data Checks

A first-pass Excel review identified an issue with **incorrectly scaled data** in 3 of the seasons.

### Data Cleaning & Formatting

- [Python script for correcting scaled data](#)  
- [Python script for general cleaning, formatting, and grouping](#)

### Data Structure

The cleaned data was consolidated into a single database, with key fields structured as shown below:

> 🖼️ *(Insert visual schema of cleaned database here)*

---

## Data Visualisation

Visualizations were created using **Tableau Public**.

> [View the dashboard on Tableau Public](#)

---

## Data Limitations

- No player-specific data included
- Lacks seasons **prior to 2004**, notably missing data from **1979–2004**, including the **inception of the 3-point line in 1979**

---

## Key Questions

This project is based on three central questions:

1. **How has 3-point shot selection evolved in the last 20 years?**
2. **How has mid-range shot selection changed in response?**
3. **What are the broader consequences of this transformation?**

---

## Key Findings

- In **2003/04**, **mid-range shots** made up **35.65%** of total FGAs; by **2023/24**, that dropped to **~11%**
- In contrast, **3-point attempts** nearly **doubled** — from **18.68%** to **39.48%** of total FGAs
- Teams now average **~35 3PA per game**, compared to **~14 two decades ago**

### Position-Based Growth in 3PA (2004 → 2024)

| Position | 3PA (2004) | 3PA (2024) | % Increase |
|----------|------------|------------|------------|
| Guards   | ~6         | ~12        | +93%       |
| Forwards | ~5         | ~15        | +187%      |
| Centers  | ~0.2       | ~2.5       | +1039%     |

> The traditional roles have evolved — even **7'2" centers** are now expected to shoot 3s regularly.

---

## Efficiency and Strategy

- **3P% ≈ 40%** from 22–27 ft range, with little drop-off past the arc
- This has incentivized teams to emphasize:
  - 3-point shots
  - Rim finishes
  - **De-prioritize** mid-range shots

### Strategic Adaptation

- Teams should **exploit defensive gaps** by selectively reintroducing mid-range shots
- Mid-range zones are increasingly **undefended** due to defensive focus on perimeter and paint

---

## Recommendations

- Continue tracking 3-point trends and adjusting rosters accordingly
- Use the **mid-range as a counter-strategy** where appropriate
- Encourage **versatility in player development** — regardless of position
- Avoid overcommitting to a single strategy: **Adaptability** wins games

> On a **microscopic level**, basketball is a **game of reads and reactions**. Coaches should mix shot profiles to remain unpredictable.

---

## Assumptions and Caveats

- Certain seasons (e.g. 2011–12, 2019–20, 2021–22) had **fewer games** due to lockouts, COVID-19, or other events
- The analysis is based solely on **shot-level data**
- It lacks **player identity**, **play types**, and **advanced play-by-play context**
- For deeper insight, refer to [this article](#) that inspired the project

---

## Summary

The 3-point revolution is here to stay — and it’s not just about math, but **how that math has reshaped the court, the players, and the tactics** of the modern NBA. 
