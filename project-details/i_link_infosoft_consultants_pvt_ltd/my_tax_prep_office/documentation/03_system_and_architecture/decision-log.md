# Decision Log

Lightweight log of significant decisions. Complements the ADRs in `architecture-decision-records/`.

| ID | Date | Decision | Rationale | Status |
|---|---|---|---|---|
| D-001 | 2016-09 | LLM/generative models excluded | Not production-viable in 2016–2017; tax correctness does not want them | Accepted |
| D-002 | 2016-09 | Confidence-scored extraction with human review | Never silently accept a low-confidence value | Accepted |
| D-003 | 2016-10 | BiLSTM-CRF + pointer network | Best period-accurate sequence labeling + span extraction | Accepted |
| D-004 | 2016-10 | Tesseract local + Cloud Vision fallback | Local-first, cloud fallback for degraded scans | Accepted |
| D-005 | 2016-11 | Isotonic/Platt calibration | Raw scores are not probabilities | Accepted |
| D-006 | 2016-11 | Per-field thresholds (cost asymmetry) | High-cost fields route aggressively to review | Accepted |
| D-007 | 2016-12 | Synthetic degradation in training | Cover the long tail of real scan conditions | Accepted |
| D-008 | 2017-01 | Ack-without-amendment as ground truth proxy | Scalable labels; human verification on a sample | Accepted |
| D-009 | 2017-02 | Reviewer efficiency gate (≤ 8 s/field) | If review is slower than manual entry, the system failed | Accepted |
| D-010 | 2017-03 | Shadow deployment before auto-fill | Prove reject-rate reduction without risking live filing | Accepted |
| D-011 | 2017-03 | Single deployable behind existing gateway | Match an Express-era shop's appetite | Accepted |

## Change process

- New decisions appended with next ID.
- Status: Proposed → Accepted → Superseded.
- Architectural decisions get a full ADR in `architecture-decision-records/`.