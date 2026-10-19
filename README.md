# 🇸🇬 MAS Monetary Policy Stance Dataset

**The only publicly available classified dataset of all Monetary Authority of Singapore (MAS) monetary policy decisions from 2001 to 2026.**

Built by [Anuja A. Gokhale](https://ssrn.com/author=10973290) (MA Applied Economics, NUS Merit Scholar) as a companion to the working paper:

> Gokhale, A.A. (2026). *Cross-Country Macroeconomic Dynamics: Inflation, Growth, and Monetary Policy — India, Singapore, and the United Kingdom.* SSRN Working Paper. [ssrn.com/abstract=6514338](https://ssrn.com/abstract=6514338)

---

## 📊 Live Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mas-policy-dataset.streamlit.app)

---

## 📁 Dataset

**File:** `mas_policy_stance_gokhale2026.csv`

**Coverage:** 55 MAS Monetary Policy Statements · October 2001 to January 2026

**Classification methodology:**

Each statement is classified across three policy levers:

| Variable | Values | Description |
|----------|--------|-------------|
| `slope` | steepen / maintain / flatten | Direction of S$NEER appreciation path |
| `width` | widen / maintain / narrow | Width of S$NEER policy band |
| `centring` | recentre_up / maintain / recentre_down | Mid-point adjustment of policy band |
| `stance` | tighten / neutral / ease | Overall policy stance |
| `score` | -2 to +2 | Weighted hawkishness score |
| `note` | text | Key phrase summarising decision context |

**Hawkishness score construction:**

- +2: Aggressive tightening (slope steepen + recentre up)
- +1: Moderate tightening (slope steepen only)
- 0: Hold (no changes)
- -1: Moderate easing (slope flatten only)
- -2: Aggressive easing (slope flatten + recentre down)

---

## 🏛️ MAS Monetary Policy Framework

Unlike most central banks, MAS does not use interest rates as its primary monetary policy instrument. Instead it manages the Singapore Dollar Nominal Effective Exchange Rate (S$NEER) — a trade-weighted basket of currencies — within an undisclosed policy band.

The band has three adjustable dimensions:

1. **Slope** — the rate of appreciation or depreciation of the S$NEER over time
2. **Width** — the range within which the S$NEER is allowed to fluctuate
3. **Centring** — the midpoint level at which the band is set

MAS publishes a Monetary Policy Statement (MPS) twice a year (April and October), with occasional off-cycle statements during episodes of significant economic disruption (e.g. January 2022, July 2022, March 2020, January 2022).

---

## 📈 Key Episodes in the Dataset

| Period | Stance | Context |
|--------|--------|---------|
| Apr 2003 | Aggressive ease (-2) | SARS — zero appreciation, recentre down |
| Apr 2008 | Aggressive tighten (+2) | Inflation surge — steepen + recentre up |
| Apr 2009 | Aggressive ease (-2) | GFC bottom — zero appreciation, recentre down |
| Apr 2010 | Aggressive tighten (+2) | Recovery — steepen + recentre up |
| Oct 2021 | Tighten (+1) | First move of 2021-2022 tightening cycle |
| Apr 2022 | Aggressive tighten (+2) | Supply shock — steepen + recentre up |
| Jul 2022 | Aggressive tighten (+2) | Off-cycle — fifth tightening in a row |
| Jan 2025 | Ease (-1) | First easing after 2023-2024 pause |

---

## 🚀 Run Locally

```bash
git clone https://github.com/anujagokhale1604/mas-policy-dataset
cd mas-policy-dataset
pip install -r requirements.txt
streamlit run mas_app.py
```

---

## 📖 Citation

If you use this dataset in your research, please cite:

```
Gokhale, A.A. (2026). MAS Monetary Policy Stance Dataset [Data set].
GitHub. https://github.com/anujagokhale1604/mas-policy-dataset

Gokhale, A.A. (2026). Cross-Country Macroeconomic Dynamics: Inflation,
Growth, and Monetary Policy — India, Singapore, and the United Kingdom.
SSRN Working Paper. https://ssrn.com/abstract=6514338
```

---

## 📬 Contact

Anuja A. Gokhale · anujagokhale1604@gmail.com · [ssrn.com/author=10973290](https://ssrn.com/author=10973290)

---

*Classification based on publicly available MAS Monetary Policy Statements. All statements are available at [mas.gov.sg](https://www.mas.gov.sg/monetary-policy/monetary-policy-decisions). This dataset is provided for research purposes.*
