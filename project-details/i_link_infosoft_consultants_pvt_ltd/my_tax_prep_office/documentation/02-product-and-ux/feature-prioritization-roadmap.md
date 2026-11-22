# Feature Prioritization Roadmap

## 1. Prioritization method

Features scored on **value** (reject-rate reduction × adoption) vs. **effort** (data readiness + model complexity), with **risk** (PII/regulatory) as a gate. Phased to the 8-month window.

## 2. Roadmap

### Phase 0 — Weeks 1–3: Foundations
- Assemble labeled corpus (acknowledgements, rejections, amendments).
- Define field schema (JSON) per document type.
- Build evaluation harness + baseline metrics.
- **Gate:** baseline reject rate + manual-extraction error rate measured.

### Phase 1 — Weeks 4–9: OCR + rule baseline
- Preprocessing pipeline.
- Tesseract + layout segmentation.
- Regex/coordinate rules for high-confidence fields.
- **Gate:** ≥ 0.90 field precision on clean scans.

### Phase 2 — Weeks 10–17: Learned extraction
- BiLSTM-CRF sequence labeler.
- Pointer network for span values.
- Document-type classifier.
- **Gate:** ≥ 0.95 field precision on degraded scans.

### Phase 3 — Weeks 18–25: Classification + confidence
- Dependent-category classifier.
- Confidence calibration.
- Threshold policy per field type.
- **Gate:** ECE ≤ 0.05; auto-accept ≥ 0.75.

### Phase 4 — Weeks 26–31: Review queue
- Reviewer UI.
- Log every reviewer action as a training label.
- Efficiency measurement.
- **Gate:** median review ≤ 8 s/field.

### Phase 5 — Weeks 32–35: Shadow deployment
- Run in parallel with manual entry, no auto-fill.
- Compare extraction output against what preparers actually entered.
- **Gate:** downstream reject rate ↓ 50% in shadow measurement.

## 3. Deferred / out of scope

- Handwriting recognition.
- Spanish-language layouts (phase-2).
- Tax computation (existing engine).
- Generative assistance (excluded by design).