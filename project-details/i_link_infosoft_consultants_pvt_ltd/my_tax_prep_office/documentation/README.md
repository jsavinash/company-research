# Project Documentation — Confidence-Scored Tax Document Extraction (MyTAXPrepOffice)

**Project:** Confidence-scored tax document extraction & eligibility-classification service for MyTAXPrepOffice (Advanced Tax Solutions, Inc.)
**Working title:** `doc-extract-2017`
**Role title:** Associate AI Engineer — Document Intelligence
**Author tenure:** Sep 2016 – Apr 2017 (8 months, spanning the Jan–Apr 2017 filing season)
**Status:** Retrospective project spec — reconstructs a buildable 2016–2017 system, not a modern LLM design
**Owner:** Associate AI Engineer — Document Intelligence (author) · Advanced Tax Solutions, Inc.
**Last updated:** 2026-11-22

---

## Overview

This documentation set specifies a **confidence-scored document extraction and eligibility-classification service** for MyTAXPrepOffice, scoped to what was technically achievable in the Sep 2016 – Apr 2017 window. It converts uploaded tax source documents (W-2, 1099 series, K-1, SSA-1099) into structured field values, attaches a calibrated confidence to every field, and routes low-confidence fields to a human review queue before values are committed to a return.

**Thesis:** the accuracy complaints MyTAXPrepOffice later became known for (dependent-classification errors, EIC miscalculation, missing state schedules) are predominantly *bad-input* defects. Fixing extraction quality and making uncertainty explicit addresses the root cause rather than the arithmetic symptom.

## Navigation

| Folder | Contents |
|---|---|
| `00-glossary-and-terminology.md` | Terms, acronyms, definitions |
| `01-business-and-strategy/` | Business case/ROI, scope/SLA, solution overview |
| `02-product-and-ux/` | PRD, user journeys, roadmap |
| `03_system_and_architecture/` | System design, NFRs, data strategy, decision log, ADRs |
| `04_engineering_and_code/` | Principles, LLD, schema/ERD, API contracts |
| `05-quality-and-verification/` | Test strategy, acceptance criteria, performance |
| `06-operations-and-infrastructure/` | Deployment, environments, CI/CD, runbooks |
| `07-security-compliance-and-users/` | Threat model, privacy, help guides, escalation |

## Source-of-truth hierarchy

1. `03_system_and_architecture/decision-log.md` + ADRs
2. `03_system_and_architecture/system-design-document.md`
3. `01-business-and-strategy/project-scope-and-sla.md`
5. `02-product-and-ux/product-requirements-doc.md`
6. Everything else

## Provenance

- Company/product facts: `MyTAXPrepOffice-Research.md` (2026-11-21), reflecting the **2026** product — later than the 2016–2017 project.
- Project spec: `MyTAXPrepOffice-DocExtract-ProjectDoc.md`.
- This set is a reconstruction of a system that *could* have been built with 2016–2017 tools and matches the company's later document-AI direction (Smart Import). It is not a verified internal record. Validate before external use.