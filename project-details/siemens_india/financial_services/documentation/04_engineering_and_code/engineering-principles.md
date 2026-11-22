# Engineering Principles

## 1. How we build

1. **No autonomous credit decision.** The system scores, explains, flags; a credit officer decides.
2. **Calibrated over confident.** Every PD is calibrated with a confidence statement.
4. **No black box.** Reason codes are a regulatory requirement.
5. **Operational lift is a gate.** If the operational signal doesn't beat financial-only, the moat claim fails.
6. **Point-in-time correctness.** No future data in historical features.
7. **Period-accurate tooling.** 2019–2022 stack; no LLMs.

## 2. How we write code

- **Python 3.7** for models/pipelines.
- **Type hints** and **schema validation** at boundaries.
- **Idempotent Airflow jobs** with backfills.
- **Versioned feature store + model registry.**

## 3. How we review

- Every PR reviewed; model PRs also by a model-risk reviewer.
- **Model PRs** require an eval report (KS, ECE, operational lift, per cohort).
- **Feature PRs** require point-in-time validation.
- **Governance changes** require model-risk sign-off.

## 4. How we make trade-offs

| Trade-off | Default |
|---|---|
| Accuracy vs. interpretability | Prefer interpretable (scorecard companion) |
| PD vs. survival | Both — PD for how likely, survival for when |
| Build vs. buy | Buy platform (Databricks/Snowflake); build models + governance |
| Human vs. automation | Credit officer decides |

## 5. Definition of done

- Code reviewed and merged.
- Tests pass.
- For models: eval report (KS, ECE, lift, per cohort).
- Docs updated; ADR/decision-log entry if architectural.
- Deployed to staging; shadow validation clean.

## 6. Prohibited

- Secrets in code.
- Cross-entity raw-data pooling without governance.
- Autonomous approve/decline.
- Black-box models without reason codes.
- Anachronistic tooling (LLMs) for a 2019–2022 credit project.