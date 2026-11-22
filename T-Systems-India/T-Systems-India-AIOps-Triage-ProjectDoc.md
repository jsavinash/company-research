# Project Documentation — Multi-Tenant Change-Risk & Incident Triage (AIOps)

**Working title:** `tsindia-aiops-triage`
**Company context:** T-Systems ICT India Pvt. Ltd. — captive GCC and third-party IT/cloud services arm of T-Systems International (Deutsche Telekom)
**Author tenure:** Dec 2018 – Aug 2019 (9 months), Data / AI Engineering
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable Dec 2018 – Aug 2019 system

---

## 1. Summary

This document specifies a **multi-tenant change-risk and incident-triage capability** for T-Systems India: a service that predicts which changes are likely to fail, classifies and routes incoming incidents, surfaces probable duplicates, and attaches explainable evidence to every score.

**Thesis:** T-Systems India's exposure is not competition — it is **strategic obsolescence** (§12 of the research file). The work that justifies the group's 80%-offshoring target is precisely the work automation erodes: application maintenance, testing, infrastructure operations, service desk. A change-risk and triage layer attacks that from the *cost* side rather than the *headcount* side: it makes the same maintenance and operations workload materially cheaper to deliver, which defends the 21.4% EBITDA margin that funds the group.

**Positioning:** this is not a research artifact. It is a reusable **AI Foundation Services** capability — the thing §3.2 of the research file lists as a service line but which, on the evidence available, India was positioned to build rather than merely resell.

---

## 2. Problem Statement

### 2.1 The business problem

Three facts from the research file converge here:

1. **The captive workload is shrinking at the margin.** §10.2 identifies "AI-driven scope reduction in application maintenance and testing" as a live threat to the core captive workload. Application management, infrastructure operations and service desk are exactly the categories exposed.
2. **India must move up the value chain or slowly shrink.** §12: "If India only does migration and maintenance while AI engineering stays in Germany, the offshoring thesis stalls."
3. **The company has a stated automation target it must hit.** §7.1: 20% efficiency gain through automation, 10,000 people reskilled in AI by 2027, 1,500+ AI experts group-wide. India is where three of those five levers physically happen.

Change and incident volume is the highest-frequency, best-labeled, least glamorous dataset in any IT services operation. It is also the one where errors are immediately visible to the customer as SLA breaches.

### 2.2 The specific failure modes

- **Change-induced incidents.** A large share of unplanned outages originate from changes. Most changes are fine; a small minority cause incidents. That class imbalance is the core modelling difficulty.
- **Misrouted incidents.** Tickets arrive at the wrong resolver group, get reassigned, and burn SLA clock. Every reassignment is a measurable cost and a measurable label.
- **Duplicate incidents.** The same underlying fault produces many tickets. Humans spot duplicates unreliably at volume.
- **Alert noise.** Event storms during an incident obscure signal.

### 2.3 Why this is the right 2018–2019 intervention

| Capability | Availability in window | Use in this project |
|---|---|---|
| Gradient-boosted trees | XGBoost 0.90, LightGBM 2.x, scikit-learn 0.20 | Primary tabular model |
| Calibrated probabilities | Isotonic / Platt | Risk score confidence |
| Transformer NLP | **BERT (Oct 2018)**, `pytorch-pretrained-BERT` | Change/incident text embedding |
| Class imbalance handling | Class weights, focal loss, SMOTE | Rare-failure modelling |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Model registry and lineage |
| Pipeline orchestration | **Kubeflow 1.0 (Jul 2019)**, TFX, Airflow 1.10 | Training/serving workflows |
| Model serving | KFServing, TensorFlow Serving, Flask | Inference endpoint |
| Log/metric processing | Elasticsearch, Spark 2.4, Kafka | Event pipeline |
| Generative LLMs | GPT-2 (Feb 2019) withheld; **not production-viable** | **Excluded** |

The window is unusually well-matched: BERT is nine months old and production-usable, Kubeflow and MLflow have just hit 1.0, and AIOps is at peak industry attention. This is the exact moment this system becomes buildable by a small team.

---

## 3. Scope

### 3.1 In scope

**Change risk**
- Binary classification: will this change be "problematic" (linked to an incident, or closed with an unsuccessful code)?
- Calibrated risk score with the top contributing factors surfaced
- Per-tenant and per-change-type calibration

**Incident triage**
- Multi-label classification: category, subcategory, affected CI, resolver group
- Priority/severity suggestion with rationale
- Duplicate detection against recent open and resolved incidents
- Similar-resolution retrieval from the knowledge base

**Data and platform**
- Ingestion from ServiceNow (change, incident, CI, knowledge articles)
- Feature store for change and CI features
- Model registry, versioning, and audit trail
- Explainability layer for every prediction

### 3.2 Out of scope

- Automated remediation or auto-closing changes (decision-support only)
- Anomaly detection on raw infrastructure metrics (adjacent capability, separate service)
- Capacity planning and forecasting
- Application code analysis or test generation (see §11)
- SAP functional configuration

### 3.3 Non-goals

- **No autonomous change approval.** The score informs a human change advisory board; it does not replace it.
- **No auto-assignment without confidence threshold.** Below the threshold, the ticket goes to a human triage queue.
- **No black-box scores.** Every prediction must carry a human-readable rationale. Regulated European customers require this.

---

## 4. System Architecture (Dec 2018 – Aug 2019 buildable)

```
  ServiceNow (change, incident, CI, KB)
  + event/metric stream (Elasticsearch)
            │
            ▼
  ┌───────────────────────────────────────────────────┐
  │ 1. Ingestion + normalization                       │
  │    Kafka topics → Spark 2.4 structured stream      │
  │    tenant_id, change_id, CI, timestamps, closure   │
  └─────────────────────┬─────────────────────────────┘
                        │
        ┌───────────────▼───────────────┐
        │ 2. Feature assembly            │
        │    tabular: change type, CI    │
        │      criticality, environment, │
        │      team, window, history     │
        │    text: BERT [CLS] embedding  │
        │      of description/justification│
        │    graph: CI dependency features│
        └───────────────┬───────────────┘
                        │
     ┌──────────────────┴──────────────────┐
     ▼                                     ▼
┌──────────────────────────┐   ┌──────────────────────────┐
│ 3. Change-risk model     │   │ 4. Incident models       │
│    XGBoost / LightGBM    │   │    category: XGBoost     │
│    + class weights       │   │    priority: ordinal GBM │
│    + isotonic calibr.    │   │    duplicate: LSH +      │
│    + SHAP explainability │   │      embedding cosine    │
└────────────┬─────────────┘   │    similar: ANN over KB  │
             │                 └────────────┬─────────────┘
             └──────────────┬───────────────┘
                            ▼
  ┌───────────────────────────────────────────────────┐
  │ 5. Routing + confidence policy                     │
  │    score ≥ τ_high  → flag for CAB / auto-suggest  │
  │    τ_low < s < τ_high → human triage queue         │
  │    score ≤ τ_low   → standard path                │
  │    below min confidence → abstain, explain why     │
  └─────────────────────┬─────────────────────────────┘
                        ▼
  ┌───────────────────────────────────────────────────┐
  │ 6. Presentation                                    │
  │    change record: risk badge + top 5 factors       │
  │    incident record: category, CI, group, dupes, KB  │
  │    every score → "why" panel + model version       │
  └───────────────────────────────────────────────────┘
                        │
                        ▼
  ┌───────────────────────────────────────────────────┐
  │ 7. Feedback loop                                   │
  │    CAB decision, reassignment, closure code        │
  │    → new labels → retrain + re-calibrate           │
  └───────────────────────────────────────────────────┘
```

### 4.1 Component notes

**Ingestion.** ServiceNow is the system of record and the label source. Changes carry a closure code; incidents carry a `caused by change` link. Both are structured, historical, and abundant. Kafka plus Spark Structured Streaming is the standard 2019 pattern and is already how most IT services firms handle event data.

**Features.** Two families:
- *Tabular*: change type, CI criticality, environment, implementing team, planned window (start time, duration, overlap with peak), historical failure rate for this CI and this team, CAB approver, number of affected CIs.
- *Text*: BERT `[CLS]` embedding of the change description, justification, and backout plan. BERT (Oct 2018) is the correct choice for this window and materially beats TF-IDF on short, jargon-heavy text.
- *Graph*: CI dependency features — a change touching a heavily depended-upon CI is riskier. Dependency data already exists in the CMDB.

**Change-risk model.** XGBoost or LightGBM, not a neural network. The dataset is tabular, moderate-volume, and interpretability is a hard requirement. Class weights for the rare-failure problem; isotonic regression for calibrated probabilities; SHAP for per-prediction explanations.

**Incident models.** Three separate problems, not one: multi-label category classification, ordinal priority prediction, and duplicate/similarity detection. Similarity uses LSH bucketing plus embedding cosine over BERT vectors — cheap, fast, and adequate.

**Confidence policy.** Threshold selection is per-tenant and per-change-type. A high-risk core banking change gets a different threshold than a low-risk internal portal change. Below the minimum confidence, the system abstains and says why.

**Feedback.** CAB outcomes, reassignments, and closure codes are labels. Every human action improves the model. This loop is the product, not the model.

---

## 5. Data Strategy

### 5.1 Label sources

| Label | Source field | Definition |
|---|---|---|
| Change problematic | Change closure code, `caused by` incident links | "Unsuccessful" or linked incident |
| Incident category | Incident category/subcategory fields | Resolver-assigned |
| Incident resolver group | Assignment group at first resolution | Routing target |
| Incident duplicate | Parent/child incident links, problem records | Curated + inferred |
| Priority | Priority field at closure | Ordinal |
| CAB outcome | Change request approval record | Approve / reject / defer |

### 5.2 The multi-tenant problem

This is the project's differentiator. T-Systems India is simultaneously a captive GCC and a third-party provider (§3.1). A model trained on one tenant's change data does not transfer cleanly to another, because:

- Change taxonomies differ per customer
- CI criticality schemes differ
- Baseline failure rates differ by an order of magnitude
- Regulatory context differs (DORA, NIS2, ISO 27001 customers need different risk tolerances)

Therefore:

1. **Per-tenant calibration.** Global model for the shared signal, per-tenant isotonic calibrators on top.
2. **Tenant as a feature, plus hierarchical shrinkage.** Small tenants borrow strength from the global model; large tenants get their own fit.
3. **Cross-tenant evaluation is mandatory.** Report per-tenant metrics, never just an aggregate. An aggregate that hides a bad tenant is worse than no metric.

### 5.3 Class imbalance

Problematic changes are rare — typically 2–5% of all changes. This is the single biggest technical risk. Mitigations:

- Class weights and focal loss
- Precision-recall AUC as the primary metric, not ROC AUC
- Threshold tuned for the cost asymmetry: a missed bad change costs an outage; a false alarm costs a CAB reviewer's time
- Explicit "insufficient data" handling for new tenants with < 6 months of history

### 5.4 Governance

- Every prediction logged with model version, feature snapshot, and explanation
- Audit-grade lineage for regulated customers (ISO 27001, DORA-aligned)
- Tenant data isolation enforced at the feature store and model registry
- No cross-tenant training on raw text without contractual cover; shared learning happens only through aggregate, de-identified statistics

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| **Change failure rate reduction** | Problematic changes as % of total, before vs. after | **↓ 20% relative** |
| Recall on problematic changes | Of truly problematic changes, fraction flagged | ≥ 0.80 |
| Precision on flagged changes | Of flagged changes, fraction truly problematic | ≥ 0.50 |
| PR-AUC | Primary ranking metric under imbalance | ≥ 0.60 |
| Calibration error (ECE) | Expected calibration error | ≤ 0.05 |
| Incident first-assignment accuracy | Fraction routed correctly first time | ≥ 0.75 |
| Reassignment rate | Tickets reassigned after first assignment | ↓ 25% relative |
| Duplicate detection precision@5 | Of top-5 suggested duplicates, fraction real | ≥ 0.70 |
| MTTR impact | Mean time to restore, before vs. after | ↓ 10% relative |
| CAB reviewer time | Median review seconds per flagged change | ≤ 60 s |

**The headline metric is change failure rate reduction.** Everything else is diagnostic. A model with beautiful PR-AUC that does not reduce outages has not paid for itself.

### 6.2 Evaluation protocol

- **Temporal split.** Train on months 1..N, evaluate on N+1. Never random-split time-series data.
- **Per-tenant reporting.** Aggregate metrics plus a per-tenant breakdown. A tenant below threshold is a launch blocker for that tenant.
- **Change-type stratification.** Report separately for standard, normal, and emergency changes — their base rates and feature distributions differ sharply.
- **Shadow period.** Run in parallel with the existing process for a full release cycle before any score is shown to CAB.

### 6.3 Error analysis

Every failure attributed to:

1. Feature error (stale CMDB, missing CI relationship)
2. Label error (bad closure code, unlinked incident)
3. Model error (ranked a benign change as high-risk)
4. Calibration error (confidently wrong — most dangerous)
5. Concept drift (process or tooling changed)
6. Cold start (new tenant, new CI, new change type)

Category 4 is reviewed at every model release. Category 6 is the expected failure mode for a multi-tenant business and must be planned for, not treated as a defect.

---

## 7. Human-in-the-Loop Design

**CAB reviewer sees for a flagged change:**
- Risk score with calibrated probability and a plain-language band (low / elevated / high)
- Top contributing factors via SHAP, in business language ("affects 3 CIs", "overlaps month-end close", "implementing team's 90-day failure rate is 4x baseline")
- The three most similar historical changes and what happened
- The backout plan completeness check

**Triage agent sees for a new incident:**
- Suggested category, CI, and resolver group with confidence
- Top 5 candidate duplicates with similarity scores and links
- Top 3 knowledge articles by relevance
- An explicit abstention reason where confidence is below threshold

**Actions logged as labels:** accept / override with reason / reject / escalate. Every override is a labelled example.

**Requirement:** median CAB review ≤ 60 seconds, median triage ≤ 20 seconds. If the system is slower than doing it manually, it has failed regardless of its metrics.

---

## 8. Technology Stack (Dec 2018 – Aug 2019)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.6 | Standard |
| Data ingestion | Kafka 2.x, Spark 2.4 Structured Streaming | Event backbone |
| Storage | Elasticsearch (events), PostgreSQL (features/audit), S3 (artifacts) | Conventional |
| Tabular ML | XGBoost 0.90, LightGBM 2.x, scikit-learn 0.20 | Best-in-class for tabular |
| NLP | **BERT (Oct 2018)** via `pytorch-pretrained-BERT` | Period-correct, production-viable |
| Deep learning | PyTorch 1.0–1.1 | BERT support |
| Calibration | scikit-learn isotonic / Platt | Standard |
| Explainability | SHAP 0.3x, LIME | Per-prediction rationale |
| Similarity | LSH (datasketch), ANN over BERT vectors | Fast duplicate detection |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Model registry, lineage, audit |
| Orchestration | **Kubeflow 1.0 (Jul 2019)**, Airflow 1.10 | Pipelines |
| Serving | KFServing / TensorFlow Serving, Flask fallback | Inference |
| Deployment | Docker, Kubernetes | Standard |
| Cloud | AWS / Azure (T-Systems operates both) | Matches existing footprint |

**Excluded deliberately:** GPT-2 (withheld, research-only), any LLM, any autonomous remediation. None belong in a change-approval path in this period.

---

## 9. Delivery Plan (phased to 9 months)

### Phase 0 — Weeks 1–3: Foundations
- Extract 24 months of change and incident history per pilot tenant
- Define the "problematic" label precisely and validate against CAB records
- Baseline metrics: current change failure rate, reassignment rate, MTTR
- **Gate:** baseline measured and signed off by the service delivery owner

### Phase 1 — Weeks 4–10: Feature pipeline
- Kafka + Spark ingestion from ServiceNow
- Tabular feature store with per-tenant versioning
- BERT embedding pipeline for change text
- **Gate:** features reproducible for any historical change from a tagged snapshot

### Phase 2 — Weeks 11–20: Change-risk model
- XGBoost with class weights; per-tenant calibration
- SHAP explanations
- Cross-tenant and temporal evaluation
- **Gate:** recall ≥ 0.75 on problematic changes; ECE ≤ 0.05; per-tenant floor met

### Phase 3 — Weeks 21–30: Incident triage
- Multi-label category and CI classifier
- Duplicate detection (LSH + embedding cosine)
- Similar-resolution retrieval over the KB
- **Gate:** first-assignment accuracy ≥ 0.70; duplicate precision@5 ≥ 0.65

### Phase 4 — Weeks 31–36: Routing and confidence policy
- Per-tenant, per-change-type thresholds
- Abstention logic and explanation surfaces
- UI integration into the change and incident records
- **Gate:** CAB review ≤ 60 s; triage ≤ 20 s

### Phase 5 — Weeks 37–39: Shadow deployment
- Full release cycle in shadow; no scores shown to CAB
- Compare against what the process actually did
- **Gate:** change failure rate ↓ 20% relative in shadow measurement

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Class imbalance makes the model useless | **Critical** | Class weights, focal loss, PR-AUC as primary metric, threshold tuned for cost asymmetry |
| Bad labels (closure codes, unlinked incidents) | High | Validate label definition with CAB; report label-quality sensitivity |
| Tenant data does not transfer | High | Per-tenant calibration, hierarchical shrinkage, mandatory per-tenant metrics |
| Alert fatigue / CAB ignores scores | High | High precision threshold; abstain rather than cry wolf; measure override rate |
| Concept drift after tooling change | High | Monthly drift monitoring; automatic retrain triggers |
| Cold start for new tenants | Medium | Hierarchical model; explicit "insufficient data" state |
| Regulatory audit failure | High | Full lineage, model versioning, immutable prediction logs |
| Cross-tenant data leakage | High | Isolation at feature store and registry; aggregate-only sharing |
| Scope creep into auto-remediation | Medium | Hard boundary — this service scores, humans decide |

---

## 11. What This Deliberately Is Not

- **Not** an auto-remediation engine. It scores and explains; humans act.
- **Not** an infrastructure anomaly detector. That is a separate, adjacent capability on metrics and logs.
- **Not** a GPT-era assistant. GPT-2 was withheld in this window; the NLP layer is BERT-based by construction.
- **Not** a headcount-reduction tool. The business case is margin defence on the existing workload, which is a different and more durable argument than "replace people with models."

### Runner-up use cases (adjacent, same stack)

1. **Legacy application maintenance triage.** Defect prediction and change-impact analysis over application code and ticket history, using the same tabular + BERT stack. Directly addresses §10.2's "AI-driven scope reduction in application maintenance," but needs a code-analysis layer this project does not include.
2. **SAP custom-code remediation assessment.** Rank custom objects by S/4HANA migration risk. Very high business value given the 8 open SAP roles and the multi-year S/4HANA runway (§11), but sits in the SAP function rather than data/AI engineering.
3. **Knowledge-base article quality and gap detection.** BERT-based clustering of resolved incidents against KB coverage. Cheap, fast, and a natural extension of the retrieval component.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `T-Systems-India-Research.md` (research dated 2026-11-21) and describe the **2026** entity: ~4,835 employees, ₹1,413 Cr revenue, 72 open roles, three cities. In Dec 2018 – Aug 2019 the India entity was materially smaller and earlier in its build-out — Pune had opened in Sep 2016 with ~100 people, and the 5,000-person milestone is dated Sep 2026. Any 2019 project would have been scoped to a fraction of the current estate.
- The author's tenure (Dec 2018 – Aug 2019) and function (data / AI engineering) were supplied by the author and are not independently verified.
- Technical claims about the window are period-accurate: BERT released Oct 2018; GPT-2 Feb 2019 (withheld); MLflow 1.0 Jun 2019; Kubeflow 1.0 Jul 2019. GPT-3 (2020) and ChatGPT (2022) postdate the tenure and are excluded by design.
- AIOps was at peak industry attention in 2019 and the literature on change-risk prediction (e.g. IBM's later Cloud Pak work) postdates this window. The architecture here reflects what a competent team could build in 2019, not what was documented publicly at the time.
- Financial and headcount figures are MCA-derived or third-party estimates and are unaudited in this analysis.
- This is a reconstruction. It specifies a system that *could* have been built with the tools of the time and that aligns with the company's stated automation and AI-engineering direction. It is not a claim about what was actually built.