# Decision Log

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2023-01 | LLM never chooses a diet | Safety; inherited from ProjectDoc | Accepted |
| D-002 | 2023-01 | Intake extraction is schema-constrained | Always parseable; no free generation | Accepted |
| D-003 | 2023-02 | Grounded coaching via RAG | No nutritional hallucination | Accepted |
| D-004 | 2023-02 | Grounding verifier (NLI entailment) | Reject ungrounded claims | Accepted |
| D-005 | 2023-03 | Fine-tune the extractor, RAG the coach | Extractor benefits from LoRA; coach needs current facts | Accepted |
| D-006 | 2023-03 | Medical questions → vet | No diagnosis | Accepted |
| D-007 | 2023-04 | Small/fast for intake, frontier for coaching | Cost vs. quality | Accepted |
| D-008 | 2023-05 | Prompt-injection defense (owner text as data) | Reviews/notes are untrusted | Accepted |
| D-009 | 2023-06 | Red-team regression suite | Release safety | Accepted |
| D-010 | 2024-01 | LoRA fine-tune of the extractor | Tightens schema adherence; cuts cost | Accepted |
| D-011 | 2024-06 | Retrieval reranking (cross-encoder) | Keep authoritative chunks | Accepted |
| D-012 | 2025-01 | Continuous eval in CI | Regression safety | Accepted |

## Change process

- New decisions appended with next ID.
- Status: Proposed → Accepted → Superseded.
- Architectural decisions get a full ADR in `architecture_decision_records/`.