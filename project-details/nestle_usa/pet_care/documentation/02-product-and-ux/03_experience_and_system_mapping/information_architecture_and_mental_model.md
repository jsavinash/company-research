# Information Architecture and Mental Model

## 1. Object model

| Object | Attributes | Relationships |
|---|---|---|
| **PetProfile** | species, breed, age, condition, allergy, preference, completeness | has many plans |
| **Plan** | formula, portion, rationale | belongs to profile |
| **CoachingSession** | query, response, citations | belongs to plan |
| **VetSummary** | facts, prose, endorsement | belongs to plan |

## 2. Navigation / IA

```
Home
├── Intake (describe pet)
├── Plan (recommendation + rationale)
├── Coaching (chat + citations)
├── Vet summary (endorse/override)
└── Profile (edit, history)
```

## 3. Mental model

Owners think in terms of:
- **Pet** (species, breed, age, condition).
- **Food** (formula, portion, transition).
- **Why** (nutrition, not medical).

The IA should mirror this: pet → plan → why → vet.

## 4. Key screens

| Screen | Purpose | Key elements |
|---|---|---|
| **Intake** | Describe pet | Chat, slots, completeness |
| **Plan** | Recommendation | Formula, grams, adequacy |
| **Coaching** | Explain | Citations, transition plan |
| **Vet summary** | Clinician handoff | Facts + endorse/override |

## 5. Navigation principles

- **Pet-first:** profile → plan → geography → time.
- **Progressive disclosure:** summary → rationale → citations.
- **Consistent run IDs:** every answer auditable.