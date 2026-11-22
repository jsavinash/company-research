# Engineering Principles

## 1. How we build

1. **No autonomous classification.** Curators decide; the system prioritizes and explains.
2. **Abstention is a feature.** The system must be able to say "insufficient evidence."
3. **Calibrated over confident.** Raw scores are not probabilities.
4. **Interpretable by default.** A clinical tool that can't be explained won't be trusted.
5. **Period-accurate tooling.** 2017–2018 stack; no BERT, no LLMs.
6. **Auditability.** Every code carries provenance.

## 2. How we write code

- **Python 3.6** for the pipeline; **JavaScript** for the review UI.
- **Type hints** and **schema validation** at boundaries.
- **Reproducible pipelines:** Snakemake / Nextflow.
- **Versioned feature store.**

## 3. How we review

- Every PR reviewed by one engineer; data/ML PRs also by a clinical reviewer.
- **Model PRs** require an eval report (top-20 recall, ECE, ancestry transfer gap).
- **Rule PRs** (ACMG mapping) require clinical review.
- **Policy changes** (thresholds) require clinical sign-off.

## 4. How we make trade-offs

| Trade-off | Default |
|---|---|
| Accuracy vs. interpretability | Prefer interpretable (GBM) |
| Calibrated vs. confident | Always calibrated + abstain |
| Build vs. buy | Buy annotation (VEP/dbNSFP); build triage + calibration |
| Human vs. automation | Human sign-off for classification |

## 5. Definition of done

- Code reviewed and merged.
- Tests pass.
- For ML: eval report attached (top-20 recall, ECE, ancestry gap).
- Docs updated; ADR/decision-log entry if architectural.
- Deployed to staging; monitoring in place.

## 6. Prohibited

- Secrets in code.
- Identifiable genomes in training without governance.
- Autonomous classification.
- Anachronistic tooling (BERT, LLMs) for a 2017–2018 project.
- Confidently wrong outputs without abstention.