# Glossary and Terminology

## Domain

| Term | Definition |
|---|---|
| **Preparer** | A paid tax professional who prepares returns for clients (as opposed to a consumer). |
| **Return** | A filed tax return (1040, 1065, 1120, etc.). |
| **E-file** | Electronic filing via IRS/ATO. |
| **Acknowledgement (ack)** | IRS confirmation that a return was accepted. |
| **Rejection** | IRS refusal; identifies the field that failed validation. |
| **Amended return** | A corrected re-filing; post-hoc evidence of an extraction/classification defect. |
| **EFIN** | Electronic Filing Identification Number. |
| **WISP** | Written Information Security Plan (IRS requirement). |
| **Bank product** | Refund-transfer / fee-withholding product (SBTPG, EPS, etc.). |
| **Schedule** | A specific IRS form (e.g., NJ SCH-HCC, federal Schedule 1-A). |

## Technical

| Term | Definition |
|---|---|
| **OCR** | Optical Character Recognition (Tesseract, Google Cloud Vision). |
| **BiLSTM-CRF** | Bidirectional LSTM + Conditional Random Field — sequence labeling for field extraction. |
| **Pointer network** | Neural model that copies values (spans) out of a document. |
| **Sequence labeling** | Tagging each token with a field label. |
| **Span extraction** | Identifying the start/end of a value in text. |
| **Calibration** | Mapping raw model scores to probabilities (isotonic/Platt scaling). |
| **ECE** | Expected Calibration Error — measures calibration quality. |
| **Confidence threshold (τ)** | Per-field cutoff below which a value routes to human review. |
| **Human-in-the-loop** | Human review of low-confidence extractions. |
| **Synthetic augmentation** | Degrading clean forms (skew, blur, noise) to match real scans. |
| **Point-in-time correctness** | Using only data available at prediction time. |
| **Shadow deployment** | Running in parallel without auto-fill, comparing to human entry. |

## Abbreviations

| Abbreviation | Expansion |
|---|---|
| OCR | Optical Character Recognition |
| BiLSTM | Bidirectional Long Short-Term Memory |
| CRF | Conditional Random Field |
| ECE | Expected Calibration Error |
| PII | Personally Identifiable Information |
| TIN | Taxpayer Identification Number |
| WISP | Written Information Security Plan |
| SLA | Service Level Agreement |
| NFR | Non-Functional Requirement |
| ADR | Architecture Decision Record |