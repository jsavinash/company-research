# LinkedIn — Experience & Project Sections: Siemens India (Healthineers + Financial Services)

**Prepared for:** LinkedIn Experience + Projects sections
**Tenure:** Aug 2019 – Mar 2022 (2 yrs 8 mos), **split** between the two projects:
- Siemens Healthineers India (ChestTriage): **Aug 2019 – Mar 2021** (1 yr 8 mos)
- Siemens Financial Services (Credit Risk): **Apr 2021 – Mar 2022** (1 yr)
**Documentation basis:** `Siemens-Healthineers-ChestTriage-ProjectDoc.md`, `Siemens-FinancialServices-CorporateUnits-ProjectDoc.md`, and `Siemens-Research.md`. Both projects are reconstructions and must be validated before publishing.

> **Entity resolution (read first):** the two docs attribute the *same* Aug 2019 – Mar 2022 window to **two different Siemens legal entities** — Siemens Healthineers India (ChestTriage) and Siemens Financial Services + Corporate Units (FinancialServices). Both are distinct from Siemens Limited (India) (the listed subsidiary). This file creates **two separate experience entries**; confirm each against your actual legal employer and make CV / LinkedIn agree.
>
> **Nagarro overlap:** your profile already has a "Nagarro" entry for Aug 2019 – Mar 2022. Adding these Siemens entries produces three concurrent full-time roles for the same window. Proceed only if that reflects reality (e.g. client engagements) — otherwise consolidate.

---

## Experience entry 1 — Siemens Healthineers India

**Title:** Machine Learning Engineer — Medical Imaging
**Company:** Siemens Healthineers India
**Dates:** Aug 2019 – Mar 2021 · 1 yr 8 mos
**Location:** [Use the location on your existing profile]
**Employment type:** [Full-time / Contract — match your records]

**Description:**

Designed a chest-radiograph triage and calibrated computer-aided detection capability for Siemens Healthineers (AI-Rad Companion / syngo.via lineage), prioritizing the worklist by likelihood of actionable disease while keeping the radiologist as the diagnostic authority.

- Built a DICOM ingestion and de-identification pipeline (pydicom/SimpleITK → MONAI transforms) with device-class and acquisition metadata captured as features.
- Trained nnU-Net segmentation + DenseNet multi-head classification (PyTorch) with focal loss and hard-negative mining for rare actionable findings.
- Added per-site / per-prevalence calibration (temperature scaling + isotonic) and Grad-CAM localization heatmaps, with an explicit "cannot assess" abstention state.
- Delivered a syngo.via reading overlay (heatmap + calibrated confidence + finding list + similar priors) and logged radiologist accept/adjust/reject actions as labels.
- Ran site-held-out and temporal validation, multi-reader reader studies, and shadow deployment toward CE-MDR / FDA / CDSCO-grade hardening.

**Skills:** Medical Imaging, Deep Learning, PyTorch, MONAI, nnU-Net, DICOM, Grad-CAM, Model Calibration, Python, MLOps.

---

## Experience entry 2 — Siemens Financial Services

**Title:** Machine Learning Engineer — Credit Risk
**Company:** Siemens Financial Services (Corporate Units)
**Dates:** Apr 2021 – Mar 2022 · 1 yr
**Location:** [Use the location on your existing profile]
**Employment type:** [Full-time / Contract — match your records]

**Description:**

Designed an equipment-embedded credit-risk early-warning capability for Siemens Financial Services (B2B equipment finance), predicting default and delinquency 3–6 months ahead using how the financed machine is actually operated — plus a corporate risk-data and model-governance layer.

- Built a time-aware risk-data platform (Kafka → Spark → feature store) joining SFS credit data with Siemens service/operations telemetry (utilization, downtime, service deferrals, energy).
- Trained gradient-boosted PD models (LightGBM/XGBoost) with cost-sensitive loss and Cox PH / AFT survival models for time-to-delinquency with censoring.
- Added Platt/isotonic calibration, a WoE scorecard companion, and SHAP reason codes in credit language.
- Measured operational-signal lift vs. a financial-only baseline and ran out-of-time / out-of-universe validation with PSI and calibration monitoring.

**Skills:** Credit Risk, Machine Learning, XGBoost, LightGBM, Survival Analysis, SHAP, Python, MLOps.

---

## Project entry 1 — Chest Radiograph Triage & Calibrated CAD

**Project name:** Chest Radiograph Triage & Calibrated CAD (AI-Rad Companion)
**Associated with:** Siemens Healthineers India — Experience entry 1
**Dates:** Aug 2019 – Mar 2021

**Description:**

Designed a chest-radiograph triage and calibrated CAD system for Siemens Healthineers: worklist prioritization by likelihood of actionable disease, finding localization, and per-site calibrated confidence — with the radiologist remaining the diagnostic authority.

- Built a nnU-Net + DenseNet inference core in PyTorch/MONAI with Grad-CAM heatmaps and a "cannot assess" abstention gate.
- Added per-site / per-prevalence calibration (temperature scaling + isotonic) — the core differentiator against prevalence shift between clinic and screening.
- Deployed via a syngo.via overlay and DICOM ingestion; ran site-held-out validation, multi-reader reader studies, and shadow mode toward regulatory hardening.

**Skills:** Medical Imaging, nnU-Net, MONAI, PyTorch, Grad-CAM, Model Calibration, DICOM, Python.

---

## Project entry 2 — Equipment-Embedded Credit-Risk Early-Warning

**Project name:** Equipment-Embedded Credit-Risk Early-Warning (SFS)
**Associated with:** Siemens Financial Services — Experience entry 2
**Dates:** Apr 2021 – Mar 2022

**Description:**

Designed a credit-risk early-warning system for SFS B2B equipment finance: calibrated PD plus survival time-to-delinquency, using operational machine telemetry as a leading signal beyond lagging financials.

- Built a governed risk-data platform joining credit, finance, and equipment-telemetry sources with point-in-time-correct features.
- Trained LightGBM/XGBoost PD and Cox PH / AFT survival models; added Platt/isotonic calibration, a WoE scorecard, and SHAP reason codes.
- Validated out-of-time and out-of-universe with PSI/calibration monitoring; measured operational-signal lift as a release gate.

**Skills:** Credit Risk, XGBoost, LightGBM, Survival Analysis, SHAP, Calibration, Python, MLOps.

---

## Claims discipline — validate before publishing

| Claim | Status | Action |
|---|---|---|
| Which Siemens entity employed you (Healthineers vs SFS vs Siemens Ltd India) | Ambiguous across docs | Confirm legal employer; keep entity consistent |
| 2026 group figures (€83.4B rev, 319k staff, Healthineers €23.6B) | 2026 data, not 2019–22 | Do not imply these describe the tenure-period entity |
| Specific projects were actually built | Reconstructed | Phrase as "designed"; confirm what was shipped |
| Operational-signal moat (SFS sees the machine) | Partial in reality | State achievable telemetry coverage, not universal |
| Used LLMs / GPT | No | Exclude; these are CNN / gradient-boosted / survival stacks |
| Shadow validation = clinical/financial impact | No | Keep shadow as release safety only |
| Nagarrole overlap with same dates | Real profile conflict | Resolve per your actual employment |

**Anachronism guard:** keep 2019–2022 vocabulary — MONAI (Dec 2019), nnU-Net, PyTorch, DenseNet, Grad-CAM, temperature scaling/isotonic, LightGBM/XGBoost, Cox PH/AFT, SHAP, MLflow 1.0, Kubeflow 1.0, Airflow 1.10, EU MDR (May 2021). Exclude GPT/LLMs and the 2026 "Eigen/ICX/€1B AI" narrative (Siemens AG, not Healthineers).

---

## Provenance

- Company facts from `Siemens-Research.md` (2026-11-21), describing the 2026 group — later than the 2019–22 tenure.
- Entity distinction is unresolved in the source docs and must be settled before publishing.
- Tenure (Aug 2019 – Mar 2022) and functions supplied by the author; not independently verified.
- Both projects are reconstructions aligned with Siemens' actual "data as moat" trajectory, not verified case studies.