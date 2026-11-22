# To-Be Target Capabilities

## 1. Future (To-Be) workflow

1. **Automated ingestion** — structured (sell-out, shipment, price, distribution, GLP-1 Rx) and unstructured (reviews, search, notes) data flow into a governed lakehouse via Kafka/batch.
2. **Feature store** — point-in-time-correct features (dbt + Feast) feed the forecast core.
3. **Regime-aware forecasting** — LightGBM / Temporal Fusion Transformer with GLP-1 as a first-class driver; hierarchical reconciliation (MinT); P10/P50/P90 intervals.
4. **Causal attribution** — synthetic control + DiD decompose demand deltas (GLP-1, price, mix, private label).
5. **Conversational copilot** — planners ask what-if questions; agents orchestrate and narrate grounded answers with run IDs.
6. **Governance** — OPA/ABAC permissions, Purview DLP, audit trail on every run.

## 2. Target capabilities

| Capability | Description | Business outcome |
|---|---|---|
| **Regime-aware forecasting** | GLP-1-aware, store-level, hierarchical | Accuracy under structural break |
| **Causal attribution** | Decompose demand drivers | Better trade-spend decisions |
| **Scenario copilot** | Conversational what-if | Faster, auditable analysis |
| **Permission-aware retrieval** | Per-banner/DMA access | Compliance; no data leaks |
| **Continuous evaluation** | Out-of-regime WMAPE, calibration, bias | Trustworthy models |
| **FinOps** | Chargeback, cost visibility | ROI accountability |
| **Auditability** | Run IDs, feature snapshots | Governance & compliance |

## 3. To-Be vs. As-Is

| Dimension | As-Is | To-Be |
|---|---|---|
| Forecast method | Legacy / Excel | Regime-aware ML + causal |
| Horizon | Short-term | 2–3 quarters |
| Scenario analysis | Manual (days) | Conversational (seconds) |
| Data access | Ad hoc | OPA-governed |
| Audit | None | Full run-level audit |
| Accuracy | Degrading | Out-of-regime validated |

## 4. Success criteria

- Out-of-regime WMAPE ≥ 15% relative improvement.
- Attribution sign-consistent.
- Copilot adoption ≥ 80%.
- Zero PII incidents.

## 5. Transition approach

Phased: Foundations → Intelligence → Copilot → Scale (see `../02-product-and-ux/feature-prioritization-roadmap.md`).