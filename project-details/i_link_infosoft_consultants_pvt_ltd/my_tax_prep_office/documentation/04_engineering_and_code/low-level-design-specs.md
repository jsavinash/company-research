# Low-Level Design Specs

## 1. Extraction service

**Input:** document (PDF/TIFF) + document type hint (optional).
**Output:** structured fields with per-field confidence + provenance.

```
extract(document) -> ExtractionResult
  1. preprocess(document)          # OpenCV: deskew, denoise, binarize
  2. ocr = run_ocr(document)       # Tesseract + Cloud Vision fallback
  3. regions = segment(ocr)        # rule-based per form type
  4. fields = extract_fields(ocr, regions)  # BiLSTM-CRF + pointer net
  5. doc_type = classify_type(ocr) # CNN / fastText
  6. for each field: confidence = calibrate(score)
  7. route: score >= tau ? auto-fill : review queue
  8. return JSON
```

## 2. Field extraction model

- **BiLSTM-CRF** for line-level tagging (each token → field label).
- **Pointer network** for span copying where the value is not a simple tagged token.
- **Training:** synthetically augmented real scans (skew, blur, noise, JPEG, low DPI).

## 3. Classification

| Classifier | Method | Features |
|---|---|---|
| **Document type** | CNN over OCR token sequence (fastText baseline) | Token sequence |
| **Dependent category** | Gradient-boosted trees | DOB, age at year end, relationship, student status, months in household |

## 4. Confidence calibration

- **Isotonic regression** on a held-out labeled set.
- Report **calibrated probability** + **OCR token confidence** (so reviewers see *why* the system is unsure).
- Track **ECE** (Expected Calibration Error) ≤ 0.05.

## 5. Routing / thresholds

- **Per-field τ** by cost asymmetry:
  - High-cost (TIN, dependent DOB, relationship): high τ, aggressive review.
  - Low-cost (payer address): lower τ, auto-accept.
- τ reviewed monthly against observed defect cost.

## 6. Review queue

- Reviewer sees: image + highlighted region, value + confidence, OCR token confidence, ranked alternatives, downstream fields.
- Actions: accept / correct / reject-document → logged as training label.
- Efficiency gate: median ≤ 8 s/field.

## 7. Error handling

| Error | Handling |
|---|---|
| OCR failure | Cloud fallback; lower confidence → review |
| Layout unknown | Rule-based fails → review |
| Model failure | Degrade to last-good / manual |
| Low confidence | Review queue (never auto-commit) |

## 8. Observability

- Log every extraction with run ID + model version.
- Track category-5 errors (confidently wrong) separately.
- Monitor review queue load + review time.