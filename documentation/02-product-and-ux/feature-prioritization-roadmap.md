# Feature Prioritization Roadmap

## 1. Prioritization method

Features are scored on **value** (business impact × adoption) vs. **effort** (engineering + data readiness), with **risk** (governance/regulatory) as a gate. MoSCoW used for release scoping: **Must** (essential for Phase 1), **Should** (important but not critical), **Could** (nice to have), **Won't** (explicitly deferred).

## 2. Roadmap

### Phase 1 — Foundations (MVP)

| Feature | Priority | Notes |
|---|---|---|
| Structured data ingestion (sell-out, shipments, pricing, distribution, GLP-1 Rx) | Must | Snowflake + Kafka |
| Regime-aware forecast core (LightGBM/TFT) | Must | Hierarchical reconciliation |
| Out-of-regime evaluation harness | Must | Train ≤2022, test 2024–26 |
| Basic dashboard (P10/P50/P90) | Must | Power BI / Fabric |

### Phase 2 — Intelligence

| Feature | Priority | Notes |
|---|---|---|
| Causal attribution (synthetic control, DiD) | Must | Separates GLP-1 vs price/mix |
| Unstructured signal extraction (reviews, search) | Should | LLM extraction → structured indicators |
| AI Gateway (routing, caching, chargeback) | Should | Portkey/LiteLLM |
| Permission-aware retrieval (OPA/ABAC) | Must | Governance gate |

### Phase 3 — Copilot

| Feature | Priority | Notes |
|---|---|---|
| Conversational scenario copilot | Should | Frontier model, grounded |
| A2A agent orchestration | Should | LangGraph + Temporal |
| Audit trail + run IDs | Must | Compliance |

### Phase 4 — Scale & optimize

| Feature | Priority | Notes |
|---|---|---|
| Analog forecasting for new products | Could | |
| Continuous eval in CI (LangSmith/Braintrust) | Should | |
| FinOps dashboards (chargeback) | Could | |
| Cross-category reuse (Coffee → Baking) | Could | |

## 3. Release gates

- **Phase 1 exit:** out-of-regime WMAPE baseline established; data pipelines SLA met.
- **Phase 2 exit:** attribution sign-consistent across windows; OPA policy enforced.
- **Phase 3 exit:** copilot adoption ≥ 50%; audit trail complete.
- **Phase 4 exit:** adoption ≥ 80%; FinOps chargeback live.

## 4. Deferred / out of scope

- Price-setting / promotion optimization.
- LLM-based forecasting.
- Cross-retailer pooling without permission.