# Product Requirements Document (PRD)

## 1. Summary

A confidence-scored document extraction and eligibility-classification service for MyTAXPrepOffice, scoped to the 2016–2017 toolchain. It reduces bad-input defects that drive e-file rejections and amended returns.

## 2. Goals

- Reduce downstream e-file rejections attributable to extraction by ≥ 50%.
- Make uncertainty explicit (calibrated confidence + review queue).
- Keep review fast (median ≤ 8 s/field).
- Produce audit-grade outputs (provenance per field).

## 3. Non-goals

- Tax computation, form generation, e-file transmission.
- Generative advice.
- Handwriting recognition beyond printed forms.
- Autonomous filing.

## 4. Personas

| Persona | Needs |
|---|---|
| **Preparer** | Fast, accurate extraction; review only uncertain fields |
| **Reviewer** | Clear UI: image + confidence + alternatives + downstream fields |
| **Compliance** | Audit trail, PII protection, retention |
| **Data science** | Labeled corpus, eval harness |

## 5. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Ingest PDF/TIFF uploads (W-2, 1099 series, K-1, SSA-1099, 1098 series) | Must |
| FR-2 | Preprocess (deskew, denoise, binarize) | Must |
| FR-3 | OCR with token-level confidence | Must |
| FR-4 | Layout segmentation per form type | Must |
| FR-5 | Field extraction (BiLSTM-CRF + pointer network) | Must |
| FR-6 | Document-type + dependent-category classification | Must |
| FR-7 | Per-field calibrated confidence | Must |
| FR-8 | Routing: auto-fill above τ, review queue below τ | Must |
| FR-9 | Reviewer UI (image, value, confidence, alternatives, downstream fields) | Must |
| FR-10 | Log every reviewer action as a training label | Must |
| FR-11 | Structured JSON output to return engine | Must |
| FR-12 | Audit trail (field → confidence → provenance) | Must |

## 6. Non-functional requirements (summary)

- Extraction p95 ≤ 2 s per document.
- Field precision ≥ 0.98; ECE ≤ 0.05.
- Review ≤ 0.20 fields/document; median ≤ 8 s/field.
- PII: AES-256 at rest, TLS in transit, access logged.
- Availability 99.5% in filing season.

See `../03_system_and_architecture/non-functional-requirements.md`.

## 7. Success metrics

- Downstream reject rate ↓ 50% (primary).
- Auto-accept rate ≥ 0.80.
- Review queue load ≤ 0.20.
- Calibration error ≤ 0.05.

## 8. Open questions

- Exact field schema per document type.
- Threshold policy per field type (cost asymmetry).
- Cloud OCR vendor terms (no training on customer data).