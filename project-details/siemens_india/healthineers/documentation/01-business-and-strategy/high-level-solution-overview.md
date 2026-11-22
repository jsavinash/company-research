# High-Level Solution Overview

## 1. One-line description

> A chest-radiograph triage and calibrated computer-aided detection (CAD) capability: it ingests chest X-rays from the installed base, prioritizes the worklist by likelihood of actionable disease, localizes findings, attaches a *site-calibrated* confidence, and keeps the radiologist as the diagnostic authority — delivered as a companion on syngo.via.

## 2. Core design decision

**Per-site / per-prevalence calibration is the differentiator.** A model calibrated on a symptomatic hospital cohort is badly miscalibrated for screening (prevalence 1–2 orders of magnitude lower). The same image must get a different, correct probability at a hospital clinic vs. a rural screening camp. And **the radiologist always decides** — AI prioritizes and second-reads.

## 3. Architecture at a glance

```
Acquisition (installed base): DR / portable / CR chest X-ray → DICOM
   ▼
Ingestion + de-identification: pydicom / SimpleITK → MONAI transforms; PHI scrub; device class + acquisition metadata
   ▼
Inference core (per study): nnU-Net (lung/field + finding segmentation) + DenseNet (multi-finding heads) + Grad-CAM (heatmaps)
   ▼
Calibration layer (differentiator): per-site / per-device temperature scaling + per-prevalence isotonic + "cannot assess" gate
   ▼
Triage + presentation: worklist category (routine/priority/urgent) + syngo.via overlay (heatmap + confidence + finding list + similar prior cases)
   ▼
Radiologist reads + signs: final report + action code; feedback (accept/adjust/reject) → labels → locked-model retrain
```

## 4. The stages

| Stage | Purpose | Key tech |
|---|---|---|
| **Ingestion** | DICOM + de-id + device metadata | pydicom, SimpleITK, MONAI |
| **Inference core** | Segmentation + classification | nnU-Net, DenseNet, Grad-CAM |
| **Calibration** | Site-calibrated confidence | Temperature scaling, isotonic |
| **Triage** | Worklist reorder | Rule engine |
| **Presentation** | syngo.via overlay | syngo.via |
| **Feedback** | Labels + locked retrain | MLflow, Airflow/Kubeflow |

## 5. Why this was buildable in Aug 2019 – Mar 2022

| Capability | Availability | Use |
|---|---|---|
| 2D CNNs (DenseNet, ResNet) | Mature | Classification |
| nnU-Net | Preprint 2018/19, Nature Methods 2021 | Segmentation |
| Transfer learning (ImageNet) | Standard | Low-label regimes |
| Class imbalance | Focal loss, hard-negative mining | Rare actionable findings |
| Calibration | Temperature scaling, isotonic | Per-site probability |
| Explainability | Grad-CAM | Localization heatmaps |
| Medical imaging framework | **MONAI (Dec 2019)** | DICOM, transforms, training |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | Airflow 1.10, **Kubeflow 1.0 (2020)** | Pipelines |
| Multi-site learning | NVIDIA Clara | Optional federation |
| Generative LLMs | GPT-3 (2020) — no imaging role | **Excluded** |

**Excluded:** GPT-family / any LLM (no role in imaging), any black-box model without localization, any autonomous reporting.

See `../03_system_and_architecture/system-design-document.md` for the detailed design.