# Project Documentation — Real-Time E-Commerce Search Relevance & Recommendation Platform

**Project:** Real-time product-discovery platform (personalized recommendations + query-conditioned search re-ranking) delivered by T-Systems ICT India as a third-party engagement for a European omnichannel retailer
**Working title:** `tsindia-retail-discovery`
**Author tenure:** Dec 2018 – Aug 2019 (9 months), Machine Learning Engineer — Search & Recommendation (client delivery)
**Status:** Retrospective project spec — reconstructs a buildable Dec 2018 – Aug 2019 system for an external retail client
**Owner:** Machine Learning & MLOps Engineering (author) · T-Systems ICT India Pvt. Ltd.
**Last updated:** 2026-11-22

---

## Overview

This documentation set specifies a **real-time product-discovery platform** — personalized recommendations plus query-conditioned search re-ranking — delivered by T-Systems India as a third-party engagement for a European omnichannel retailer. The system separates candidate retrieval from ranking: a two-tower model retrieves a candidate set from a large, changing catalog; a LightGBM LambdaMART ranker re-orders candidates using query, product, user, and session signals; and a serving stack exposes results to the client's search and recommendation placements.

**Thesis:** T-Systems India's durable risk is not competition but **strategic obsolescence** — the captive workload that justifies the group's offshoring target is the work automation erodes. The counter-move is the *third-party provider* half of its dual mandate: a modern ML discovery platform delivered for an external retail client is exactly the high-value AI-engineering work that moves India *up* the value chain.

**Positioning:** two-tower retrieval and LambdaMART ranking are the correct 2018–2019 choices. **TensorFlow Recommenders (TFRS, Sep 2020)** postdates the tenure and is *not* used; the two-tower model is implemented directly in TensorFlow 1.x. "Semantic" means **embedding-based** (Prod2Vec / FastText), not transformer dense retrieval.

## Navigation

| Folder | Contents |
|---|---|
| `00-glossary-and-terminology.md` | Terms, acronyms, definitions |
| `01-business-and-strategy/` | Business case/ROI, scope/SLA, solution overview |
| `02-product-and-ux/` | PRD, user journeys, roadmap |
| `03_system_and_architecture/` | System design, NFRs, data strategy, decision log, ADRs |
| `04_engineering-and-code/` | Principles, LLD, schema/ERD, API contracts |
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

- Company facts: `T-Systems-India-Research.md` (2026-11-21), reflecting the 2026 entity — later than the 2018–2019 project.
- Project spec: `T-Systems-India-EcomSearch-ProjectDoc.md`.
- **Client framing is a reconstruction.** The specific client is not named; the engagement is a plausible reconstruction consistent with T-Systems India's third-party provider mandate. Confirm the client, SOW, and employer record before publishing.
- This set is a reconstruction of a system that *could* have been built with 2018–2019 tools. Validate all figures before external use.