# Non-Functional Requirements Matrix

## 1. NFR matrix

| ID | Category | Requirement | Target | Verification |
|---|---|---|---|---|
| NFR-P1 | Performance | Discovery API (search/reco) | p95 ≤ 35 ms (benchmark boundary defined) | Load test |
| NFR-P2 | Performance | p99 latency | Reported alongside p95 | Load test |
| NFR-P3 | Performance | Peak throughput | 2,500+ req/s (if evidenced) | Load test |
| NFR-R1 | Reliability | Availability | 99.9% | Monitoring |
| NFR-R2 | Reliability | Graceful degradation | Fallback to popularity/lexical on timeout | Chaos test |
| NFR-S1 | Scalability | Horizontal scaling | HPA on CPU/concurrency | Load test |
| NFR-SEC1 | Security | Authentication | SSO / API keys | Audit |
| NFR-SEC2 | Security | Data protection | TLS, at-rest encryption | Audit |
| NFR-C1 | Compliance | Client-data boundary | Single-client isolation; no cross-client training | Design review |
| NFR-C2 | Compliance | Consent/retention | Per client policy | Audit |
| NFR-U1 | Usability | p95 latency under peak | No guardrail regression | Load test |
| NFR-M1 | Maintainability | Documentation | ADRs + decision log | Review |

## 2. Prioritization

- **Must:** NFR-P1, R1, SEC1-2, C1, C2.
- **Should:** NFR-S1, R2, P2.
- **Could:** NFR-P3, M1.

## 4. Verification methods

| Method | Applies to |
|---|---|
| Load test | Performance, scalability |
| Chaos test | Reliability (fallback) |
| Audit review | Compliance |
| CI parity checks | Online/offline skew |

## 5. Trade-off guidance

- **Measured > claimed:** no conversion claim without experiment.
- **Guardrails > lift:** a launch that lifts ATC but degrades no-results/latency is a regression.
- **Separate > collapsed:** search vs. reco labels stay separate.