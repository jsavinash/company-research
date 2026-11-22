# Glossary and Terminology

## Domain

| Term | Definition |
|---|---|
| **SFS** | Siemens Financial Services — B2B equipment finance and leasing (Siemens AG corporate unit). |
| **B2B equipment finance** | Financing/leasing of industrial equipment to businesses. |
| **PD** | Probability of Default. |
| **Delinquency** | Payment overdue (30/60/90 days past due). |
| **Default** | 90+ days past due / write-off. |
| **ECL** | Expected Credit Loss (IFRS 9). |
| **IFRS 9** | Accounting standard requiring forward-looking expected credit losses. |
| **Cohort** | A group of loans (by asset class, contract type, vintage). |
| **Watchlist** | Ranked list of accounts for credit review. |
| **Restructuring / forbearance** | Contract modification to avoid default. |
| **DPD** | Days Past Due. |
| **Firmographics** | Business attributes (sector, size, region). |
| **Operational signal** | Machine telemetry (utilization, downtime, service deferral, energy) — the differentiator. |

## Technical

| Term | Definition |
|---|---|
| **Survival analysis** | Time-to-event modeling with censoring (Cox PH, AFT). |
| **Right-censoring** | Loans that do not default within the observation window. |
| **Time-to-event** | Months from observation to delinquency/default. |
| **Cox PH** | Cox proportional hazards model. |
| **AFT** | Accelerated Failure Time model. |
| **XGBoost / LightGBM** | Gradient-boosted trees. |
| **Calibration** | Platt / isotonic scaling → reliable PD. |
| **ECE** | Expected Calibration Error. |
| **WoE** | Weight of Evidence (scorecard binning). |
| **Scorecard** | Interpretable logistic model (regulatory-friendly). |
| **SHAP** | SHapley Additive exPlanations — reason codes. |
| **KS statistic** | Kolmogorov–Smirnov discrimination metric. |
| **Gini / AUC** | Discrimination metrics. |
| **PSI** | Population Stability Index (drift). |
| **Swap-set analysis** | Challenger vs. champion on common good/bad. |
| **Reject inference** | Inferring outcomes for rejected applicants. |
| **Point-in-time correctness** | Features computed as of prediction date. |

## Abbreviations

| Abbreviation | Expansion |
|---|---|
| SFS | Siemens Financial Services |
| PD | Probability of Default |
| ECL | Expected Credit Loss |
| DPD | Days Past Due |
| KS | Kolmogorov–Smirnov |
| PSI | Population Stability Index |
| SHAP | SHapley Additive exPlanations |
| WoE | Weight of Evidence |
| AFT | Accelerated Failure Time |
| PH | Proportional Hazards |
| ECE | Expected Calibration Error |
| AUC | Area Under Curve |
| IFRS | International Financial Reporting Standard |
| DPDP | Digital Personal Data Protection (India) |
| SLA | Service Level Agreement |
| NFR | Non-Functional Requirement |
| ADR | Architecture Decision Record |