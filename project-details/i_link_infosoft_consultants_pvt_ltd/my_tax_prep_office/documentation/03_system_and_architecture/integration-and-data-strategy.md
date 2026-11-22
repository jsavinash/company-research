# Integration and Data Strategy

## 1. Data sources

| Source | Type | Freshness | Notes |
|---|---|---|---|
| E-file acknowledgements | Structured | Per filing | Which returns were accepted |
| Rejections | Structured | Per filing | Which field failed validation |
| Amended returns | Structured | Post-filing | Evidence of extraction/classification defects |
| Prior-year return data | Structured | Annual | Ground-truth field values |
| Support tickets | Unstructured | Daily | Natural-language reports of extraction failures |
| Uploaded documents | Unstructured (PDF/TIFF) | Real-time | W-2, 1099, K-1, SSA-1099, 1098 |

## 2. Labeling corpus

The company holds a corpus no outside vendor could assemble:

| Source | Label value |
|---|---|
| E-file acknowledgements | Which returns were accepted |
| Rejections | Which field failed validation, and why |
| Amended returns | Post-hoc evidence of a defect |
| Prior-year return data | Ground-truth field values for re-filed documents |
| Support tickets | Natural-language reports of extraction failures |

## 3. Label construction

1. **Field-level ground truth** from the return as filed and accepted (ack without amendment → filed value correct).
2. **Defect labels** from amendments/rejections: diff the amended return against the original.
3. **Synthetic augmentation**: render clean forms, then degrade (skew, blur, noise, JPEG artifacts, low DPI).
4. **Human verification** on a stratified sample (ack-without-amendment is a noisy proxy).

## 4. Data handling constraints

- Tax documents contain PII and TINs. Data at rest encrypted (AES-256), in transit TLS.
- Access limited to named reviewers; every access logged.
- Documents retained per WISP obligations; extraction artifacts purged on a schedule.
- **No third-party training on customer documents.** Vendor OCR only; no vendor model training.

## 5. Integration architecture

```
Upload → Preprocess → OCR → Segment → Extract → Classify → Calibrate → Route → Return engine
                                    │                                  │
                              PostgreSQL (fields/audit)          Review queue (UI)
```

## 6. Integration with existing systems

| System | Purpose | Protocol |
|---|---|---|
| MyTAXPrepOffice API (Express) | Return engine, client data | REST |
| PostgreSQL | Fields, audit, config | SQL |
| S3-compatible | Document storage | S3 API |
| Redis | Async job queue | Redis protocol |

## 7. Data governance

- **Ownership:** Data science + compliance.
- **Lineage:** every field carries provenance (source doc, OCR token, model version).
- **Retention:** per WISP schedule.
- **Access:** role-based + logged.