# Project Documentation — Confidence-Scored Variant Triage for Nala CDS

**Project:** Confidence-scored variant triage layer for NalaGenetics' Nala Clinical Decision Support (CDS) platform
**Working title:** `nala-variant-triage`
**Author tenure:** May 2017 – Jul 2018 (1 yr 3 mos), AI Engineer — Variant Interpretation
**Status:** Retrospective project spec — reconstructs a buildable May 2017 – Jul 2018 system
**Owner:** Bioinformatics / Software (author) · NalaGenetics Pte. Ltd.
**Last updated:** 2026-11-22

---

## Overview

This documentation set specifies a **confidence-scored variant triage layer** for Nala CDS: a supervised system that ranks germline variants for clinical review, attaches ACMG-aligned evidence codes and calibrated confidence to each, and routes uncertain cases to a human curator queue.

**Thesis:** NalaGenetics' structural problem is not sequencing throughput but *interpretation underrepresentation*. Southeast Asia contributes a small fraction of global genomic reference data, producing elevated variants of uncertain significance (VUS), poorly transferring polygenic scores, and miscalibrated screening. A triage layer that prioritizes the right variants for expert review converts that bottleneck from a headcount problem into a ranking problem.

**Positioning:** DeepVariant (Dec 2017) solved *variant calling* — reads into a VCF. It does not solve *variant interpretation*. This project targets the gap directly downstream.

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

- Company/product facts: `NalaGenetics-Research.md` (2026-11-21), reflecting the **2026** product — later than the 2017–2018 project.
- Project spec: `NalaGenetics-VariantTriage-ProjectDoc.md`.
- This set is a reconstruction of a system that *could* have been built with 2017–2018 tools and aligns with the company's stated platform direction (Nala CDS, Asian-enriched knowledge base). It is not a verified internal record. Validate before external use.