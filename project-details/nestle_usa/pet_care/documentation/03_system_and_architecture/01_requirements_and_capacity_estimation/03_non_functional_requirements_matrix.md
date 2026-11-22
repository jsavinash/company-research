# Non-Functional Requirements Matrix

## 1. NFR matrix

| ID | Category | Requirement | Target | Verification |
|---|---|---|---|---|
| NFR-P1 | Performance | Copilot interactive | p95 ≤ 5 s | Load test |
| NFR-P2 | Performance | Intake→coach | ≤ a few seconds | Load test |
| NFR-R1 | Reliability | Availability | 99.9% | Monitoring |
| NFR-R2 | Reliability | Graceful degradation | Cached / generic / form-only | Chaos test |
| NFR-S1 | Scalability | Concurrent owners | Scale horizontally | Load test |
| NFR-SEC1 | Security | Authentication | Entra ID SSO | Audit |
| NFR-SEC2 | Security | PII | No PII in prompts/logs | DLP scan |
| NFR-SEC3 | Security | Per-owner isolation | ABAC | Audit |
| NFR-C1 | Compliance | Auditability | Every claim traceable | Audit |
| NFR-C2 | Compliance | Model governance | Versioned prompts/models | Audit |
| NFR-U1 | Usability | Comprehension | ≥ 4.0/5 | Survey |
| NFR-U2 | Accessibility | WCAG 2.1 AA | Pass | Audit |
| NFR-M1 | Maintainability | Documentation | ADRs + decision log | Review |

## 2. Prioritization

- **Must:** NFR-P1, R1, SEC1-3, C1.
- **Should:** NFR-S1, R2, U1.
- **Could:** NFR-P2, U2, M1.

## 5. Verification methods

| Method | Applies to |
|---|---|
| Load test | Performance, scalability |
| Chaos test | Reliability |
| DLP scan | Security |
| Audit review | Compliance |
| Survey | Usability |

## 6. Trade-off guidance

- **Grounded > fluent.**
- **Calibrated > confident.**
- **Safe > fast.**