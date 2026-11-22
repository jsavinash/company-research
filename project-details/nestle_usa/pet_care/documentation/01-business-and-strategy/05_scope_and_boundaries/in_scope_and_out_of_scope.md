# In Scope and Out of Scope

## 1. In scope

- **Conversational intake** — free text → structured pet profile (JSON schema, slot confidence, missing slots).
- **Grounded coaching** — RAG over AAFCO/FEDIAF + product nutrient specs → plain-language rationale.
- **Vet summary drafting** — deterministic facts + LLM prose; vet endorses/overrides.
- **Safety** — grounding verifier, prompt-injection defense, medical-question routing, refusal paths.
- **Evaluation** — slot accuracy, schema validity, grounding faithfulness, hallucination rate, escalation recall, red-team suite.

## 2. Out of scope

- The constrained recommender + nutrient-adequacy gate (the decision core — separate ProjectDoc).
- The multi-agent orchestration (separate Agentic AI use case).
- Veterinary diagnosis / medical advice.
- Autonomous diet selection.

## 3. Explicit non-goals

- **No LLM-authored diet.** The LLM narrates; the solver decides.
- **No fine-tuned nutrition oracle.** The coach is RAG-grounded; fine-tuning is reserved for the intake extractor.
- **No medical/veterinary advisor.** Medical questions route to vets.
- **No free generation of nutrient facts.** Every claim traces to a retrieved chunk.

## 4. Change control

Scope changes require a decision-log entry. Model/prompt changes require an eval report + red-team run.