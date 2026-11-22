# Scoping and Constraints

## 1. In scope

- **Conversational intake** — free text → structured pet profile.
- **Grounded coaching** — RAG over AAFCO/FEDIAF + product specs.
- **Vet summary drafting** — deterministic facts + LLM prose.
- **Safety** — grounding verifier, prompt-injection defense, medical routing, refusal paths.
- **Evaluation** — slot accuracy, schema validity, grounding faithfulness, hallucination, red-team.

## 2. Out of scope

- The constrained recommender + adequacy gate (decision core).
- The multi-agent orchestration (separate doc).
- Veterinary diagnosis.
- LLM-authored diets.

## 3. Constraints

- **LLM never chooses a diet.**
- **Grounding-or-refuse.**
- **Medical questions → vet.**
- **PII never in prompts.**
- **Period:** LLM layer post-2022.

## 4. Assumptions

See `../../01-business-and-strategy/05_scope_and_boundaries/assumptions_and_dependencies.md`.

## 5. Change control

Scope changes require a decision-log entry.