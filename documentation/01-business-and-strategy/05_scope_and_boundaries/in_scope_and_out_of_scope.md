# In Scope and Out of Scope

## 1. In scope

- **Demand sensing** for Nestlé USA **Frozen** and **Coffee** categories.
- **GLP-1-aware, regime-aware forecasting** with causal attribution (GLP-1, price, mix, private label).
- **Hierarchical forecasts** (store → banner → DMA → national) with reconciliation and intervals.
- **Conversational scenario copilot** (planner queries, what-ifs).
- **Permission-aware retrieval** and **governance** (retailer contracts, panel privacy).
- **Continuous evaluation** (out-of-regime WMAPE, calibration, bias).
- **Audit trail** and **FinOps/chargeback**.

## 2. Out of scope

- **Descriptive shelf monitoring** (digital-shelf analytics — exists elsewhere).
- **Price-setting / promotion optimization** (copilot explains; it never sets prices).
- **LLM-based forecasting** (LLM extracts + narrates only).
- **Cross-retailer pooling** without contractual permission.
- **Household-level PII** exposure (aggregate panel only).
- **Medical/nutrition advice** (not a pet/infant health product).
- **Cross-category expansion** (Frozen → Coffee → Baking is future).

## 3. Scope boundaries (decision rules)

| Question | Rule |
|---|---|
| Is it a number? | Must come from the forecast core, not the LLM |
| Is it causal? | Must have a holdout or validated causal design |
| Is it cross-retailer? | Only with explicit permission |
| Is it PII? | Aggregate only; redact before prompts |
| Is it a price recommendation? | Out of scope — never |

## 4. Change control

Scope changes require a decision-log entry and, if architectural, a new ADR. See `../../Nestle-USA-DemandSensing-AIArchitect-UseCase/03-system-and-architecture/decision-log.md`.

## 5. Assumptions

See `assumptions_and_dependencies.md`.