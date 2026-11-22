# System Design Document

## 1. Context

This document specifies the as-built design of the confidence-scored document extraction service for MyTAXPrepOffice, scoped to the 2016–2017 toolchain. It complements `../01-business-and-strategy/high-level-solution-overview.md` (business view).

## 2. Goals & non-goals

**Goals:** calibrated, auditable field extraction; human review of uncertain fields; low review time; integration with the existing return engine.

**Non-goals:** tax computation, generative advice, handwriting recognition, autonomous filing.

## 3. Component design

| Stage | Component | Technology | Responsibility |
|---|---|---|---|
| 1 | Preprocess | OpenCV 3, ImageMagick | Deskew, denoise, binarize |
| 2 | OCR | Tesseract 4 (LSTM), Google Cloud Vision | Words + bounding boxes + token confidence |
| 3 | Layout segmentation | Rule-based (per form type) | Region detection |
| 4 | Field extraction | BiLSTM-CRF + pointer network (TF 1.0/Keras) | Line tagging + span copying |
| 5 | Classification | CNN/fastText, gradient-boosted trees | Doc type + dependent category |
| 6 | Calibration | Isotonic / Platt (scikit-learn) | Raw scores → probabilities |
| 7 | Routing | Rule engine | Auto-fill vs. review queue |
| 8 | Serving | Flask + gunicorn, Redis queue | API + async processing |

## 4. Data flow

1. **Upload** — PDF/TIFF to upload service.
2. **Preprocess** — OpenCV pipeline.
3. **OCR** — Tesseract local, Cloud Vision fallback; token confidence persisted.
4. **Segment** — normalized-coordinate rules per form type + token anchoring.
5. **Extract** — BiLSTM-CRF + pointer network; synthetic augmentation in training.
6. **Classify** — CNN over OCR tokens; GBM over interpretable features.
7. **Calibrate** — isotonic regression on held-out labeled set.
8. **Route** — per-field τ; below τ → review queue.
9. **Commit** — JSON payload → return engine; audit logged.

## 5. Component notes

- **Preprocessing:** tax documents are scanned faxes/phone photos in the independent-preparer segment. Deskew + binarization measurably lift OCR accuracy; non-negotiable first stage.
- **OCR:** Tesseract LSTM is local, free, adequate for printed forms; Cloud Vision fallback for degraded scans. Persist per-token confidence (a feature for calibration).
- **Layout segmentation:** forms are semi-structured (fixed box positions, varying scan offsets). Hybrid of normalized-coordinate rules + OCR token anchoring.
- **Field extraction:** two-model stack — BiLSTM-CRF for line-level tagging; pointer network for span copying. Train on synthetically augmented real scans.
- **Classification:** doc type via CNN over OCR token sequence (fastText baseline); dependent category via gradient-boosted trees over interpretable features (DOB, age at year end, relationship, student status, months in household).
- **Confidence:** raw scores are not probabilities; isotonic regression on held-out labeled set. Report calibrated probability + OCR token confidence so reviewers see *why* the system is unsure.

## 6. Deployment topology

- **Single new deployable** behind the existing API gateway.
- **Services:** extraction API (Flask + gunicorn), Redis queue for async jobs, PostgreSQL (fields/audit), S3-compatible (documents).
- **Review UI:** server-rendered + small JS layer (no SPA framework needed).

## 7. Key design decisions

See `decision-log.md` and `architecture-decision-records/`.

## 8. Risks & mitigations

| Risk | Mitigation |
|---|---|
| Confidently wrong extraction | Calibration + mandatory review; category-5 tracking |
| Scan quality | Synthetic degradation; cloud OCR fallback |
| Label noise | Human verification on stratified sample |
| Review queue bottleneck | Efficiency gate ≤ 8 s/field; per-field thresholds |
| Scope creep into computation | Hard boundary — emits fields, never computed tax |

## 9. Related

- `../02-product-and-ux/product-requirements-doc.md`
- `non-functional-requirements.md`
- `integration-and-data-strategy.md`