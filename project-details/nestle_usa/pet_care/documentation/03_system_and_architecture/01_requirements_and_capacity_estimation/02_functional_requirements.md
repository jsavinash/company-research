# Functional Requirements

## 1. Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-1 | Ingest free-text owner messages | Must |
| FR-2 | Extract structured pet profile (JSON schema, slot confidence, missing slots) | Must |
| FR-3 | Ask at most one follow-up when completeness is low | Must |
| FR-4 | Recommend via the constrained solver + adequacy gate | Must |
| FR-5 | Ground coaching via RAG over AAFCO/FEDIAF + product specs | Must |
| FR-6 | Grounding verifier rejects ungrounded claims | Must |
| FR-7 | Vet summary drafting (deterministic facts + LLM prose) | Must |
| FR-8 | Medical-question classifier → vet | Must |
| FR-9 | Prompt-injection defense | Must |
| FR-10 | Refusal paths (thin profile / low relevance) | Must |
| FR-11 | PII redaction before prompts | Must |
| FR-12 | LoRA fine-tune of the intake extractor | Should |
| FR-13 | Red-team regression suite | Must |

## 2. Categories

| Category | Requirements |
|---|---|
| **Intake** | FR-1, FR-2, FR-3 |
| **Recommendation** | FR-4 |
| **Coaching** | FR-5, FR-6 |
| **Vet** | FR-7 |
| **Safety** | FR-8, FR-9, FR-10, FR-11 |
| **Optimization** | FR-12 |
| **Evaluation** | FR-13 |

## 3. Prioritization

- **Must:** FR-1..FR-11, FR-13.
- **Should:** FR-12.

## 4. Traceability

Maps to `../10_testing_cicd_and_observability/` and `../../05-quality-and-verification/`.