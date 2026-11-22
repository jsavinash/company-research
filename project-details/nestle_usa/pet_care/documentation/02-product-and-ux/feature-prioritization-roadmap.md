# Feature Prioritization Roadmap

## 1. Prioritization method

Features scored on **value** (safety × adoption) vs. **effort** (data readiness + model complexity), with **risk** (safety/regulatory) as a gate.

## 2. Roadmap

### Phase 0–1 (2022) — Pre-LLM
- Rules-based intake; no LLM in path.

### Phase 2 (Jan–Jun 2023) — Intake extractor
- Small model + JSON schema; slot confidence; missing-slot follow-ups.
- Grounding verifier; red-team suite v1.
- **Gate:** slot accuracy ≥ 0.95; schema validity 100%.

### Phase 3 (Jul–Dec 2023) — Coaching
- RAG pipeline over AAFCO/FEDIAF + product specs.
- Vet summary drafter; injection defenses.
- **Gate:** grounding faithfulness ≥ 0.95; injection resistance 100%.

### Phase 4–5 (2024) — Scale & optimize
- LoRA fine-tune of the extractor.
- Retrieval reranking; latency tuning.
- **Gate:** cost/query trend down; latency p95 ≤ 5 s.

### Phase 6 (2025–26) — Continuous eval
- Continuous eval in CI; model/prompt regression gates; audit sampling.
- **Gate:** hallucination ~0; medical-escalation recall ≥ 0.95.

## 3. Deferred / out of scope

- LLM-authored diets.
- Fine-tuned nutrition oracle.
- Medical/veterinary advice.
- Agentic orchestration (separate doc).