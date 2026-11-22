# High-Level Solution Overview

## 1. One-line description

> A confidence-scored document extraction and eligibility-classification service that converts uploaded tax source documents into structured field values, attaches a calibrated confidence to every field, and routes low-confidence fields to a human review queue before they are committed to a return.

## 2. Core design decision

**The system never silently accepts a value it is unsure about.** Confidence is calibrated, uncertainty is explicit, and low-confidence fields go to a human. This is a hard product constraint, not a tuning preference.

## 3. Architecture at a glance

```
upload (PDF/TIFF)
   │
   ▼
1. Preprocess (deskew, denoise, binarize)        OpenCV / ImageMagick
   │
   ▼
2. OCR (Tesseract 4 LSTM + Cloud Vision fallback) words + bounding boxes
   │
   ▼
3. Layout segmentation (rule-based regions)      box coordinates per form type
   │
   ▼
4. Field extraction (BiLSTM-CRF + pointer net)   TensorFlow 1.0 / Keras
   │
   ▼
5. Classification (doc type CNN/fastText;        scikit-learn GBM
   dependent category GBM)
   │
   ▼
6. Confidence calibration (isotonic/Platt)       scikit-learn
   │
   ▼
7. Routing (score ≥ τ → auto-fill;               per-field thresholds
   score < τ → review queue)
   │
   ▼
8. Structured output (JSON → return engine)
```

## 4. The eight stages

| Stage | Purpose | Key tech |
|---|---|---|
| **Preprocess** | Deskew, denoise, binarize | OpenCV 3, ImageMagick |
| **OCR** | Words + bounding boxes + token confidence | Tesseract 4 (LSTM), Google Cloud Vision |
| **Layout segmentation** | Region detection per form type | Rule-based coordinates + token anchoring |
| **Field extraction** | Line-level tagging + span copying | BiLSTM-CRF, pointer network (TF 1.0/Keras) |
| **Classification** | Doc type + dependent category | CNN/fastText, gradient-boosted trees |
| **Confidence calibration** | Raw scores → probabilities | Isotonic / Platt scaling |
| **Routing** | Auto-fill vs. review queue | Per-field thresholds (τ) |
| **Structured output** | JSON payload to return engine | Flask + gunicorn |

## 5. Why this is the right 2016–2017 intervention

| Capability | 2016–2017 availability | Relevance |
|---|---|---|
| OCR | Production-grade (Tesseract, Cloud Vision) | Required first stage |
| Sequence labeling | BiLSTM-CRF (Lample et al., 2016) | Field extraction |
| Structured extraction | Pointer networks (Vinyals et al., 2015) | Copying values |
| Text classification | CNN (Kim, 2014), fastText (2016) | Doc-type routing |
| Tabular ML | Gradient boosting, logistic regression | Calibration, reject prediction |
| Generative text | **Not usable** | Excluded by design |

**No generative component.** This is both a technical constraint of the period and a correctness requirement for tax data.

See `../03_system_and_architecture/system-design-document.md` for the detailed design.