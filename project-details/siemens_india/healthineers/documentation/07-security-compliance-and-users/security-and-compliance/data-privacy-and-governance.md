# Data Privacy and Governance

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | DICOM (PHI), patient data | AES-256, de-id, access logged, per-site isolation |
| **Confidential** | Findings, heatmaps, audit | Internal access |
| **Internal** | Model configs, calibration sets | Internal |
| **Public** | Product specs | Unrestricted |

## 2. Privacy principles

- **Per-site data isolation;** no cross-site raw-PHI training without governance (federation or per-site).
- **De-identification** at ingestion (DICOM tag scrub, burned-in annotation handling).
- **India DPDP Act** obligations; some sites on-premise only.
- **Data minimization; purpose limitation.**

## 3. PII handling

- **De-identification** before training/analytics.
- **Encryption:** AES-256 at rest, TLS in transit.
- **Access control:** ABAC + per-site.

## 4. Retention

| Data | Retention | Disposal |
|---|---|---|
| DICOM | Per policy | Secure delete |
| Findings | 2 years | Secure delete |
| Audit logs | Per policy (7y) | Archive |
| Model artifacts | Versioned, 2 years | Archive |

## 5. Compliance mapping

| Regulation / policy | Control |
|---|---|
| EU MDR (May 2021) | Locked versions, audit, documentation |
| FDA 510(k) | Validation, documentation |
| CDSCO (India) | Registration, quality |
| India DPDP Act | Consent, de-id, residency |
| HIPAA (if applicable) | PHI protection |

## 6. Model governance

- **Locked model versions** with immutable prediction logs (model version, device class, calibration set).
- **Audit trail** for every study.
- **Bias/fairness** checks across subgroups.

## 7. Roles

- Clinical owner, data steward, DPO, regulatory affairs.