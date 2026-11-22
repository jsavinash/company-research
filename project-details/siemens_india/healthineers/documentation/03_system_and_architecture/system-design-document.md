# System Design Document

## 1. Context

This document specifies the as-built design of the chest-radiograph triage and calibrated CAD capability for Siemens Healthineers, scoped to the 2019–2022 toolchain. It complements `../01-business-and-strategy/high-level-solution-overview.md` (business view).

## 2. Goals & non-goals

**Goals:** worklist triage; calibrated CAD; radiologist-in-the-loop; regulatory-grade audit.

**Non-goals:** autonomous diagnosis, CT/MR, mammography, theranostics, PACS replacement, LLMs.

## 3. Component design

| Stage | Component | Technology | Responsibility |
|---|---|---|---|
| 1 | Ingestion + de-id | pydicom, SimpleITK, MONAI | DICOM ingest, PHI scrub, device metadata |
| 2 | Segmentation | nnU-Net | Lung fields + findings |
| 3 | Classification | PyTorch 1.x, DenseNet/ResNet | Multi-finding heads |
| 4 | Explainability | Grad-CAM | Localization heatmaps |
| 5 | Calibration | Temperature scaling, isotonic | Per-site/per-prevalence confidence |
| 6 | Triage | Rule engine | Worklist category |
| 7 | Presentation | syngo.via | Overlay |
| 8 | Training/registry | MONAI, MLflow, Airflow/Kubeflow | Pipelines + registry |
| 9 | Monitoring | Prometheus/Grafana | Site-level drift |

## 4. Data flow

1. **Ingest** — DICOM + de-id + device metadata.
4. **Segment** — nnU-Net.
5. **Classify** — DenseNet multi-head.
6. **Localize** — Grad-CAM.
7. **Calibrate** — per-site temperature + per-prevalence isotonic.
8. **Triage** — worklist reorder.
9. **Present** — syngo.via overlay.
10. **Feedback** — radiologist accept/adjust/reject → labels → locked retrain.

## 5. Component notes

- **Ingestion and device class.** DICOM is the input and label carrier. Device class (fixed DR / portable / CR), acquisition parameters, site ID are captured as features — because domain shift across exactly these dimensions is the dominant real-world failure mode.
- **Inference core.** nnU-Net (segmentation) + DenseNet multi-head (classification). Era-standard, intentionally not novel — the novelty is calibration and workflow.
- **Calibration layer — the differentiator.** A global model is trained once, then **per-site temperature scaling and per-prevalence isotonic calibration** are fitted on local labelled data. The same image gets a different, correct probability at a hospital clinic vs. a rural screening camp.
- **Triage and presentation.** Output is a worklist reorder + syngo.via overlay (heatmap + calibrated confidence + finding list + similar prior cases). The radiologist always reads the image; the AI never suppresses a study.

## 6. Deployment topology

- **Kubernetes** (Docker) for inference + training.
- **MONAI** for DICOM/transforms; **MLflow** registry; **Airflow/Kubeflow** pipelines.
- **syngo.via** integration at the reading surface.
- **Prometheus/Grafana** for site-level monitoring.

## 7. Key design decisions

See `decision-log.md` and `architecture-decision-records/`.

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Prevalence shift → miscalibration at screening | Per-site/per-prevalence calibration; site-held-out validation |
| Domain shift (sites/devices) | Device-class features; harmonization; subgroup parity |
| Automation bias | Reader study; AI as triage not truth |
| Label noise | NLP + microbio linkage; adjudicated eval set |
| Regulatory (MDR/FDA/CDSCO) | Locked versions; audit logs; documentation |

## 9. Related

- `../02-product-and-ux/product-requirements-doc.md`
- `non-functional-requirements.md`
- `integration-and-data-strategy.md`