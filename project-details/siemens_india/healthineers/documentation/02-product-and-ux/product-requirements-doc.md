# Product Requirements Document (PRD)

## 1. Summary

A chest-radiograph triage and calibrated CAD capability for Siemens Healthineers, scoped to the 2019–2022 toolchain. It prioritizes the worklist, localizes findings, attaches site-calibrated confidence, and keeps the radiologist as the diagnostic authority.

## 2. Goals

- Reduce radiologist read time (↓ 15% relative).
- Improve early actionable detection (sensitivity ≥ 0.85, site-stratified).
- Site-calibrated confidence (ECE ≤ 0.05; slope 0.8–1.25).
- Radiologist acceptance ≥ 0.70.
- Regulatory-grade auditability (MDR/FDA/CDSCO).

## 3. Non-goals

- Autonomous diagnosis / auto-sign-off.
- CT/MR primary reading.
- Mammography / tomosynthesis.
- Theranostics dosimetry.
- PACS/RIS replacement.
- LLMs.

## 4. Personas

| Persona | Needs |
|---|---|
| **Radiologist** | Fast triage, heatmap, calibrated confidence, remains signer |
| **Clinical lead** | Label definition, acceptance |
| **Regulatory / compliance** | Locked versions, audit, documentation |
| **Data governance / DPO** | De-identification, per-site isolation |

## 5. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Ingest DICOM (DR/portable/CR) + device metadata | Must |
| FR-2 | De-identification at ingestion | Must |
| FR-3 | nnU-Net segmentation (lung fields + findings) | Must |
| FR-4 | DenseNet multi-head classification | Must |
| FR-5 | Grad-CAM localization per finding | Must |
| FR-6 | Per-site/per-prevalence calibration | Must |
| FR-7 | "Cannot assess" abstention | Must |
| FR-8 | Triage category (routine/priority/urgent) | Must |
| FR-9 | syngo.via overlay (heatmap + confidence + findings) | Must |
| FR-10 | Radiologist accept/adjust/reject → labels | Must |
| FR-11 | Locked model versions + audit logs | Must |
| FR-12 | Per-site monitoring (drift, calibration) | Must |

## 6. Non-functional requirements (summary)

- Inference p95 ≤ 3 s per study.
- ECE ≤ 0.05 per site.
- Availability 99.5%.
- Per-site isolation; India DPDP.
- Regulatory-grade auditability.

See `../03_system_and_architecture/non-functional-requirements.md`.

## 7. Success metrics

- Sensitivity ≥ 0.85 (site-stratified).
- Read-time ↓ 15%.
- Radiologist acceptance ≥ 0.70.
- Subgroup parity ≤ 5 pp.

## 8. Open questions

- Achievable multi-site data access (contracts).
- Federation vs. per-site training.
- Choice of calibration per site/prevalence.