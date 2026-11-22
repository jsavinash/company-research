# Non-Functional Requirements Matrix

## 1. NFR matrix

| ID | Category | Requirement | Target | Verification |
|---|---|---|---|---|
| NFR-P1 | Performance | Scoring API (on-demand) | p95 ≤ 5 s per account | Load test |
| NFR-P2 | Performance | Batch scoring | Nightly | Airflow logs |
| NFR-R1 | Reliability | Availability | 99.5% | Monitoring |
| NFR-R2 | Reliability | Graceful degradation | Last-good / flag on failure | Chaos test |
| NFR-S1 | Scalability | Book-scale scoring | Scale horizontally | Load test |
| NFR-SEC1 | Security | Authentication | SSO / Entra | Audit |
| NFR-SEC2 | Security | Data protection | AES-256, TLS | Audit |
| NFR-SEC3 | Security | Per-entity isolation | Row/column-level + ABAC | Audit |
| NFR-C1 | Compliance | Model risk (SR 11-7) | Versioned, validated, documented | Audit |
| NFR-C2 | Compliance | Reason codes | Every PD has SHAP reason codes | Audit |
| NFR-C3 | Compliance | Bias/fairness | Checks across segments | Audit |
| NFR-C4 | Compliance | India DPDP | Consent, residency | Audit |
| NFR-U1 | Usability | Officer actionability | Reason codes officer-rated ≥ 0.70 | Survey |
| NFR-M1 | Maintainability | Documentation | ADRs + decision log | Review |

## 2. Prioritization

- **Must:** NFR-P1, R1, SEC1-3, C1-4, U1.
- **Should:** NFR-S1, R2, P2.
- **Could:** NFR-M1.

## 3. Verification methods

| Method | Applies to |
|---|---|
| Load test | Performance, scalability |
| Chaos test | Reliability |
| Audit review | Compliance |
| Bias testing | Fairness |

## 4. Trade-off guidance

- **Calibrated > confident:** every PD calibrated.
- **Auditable > accurate:** reason codes + governance.
- **Human decision > automation:** credit officer decides.