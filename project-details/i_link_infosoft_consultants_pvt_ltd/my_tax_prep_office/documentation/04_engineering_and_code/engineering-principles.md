# Engineering Principles

## 1. How we build

1. **Never silently accept uncertainty.** Low-confidence fields go to a human. This is a hard product constraint.
3. **Calibrated over confident.** Raw scores are not probabilities; calibrate them.
4. **Period-accurate tooling.** 2016–2017 stack; no transformers, no LLMs.
4. **Point-in-time correctness.** Features use only data available at prediction time.
5. **Auditable by default.** Every field carries confidence + provenance.
6. **Boring, auditable designs.** Prefer proven, inspectable systems.

## 2. How we write code

- **Python 3.5** for ML/services; **JavaScript** for the review UI.
- **Type hints** and **schema validation** at boundaries.
- **Small functions**, single responsibility.
- **No comments unless necessary** — code should be self-documenting.

## 3. How we review

- Every PR reviewed by one engineer; data/ML PRs also by a data reviewer.
- **Model PRs** require an eval report (field precision, recall, ECE).
- **Prompt/rule PRs** require a regression run.
- **Policy changes** (thresholds) require compliance review.

## 4. How we make trade-offs

| Trade-off | Default |
|---|---|
| Accuracy vs. latency | Prefer calibrated, slightly slower answers |
| Build vs. buy | Buy OCR (Tesseract/Cloud Vision); build extraction + calibration |
| Deterministic vs. ML | Deterministic for rules; ML for extraction/calibration |
| Review vs. silent accept | Always review low-confidence |

## 5. Definition of done

- Code reviewed and merged.
- Tests (unit + integration) pass.
- For ML: eval report attached (precision, recall, ECE).
- Docs updated; ADR/decision-log entry if architectural.
- Deployed to staging; monitoring in place.

## 6. Prohibited

- Secrets in code.
- PII in logs.
- Third-party training on customer documents.
- Auto-committing low-confidence fields.
- Anachronistic tooling (transformers, LLMs) for a 2016–2017 project.