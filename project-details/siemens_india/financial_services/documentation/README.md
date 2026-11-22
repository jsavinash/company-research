# Project Documentation — Equipment-Embedded Credit-Risk Early-Warning (Siemens Financial Services)

**Project:** Credit-risk early-warning capability for B2B equipment finance, with a corporate risk-data and model-governance layer
**Working title:** `siemens-sfs-credit-earlywarning`
**Company context:** Siemens Financial Services (SFS) — a Siemens AG corporate unit (B2B equipment finance and leasing) — plus Siemens Corporate Units (Finance / Risk / Corporate IT risk-data platform)
**Author tenure:** Apr 2021 – Mar 2022 (1 yr), Senior Data Scientist — Credit Risk
**Status:** Retrospective project spec — reconstructs a buildable Apr 2021 – Mar 2022 system
**Owner:** Senior Data Scientist — Credit Risk (author) · Siemens Financial Services / Corporate Units
**Last updated:** 2026-11-22

---

## Overview

This documentation set specifies a **credit-risk early-warning capability for B2B equipment finance**, with a **corporate risk-data and model-governance layer** that makes it auditable. The system predicts default and delinquency 3–6 months ahead for SFS's portfolio of financed industrial equipment — using a signal a generic lender cannot see: **how the financed machine is actually being operated** (utilization, downtime, service deferrals, energy draw), because that machine is a Siemens asset reporting into Siemens service and operations systems.

**Thesis:** SFS's durable advantage is not a better credit model — banks can match any algorithm. It is **closed-loop Siemens data**: the financed asset's real operation, the order-to-cash relationship, and the service history. A generic lender sees financial statements and payment history — lagging signals. SFS can see the *machine* slow down months before the *payments* do. That converts credit risk from a lagging-financial-signal problem into a leading-operational-signal problem.

**Why this window:** Aug 2019 – Mar 2022 is when gradient-boosted credit models, survival analysis with censoring, and SHAP-based reason codes became production-standard in banking — and when open banking / machine-data initiatives made operational data joinable to credit.

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
- Project spec: `Siemens-FinancialServices-CorporateUnits-ProjectDoc.md`.
- **Entity distinction (critical):** SFS and Corporate Units are **Siemens AG group functions**, distinct from Siemens Limited (India) and Siemens Healthineers India. The sibling docs attribute the same Aug 2019 – Mar 2022 window to those other entities. Resolve the legal employer before publishing.
- This set is a reconstruction of a system that *could* have been built with 2019–2022 tools. Validate all figures before external use.