# Threat Model and Encryption

## 1. Scope

Threat model for the confidence-scored tax document extraction service, covering uploads, OCR, extraction, storage, and review.

## 2. Assets

| Asset | Sensitivity |
|---|---|
| Tax documents (W-2, 1099, K-1) | Restricted (PII + TIN) |
| Extracted field values | Confidential |
| Review actions | Confidential |
| Model weights & configs | Internal IP |

## 3. Trust boundaries

```
Preparer → Upload → Preprocess → OCR → Extract → Store → Review UI
                         │          │         │
                    local OCR   cloud OCR   PostgreSQL
```

## 4. Threats (STRIDE)

| Threat | Example | Mitigation |
|---|---|---|
| **Spoofing** | Stolen credentials | Signed session cookie (`mtpo.sid`), HttpOnly/Secure/SameSite |
| **Tampering** | Modified documents | Upload validation; checksums |
| **Repudiation** | Deny an action | Immutable audit log |
| **Information disclosure** | PII/TIN leak | AES-256 at rest, TLS in transit, access logging |
| **Denial of service** | Upload flood | Rate limits, size limits |
| **Elevation of privilege** | Access other firms' docs | Per-office isolation; RBAC |

## 5. AI-specific threats

| Threat | Mitigation |
|---|---|
| **Confidently wrong extraction** | Calibration + mandatory review; category-5 tracking |
| **Prompt-injection (n/a)** | No LLM in the extraction path |
| **Data exfiltration** | Local-first OCR; cloud fallback only when needed; no vendor training |
| **Model poisoning** | Signed datasets; lineage; access control |

## 6. Encryption

| Layer | In transit | At rest |
|---|---|---|
| Browser ↔ server | TLS 1.2+ | — |
| Service ↔ data | TLS | AES-256 (PostgreSQL, S3) |
| Backups | TLS | AES-256 |

## 7. Key management

- Environment-based secrets; rotation policy.
- No secrets in code or logs.

## 8. Monitoring

- Access anomaly detection.
- DLP alerts.
- Audit log review.