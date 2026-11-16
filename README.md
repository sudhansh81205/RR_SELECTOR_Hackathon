# 👑 Rajasthan Royals — SupeRR Selector Season 2: Round 1 Hackathon

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Machine Learning](https://img.shields.io/badge/Model-HistGradientBoosting-pink.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Official Round 1 Challenge:** *Identify the Most Reliable Players Under Pressure in T20 Cricket (2022–2026) for the Rajasthan Royals IPL 2027 Auction.*

An end-to-end data-driven war room analytics platform analyzing **200,999 deliveries across 883 matches** (IPL & T20Is) using Gradient-Boosted Win Probability Leverage, Format-Calibrated Contextual Par, and Empirical Bayes Regularization.

---

## ⚡ Live Streamlit Cloud Deployment (1-Click Guide)

This repository is optimized for instant deployment on **Streamlit Community Cloud**:

1. **Fork or Push** this repository to your GitHub account (`RR_SELECTOR_Hackathon`).
2. Visit **[share.streamlit.io](https://share.streamlit.io/)** and sign in with your GitHub account.
3. Click **"New app"**, select your repository:
   - **Repository:** `your-username/RR_SELECTOR_Hackathon`
   - **Branch:** `main` (or `master`)
   - **Main file path:** `streamlit_app.py` (or `app.py`)
4. Click **"Deploy!"**
5. You get an instant public URL:
   `https://<your-custom-subdomain>.streamlit.app`
   *(Paste this directly into the Unstop submission dashboard link field!)*

---

## 💻 Run Locally

Clone the repository and install requirements:

```bash
git clone https://github.com/your-username/RR_SELECTOR_Hackathon.git
cd RR_SELECTOR_Hackathon
pip install -r requirements.txt
streamlit run app.py
```
Your browser will open automatically at `http://localhost:8501`.

---

## 🏆 Official Top 10 Submissions (Unstop Dropdowns)

### 🏏 Top 10 Batters Under Pressure

| Rank | Player Name | SupeRR Rating | Pressure Balls | Pressure SR | Format Par SR | SR Lift vs Par | Baseline SR | Delta SR | Pressure Avg | Boundary % | Matches |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Quinton de Kock** | **100.0** | 139 | 189.2 | 145.3 | **+43.9** | 138.2 | **+51.0** | 43.8 | 29.5% | 15 |
| **2** | **Jos Buttler** | **98.8** | 307 | 195.1 | 145.2 | **+49.9** | 145.3 | **+49.8** | 28.5 | 31.9% | 34 |
| **3** | **Suryakumar Yadav** | **98.8** | 529 | 182.6 | 140.4 | **+42.2** | 156.4 | **+26.3** | 43.9 | 27.4% | 41 |
| **4** | **Glenn Maxwell** | **96.6** | 195 | 190.3 | 135.0 | **+55.3** | 144.7 | **+45.5** | 28.5 | 29.7% | 21 |
| **5** | **Rinku Singh** | **95.7** | 418 | 188.0 | 154.7 | **+33.4** | 126.0 | **+62.0** | 32.8 | 29.4% | 50 |
| **6** | **Dinesh Karthik** | **93.5** | 323 | 190.4 | 154.8 | **+35.6** | 126.1 | **+64.3** | 22.8 | 30.3% | 43 |
| **7** | **Shashank Singh** | **93.2** | 222 | 174.3 | 147.8 | **+26.5** | 141.5 | **+32.8** | 48.4 | 24.8% | 23 |
| **8** | **Phil Salt** | **92.3** | 136 | 189.7 | 140.2 | **+49.6** | 161.4 | **+28.3** | 28.7 | 27.9% | 14 |
| **9** | **Shikhar Dhawan** | **91.9** | 114 | 158.8 | 139.9 | **+18.9** | 118.1 | **+40.7** | 60.3 | 24.6% | 6 |
| **10** | **Naman Dhir** | **91.8** | 148 | 192.6 | 148.3 | **+44.3** | 155.4 | **+37.2** | 25.9 | 30.4% | 20 |

---

### 🎯 Top 10 Bowlers Under Pressure

| Rank | Player Name | SupeRR Rating | Pressure Balls | Pressure Econ | Format Par Econ | Runs Saved / Over | Balls / Wicket | Dot Ball % | Boundary % | Matches |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **Sufiyan Muqeem** | **100.0** | 171 | 4.46 | 7.41 | **+2.95** | 10.7 | 57.9% | 7.0% | 14 |
| **2** | **Matheesha Pathirana** | **87.2** | 421 | 8.15 | 9.33 | **+1.18** | **9.2** | 39.4% | 16.9% | 42 |
| **3** | **Jasprit Bumrah** | **87.1** | 467 | 7.49 | 9.63 | **+2.14** | 15.6 | 40.3% | 15.8% | 58 |
| **4** | **Maheesh Theekshana** | **86.9** | 358 | 6.91 | 8.62 | **+1.71** | 12.3 | 38.5% | 11.7% | 39 |
| **5** | **Mujeeb Ur Rahman** | **85.7** | 104 | 6.40 | 8.05 | **+1.64** | 11.6 | 46.2% | 11.5% | 16 |
| **6** | **Kuldeep Yadav** | **85.6** | 364 | 6.84 | 8.30 | **+1.46** | 12.6 | 39.8% | 11.8% | 35 |
| **7** | **Abrar Ahmed** | **85.5** | 233 | 5.69 | 7.59 | **+1.90** | 19.4 | 44.2% | 8.2% | 21 |
| **8** | **Benjamin Sears** | **84.7** | 101 | 7.13 | 8.64 | **+1.52** | **9.2** | 39.6% | 14.9% | 15 |
| **9** | **Mohammad Nawaz** | **84.4** | 191 | 6.16 | 7.39 | **+1.24** | 11.2 | 38.7% | 8.9% | 20 |
| **10** | **Umran Malik** | **84.4** | 164 | 7.43 | 8.11 | **+0.68** | **9.6** | 53.0% | 20.1% | 16 |

---

## 🎯 Rajasthan Royals IPL 2027 Auction Target Strategy

### 1. Matheesha Pathirana (Overseas Death-Over Yorker Specialist)
- **Problem Solved:** Leaking boundaries at the death in Jaipur.
- **The Metric:** Concedes 8.15 RPO vs an IPL death par of 9.33 (+1.18 runs saved/over) while striking at an unbelievable **9.15 balls per wicket** under pressure across 421 deliveries.

### 2. Shashank Singh (Indian Middle-Order Crisis Finisher)
- **Problem Solved:** Over-dependence on Sanju Samson & Yashasvi Jaiswal; middle-order stagnation during collapses.
- **The Metric:** Unbelievable **48.38 average under pressure** at 174.32 SR across 222 pressure deliveries.

### 3. Maheesh Theekshana (Powerplay & Death Mystery Spin)
- **Problem Solved:** Defending the expansive Sawai Mansingh Stadium boundaries.
- **The Metric:** Concedes only **6.91 RPO** under pressure (+1.71 runs saved/over) with a 11.7% boundary rate across 358 deliveries.

### 4. Naman Dhir (Dynamic Multi-Phase Indian Hitter)
- **Problem Solved:** Fast counter-attacking without burning dot balls.
- **The Metric:** 192.57 pressure strike rate (+44.3 above par) and 30.4% boundary execution.

---

## 🧠 Methodology & Machine Learning Architecture

```
Delivery Raw Features (200,999 Balls)
        │
        ├── State Engineering (Runs Needed, Balls Rem, Wickets, Over, Phase)
        │
        ├── Win Probability Machine Learning Model (HistGradientBoosting on 95,146 Innings 2 deliveries)
        │       └── LI = 4 * P * (1 - P) * [0.4 + 0.6 * (120 - BallsRem) / 120]
        │       └── CPI = 0.50 * LI + 0.40 * ChaseStress + 0.10 * KnockoutStage (Inn 2)
        │       └── CPI = 0.45 * DeathStress + 0.35 * CollapseCrisis + 0.10 * Deficit (Inn 1)
        │
        ├── Format-Calibrated Contextual Par (FCCP)
        │       └── Benchmarked by (is_ipl, innings, overid, is_high_pressure)
        │       └── Solves Baseline Distortion Paradox (IPL 9.95 RPO vs T20I 9.08 RPO)
        │
        ├── Empirical Bayes Shrinkage (K = 50 balls prior regularization)
        │
        └── Final SupeRR Selector Rating (SSR) & Match Variance Regularizer
```

---

## 📂 Repository Structure

```
RR_SELECTOR_Hackathon/
├── app.py                      # Main Streamlit War Room Dashboard
├── streamlit_app.py            # Streamlit Cloud entry point
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── outputs/                    # Precomputed calibrated ranking CSVs
│   ├── calibrated_top_batters.csv
│   ├── calibrated_top_bowlers.csv
│   ├── ranked_batters.csv
│   └── ranked_bowlers.csv
└── docs/                       # Official Methodology Reports
    ├── Rajasthan_Royals_SupeRR_Selector_Report.pdf  # Final PDF for Unstop upload
    ├── METHODOLOGY_REPORT.md                        # Full report in Markdown
    ├── METHODOLOGY_REPORT.html                      # Print-styled HTML report
    ├── SHARE_YOUR_JOURNEY.md                        # Journey story & video script
    └── dashboard.html                               # Standalone HTML dashboard
```

---

## 📄 License
Developed for the **Rajasthan Royals Hackathon — SupeRR Selector Season 2**. Released under the MIT License.
