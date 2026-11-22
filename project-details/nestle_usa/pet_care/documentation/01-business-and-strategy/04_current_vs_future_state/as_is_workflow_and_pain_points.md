# As-Is Workflow and Pain Points

## 1. Current (As-Is) workflow

1. **Static intake form** — owner fills rigid fields (species, breed, age, weight).
3. **Rules-based recommendation** — if/else logic maps profile → formula.
4. **Generic feeding guidance** — templated text, same for everyone.
5. **No coaching** — owner reads a spec sheet.
6. **No vet summary** — vet re-derives from scratch.

## 2. Pain points

| Pain point | Impact |
|---|---|
| **Rigid intake** — owners can't express nuance ("itchy paws, hates fish") | Incomplete profiles → poor recommendations |
| **Rules can't handle free text** | Owners abandon the form or give vague answers |
| **Templates feel robotic** | Low engagement, low adherence |
| **No explanation** | Owners don't understand *why* a formula was chosen |
| **No vet handoff** | Vet can't see the reasoning |
| **Risk of hallucination** (if naively adding an LLM) | Unsafe nutrition advice |

## 3. Root causes

- Intake is form-based, not conversational.
- Coaching is templated, not generated.
- No retrieval layer to ground claims.
- No evaluation/red-team discipline for LLM outputs.

## 4. Triggers for change

- LLM inflection (ChatGPT Nov 2022) makes conversational intake feasible.
- RAG + grounding verifiers make LLM coaching safe.
- Purina's precision-nutrition strategy needs per-pet reasoning at scale.