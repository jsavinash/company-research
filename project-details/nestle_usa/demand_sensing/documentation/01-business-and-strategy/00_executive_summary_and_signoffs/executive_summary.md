# Executive Summary

## Project

**Agentic GLP-1 Demand Sensing & Scenario Copilot** — a target-state AI Solutions Architect platform for Nestlé USA's Frozen and Coffee demand planning.

## The problem

Nestlé USA faces a structural demand break: US food volumes per capita are declining (-0.6% H1 2026), GLP-1 adoption is hitting frozen hardest (~3-pt dollar-spend drop in year one), private label is at 23.8% of units, and models trained on 2015–2022 history produce confident, wrong forecasts. The gap is predictive and causal: planners need a 2–3 quarter forward view and the *why*, not a descriptive shelf snapshot.

## The solution

A permission-aware, agentic decision-support platform that:
- Produces calibrated, causally-attributed, store-level forecasts (GLP-1 as a first-class driver).
- Lets planners interrogate them conversationally ("GLP-1 +5pp in SE → DiGiorno by Q3?").
- Enforces governance (retailer contracts, household-panel privacy) and auditability.
- Runs on a 6-layer enterprise architecture (cloud/AI platforms, AI gateway, data + permission-aware RAG, agentic orchestration, security, FinOps/observability).

**Core design decision:** the LLM never forecasts. It extracts structured signals and narrates grounded results; the constrained solver decides.

## Business value

- ≥15% relative out-of-regime WMAPE improvement.
- Causal attribution separates GLP-1 / price / mix / private label → better trade-spend decisions.
- Reusable across Frozen, Coffee, Baking.
- Audit-grade decisions (every answer traceable to a run ID).

## Status

Draft reference architecture (reconstruction). Validate figures and claims before external use. See `approval_and_change_log.md` for governance.

## Key risks

Retailer data access, regime shift outpacing updates, adoption resistance, overclaiming accuracy. See `../11_risk_analysis_and_mitigation.md`.