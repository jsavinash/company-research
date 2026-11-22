# Glossary and Terminology

## Domain

| Term | Definition |
|---|---|
| **Pet profile** | Structured slots: species, breed, age, condition, allergy, preference. |
| **Nutrient adequacy** | Whether a diet meets AAFCO/FEDIAF requirements for life stage. |
| **AAFCO / FEDIAF** | Pet food nutrient standards (US / Europe). |
| **VUS** | (n/a here) — for pets: "cannot assess" / insufficient profile. |
| **Therapeutic diet** | Prescription diet (veterinary channel). |
| **Cold start** | New pet / thin profile with no history. |
| **Churn / retention** | Subscription repurchase behavior. |
| **Holdout** | Randomized control group to measure true lift. |

## LLM / GenAI

| Term | Definition |
|---|---|
| **RAG** | Retrieval-Augmented Generation — grounding LLM output in retrieved context. |
| **Grounding verifier** | NLI-style entailment check that rejects ungrounded claims. |
| **Schema-constrained decoding** | JSON schema / function calling so output is always parseable. |
| **Slot confidence** | Per-slot extraction confidence. |
| **Missing slots** | Slots the model could not fill. |
| **Prompt injection** | Malicious text in owner input that tries to change model behavior. |
| **LoRA fine-tuning** | Parameter-efficient fine-tuning. |
| **Grounding faithfulness** | Fraction of claims entailed by retrieved chunks. |
| **Nutritional hallucination** | Ungrounded nutrient/health claim. |
| **Refusal path** | Safe fallback when retrieval is low-relevance. |
| **Red-team suite** | Adversarial regression tests. |

## Abbreviations

| Abbreviation | Expansion |
|---|---|
| RAG | Retrieval-Augmented Generation |
| NLI | Natural Language Inference |
| LoRA | Low-Rank Adaptation |
| AAFCO | Association of American Feed Control Officials |
| FEDIAF | European Pet Food Industry Federation |
| LLM | Large Language Model |
| PII | Personally Identifiable Information |
| SLA | Service Level Agreement |
| NFR | Non-Functional Requirement |
| ADR | Architecture Decision Record |