# Non-Functional Requirements Matrix

## 1. NFR matrix

| ID | Category | Requirement | Target | Verification |
|---|---|---|---|---|
| NFR-P1 | Performance | Triage API (per batch) | p95 ≤ 3 s | Load test |
| NFR-P2 | Performance | Curator UI interaction | p95 ≤ 1 s | Front-end test |
| NFR-R1 | Reliability | Availability | 99.5% | Uptime monitoring |
| NFR-R2 | Reliability | Graceful degradation | Abstain / last-good on failure | Chaos test |
| NFR-S1 | Scalability | Genome-scale batches | Scale horizontally | Load test |
| NFR-SEC1 | Security | Authentication | Session cookie / SSO | Audit |
| NFR-SEC2 | Security | Data protection | AES-256 at rest, TLS in transit | DLP scan |
| NFR-SEC3 | Security | Access logging | Every variant/decision logged | Audit |
| NFR-C1 | Compliance | ISO 13485 traceability | Model + data versioning | Audit |
| NFR-C2 | Compliance | Auditability | Code → evidence → provenance | Audit |
| NFR-C3 | Compliance | No autonomous classification | Human sign-off required | Design review |
| NFR-U1 | Usability | Curator efficiency | Median ≤ 90 s/variant | Time study |
| NFR-M1 | Maintainability | Documentation | ADRs + decision log | Review |

## 2. Prioritization

- **Must:** NFR-P1, R1, SEC1-3, C1, C2, C3, U1.
- **Should:** NFR-S1, R2.
- **Could:** NFR-P2, M1.

## 3. Verification methods

| Method | Applies to |
|---|---|
| Load test | Performance, scalability |
| Chaos test | Reliability (abstain fallback) |
| DLP scan | Security |
| Audit review | Compliance |
| Time study | Usability |

## 4. SLAs

See `../01-business-and-strategy/project-scope-and-sla.md`.

## 5. Trade-off guidance

- **Calibrated > confident:** probabilities + abstention over raw scores.
- **Auditability > speed:** provenance for every code.
- **Human sign-off > automation:** no autonomous classification.