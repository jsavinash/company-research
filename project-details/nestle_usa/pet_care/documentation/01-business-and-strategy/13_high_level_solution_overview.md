# High-Level Solution Overview

## 1. One-line description

> A generative AI layer for Purina's precision pet nutrition: schema-constrained intake extraction + grounded RAG coaching, with a hard rule that an LLM never chooses a pet's diet.

## 2. Core design decision

**The LLM narrates; the constrained solver decides.** And **grounding-or-refuse** — every nutritional claim traces to a retrieved chunk, or the model refuses.

## 3. Architecture at a glance

```
Owner free text
   ▼
1. Intake extraction (small model + JSON schema) → structured profile + slot confidence
   ▼
2. Constrained recommender + adequacy gate (the decision core) → plan
   ▼
3. RAG coaching: retrieve KB (AAFCO/FEDIAF + product) → frontier LLM → grounding verifier → rationale
   ▼
4. Vet summary: deterministic facts + LLM prose → vet endorses/overrides
   ▼
5. Feedback: owner/vet actions → labels → improve
```

## 4. The three LLM systems

| System | Input → Output | Model tier |
|---|---|---|
| **Intake extraction** | Free text → JSON profile | Small/fast |
| **Grounded coaching** | Plan + retrieved KB → rationale | Frontier |
| **Vet summary** | Profile + plan → clinician prose | Mid-tier |

## 5. Why this is a GenAI/LLM engineering use case

- Prompt & context engineering (schema, grounding, injection defense).
- RAG architecture (hybrid retrieval, rerank, chunk metadata).
- Fine-tuning (LoRA for the extractor) vs. RAG (coach).
- LLM evaluation (slot accuracy, grounding faithfulness, hallucination, red-team).
- Safety (guardrails, PII, medical routing).

See `../03_system_and_architecture/` for the detailed design.