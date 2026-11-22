# Feature Prioritization Roadmap

## 1. Prioritization method

Features scored on **value** (read-time × early detection) vs. **effort** (data readiness + model complexity), with **risk** (regulatory, patient safety) as a gate. Phased to the 2 yrs 8 mos window.

## 2. Roadmap

### Phase 0 — Months 1–2: Foundations
- Select pilot sites: one high-burden TB screening setting + one hospital cohort.
- Extract DICOM + reports; define "actionable findings" + label vocabulary with radiologists.
- Baseline: report turnaround + read-time per study.
- **Gate:** label definition + baseline signed off by clinical lead.

### Phase 1 — Months 3–7: Data & preprocessing platform
- DICOM ingestion + de-identification; device-class capture; MONAI preprocessing.
- NLP-over-reports label extraction + microbiological linkage (TB subset).
- nnU-Net segmentation baseline.
- **Gate:** features/labels reproducible; de-id verified.

### Phase 2 — Months 8–14: Detection & triage models
- nnU-Net + DenseNet multi-head; focal loss; hard-negative mining.
- Grad-CAM localization per finding.
- **Gate:** sensitivity ≥ 0.80 at agreed FPR on random holdout.

### Phase 3 — Months 15–22: Calibration & localization
- Per-site temperature scaling + per-prevalence isotonic; slope/intercept per site.
- IoU evaluation of heatmaps vs. radiologist boxes.
- **Gate:** ECE ≤ 0.05 per site; localization IoU meets threshold.

### Phase 4 — Months 23–28: Site-held-out validation & domain adaptation
- Held-out site; harmonization / device-class adaptation.
- "Cannot assess" for OOD / poor-quality studies.
- **Gate:** site-held-out sensitivity within 5 pp of in-site; no silent miscalibration.

### Phase 5 — Months 29–33: Reader study & silent deployment
- MRMC reader study; prospective silent run.
- Automation-bias measurement; audit every false negative.
- **Gate:** radiologist acceptance ≥ 0.70; read-time ↓ ≥ 15%.

### Phase 6 — Months 34–38: Regulatory-grade hardening & integration
- Locked model versioning, immutable audit logs, syngo.via integration.
- Documentation packages for CE (MDR) / FDA 510(k) / CDSCO.
- **Gate:** audit trail complete; versioned rollback demonstrated.

## 3. Deferred / out of scope

- CT/MR reading.
- Mammography / tomosynthesis.
- Theranostics dosimetry.
- PACS replacement.
- LLMs.