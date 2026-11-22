# Non-Functional Business Constraints

## 1. Business constraints

| ID | Constraint | Impact |
|---|---|---|
| BC-1 | Retailer data is contractually restricted | No cross-retailer pooling; per-retailer governance |
| BC-2 | Household panel is privacy-sensitive | Aggregate only; minimum cell sizes |
| BC-3 | Audit-grade decisions required | Every run logged; reproducible |
| BC-4 | Microsoft-centric enterprise | Entra ID, Fabric, Azure preferred |
| BC-5 | Planning cadence (1–2 quarters) | Forecast horizon must match lead times |
| BC-6 | Cost accountability | Chargeback per business unit |

## 2. Non-functional requirements (business view)

| Category | Requirement | Target |
|---|---|---|
| **Performance** | Copilot interactive | p95 ≤ 5 s |
| **Performance** | Scenario what-if | p95 ≤ 10 s |
| **Reliability** | Availability | 99.9% |
| **Reliability** | Forecast batch | Complete by 06:00 |
| **Security** | Authentication | Entra ID SSO |
| **Security** | Authorization | OPA/ABAC |
| **Security** | PII | No PII in prompts; DLP |
| **Compliance** | Audit | Immutable log; retention |
| **Compliance** | Model governance | Model cards, validation |
| **Usability** | Planner comprehension | < 1 minute |
| **Accessibility** | WCAG 2.1 AA | Copilot UI |
| **Maintainability** | Documentation | ADRs + decision log |

## 3. Compliance constraints

| Regulation / policy | Constraint |
|---|---|
| Retailer contracts | No pooling without permission |
| Panel licensing | Aggregate + consent |
| Enterprise data policy | DLP + retention |
| Audit requirements | Immutable log |

## 4. Cost constraints

- Token/compute spend controlled via gateway (rate limit, cache, chargeback).
- FinOps visibility per business unit.
- ROI tracked against baseline.

## 5. Trade-off guidance

When constraints conflict:
- **Compliance > convenience** (no pooling without permission).
- **Auditability > speed** (log every run).
- **Calibrated > confident** (intervals over points).