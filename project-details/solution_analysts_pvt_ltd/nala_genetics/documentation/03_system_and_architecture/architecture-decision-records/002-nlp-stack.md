# ADR 002: NLP Stack (ULMFiT/ELMo over BERT)

## Status

Accepted (2017-08)

## Context

The literature triage layer must score PubMed/ClinVar abstracts for relevance to a specific gene–variant–disease question. The tenure is May 2017 – Jul 2018. BERT was released Oct 2018 — after the tenure. The available transfer-learning options were ULMFiT (Jan–May 2018) and ELMo (Feb 2018).

## Decision

Adopt a **two-stage literature triage**:
1. **Cheap retrieval:** TF-IDF / LSA to shortlist candidate abstracts.
2. **Relevance classifier:** ULMFiT or ELMo-based text classifier to score relevance.

**Exclude BERT and any LLM** — BERT postdates the tenure; generative models do not belong in a clinical classification path.

## Consequences

**Positive:**
- Period-accurate; reproducible.
- Transfer learning improves relevance scoring over TF-IDF alone.
- Two-stage design keeps cost low.

**Negative:**
- ULMFiT/ELMo are heavier than TF-IDF.
- BERT would be better, but isn't available in the window.

**Mitigation:**
- Use TF-IDF/LSA for the first-stage shortlist; ULMFiT/ELMo only on the shortlist.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| TF-IDF/LSA only | Cheap | Weaker relevance |
| BERT | Best | Postdates tenure |
| LLM | Best | Postdates tenure; unsuitable for clinical path |

## Compliance / Governance

- Period-accurate tooling (no anachronisms).
- Literature triage is decision-support; curators verify.

## References

- `../system-design-document.md` §5
- `../decision-log.md` D-006, D-008