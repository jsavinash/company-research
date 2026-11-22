# Project Documentation — Agentic GLP-1 Demand Sensing & Scenario Copilot (Nestlé USA)

**Project:** Target-state AI Solutions Architect architecture for Nestlé USA's GLP-1-aware demand sensing (Frozen & Coffee)
**Status:** Draft / reference architecture (reconstruction — validate before external use)
**Owner:** AI Solutions Architect (Capgemini Engineering)
**Last updated:** 2026-11-22

---

## Overview

This folder is the full documentation set for the **Agentic GLP-1 Demand Sensing & Scenario Copilot** — a permission-aware, agentic decision-support platform that turns Nestlé USA's structured demand data and unstructured consumer signal into calibrated, causally-attributed, store-level forecasts, and lets demand planners interrogate them conversationally.

The design is an **AI Solutions Architect** deliverable, not a data-science project: the hard problems are integration (SAP/Salesforce/ServiceNow), governance (retailer-contract and household-panel restrictions), permission-aware retrieval, and proving ROI — not the gradient-boosted model.

## Navigation

| Folder | Contents |
|---|---|
| `00-glossary-and-terminology.md` | Single source of truth for terms and acronyms |
| `01-business-and-strategy/` | Business case, scope/SLA, solution overview |
| `02-product-and-ux/` | PRD, user journeys, roadmap, experimentation |
| `03-system-and-architecture/` | System design, NFRs, integration/data, decision log, ADRs |
| `04-engineering-and-code/` | Principles, onboarding, LLD, schema/ERD, API contracts |
| `05-quality-and-verification/` | Test strategy, acceptance criteria, performance reports |
| `06-operations-and-infrastructure/` | Cloud topology, environments, CI/CD, DR, runbooks |
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

1. `03-system-and-architecture/decision-log.md` + ADRs (binding decisions)
2. `03-system-and-architecture/system-design-document.md` (as-built design)
3. `01-business-and-strategy/project-scope-and-sla.md` (scope & commitments)
4. `02-product-and-ux/product-requirements-doc.md` (requirements)
5. Everything else (supporting detail)

## Provenance

This documentation set is a reconstruction aligned with Nestlé USA's actual business context (see `Nestle-USA-Research.md` and `Nestle-USA-DemandSensing-ProjectDoc.md`). It is not a verified internal case study; validate all figures and claims before external use.