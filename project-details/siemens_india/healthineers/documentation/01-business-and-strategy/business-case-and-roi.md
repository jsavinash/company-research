# Business Case and ROI

## 1. The business problem

Siemens Healthineers' economics are tied to installed base and to the software and AI that ride on it. Chest radiography is the highest-volume, most globally distributed, and — in India — most *public-health-relevant* exam in radiology. Three facts converge:

- **Volume.** Chest X-ray is the workhorse of radiology and of TB screening programs at a scale no other modality approaches. Triage value scales with volume.
- **Shortage of readers.** India has a well-documented radiologist shortage; in high-burden screening settings, a human reading every chest X-ray is not achievable. Prioritization — read the urgent ones first — is a real, measurable intervention.
- **The AI moat is workflow + clearance, not the model.** A triage/CAD feature that ships *inside* syngo.via on the scanner's own images, as a cleared companion, is where that moat is monetised.

## 2. The thesis

> Siemens Healthineers' durable advantage is not model capability — hyperscalers and pure-play imaging-AI vendors can match any single architecture. It is the **installed base + clinical workflow + regulatory trust + de-identified imaging data**. This project turns a chest X-ray already acquired on a Healthineers system into a triage and second-read signal that is cleared, workflow-native, and explainable.

## 4. The five technical problems

1. **Prevalence shift breaks calibration** — a model calibrated on a symptomatic cohort is miscalibrated for screening (prevalence 1–2 orders of magnitude lower). Per-site/per-prevalence calibration is mandatory.
4. **Site and device heterogeneity (domain shift)** — fixed DR, portable/mobile, CR, pediatric vs. adult produce very different distributions.
5. **Localization and interpretability are the product** — a radiologist needs a heatmap + meaningful confidence, and remains the decision-maker.
6. **Label quality and scarcity** — mostly radiologist reports (weak labels); microbiological confirmation for a TB subset.
7. **Regulation and audit** — CE (EU MDR from May 2021), FDA 510(k), CDSCO demand locked versions, audit trails, documented performance.

## 5. The intervention

A **chest-radiograph triage and calibrated CAD**:
- Ingest chest X-rays from the installed base (DICOM).
- Prioritize the worklist (routine / priority / urgent).
- Localize findings (Grad-CAM heatmaps).
- Attach **site-calibrated** confidence per finding.
- Keep the radiologist as the diagnostic authority (syngo.via overlay).

## 6. Value drivers

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **Read-time reduction** | Triage prioritizes urgent cases | Radiologists |
| **Earlier actionable detection** | CAD second-read | Patients, health system |
| **Workflow-native adoption** | Ships inside syngo.via | Siemens Healthineers |
| **Regulatory-grade trust** | Cleared companion + audit | Compliance, clinicians |
| **Reusable imaging AI** | AI-Rad Companion lineage | Siemens Healthineers |

## 7. Success criteria (business)

- **Sensitivity for actionable findings ≥ 0.85** (site-stratified, at clinically agreed FPR).
- ECE ≤ 0.05; calibration slope 0.8–1.25 per site.
- Read-time reduction ↓ 15% relative.
- Radiologist acceptance ≥ 0.70.
- Subgroup parity ≤ 5 pp gap.

## 8. ROI model

The ROI is dominated by **read-time reduction** (radiologist productivity) and **earlier actionable detection** (TB screening), plus the strategic value of workflow-native AI on the installed base. Illustrative:
- Read-time saved × study volume.
- Earlier TB detection → better outcomes.
- Reusable AI-Rad Companion portfolio.

> Replace with Siemens Healthineers India's actual baselines before any business-case submission.

## 9. Risks to the business case

| Risk | Mitigation |
|---|---|
| Prevalence shift makes a clinic-calibrated model harm at a screening site | Per-site calibration; site-held-out validation; calibration as a release gate |
| Domain shift across sites/devices | Device-class features; harmonization; subgroup parity gate |
| Automation bias — readers over-trust AI | Reader study measures both; AI as triage not truth |
| Label noise | NLP + microbiological linkage; adjudicated evaluation set |
| Regulatory (MDR, FDA, CDSCO) | Locked versions; audit logs; documentation as deliverable |
| PHI / India DPDP | De-id at ingest; per-site isolation; federation option |