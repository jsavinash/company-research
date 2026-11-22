# Project Documentation — Agentic GLP-1 Demand Sensing & Scenario Copilot (Nestlé USA)

**Project:** Target-state AI Solutions Architect architecture for Nestlé USA's GLP-1-aware demand sensing (Frozen & Coffee)
**Status:** Draft / reference architecture (reconstruction — validate before external use)
**Owner:** AI Solutions Architect (Capgemini Engineering)
**Author tenure:** Mar 2022 – Jun 2024 (2 yrs 4 mos) — split from the Mar 2022 – Nov 2026 Nestlé USA window
**Role title:** Lead AI Engineer — Demand Sensing
**Last updated:** 2026-11-22

---

## Overview

This folder is the full documentation set for the **Agentic GLP-1 Demand Sensing & Scenario Copilot** — a permission-aware, agentic decision-support platform that turns Nestlé USA's structured demand data and unstructured consumer signal into calibrated, causally-attributed, store-level forecasts, and lets demand planners interrogate them conversationally.

The design is an **AI Solutions Architect** deliverable, not a data-science project: the hard problems are integration (SAP/Salesforce/ServiceNow), governance (retailer-contract and household-panel restrictions), permission-aware retrieval, and proving ROI — not the gradient-boosted model.

## Navigation

| Folder | Contents |
|---|---|
| `00-glossary-and-terminology.md` | Single source of truth for terms and acronyms |
| `01-business-and-strategy/` | Executive summary, scope/SLA, stakeholders, KPIs, personas, cost/ROI, risks, solution overview |
| `02-product-and-ux/` | Personas, JTBD, value/retention, journeys, permissions, edge cases, analytics |
| `03_system_and_architecture/` | Requirements & capacity, tech choices & ADRs, HLD, frontend, backend/async, data, API, scalability/DR, security, testing/observability |
| `04_engineering_and_code/` | Repo structure, conventions, LLD/UML, concurrency, internal APIs, quality/workflow, reference implementation |
| `05-quality-and-verification/` | Test strategy, acceptance criteria, performance reports |
| `06-operations-and-infrastructure/` | Cloud topology, environments/secrets, CI/CD, DR, incident runbooks |
| `07-security-compliance-and-users/` | Threat model, privacy, help guides, escalation, release notes |

## Ownership

- **Accountable:** AI Solutions Architect (Capgemini Engineering)
- **Contributors:** Data Science (Nestlé USA), ML Engineering, Platform/SRE, Security & Compliance
- **Approvers:** Nestlé USA Demand Planning leadership; Enterprise Architecture Review Board

## Status rules

- **Draft** — authored, not reviewed.
- **Review** — in architecture review board.
- **Approved** — signed off; changes require a new ADR or decision-log entry.
- **Deprecated** — superseded; see decision log.

## Source-of-truth hierarchy

When documents conflict, precedence is:

1. `03_system_and_architecture/02_tech_choices_and_adrs/decision-log.md` + ADRs (binding decisions)
2. `03_system_and_architecture/03_high_level_design_hld/01_end_to_end_system_architecture.md` (as-built design)
3. `01-business-and-strategy/01_project_overview_and_context.md` (scope, SLAs, constraints)
4. `01-business-and-strategy/13_high_level_solution_overview.md` (solution overview)
5. Everything else (supporting detail)

## Provenance

This documentation set is a reconstruction aligned with Nestlé USA's actual business context (see `../Nestle-USA/Nestle-USA-Research.md` and `../Nestle-USA/Nestle-USA-DemandSensing-ProjectDoc.md`). It is not a verified internal case study; validate all figures and claims before external use.