# Tenets and Guiding Principles

## 1. Tenets

1. **An LLM never chooses a pet's diet.** It narrates; the solver decides.
2. **Grounding or refuse.** Every nutritional claim traces to a retrieved chunk.
4. **Calibrated / schema-constrained output.** No free generation.
5. **Medical questions route to vets.** No diagnosis.
5. **PII never enters prompts.** Redact first.
6. **Fine-tune the extractor, RAG the coach.** Keep nutrition facts current.

## 2. Guiding principles

| Principle | Application |
|---|---|
| **Safety first** | Grounding verifier; adequacy gate |
| **Human in the loop** | Vet endorses/overrides |
| **Least privilege** | ABAC; only the data you're entitled to |
| **Measure twice** | Eval + red-team before release |
| **Transparent** | Citations, run IDs |

## 3. Anti-patterns

- LLM-authored diets.
- Hallucinated nutrition facts.
- PII in prompts/logs.
- Fine-tuned nutrition oracle (stale facts).
- Scope creep into diagnosis.