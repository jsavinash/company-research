# Engineering Principles

## 1. How we build

1. **No autonomous diagnosis.** The radiologist reads, decides, signs.
2. **Calibrated over confident.** Every confidence is site-calibrated; an uncalibrated score is a defect.
5. **No black box.** Every prediction carries a localization + rationale.
6. **Abstention is a feature.** "Cannot assess" over confident wrong.
7. **Point-in-time correctness.** No future data.
8. **Period-accurate tooling.** 2019–2022 stack; no LLMs.

## 2. How we write code

- **Python 3.7** for models/pipelines.
- **Type hints** and **schema validation** at boundaries.
- **Idempotent Airflow jobs** with backfills.
- **Versioned model registry + calibration sets.**

## 3. How we review

- Every PR reviewed; model PRs also by a clinical reviewer.
- **Model PRs** require an eval report (sensitivity, ECE, per site, subgroup parity).
- **Calibration PRs** require per-site validation.
- **Regulatory changes** require compliance review.

## 4. How we make trade-offs

| Trade-off | Default |
|---|---|
| Sensitivity vs. specificity | Prefer sensitivity at clinically agreed FPR |
| Calibrated vs. confident | Always calibrated + abstain |
| Build vs. buy | Buy platform (Databricks/Snowflake/Azure); build models + calibration |
| AI vs. radiologist | Radiologist decides |

## 5. Definition of done

- Code reviewed and merged.
- Tests pass.
- For models: eval report (sensitivity, ECE, subgroup parity).
- Docs updated; ADR/decision-log entry if architectural.
- Deployed to staging; reader study / shadow clean.

## 6. Prohibited

- Secrets in code.
- Cross-site raw-PHI training without governance.
- Autonomous diagnosis / auto-sign-off.
- Black-box models without localization.
- Anachronistic tooling (LLMs) for a 2019–2022 imaging project.