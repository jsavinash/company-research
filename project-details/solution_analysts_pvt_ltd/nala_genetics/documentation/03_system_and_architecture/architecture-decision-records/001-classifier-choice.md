# ADR 001: Classifier Choice (GBM over Deep Learning)

## Status

Accepted (2017-06)

## Context

The triage layer must rank germline variants for clinical review. Options were gradient-boosted trees (XGBoost/LightGBM) or deep learning (neural networks). Variant features are tabular (~40–60 interpretable features), sample sizes are moderate, and the tool is clinical/regulatory (ISO 13485).

## Decision

Adopt **gradient-boosted trees (XGBoost / LightGBM)** as the primary classifier.

## Consequences

**Positive:**
- Best tabular performance in the period.
- Interpretable (feature importance, SHAP-style attributions) — a regulatory asset.
- Fast to train and serve.
- Works well with moderate sample sizes.

**Negative:**
- Less expressive than deep learning for complex interactions.
- Requires careful feature engineering.

**Mitigation:**
- Rich, interpretable features from VEP/dbNSFP/gnomAD.
- Calibration layer on top.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Deep learning (MLP) | Expressive | Opacity; overkill for tabular; harder to validate |
| Logistic regression | Interpretable | Weaker performance |
| Rule-based only | Transparent | Doesn't scale; no ranking |

## Compliance / Governance

- Interpretability supports ISO 13485 validation.
- Model versioning + eval reports.

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-003