# Low-Level Design Specs

## 1. Inference service

**Input:** DICOM study + site/device metadata.
**Output:** triage category + finding list + heatmaps + site-calibrated confidence + abstention.

```
infer(study) -> InferenceResult
  1. preprocess(study)            # MONAI transforms; de-id
  2. seg = nnunet.segment(study)  # lung fields + findings
  3. cls = densenet.classify(seg) # multi-finding heads
  4. maps = gradcam(cls)          # per-finding heatmaps
  5. conf = calibrate(cls, site)  # per-site/per-prevalence
  6. triage = worklist_category(cls, conf)
  7. return InferenceResult
```

## 2. Segmentation (nnU-Net)

- Self-configuring; lung fields + findings.
- Era-standard; reproducible.

## 3. Classification (DenseNet)

- Multi-head per finding (TB, nodule, consolidation, effusion, pneumothorax, cardiomegaly).
- Focal loss + hard-negative mining.

## 8. Localization (Grad-CAM)

- Per-finding heatmaps overlaid on the image.
- IoU evaluated vs. radiologist boxes.

## 5. Calibration

- Per-site temperature scaling + per-prevalence isotonic.
- "Cannot assess" gate (quality/coverage).
- Calibration slope/intercept per site.

## 6. Triage

- Routine / priority / urgent.
- Rule-based on calibrated confidence + finding type.

## 7. Error handling

| Error | Handling |
|---|---|
| Poor image quality | "Cannot assess" (abstain) |
| OOD site | Flag; no confident score |
| Rare finding | "Cannot assess"; never overclaim |
| Model failure | Fall back to worklist-only |

## 8. Observability

- MLflow registry + lineage.
- Per-site monitoring (drift, calibration).
- Audit logs (model version, device, calibration set).