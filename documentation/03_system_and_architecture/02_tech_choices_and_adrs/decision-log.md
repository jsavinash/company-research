# Decision Log

Lightweight log of significant decisions. Complements the ADRs in `architecture_decision_records/`.

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2026-01 | LLM never forecasts; it extracts + narrates only | Safety, auditability, and defensibility in a regulated domain | Accepted |
| D-002 | 2026-01 | GLP-1 as a first-class exogenous driver | Regime shift invalidates history-only models | Accepted |
| D-003 | 2026-01 | Causal attribution (synthetic control + DiD) as a release gate | Correlational deltas mislead trade-spend decisions | Accepted |
| D-004 | 2026-02 | Hybrid cloud (Azure primary, AWS/GCP fallback) | Avoid lock-in; compliance; SLAs | Accepted |
| D-005 | 2026-02 | AI gateway (Portkey/LiteLLM) with semantic caching + chargeback | Cost control, no vendor lock-in | Accepted |
| D-006 | 2026-02 | OPA/ABAC for permission-aware retrieval | Prevent cross-retailer / cross-DMA leakage | Accepted |
| D-007 | 2026-03 | LangGraph + MS Agent Framework + Temporal for orchestration | Stateful, durable, enterprise-integrated | Accepted |
| D-008 | 2026-03 | Out-of-regime evaluation (train ≤2022, test 2024–26) | Honest accuracy under regime shift | Accepted |
| D-009 | 2026-03 | Small/fast models for extraction; frontier for reasoning | Cost vs. quality; high-volume extraction | Accepted |
| D-010 | 2026-04 | No cross-retailer pooling without permission | Contractual + privacy compliance | Accepted |
| D-011 | 2026-04 | LLM extraction layer on vLLM/NIM; forecast core on Databricks/SageMaker | Separate LLM serving from numeric forecasting | Accepted |
| D-012 | 2026-05 | Continuous eval in CI (LangSmith/Braintrust) | Regression safety for prompts/models | Accepted |
| D-013 | 2026-06 | Chargeback per business unit (Frozen/Coffee/Baking) | FinOps accountability | Accepted |

## Change process

- New decisions appended with next ID.
- Status: Proposed → Accepted → Superseded.
- Architectural decisions get a full ADR in `architecture_decision_records/`.