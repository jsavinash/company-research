# Project Scope and SLA

## 1. In scope

- **Input documents:** W-2, 1099-INT, 1099-DIV, 1099-MISC, 1099-NEC, 1099-K, K-1 (1065/1120-S), SSA-1099, 1098, 1098-E, 1098-T
- **Extracted fields:** payer name/TIN, recipient name/TIN, income amounts by box, withholding amounts, dates, dependent DOB, dependent relationship
- **Derived classifications:** dependent category (qualifying child <17 / qualifying child 17+ / qualifying relative / college dependent), document type, tax year
- **Confidence:** per-field calibrated probability + aggregate document-level score
- **Routing:** fields below an adjustable threshold enter a human review queue

## 2. Out of scope

- Tax computation, form generation, e-file transmission (existing engine responsibility)
- Free-form generative advice or narrative drafting
- Handwriting recognition beyond printed/semi-structured forms
- Non-US / non-English document layouts (Spanish IRS forms = phase-2 extension)

## 3. Explicit non-goals

- **No auto-commit of low-confidence fields.** The system must never silently accept a value it is unsure about.
- **No autonomous filing decision.** Output is decision-support for a human preparer.

## 4. Stakeholders

| Stakeholder | Role |
|---|---|
| Preparers | Primary users (review queue) |
| Compliance / operations | Accuracy, audit, WISP obligations |
| Data science | Model development + evaluation |
| Engineering | Platform + serving |
| Leadership (Squire Dahl, Norma Escalona) | Product direction |

## 5. SLAs

| Service | SLA | Measurement |
|---|---|---|
| Extraction API response | p95 ≤ 2 s per document | Service logs |
| Review queue load | ≤ 0.20 fields/document | Queue metrics |
| Field precision (auto-filled) | ≥ 0.98 | Eval harness |
| Calibration error (ECE) | ≤ 0.05 | Eval harness |
| Downstream reject rate | ↓ 50% vs. baseline | E-file outcomes |
| Availability | 99.5% (filing season) | Uptime monitoring |

## 6. Constraints & dependencies

- **Period-accurate tooling (2016–2017):** no transformers, no BERT, no LLMs.
- **PII/TIN data:** encryption, access logging, retention per WISP.
- **Existing stack:** Express/Node API, Angular front-end, PostgreSQL.
- **Filing-season peak:** Jan–Apr demand spike; system must scale.

## 7. Change control

Scope changes require a decision-log entry and, if architectural, a new ADR. SLA changes require sign-off from operations leadership.