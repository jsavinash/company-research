# Project Documentation — Chest Radiograph Triage & Calibrated CAD (AI-Rad Companion Lineage)

**Project:** Chest-radiograph triage and calibrated computer-aided detection (CAD) for Siemens Healthineers
**Working title:** `siemens-healthineers-chest-triage`
**Company context:** Siemens Healthineers India (Medical Solutions) — imaging, radiotherapy, diagnostics, advanced theranostics; AI companion / syngo.via function
**Author tenure:** Aug 2019 – Mar 2021 (1 yr 8 mos), Senior AI Engineer — Medical Imaging
**Status:** Retrospective project spec — reconstructs a buildable Aug 2019 – Mar 2021 system
**Owner:** Senior AI Engineer — Medical Imaging (author) · Siemens Healthineers India
**Last updated:** 2026-11-22

---

## Overview

This documentation set specifies a **chest-radiograph triage and calibrated computer-aided detection (CAD) capability** for Siemens Healthineers: a system that ingests chest X-rays from the installed base, prioritizes the worklist by likelihood of actionable disease, localizes suspicious findings, attaches a *site-calibrated* confidence to each finding, and keeps the radiologist as the diagnostic authority — delivered as a companion on syngo.via in the AI-Rad Companion lineage, India-first against the world's largest TB burden.

**Thesis:** Siemens Healthineers' durable advantage is not model capability — hyperscalers and pure-play imaging-AI vendors can match any single architecture. It is the **installed base of scanners + clinical workflow integration (syngo.via / teamplay) + regulatory clearance and clinical trust + the de-identified imaging data that base produces**. This project monetises exactly that moat: it turns a chest X-ray already acquired on a Healthineers system into a triage and second-read signal that is cleared, workflow-native, and explainable.

**Why this window:** Aug 2019 – Mar 2022 is when (1) AI-Rad Companion expanded from CT into chest radiography, (2) COVID made chest-imaging triage AI both urgent and regulatorily/clinically acceptable, and (3) in **March 2021 the WHO endorsed CAD** as an alternative to human reading of chest X-rays for TB screening — a guideline-anchored, India-relevant use case.

## Navigation

| Folder | Contents |
|---|---|
| `00-glossary-and-terminology.md` | Terms, acronyms, definitions |
| `01-business-and-strategy/` | Business case/ROI, scope/SLA, solution overview |
| `02-product-and-ux/` | PRD, user journeys, roadmap |
| `03_system_and_architecture/` | System design, NFRs, data strategy, decision log, ADRs |
| `04_engineering_and_code/` | Principles, LLD, schema/ERD, API contracts |
| `05-quality-and-verification/` | Test strategy, acceptance criteria, performance |
| `06-operations-and-infrastructure/` | Deployment, environments, runbooks |
| `07-security-compliance-and-users/` | Threat model, privacy, help guides, escalation |

## Source-of-truth hierarchy

1. `03_system_and_architecture/decision-log.md` + ADRs
2. `03_system_and_architecture/system-design-document.md`
3. `01-business-and-strategy/project-scope-and-sla.md`
4. `02-product-and-ux/product-requirements-doc.md`
5. Everything else

## Provenance

- Company facts: `Siemens-Research.md` (2026-11-21), describing the **2026** group — later than the 2019–2022 tenure.
- Project spec: `Siemens-Healthineers-ChestTriage-ProjectDoc.md`.
- **Entity distinction (critical):** Siemens Healthineers India is a **separate legal entity** (majority-owned by Siemens Healthineers AG), distinct from Siemens Limited (India) and Siemens Financial Services. The sibling docs attribute the same Aug 2019 – Mar 2022 window to those other entities. Resolve the legal employer before publishing.
- This set is a reconstruction of a system that *could* have been built with 2019–2022 tools. Validate all figures before external use.