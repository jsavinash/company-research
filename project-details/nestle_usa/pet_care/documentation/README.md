# Project Documentation — Grounded Nutrition Intake & Coaching LLM System (Purina / Nestlé USA)

**Project:** Generative AI / LLM layer for Purina's precision pet nutrition platform — intake extraction + grounded coaching
**Role framing:** Generative AI / LLM Engineer (prompt & context engineering, RAG, fine-tuning, LLM evaluation, safety)
**Business context:** Nestlé USA — Purina PetCare (Pro Plan, Pro Plan Veterinary Diets, Purina ONE, Beneful, Friskies, Beyond)
**Author tenure:** Jul 2024 – Nov 2026 (2 yrs 5 mos) — split from the Mar 2022 – Nov 2026 Nestlé USA window; LLM layer post-2022
**Role title:** Principal AI Engineer — Generative AI
**Status:** Target-state reference (reconstruction — validate before external use)
**Owner:** Principal AI Engineer — Generative AI (author) · Nestlé USA
**Last updated:** 2026-11-22

---

## Overview

This documentation set specifies the **generative AI / LLM layer** for Purina's precision pet nutrition platform: how LLMs convert messy owner text into a structured pet profile, how a grounded RAG pipeline produces safe coaching, how outputs are evaluated and red-teamed, and how the **"LLM never chooses a diet"** boundary is engineered.

**Core rule (inherited):** an LLM may **explain and coach**; it may **never select a pet's food.** The constrained recommender + nutrient-adequacy gate (the decision core) decides; the LLM narrates.

## Navigation

| Folder | Contents |
|---|---|
| `00-glossary-and-terminology.md` | Terms, acronyms, definitions |
| `01-business-and-strategy/` | Executive summary, scope, cost/ROI, risk |
| `02-product-and-ux/` | Personas, JTBD, value/retention, journeys, edge cases, analytics |
| `03_system_and_architecture/` | Requirements, tech choices/ADRs, HLD, frontend, backend, data, API, scalability, security, testing |
| `04_engineering_and_code/` | Codebase, LLD/patterns, concurrency, internal APIs, quality/workflow |
| `05-quality-and-verification/` | Test strategy, acceptance criteria, performance |
| `06-operations-and-infrastructure/` | Deployment, environments, runbooks |
| `07-security-compliance-and-users/` | Threat model, privacy, help guides, escalation |

## Source-of-truth hierarchy

1. `03_system_and_architecture/02_tech_choices_and_adrs/decision-log.md` + ADRs
2. `03_system_and_architecture/system-design-document.md`
3. `01-business-and-strategy/project-scope-and-sla.md`
4. `02-product-and-ux/product-requirements-doc.md`
5. Everything else

## Provenance

- Company facts: `Nestle-USA-Research.md` (2026-11-21).
- Project spec: `Nestle-USA-PetCare-PrecisionNutrition-ProjectDoc.md`; agentic companion: `Nestle-USA-PetCare-AgenticAI-UseCase.md`; GenAI source: `Nestle-USA-PetCare-GenAI-LLM-UseCase.md`.
- This set is a reconstruction; validate before external use.