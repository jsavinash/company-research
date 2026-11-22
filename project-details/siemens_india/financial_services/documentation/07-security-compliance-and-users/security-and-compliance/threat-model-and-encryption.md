# Threat Model and Encryption

## 1. Scope

Threat model for the credit-risk early-warning platform, covering credit data, telemetry, models, and scoring.

## 2. Assets

| Asset | Sensitivity |
|---|---|
| Credit book (contracts, payments, DPD) | Restricted (financial) |
| Operational telemetry | Restricted (customer/asset) |
| PD scores + reason codes | Confidential |
| Model weights & configs | Internal IP |

## 3. Trust boundaries

```
SFS credit ─┐
Telemetry ──┼─▶ Kafka → Spark → feature store → models → watchlist
Finance ────┘
```

## 4. Threats (STRIDE)

| Threat | Example | Mitigation |
|---|---|---|
| **Spoofing** | Stolen credentials | SSO / Entra, MFA |
| **Tampering** | Modified telemetry | Schema validation, checksums |
| **Repudiation** | Deny an action | Immutable audit log |
| **Information disclosure** | Cross-entity data leak | Per-entity isolation; ABAC |
| **Denial of service** | Scoring flood | Rate limits |
| **Elevation of privilege** | Access other entities' data | Tenant isolation |

## 5. AI-specific threats

| Threat | Mitigation |
|---|---|
| **Black-box / no reason codes** | SHAP reason codes mandatory |
| **Uncalibrated PD** | Calibration + ECE monitoring |
| **Concept drift** | PSI + calibration monitoring |
| **Model poisoning** | Signed datasets; lineage |
| **Cross-entity data pooling** | Per-entity isolation; DPDP |

## 6. Encryption

| Layer | In transit | At rest |
|---|---|---|
| Client ↔ API | TLS 1.2+ | — |
| Service ↔ data | TLS | AES-256 |
| Backups | TLS | AES-256 |

## 7. Key management

- Vault; rotation policy.
- No secrets in code or logs.

## 8. Monitoring

- Access anomaly detection.
- DLP alerts.
- Audit log review.