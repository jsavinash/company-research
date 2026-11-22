# Project Scope and SLA

## 1. In scope

**Modality and population**
- Chest radiography (PA / AP, adult primary; pediatric flagged as a separate profile).
- Fixed DR, portable/mobile, and CR acquisitions (device class is a first-class feature).

**Findings (triage / second-read)**
- TB-suggestive abnormalities (primary India use case).
- Pulmonary nodule, consolidation, pleural effusion, pneumothorax, cardiomegaly.
- "Inadequate / cannot assess" as an explicit output state.

**Outputs**
- Per-study triage category: routine / priority / urgent (worklist reordering).
- Finding localization heatmap overlaid on the image.
- Site-calibrated confidence per finding (never a bare score).
- Structured finding list mapping into syngo.via.
- Explicit abstention ("cannot assess — image quality / coverage").

**Platform**
- DICOM ingestion, de-identification, preprocessing, training, registry, serving, monitoring, audit.
- Per-site calibration and per-site monitoring.

## 2. Out of scope

- Autonomous diagnosis or auto-generated final reports (triage / decision-support only).
- CT and MR primary reading.
- Mammography / tomosynthesis.
- Theranostics dosimetry and response assessment.
- PACS / RIS replacement (syngo.via integrates with, does not replace).
- Screening-program administration.

## 3. Explicit non-goals

- **No autonomous diagnosis or auto-sign-off.** The radiologist reads, decides, signs.
- **No uncalibrated score presented as a probability.** Every confidence is site-calibrated.
- **No black-box output.** Every prediction carries a localization + rationale.
- **No cross-site training on raw PHI without governance.** Federation or per-site training only.

## 4. Stakeholders

| Stakeholder | Role |
|---|---|
| Radiologists | Primary users (worklist + overlay) |
| Clinical lead | Label definition, sign-off |
| Regulatory / compliance | MDR, FDA, CDSCO |
| Data governance / DPO | India DPDP, de-identification |
| Siemens Healthineers product | AI-Rad Companion / syngo.via |

## 5. SLAs

| Service | SLA | Measurement |
|---|---|---|
| Inference per study | p95 ≤ 3 s | Service logs |
| Worklist triage | Real-time / near-real-time | Pipeline monitoring |
| Sensitivity (actionable) | ≥ 0.85 (site-stratified) | Eval harness |
| Calibration (ECE) | ≤ 0.05 per site | Eval harness |
| Radiologist acceptance | ≥ 0.70 | Reader study |
| Availability | 99.5% | Monitoring |

## 6. Constraints & dependencies

- **Period-accurate tooling (2019–2022):** nnU-Net, MONAI (Dec 2019), PyTorch 1.x, Grad-CAM, temperature scaling/isotonic, MLflow 1.0, Kubeflow 1.0. No LLMs.
- **Data access:** DICOM from installed base; reports; microbiological confirmation (TB subset).
- **Regulatory:** EU MDR (May 2021), FDA 510(k), CDSCO.
- **Governance:** per-site isolation, India DPDP, de-identification.

## 7. Change control

Scope changes require a decision-log entry and, if architectural, a new ADR. SLA changes require sign-off from the clinical lead.