# Executive Summary

## Project

A **generative AI / LLM layer** for Purina's precision pet nutrition platform: intake extraction + grounded coaching, with a hard rule that an LLM never chooses a pet's diet.

## The problem

Pet owners describe their pet in messy free text ("chunky lab, itchy paws, hates fish"). Traditional intake forms are rigid; pure LLM intake hallucinates; pure rules can't handle unbounded phrasing. Coaching needs to be warm and accurate without inventing nutrition facts.

## The solution

Three LLM systems:
1. **Intake extraction** — free text → validated structured profile (JSON schema, slot confidence, missing slots).
2. **Grounded coaching** — structured plan + retrieved KB → plain-language rationale (RAG + grounding verifier).
2. **Vet summary drafting** — deterministic core + LLM prose polish (vet endorses/overrides).

**Core rule:** the LLM narrates; the constrained solver decides.

## Value

- Better intake completion (vs. static forms).
- Warmer, more accurate coaching (vs. templates).
- Fewer nutritional hallucinations (grounding).
- Audit-grade outputs.

## Success criteria

- Slot-extraction accuracy ≥ 0.95.
- Schema validity 100%.
- Grounding faithfulness ≥ 0.95.
- Nutritional hallucination ~0.
- Medical-escalation recall ≥ 0.95.
- Injection resistance: 0 successful.

## Status

Target-state reference (reconstruction). Validate before external use.