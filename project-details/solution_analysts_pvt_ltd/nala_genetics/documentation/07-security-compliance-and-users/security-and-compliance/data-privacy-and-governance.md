# Data Privacy and Governance

## 1. Data classification

| Class | Examples | Handling |
|---|---|---|
| **Restricted** | Germline VCFs, genomic data | AES-256, access logged, de-identified |
| **Confidential** | Variant classifications, curator actions | Internal access |
| **Internal** | Model configs, schemas | Internal |
| **Public** | Product specs | Unrestricted |

## 2. Privacy principles

- **De-identified data only**; consent coverage verified.
- **No cross-border transfer** of identifiable genomes (UU PDP, PDPA).
- **Data minimization; purpose limitation.**
- **Access control; audit.**

## 3. PII / genomic data handling

- **Encryption:** AES-256 at rest, TLS in transit.
- **De-identification:** before training/evaluation.
- **Consent verification:** documented per dataset.
- **Retention:** per ISO 13485 / privacy policy.

## 4. Retention

| Data | Retention | Disposal |
|---|---|---|
| VCFs | Per policy | Secure delete |
| Triage results | 3 years | Secure delete |
| Review actions | 3 years | Secure delete |
| Audit logs | Per policy (7y) | Archive |

## 5. Compliance mapping

| Regulation / policy | Control |
|---|---|
| ISO 13485 | Traceability, model versioning, no autonomous classification |
| UU PDP (Indonesia) | Consent, data subject rights |
| PDPA (Singapore) | Consent, cross-border transfer controls |
| ISO 27001 | Security controls |

## 6. Data subject requests

- Access / deletion via governance workflow.
- Retention holds respected.

## 7. Cross-border

- No cross-border transfer of identifiable genomes without the governance path.

## 8. Roles

- Data owner (clinical governance), data steward (privacy), DPO.