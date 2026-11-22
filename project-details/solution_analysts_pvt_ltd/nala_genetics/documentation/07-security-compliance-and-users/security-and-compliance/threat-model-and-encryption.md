# Threat Model and Encryption

## 1. Scope

Threat model for the confidence-scored variant triage service, covering VCFs, annotation, models, curator review, and storage.

## 2. Assets

| Asset | Sensitivity |
|---|---|
| Germline VCFs (genomic data) | Restricted (identifiable / sensitive) |
| Variant classifications | Confidential |
| Curator actions | Confidential |
| Model weights & configs | Internal IP |

## 3. Trust boundaries

```
Curator → VCF upload → Annotate → Features → Classify → Store → Review UI
                              │            │           │
                        VEP/dbNSFP    PostgreSQL   S3
```

## 4. Threats (STRIDE)

| Threat | Example | Mitigation |
|---|---|---|
| **Spoofing** | Stolen credentials | SSO / session auth, MFA |
| **Tampering** | Modified VCF | Checksums; upload validation |
| **Repudiation** | Deny an action | Immutable audit log |
| **Information disclosure** | Genomic data leak | AES-256 at rest, TLS in transit, access logging |
| **Denial of service** | Large VCF flood | Rate limits, size limits |
| **Elevation of privilege** | Access other patients' data | Per-case isolation; RBAC |

## 5. AI-specific threats

| Threat | Mitigation |
|---|---|
| **Confidently wrong classification** | Calibration + mandatory abstention; category-4 tracking |
| **Gene memorization** | Gene-disjoint evaluation |
| **Ancestry bias** | Per-ancestry calibration; ancestry-disjoint evaluation |
| **Model poisoning** | Signed datasets; lineage; access control |
| **Data exfiltration** | De-identified data; no cross-border transfer |

## 6. Encryption

| Layer | In transit | At rest |
|---|---|---|
| Client ↔ server | TLS 1.2+ | — |
| Service ↔ data | TLS | AES-256 (PostgreSQL, S3) |
| Backups | TLS | AES-256 |

## 7. Key management

- Environment-based secrets; rotation policy.
- No secrets in code or logs.

## 8. Monitoring

- Access anomaly detection.
- DLP alerts.
- Audit log review.