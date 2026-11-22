# Engineering Principles

## 1. How we build

1. **Separate retrieval from ranking.** Each measured independently; retrieval is a launch gate.
2. **Separate search vs. reco labels.** Collapsing them is a known failure mode.
3. **Position-bias is first-class.** Impression + position logging is mandatory.
4. **Point-in-time correctness.** No future data in historical features.
5. **No conversion claim without experiment.** Shadow is release safety, not lift proof.
6. **Period-accurate tooling.** 2018–2019 stack; no TFRS, no LLMs.

## 2. How we write code

- **Python 3.6** for the pipeline; **TypeScript** for any front-end.
- **Type hints** and **schema validation** at boundaries.
- **Idempotent Airflow jobs** with backfills.
- **Versioned feature store + model registry.**

## 3. How we review

- Every PR reviewed by one engineer; ML PRs also by a data reviewer.
- **Model PRs** require an eval report (Recall@K, NDCG@K, per placement).
- **Label/rule PRs** require a bias review.
- **Serving changes** require latency/load validation.

## 4. How we make trade-offs

| Trade-off | Default |
|---|---|
| Recall vs. latency | Tune ANN per latency budget; measure both |
| Offline vs. online | Offline is a gate; online experiment proves lift |
| Build vs. buy | Buy infra (K8s, TF Serving, MLflow); build retrieval + ranking |
| Separate vs. collapsed | Always separate search/reco |

## 5. Definition of done

- Code reviewed and merged.
- Tests pass.
- For ML: eval report attached (Recall@K, NDCG@K, per placement).
- Docs updated; ADR/decision-log entry if architectural.
- Deployed to staging; shadow validation clean.

## 6. Prohibited

- Secrets in code.
- Cross-client raw-data training.
- Auto-merchandising / silent business-rule override.
- Anachronistic tooling (TFRS, LLMs) for a 2018–2019 project.
- Conversion claims without a controlled experiment.