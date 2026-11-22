# Product Requirements Document (PRD)

## 1. Summary

A conversational scenario copilot and forecasting platform for Nestlé USA demand planners, delivering calibrated, causally-attributed, store-level forecasts with GLP-1 as a first-class driver.

## 2. Goals

- Give planners a **2–3 quarter forward view** that survives regime shifts.
- Explain **why** demand is changing (causal attribution), not just **what**.
- Make the system **governed and auditable** (retailer contracts, panel privacy).
- Let planners **interrogate** forecasts conversationally.

## 3. Non-goals

- Descriptive shelf monitoring (exists elsewhere).
- Price-setting or promotion optimization.
- LLM-authored forecasts.
- Cross-retailer pooling without permission.

## 4. Personas

| Persona | Needs |
|---|---|
| **Demand planner** | Fast, trustworthy, explainable forecasts; scenario what-ifs |
| **RGM analyst** | Causal decomposition (price/mix/GLP-1) |
| **Supply planner** | Store/banner-level numbers by lead time |
| **Data steward** | Lineage, permissions, data quality |

## 5. Functional requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Ingest structured demand data (sell-out, shipments, pricing, distribution, GLP-1 Rx) | Must |
| FR-2 | Ingest unstructured signal (reviews, search, social, call-centre notes) → structured indicators | Must |
| FR-3 | Produce hierarchical, reconciled forecasts (store → banner → DMA → national) with intervals | Must |
| FR-4 | Causal attribution of demand deltas (GLP-1, price, mix, private label) | Must |
| FR-5 | Conversational scenario copilot ("what-if GLP-1 +5pp in SE") | Must |
| FR-6 | Permission-aware retrieval (planner sees only their banners/DMAs) | Must |
| FR-7 | Audit trail (every forecast version + feature snapshot) | Must |
| FR-8 | Out-of-regime evaluation + drift/calibration monitoring | Must |
| FR-9 | Analog forecasting for new/reformulated products | Should |
| FR-10 | Export to Excel/Power BI for planner workflows | Should |

## 6. Non-functional requirements (summary)

- Latency: copilot p95 ≤ 5 s; scenario p95 ≤ 10 s.
- Availability: 99.9%.
- Security: Entra ID SSO, OPA/ABAC, DLP, no PII in prompts.
- Auditability: every answer cites a forecast run ID.
- Cost: chargeback per business unit; semantic caching.

See `03-system-and-architecture/non-functional-requirements.md` for full NFRs.

## 7. Success metrics

- Out-of-regime WMAPE improvement ≥ 15% relative.
- Interval calibration within tolerance.
- No bias by income quintile.
- Planner adoption ≥ 80%.

## 8. Open questions

- Exact retailer data-access scope (contracts).
- Choice of gateway (Portkey vs LiteLLM) and cloud mix (Azure vs Bedrock).
- Panel-data licensing terms.