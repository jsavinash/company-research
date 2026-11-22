# ADR 001: Retrieval Architecture (Two-Tower + ANN, not TFRS)

## Status

Accepted (2018-12)

## Context

The platform must retrieve a candidate set from a large, changing catalog (millions of SKUs, thousands added weekly) within a tight latency budget, then rank. Options were a two-tower model with ANN, or a monolithic ranker over the full catalog. The tenure is Dec 2018 – Aug 2019; TensorFlow Recommenders (TFRS) shipped Sep 2020 and is not available.

## Decision

Adopt a **two-tower model in TensorFlow 1.x** for retrieval:
- Query/user tower + product tower.
- Product vectors computed offline and ANN-indexed (FAISS / Annoy).
- Query/user representation + retrieval run online.
- Exact vs. ANN retrieval is an explicit configuration (chosen by catalog scale + latency budget).

## Consequences

**Positive:**
- Sub-linear retrieval latency at catalog scale.
- Separates retrieval (recall) from ranking (precision) — each measured independently.
- Period-accurate (TF 1.x; no TFRS).

**Negative:**
- Two-tower may miss relevant items before ranking (recall ceiling).
- Two models to train/serve.

**Mitigation:**
- Recall@K is a launch gate, not an afterthought.
- ANN index tuned per latency budget.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Monolithic ranker over full catalog | Simplicity | Latency; no recall control |
| TFRS | Modern | Postdates tenure (Sep 2020) |
| Exact k-NN | Perfect recall | Too slow at scale |

## Compliance / Governance

- Client data stays within the engagement boundary.
- Model versioning + eval.

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-001, D-002