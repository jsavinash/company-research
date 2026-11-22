# Project Scope and SLA

## 1. Scope

### In scope

- **Demand sensing** for Nestlé USA **Frozen** (DiGiorno, Stouffer's, Hot Pockets, Lean Pockets, Lean Cuisine, CPK, Tombstone, Jack's, Buitoni) and **Coffee** (Coffee mate, natural bliss, Nescafé, Starbucks at Home).
- **GLP-1-aware, regime-aware forecasting** with causal attribution (GLP-1, price, mix, private label).
- **Store-level → banner → DMA → national** hierarchical forecasts with reconciliation.
- **Conversational scenario copilot** (planner queries, what-if analysis, narrated results).
- **Permission-aware retrieval** and **governance** (retailer-contract, household-panel privacy).
- **Continuous evaluation** (out-of-regime WMAPE, calibration, bias).

### Out of scope

- **Descriptive shelf monitoring** (digital-shelf analytics — already exists).
- **Pricing optimization / price-setting** (the copilot explains; it does not set prices).
- **LLM-based forecasting** (the LLM extracts and narrates; it never forecasts).
- **Cross-retailer pooling** without contractual permission.
- **Household-level PII** exposure (aggregate panel only).

## 2. Stakeholders

| Stakeholder | Role |
|---|---|
| Demand planners (Frozen, Coffee) | Primary users of the copilot |
| Revenue growth management | Trade-spend decisions |
| Supply chain / logistics | Production & procurement planning |
| Data science | Model development & evaluation |
| ML engineering | Platform & serving |
| Security & compliance | Governance, privacy, audit |
| Finance | RIG / value reporting |

## 3. SLAs

| Service | SLA | Measurement |
|---|---|---|
| Copilot response (interactive) | p95 ≤ 5 s | Gateway + app telemetry |
| Forecast batch (nightly) | Completes by 06:00 local | Airflow/Temporal run logs |
| Scenario what-if | p95 ≤ 10 s | Copilot trace (LangSmith) |
| Platform availability | 99.9% monthly | OpenTelemetry + Datadog |
| Data freshness | Sell-out ≤ 24 h lag | Pipeline monitoring |
| Forecast accuracy | Out-of-regime WMAPE ≤ target | MLflow evaluation runs |

## 4. Constraints & dependencies

- **Retailer data contracts** — no cross-retailer pooling without permission.
- **Household panel privacy** — aggregate only, minimum cell sizes.
- **Microsoft-centric enterprise** — Entra ID, Fabric, Azure services preferred.
- **Existing warehouse** — Snowflake holds retailer sell-out/shipment data.
- **Planning cadence** — forecasts must align to 1–2 quarter production/procurement lead times.

## 5. Change control

Scope changes require a decision-log entry (`03-system-and-architecture/decision-log.md`) and, if architectural, a new ADR. SLA changes require sign-off from Demand Planning leadership.