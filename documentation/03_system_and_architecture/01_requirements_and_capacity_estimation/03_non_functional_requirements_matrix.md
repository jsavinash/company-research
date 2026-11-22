# Non-Functional Requirements Matrix

## 1. NFR matrix

| ID | Category | Requirement | Target | Verification |
|---|---|---|---|
| NFR-P1 | Performance | Copilot interactive | p95 ≤ 5 s | Load test |
| NFR-P2 | Performance | Scenario what-if | p95 ≤ 10 s | Load test |
| NFR-P3 | Performance | Nightly batch | By 06:00 | Batch logs |
| NFR-R1 | Reliability | Availability | 99.9% | Datadog |
| NFR-R2 | Reliability | Batch success | ≥ 99% | Airflow/Temporal |
| NFR-R3 | Reliability | Graceful degradation | Last-good on failure | Chaos test |
| NFR-S1 | Scalability | Full hierarchy volume | Scale to all stores | Load test |
| NFR-S2 | Scalability | Horizontal scaling | Linear | Load test |
| NFR-SEC1 | Security | Authentication | Entra ID SSO | Audit |
| NFR-SEC2 | Security | Authorization | OPA/ABAC | Policy tests |
| NFR-SEC3 | Security | PII | No PII in prompts | DLP scan |
| NFR-SEC4 | Security | Secrets | Vault | Audit |
| NFR-C1 | Compliance | Audit | 100% runs logged | Audit |
| NFR-C2 | Compliance | Retention | Per policy | Audit |
| NFR-U1 | Usability | Comprehension | < 1 min | User test |
| NFR-U2 | Accessibility | WCAG 2.1 AA | Pass | Audit |
| NFR-M1 | Maintainability | Docs | ADRs + decision log | Review |

## 2. Prioritization

- **Must:** NFR-P1, P2, R1, SEC1-3, C1.
- **Should:** NFR-S1, U1, U2.
- **Could:** NFR-S2, M1.

## 3. Verification methods

| Method | Applies to |
|---|---|
| Load test | Performance, scalability |
| Chaos / game day | Reliability, DR |
| Pen test / DLP scan | Security |
| Audit review | Compliance |
| User testing | Usability |
| Accessibility audit | A11y |

## 4. SLAs

See `01_business/01_project_overview_and_context.md` and `Nestle-USA-DemandSensing-AIArchitect-UseCase/01-business-and-strategy/project-scope-and-sla.md`.

## 5. Trade-offs

- **Calibrated > confident:** prefer intervals over points.
- **Auditability > speed:** log every run.
- **Governed > convenient:** ABAC over open access.