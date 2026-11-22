# Non-Functional Requirements (NFRs)

## 1. Performance

| ID | Requirement | Target |
|---|---|---|
| NFR-P1 | Copilot interactive response | p95 ≤ 5 s |
| NFR-P2 | Scenario what-if | p95 ≤ 10 s |
| NFR-P3 | Nightly forecast batch | Complete by 06:00 local |
| NFR-P4 | Forecast API throughput | Handle peak planner concurrency |

## 2. Reliability & availability

| ID | Requirement | Target |
|---|---|---|
| NFR-R1 | Platform availability | 99.9% monthly |
| NFR-R2 | Forecast batch success | ≥ 99% |
| NFR-R3 | Graceful degradation | Fall back to last-good forecast on failure |
| NFR-R4 | Data freshness | Sell-out ≤ 24 h lag |

## 3. Scalability

| ID | Requirement | Target |
|---|---|---|
| NFR-S1 | Store-level forecast volume | Scale to full banner/DMA hierarchy |
| NFR-S2 | Horizontal scaling | Stateless agents + queue-based workers |
| NFR-S3 | Multi-category | Reusable across Frozen, Coffee, Baking |

## 4. Security

| ID | Requirement | Target |
|---|---|---|
| NFR-SEC1 | Authentication | Entra ID SSO (OIDC) |
| NFR-SEC2 | Authorization | OPA/ABAC per banner/DMA/role |
| NFR-SEC3 | PII protection | No PII in prompts; DLP via Purview |
| NFR-SEC4 | Secrets | HashiCorp Vault; no secrets in code |
| NFR-SEC5 | Audit | Every forecast version + feature snapshot logged |

## 5. Compliance

| ID | Requirement | Target |
|---|---|---|
| NFR-C1 | Retailer contracts | No cross-retailer pooling without permission |
| NFR-C2 | Household panel | Aggregate only; minimum cell sizes |
| NFR-C3 | Auditability | Immutable audit log; retention per policy |
| NFR-C4 | Model governance | Model cards, validation reports, approval workflow |

## 6. Observability

| ID | Requirement | Target |
|---|---|---|
| NFR-O1 | Tracing | OpenTelemetry end-to-end; LangSmith for agents |
| NFR-O2 | Metrics | Datadog/Grafana; token cost, cache hit, latency |
| NFR-O3 | Alerting | Drift, latency, error-rate, data-quality alerts |
| NFR-O4 | Evaluation | LangSmith/Braintrust/MLflow continuous eval |

## 7. Usability & accessibility

| ID | Requirement | Target |
|---|---|---|
| NFR-U1 | Planner comprehension | Plan understood in < 1 minute |
| NFR-U2 | Accessibility | WCAG 2.1 AA for copilot UI |
| NFR-U3 | Export | Excel/Power BI export |

## 8. Maintainability

| ID | Requirement | Target |
|---|---|---|
| NFR-M1 | Documentation | Every component documented; ADRs for decisions |
| NFR-M2 | Testing | Unit + integration + eval coverage |
| NFR-M3 | CI/CD | Automated build, test, deploy |