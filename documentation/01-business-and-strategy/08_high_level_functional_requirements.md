# High-Level Functional Requirements

## 1. Functional requirements

| ID | Requirement | Priority | Acceptance |
|---|---|---|---|
| FR-1 | Ingest structured demand data (sell-out, shipments, pricing, distribution, GLP-1 Rx) | Must | Data available with freshness ≤ 24h |
| FR-2 | Ingest unstructured signal (reviews, search, social, notes) → structured indicators | Must | Extraction schema-validated |
| FR-3 | Produce hierarchical, reconciled forecasts (store → banner → DMA → national) with intervals | Must | P10/P50/P90 + run ID |
| FR-4 | Causal attribution of demand deltas (GLP-1, price, mix, private label) | Must | Sign-consistent effects |
| FR-5 | Conversational scenario copilot ("what-if GLP-1 +5pp in SE") | Must | Grounded answer + run ID |
| FR-6 | Permission-aware retrieval (planner sees only their banners/DMAs) | Must | OPA denies unauthorized |
| FR-7 | Audit trail (every forecast version + feature snapshot) | Must | 100% of runs logged |
| FR-8 | Out-of-regime evaluation + drift/calibration monitoring | Must | WMAPE, coverage, bias reported |
| FR-9 | Analog forecasting for new/reformulated products | Should | Analog + wide intervals |
| FR-10 | Export to Excel/Power BI | Should | Planner can export |
| FR-11 | Chargeback / cost attribution per business unit | Should | FinOps dashboard |
| FR-12 | Continuous evaluation in CI (prompt/model regression) | Should | Gates on PRs |

## 2. Requirement categories

| Category | Examples |
|---|---|
| **Data** | FR-1, FR-2 |
| **Forecast** | FR-3, FR-9 |
| **Causal** | FR-4 |
| **Copilot** | FR-5 |
| **Governance** | FR-6, FR-7 |
| **Evaluation** | FR-8, FR-12 |
| **UX** | FR-10 |
| **FinOps** | FR-11 |

## 3. Prioritization

- **Must:** FR-1..FR-8 (MVP + governance).
- **Should:** FR-9..FR-12 (scale).
- **Could:** cross-category reuse (future).

## 4. Traceability

Each FR maps to acceptance criteria in `../../Nestle-USA-DemandSensing-AIArchitect-UseCase/05-quality-and-verification/acceptance-criteria-and-cases.md` and to components in the system design.

## 5. Out of scope (functional)

- Price-setting, LLM forecasting, cross-retailer pooling, PII exposure. See `05_scope_and_boundaries/`.