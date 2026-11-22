# Engineering Principles

## 1. How we build

1. **Safety over cleverness.** The LLM never forecasts; the constrained solver decides. Guardrails live in the tool surface, not just prompts.
2. **Point-in-time correctness is non-negotiable.** No feature may use future data. Leakage is a release blocker.
3. **Causal claims require causal evidence.** No "lift" without a holdout or a validated causal design (synthetic control / DiD).
4. **Governance is a feature.** Permission-aware retrieval and audit trails are first-class, not afterthoughts.
5. **Period-accurate tooling.** Match the toolchain to the era; avoid anachronisms.

## 2. How we write code

- **Python** for data/ML services; **TypeScript** for the copilot front-end.
- **Type hints** and **schema validation** at boundaries (Pydantic / Zod).
- **Structured outputs** from LLMs (JSON schema / function calling) — never free-text parsing.
- **Idempotent pipelines** — reruns are safe.
- **Feature contracts** versioned in dbt; breaking changes require a new version.

## 3. How we review

- Every PR reviewed by at least one engineer; data/ML PRs also by a data steward.
- **Model PRs** require an eval report (out-of-regime WMAPE, calibration, bias).
- **Prompt PRs** require a regression run (adversarial suite).
- **Policy changes** (OPA) require security review.

## 4. How we make trade-offs

| Trade-off | Default |
|---|---|
| Accuracy vs. latency | Prefer calibrated, slightly slower answers for decisions |
| Build vs. buy | Buy managed (Azure/Databricks/Snowflake); build only the moat (causal + governance) |
| LLM vs. deterministic | Deterministic for numbers; LLM for extraction + narration |
| Complexity vs. maintainability | Prefer boring, auditable designs |

## 5. Definition of done

- Code reviewed and merged.
- Tests (unit + integration) pass.
- For ML: eval report attached; for prompts: regression suite green.
- Documentation updated; ADR/decision-log entry if architectural.
- Deployed to staging; monitoring/alerts in place.

## 6. Prohibited

- Secrets in code.
- PII in prompts or logs.
- Cross-retailer data pooling without permission.
- Claiming lift without a holdout / causal design.
- Anachronistic tooling (e.g., LLMs for forecasting).