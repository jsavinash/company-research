# Threat Model and Encryption

## 1. Scope

Threat model for the chest triage / CAD platform, covering DICOM, PHI, models, and inference.

## 2. Assets

| Asset | Sensitivity |
|---|---|
| DICOM studies (PHI) | Restricted (patient data) |
| Findings + heatmaps | Confidential |
| Calibration sets + model weights | Internal IP |
| Audit logs | Confidential |

## 3. Trust boundaries

```
Scanner/PACS → Ingestion → MONAI → nnU-Net/DenseNet → calibration → syngo.via
                     │            │              │
                 de-id        GPU cluster    model registry
```

## 4. Threats (STRIDE)

| Threat | Example | Mitigation |
|---|---|---|
| **Spoofing** | Stolen credentials | SSO / Entra, MFA |
| **Tampering** | Modified DICOM | Checksums; ingestion validation |
| **Repudiation** | Deny an action | Immutable audit log |
| **Information disclosure** | PHI leak | De-id at ingest; AES-256; access logging |
| **Denial of service** | Study flood | Rate limits |
| **Elevation of privilege** | Access other sites' data | Per-site isolation |

## 5. AI-specific threats

| Threat | Mitigation |
|---|---|
| **Confidently wrong (miscalibration)** | Per-site calibration; ECE gate |
| **Domain shift** | Site-held-out validation; device-class features |
| **Automation bias** | Reader study; AI as triage not truth |
| **Black-box output** | Grad-CAM localization mandatory |
| **Label poisoning** | Signed datasets; lineage |
| **PHI in prompts** | De-id; no PHI in prompts |

## 6. Encryption

| Layer | In transit | At rest |
|---|---|---|
| Scanner ↔ API | TLS 1.2+ | — |
| Service ↔ data | TLS | AES-256 |
| Backups | TLS | AES-256 |

## 7. Key management

- Vault; rotation policy.
- No secrets in code or logs.

## 8. Monitoring

- Access anomaly detection.
- DLP alerts.
- Audit log review.