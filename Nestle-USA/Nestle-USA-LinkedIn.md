# LinkedIn — Experience & Project Sections: Nestlé USA

**Prepared for:** LinkedIn Experience + Projects sections
**Tenure:** Mar 2022 – Nov 2026 (4 yrs 9 mos), **split** across four projects (one employer, four business-unit projects):
- Nutrition / Gerber (Infant & Toddler Nutrition Confidence): **Mar 2022 – Apr 2023** (1 yr 2 mos)
- Purina PetCare (Precision Pet Nutrition & Retention): **May 2023 – Jun 2024** (1 yr 2 mos)
- Food & Snacks (Private-Label Gap Defense & Value Architecture): **Jul 2024 – Aug 2025** (1 yr 2 mos)
- Demand Sensing (GLP-1-Aware Demand Sensing, Frozen & Coffee): **Sep 2025 – Nov 2026** (1 yr 3 mos)
**Documentation basis:** `Nestle-USA-Nutrition-Gerber-ProjectDoc.md`, `Nestle-USA-PetCare-PrecisionNutrition-ProjectDoc.md`, `Nestle-USA-FoodSnacks-ValueDefense-ProjectDoc.md`, `Nestle-USA-DemandSensing-ProjectDoc.md`, and `Nestle-USA-Research.md`. All four projects are reconstructions and must be validated before publishing.

> **Capgemini overlap (read first):** the Mar 2022 – present window on this profile is currently occupied by the **Capgemini Engineering** roles (up to "AI Solutions Architect", Mar 2025 – Present). Adding a Nestlé USA experience entry for the same window creates concurrent full-time roles. Resolve per your actual employment — keep one, or make Nestlé the employer and remove/condense the Capgemini entries.
>
> **Wording note:** copy uses softened "Designed / Built / Delivered" phrasing and avoids unverified metrics, per the source docs' instruction that each project is a reconstruction, not a verified case study.

---

## Experience entry — Nestlé USA

**Title:** Machine Learning Engineer — Data Science
**Company:** Nestlé USA
**Dates:** Mar 2022 – Nov 2026 · 4 yrs 9 mos
**Location:** [Use the location on your existing profile]
**Employment type:** [Full-time / Contract — match your records]

**Description:**

Data science / ML engineering across Nestlé USA's business units — demand forecasting, recommender systems, value/pricing analytics, and product-safety early warning — with a consistent emphasis on causal measurement and decision-grade outputs.

- Built regime-aware demand sensing (GLP-1 as a first-class driver) with causal attribution separating volume effects from price, mix, and private-label substitution.
- Designed constrained recommender systems (pet and infant nutrition) with nutrient-adequacy gates, cold-start handling, and LLM-assisted intake/coaching that never chooses the product.
- Built private-label gap defense and value-architecture models quantifying price/quality gaps at DMA and channel level with causal attribution.
- Ran safety and trust early-warning over complaint and quality signals with anomaly detection and change-point monitoring.

**Skills:** Data Science, Machine Learning, Python, LightGBM, XGBoost, Causal Inference, Recommender Systems, Demand Forecasting, NLP, MLOps.

---

## Project 1 — Infant & Toddler Nutrition Confidence System (Gerber)

**Project name:** Infant & Toddler Nutrition Confidence System (Gerber)
**Associated with:** Nestlé USA — Experience entry
**Dates:** Mar 2022 – Apr 2023

**Description:**

Designed an infant & toddler nutrition confidence system for Gerber: age/stage feeding-plan recommendations from a living child profile, plus a safety and trust early-warning capability over complaint, review, and lot/quality signals.

- Built anomaly and change-point detection over complaint and quality streams to flag safety/trust issues before they scale.
- Added a pediatric-adequacy constraint gate so recommendations respect age-stage and allergen limits.
- Used LLM extraction over free-text complaints for cause attribution, with an evidence trail a reviewer/regulator can inspect.

**Skills:** Anomaly Detection, NLP, Python, LightGBM, Recommender Systems, MLOps.

---

## Project 2 — Precision Pet Nutrition & Retention Engine (Purina)

**Project name:** Precision Pet Nutrition & Retention Engine (Purina)
**Associated with:** Nestlé USA — Experience entry
**Dates:** May 2023 – Jun 2024

**Description:**

Designed a precision pet nutrition and retention engine for Purina: per-pet profiles, right-formula and portion recommendations, and a retention/premiumization engine using pet's fast repurchase cycle.

- Built a constrained recommender (nutrient-adequacy gate via constraint solving) with cold-start from breed/age priors.
- Added a veterinary-channel decision aid for prescription diets and an LLM-assisted intake/coaching layer.
- Measured retention lift with holdouts rather than inferring it from a churn score.

**Skills:** Recommender Systems, Constraint Optimization, Python, LightGBM, Feature Store, A/B Testing.

---

## Project 3 — Private-Label Gap Defense & Value-Architecture Engine (Food & Snacks)

**Project name:** Private-Label Gap Defense & Value-Architecture Engine (Food & Snacks)
**Associated with:** Nestlé USA — Experience entry
**Dates:** Jul 2024 – Aug 2025

**Description:**

Designed a private-label gap defense and value-architecture engine for Nestlé USA Food & Snacks: continuous price/quality gap measurement at DMA and channel level, showing where the premium is defensible versus eroded.

- Built causal attribution (DoWhy/EconML, difference-in-differences, synthetic control) separating price, quality perception, distribution, and promotion effects.
- Estimated perceived quality from reviews/complaints via NLP/LLM extraction rather than from price.
- Ranked pack-architecture and price-value actions by expected value across the brand tail.

**Skills:** Causal Inference, Python, LightGBM, NLP, Econometrics, Pricing Analytics.

---

## Project 4 — GLP-1-Aware Demand Sensing for Frozen & Coffee

**Project name:** GLP-1-Aware Demand Sensing for Frozen & Coffee
**Associated with:** Nestlé USA — Experience entry
**Dates:** Sep 2025 – Nov 2026

**Description:**

Designed a regime-aware demand sensing system for Nestlé USA frozen and coffee, treating GLP-1 adoption as a first-class exogenous driver and separating it from price, mix, and private-label substitution via causal inference.

- Built store-level forecasts that survive the structural break, with geographic and income heterogeneity rather than national averages.
- Added analog-based forecasting for reformulated/new products with no history.
- Matched forecast horizon to production and procurement decision lead times (1–2 quarters ahead).

**Skills:** Demand Forecasting, Time Series, Causal Inference, Python, LightGBM, Feature Engineering.

---

## Claims discipline — validate before publishing

| Claim | Status | Action |
|---|---|---|
| Any of the four projects were actually built | Reconstructed | Phrase as "designed"; confirm what shipped |
| "LLM chose the product/diet" | No — hard design boundary | State recommenders are constrained; LLMs assist intake/coaching only |
| 2026 group figures (31 brands, 36k employees, private label 23.8%, recall costs) | 2026 data | Describe as context, not tenure-period results |
| Measured lift / RIG / retention numbers | Not evidenced | Omit specific metrics |
| GLP-1 effect sizes (3-pt frozen drop, 11–18% prevalence) | Third-party estimates | Cite as context only |
| Capgemini vs Nestlé as employer for Mar 2022–present | Overlap on profile | Resolve per actual employment |
| LLM-era tooling (GPT-4/Claude, vector stores) | Valid from 2023 | Fine within window; keep recommenders constrained |

**Anachronism guard:** LLMs (ChatGPT Nov 2022) are period-valid from late 2022, but the *recommender* is always a constrained model, never an LLM. Keep the vocabulary period-accurate: LightGBM/XGBoost, DoWhy/EconML, constraint solvers, MLflow 2.x, Airflow 2.x/Dagster, vector stores.

---

## Provenance

- Company facts from `Nestle-USA-Research.md` (2026-11-21), describing the 2026 group — later than parts of the 2022–2026 tenure.
- All four project specs are reconstructions aligned with Nestlé USA's actual business context, not verified case studies.
- Tenure (Mar 2022 – present) and function (Data Science / ML Engineering) supplied by the author; not independently verified.
- Financial and share figures are company-reported or third-party estimates and unaudited.