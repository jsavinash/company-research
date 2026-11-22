# ADR 002: Grounded Coaching (RAG + Grounding Verifier)

## Status

Accepted (2023-02)

## Context

Coaching must explain the already-decided plan in warm, accurate language without inventing nutrition facts. A pure LLM would hallucinate; templates feel robotic. The requirement is **grounding-or-refuse**.

## Decision

Adopt a **RAG coaching pipeline**:
1. **Retrieve** — hybrid (keyword + dense) over AAFCO/FEDIAF + product nutrient specs + feeding guides.
5. **Rerank** — cross-encoder to keep authoritative chunks.
6. **Generate** — frontier LLM narrates the plan (numbers injected as structured data).
7. **Verify** — NLI-style entailment check rejects any sentence not supported by retrieved context.
8. **Refuse** — low-relevance retrieval → safe generic explanation.

## Consequences

**Positive:**
- No nutritional hallucination.
- Every claim traceable to a retrieved chunk.
- Warm, accurate coaching.

**Negative:**
- RAG adds latency.
- Requires a clean, current KB.

**Mitigation:**
- Semantic caching.
- Chunk metadata (authority, date) for reranking.
- Freshness: live KB, never model memory.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| LLM from memory | Simple | Hallucination |
| Templates only | Safe | Robotic |
| RAG + verifier (chosen) | Safe + natural | Complexity |

## Compliance / Governance

- Grounding-or-refuse.
- PII separated from public KB.

## References

- `../decision-log.md` D-003, D-004
- `001-initial-architecture-baseline.md`