# To-Be Target Capabilities

## 1. Future (To-Be) workflow

1. **Conversational intake** — owner describes the pet in free text; LLM extracts structured slots with confidence; one follow-up if needed.
2. **Constrained recommendation** — the solver + adequacy gate decides the plan.
3. **Grounded coaching** — RAG over AAFCO/FEDIAF + product specs → warm, accurate rationale; grounding verifier rejects ungrounded claims.
4. **Vet summary** — deterministic facts + LLM prose; vet endorses/overrides.
5. **Feedback loop** — owner/vet actions → labels → improve.

## 2. Target capabilities

| Capability | Description | Business outcome |
|---|---|---|
| **Conversational intake** | Free text → structured profile | Higher completion, better profiles |
| **Grounded coaching** | RAG + verifier → safe explanations | Trust, adherence |
| **Vet summary** | Clinician-readable, auditable | Vet endorsement |
| **Safety** | LLM never chooses diet; grounding-or-refuse | No nutritional hallucination |
| **Evaluation** | Slot accuracy, grounding faithfulness, red-team | Release safety |

## 3. To-Be vs. As-Is

| Dimension | As-Is | To-Be |
|---|---|---|
| Intake | Static form | Conversational + schema |
| Recommendation | Rules | Constrained solver (unchanged core) |
| Coaching | Templates | Grounded LLM narration |
| Vet handoff | None | Summary + endorse/override |
| Safety | N/A | Grounding verifier + guardrails |

## 4. Success criteria

- Slot accuracy ≥ 0.95; schema validity 100%.
- Grounding faithfulness ≥ 0.95; hallucination ~0.
- Medical-escalation recall ≥ 0.95.
- Injection resistance: 0 successful.