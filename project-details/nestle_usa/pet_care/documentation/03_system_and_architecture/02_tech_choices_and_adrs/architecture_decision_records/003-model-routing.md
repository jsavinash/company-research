# ADR 003: Model Routing and Fine-Tuning Split

## Status

Accepted (2023-03)

## Context

The platform runs high-volume intake extraction and lower-volume coaching. Using frontier models for everything is expensive; using small models for coaching hurts quality. Also, fine-tuning can bake in stale nutrition facts.

## Decision

Adopt a **routing + fine-tuning split**:
- **Intake extraction** → **small/fast models** (Gemini Flash, Claude Haiku, Llama-3, Qwen); candidate for **LoRA fine-tuning** on (message → slot) pairs.
- **Coaching narration** → **frontier models** (GPT-4o, Claude, Gemini Pro); **prompt + RAG only** (no fine-tuning).
- **Grounding verifier** → small NLI model.
- **Vet summary** → mid-tier.

**Key rule:** fine-tune the extractor (schema adherence, cost); RAG the coach (current nutrition facts).

## Consequences

**Positive:**
- Lower cost (small models for high-volume extraction).
- Better coaching quality (frontier).
- Nutrition facts stay current (RAG, not fine-tuned memory).

**Negative:**
- Two model paths to maintain.
- Routing complexity.

**Mitigation:**
- AI gateway handles routing + fallback.
- Eval per tier.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| Frontier for everything | Quality | Cost |
| Fine-tune everything | Cost | Stale nutrition facts |
| Split (chosen) | Cost + quality + freshness | Complexity |

## Compliance / Governance

- Nutrition facts current (RAG).
- Model versioning.

## References

- `../decision-log.md` D-005, D-007
- `001-initial-architecture-baseline.md`