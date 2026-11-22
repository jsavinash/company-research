# ADR 002: Ranking Model (LightGBM LambdaMART)

## Status

Accepted (2019-01)

## Context

After retrieval, the platform must re-order candidates using query, product, user, and session signals. Options were gradient-boosted ranking (LambdaMART), a neural ranker, or a simple popularity model. The data is tabular/session-grouped, and the client needs interpretability and fast iteration.

## Decision

Adopt **LightGBM LambdaMART** as the re-ranker:
- Each training row belongs to a query/session group.
- Relevance labels + gain mapping reflect the objective.
- **Separate labels/datasets for search vs. recommendation.**

## Consequences

**Positive:**
- Best-in-class structured ranker in the period.
- Fast training/serving; handles session groups.
- Interpretable feature importance.

**Negative:**
- Requires careful label/position-bias handling.
- Separate datasets double the training pipeline.

**Mitigation:**
- Position-bias controls + negative sampling.
- Separate label sets (a deliberate choice, not overhead).

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Neural ranker | Expressive | Opacity; overkill for tabular |
| Popularity model | Simple | Ignores relevance/context |
| Single ranker for search + reco | Simplicity | Known failure mode (query-conditionality gap) |

## Compliance / Governance

- No conversion claim without a controlled experiment.
- Model versioning + eval.

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-003, D-004