# Non-Functional Requirements Matrix

## 1. NFR matrix

| ID | Category | Requirement | Target | Verification |
|---|---|---|---|---|
| NFR-P1 | Performance | Inference per study | p95 ≤ 3 s | Load test |
| NFR-P2 | Performance | Worklist triage | Near-real-time | Pipeline monitoring |
| NFR-R1 | Reliability | Availability | 99.5% | Monitoring |
| NFR-R2 | Reliability | Graceful degradation | "Cannot assess" on failure | Chaos test |
| NFR-S1 | Scalability | Study volume | Scale horizontally | Load test |
| NFR-SEC1 | Security | Authentication | SSO / Entra | Audit |
| NFR-SEC2 | Security | Data protection | AES-256, TLS | Audit |
| NFR-SEC3 | Security | Per-site isolation | Row/column + ABAC | Audit |
| NFR-C1 | Compliance | Regulatory (MDR/FDA/CDSCO) | Locked versions, audit | Audit |
| NFR-C2 | Compliance | Auditability | Model version + device + calibration logged | Audit |
| NFR-C3 | Compliance | India DPDP | De-id, consent | Audit |
| NFR-U1 | Usability | Read-time reduction | ↓ 15% relative | Reader study |
| NFR-U2 | Usability | Radiologist acceptance | ≥ 0.70 | Reader study |
| NFR-M1 | Maintainability | Documentation | ADRs + decision log | Review |

## 2. Prioritization

- **Must:** NFR-P1, R1, SEC1-3, C1-3, U2.
- **Should:** NFR-S1, R2, U1.
- **Could:** NFR-P2, M1.

## 3. Verification methods

| Method | Applies to |
|---|---|
| Load test | Performance, scalability |
| Chaos test | Reliability |
| Audit review | Compliance |
| Reader study | Usability |

## 4. Trade-off guidance

- **Calibrated > confident:** every confidence site-calibrated.
- **Auditable > accurate:** locked versions + audit.
- **Radiologist decides > AI decides:** AI prioritizes and second-reads.