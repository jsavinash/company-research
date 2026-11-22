# Project Overview and Context

## 1. Overview

The Agentic GLP-1 Demand Sensing & Scenario Copilot is a decision-support platform for Nestlé USA demand planners. It turns structured demand data and unstructured consumer signal into calibrated, causally-attributed, store-level forecasts and exposes them through a conversational copilot.

## 2. Business context

- **Nestlé USA** is the US arm of Nestlé S.A.; the US is ~32% of group sales.
- **Frozen** (DiGiorno, Stouffer's, Hot Pockets, Lean Pockets, Lean Cuisine, CPK, Tombstone, Jack's, Buitoni) is the most GLP-1-exposed category and a strategic investment area.
- **Coffee** (Coffee mate, natural bliss, Nescafé, Starbucks at Home) is a second priority category.
- **Market backdrop:** flat-to-negative volumes, record private-label share (23.8%), cocoa/coffee cost shocks, tariff volatility, and measurable GLP-1-driven basket shifts.

## 3. Why now

1. The demand regime has shifted (GLP-1, private label, input costs) — history-based models are structurally biased.
2. Retailer data and digital-shelf monitoring exist, but descriptive analytics don't answer "what next, and why."
3. Enterprise AI has matured: MCP/A2A protocols, AI gateways, permission-aware RAG, and agentic orchestration are production-ready.

## 4. Objectives

- Deliver a 2–3 quarter forward view that survives regime shifts.
- Explain demand changes causally.
- Operate within retailer-contract and panel-privacy constraints.
- Prove ROI via FinOps and out-of-regime evaluation.

## 5. Success definition

- Out-of-regime WMAPE improves ≥15% relative.
- Attribution sign-consistent across rolling windows.
- Intervals calibrated; no income-quintile bias.
- Planner adoption ≥ 80%.

## 6. Out of scope (summary)

Price-setting, LLM-based forecasting, cross-retailer pooling without permission, household-level PII. See `../05_scope_and_boundaries/`.

## 7. Service Level Agreements (SLAs)

| Service | SLA | Measurement |
|---|---|---|
| Copilot response (interactive) | p95 ≤ 5 s | Gateway + app telemetry |
| Forecast batch (nightly) | Completes by 06:00 local | Airflow/Temporal run logs |
| Scenario what-if | p95 ≤ 10 s | Copilot trace (LangSmith) |
| Platform availability | 99.9% monthly | OpenTelemetry + Datadog |
| Data freshness | Sell-out ≤ 24 h lag | Pipeline monitoring |
| Forecast accuracy | Out-of-regime WMAPE ≤ target | MLflow evaluation runs |

## 8. Constraints and change control

- **Retailer data contracts** — no cross-retailer pooling without permission.
- **Household panel privacy** — aggregate only, minimum cell sizes.
- **Microsoft-centric enterprise** — Entra ID, Fabric, Azure services preferred.
- **Existing warehouse** — Snowflake holds retailer sell-out/shipment data.
- **Planning cadence** — forecasts must align to 1–2 quarter production/procurement lead times.
- **Change control** — scope changes require a decision-log entry (and a new ADR if architectural); SLA changes require sign-off from Demand Planning leadership.