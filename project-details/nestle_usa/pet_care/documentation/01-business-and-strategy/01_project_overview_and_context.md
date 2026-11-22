# Project Overview and Context

## 1. Overview

The **generative AI / LLM layer** for Purina's precision pet nutrition platform: conversational intake + grounded coaching, with a hard rule that an LLM never chooses a pet's diet.

## 2. Business context

- **Purina PetCare** is ~30% of Zone Americas and the only consistently gaining Nestlé USA unit.
- Precision nutrition is a strategic bet; per-pet reasoning at scale is the differentiator.
- The LLM layer makes the platform conversational and explainable without compromising safety.

## 4. Objectives

- Better intake completion (conversational vs. form).
- Warmer, accurate coaching (grounded, not templated).
- Vet handoff (endorse/override).
- Safety (no nutritional hallucination; LLM never decides).

## 5. Success definition

- Slot accuracy ≥ 0.95; schema validity 100%.
- Grounding faithfulness ≥ 0.95; hallucination ~0.
- Medical-escalation recall ≥ 0.95.
- Injection resistance: 0 successful.

## 6. Out of scope (summary)

The decision core (recommender + adequacy gate), the agentic orchestration, and veterinary diagnosis. See `05_scope_and_boundaries/`.