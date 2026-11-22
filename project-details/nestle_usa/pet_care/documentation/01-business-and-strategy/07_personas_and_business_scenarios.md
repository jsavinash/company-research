# Personas and Business Scenarios

## 1. Personas

| Persona | Needs |
|---|---|
| **Pet owner** | Easy intake, warm coaching, understanding *why* |
| **Veterinarian** | Clinician-readable summary; endorse/override |
| **Nutrition scientist** | KB content, adequacy rules |
| **Data scientist** | Eval + red-team |
| **Compliance** | Safety, audit |

## 2. End-to-end scenarios

### Scenario 1 — Conversational intake
> Owner: "he's a chunky 3-yr-old lab, itchy paws, hates fish."
> LLM extracts: species=dog, breed=Labrador, condition=overweight+atopy, allergen=fish/chicken, preference=no fish. One follow-up (weight?) → profile complete.

### Scenario 2 — Grounded coaching
> Structured plan → RAG over AAFCO/FEDIAF + product spec → "Because he's a 3-yr-old lab who's a bit heavy and reacting to chicken/fish, I picked a salmon-based sensitive-skin formula that still meets adult maintenance. Start with 312 g/day, transition over 7 days. This is nutrition guidance, not veterinary advice."

### Scenario 3 — Vet summary
> Deterministic facts + LLM prose → vet endorses/overrides.

### Scenario 4 — Medical question
> "My dog is vomiting" → hard route to vet, no LLM answer.

## 3. Persona-specific needs

| Persona | Needs |
|---|---|
| Owner | Speed, warmth, trust |
| Vet | Auditability, control |
| Scientist | KB accuracy |
| Compliance | Grounding, PII, audit |