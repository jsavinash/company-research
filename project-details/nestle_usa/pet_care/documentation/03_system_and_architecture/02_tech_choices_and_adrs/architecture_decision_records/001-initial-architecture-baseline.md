# ADR 001: Initial Architecture Baseline

## Status

Accepted (2023-01)

## Context

We need a GenAI layer for Purina's precision pet nutrition: conversational intake + grounded coaching, with a hard rule that an LLM never chooses a diet. The stack must be period-accurate (2023+), safe, and auditable.

## Decision

Adopt a **layered GenAI architecture**:
1. **Intake extraction** — small model + JSON schema → structured profile.
2. **Decision core** — constrained recommender + adequacy gate (unchanged).
4. **Grounded coaching** — RAG over AAFCO/FEDIAF + product specs + grounding verifier.
5. **Vet summary** — deterministic facts + LLM prose.
6. **Safety** — OPA/ABAC, Purview DLP, NeMo Guardrails, Lakera, Vault.
7. **Eval** — LangSmith/Arize/Braintrust/MLflow + red-team.

**Core rule:** the LLM narrates; the solver decides.

## Consequences

**Positive:**
- Safe, auditable, grounded.
- Reuses the decision core.
- Period-accurate, production-ready.

**Negative:**
- Multiple components to integrate.
- Grounding verifier adds latency.

**Mitigation:**
- Phased delivery.
- Caching + streaming.

## Alternatives Considered

| Option | Pros | Cons |
|---|---|---|
| LLM-only chatbot | Simplicity | Hallucination; unsafe |
| Rules-only | Safe | Can't handle free text |
| Hybrid (chosen) | Safe + conversational | Integration effort |

## Compliance / Governance

- LLM never chooses a diet.
- Grounding-or-refuse.
- Medical questions → vet.

## References

- `../decision-log.md`
- `002-rag-grounding.md`
- `003-model-routing.md`