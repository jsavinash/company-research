# Project Documentation — Chest Radiograph Triage & Calibrated CAD (AI-Rad Companion Lineage)

**Working title:** `siemens-healthineers-chest-triage`
**Company context:** Siemens Healthineers India (Medical Solutions) — imaging (X-ray, CT, MR, molecular imaging), radiotherapy, diagnostics, advanced theranostics; AI companion / syngo.via function
**Author tenure:** Aug 2019 – Mar 2022 (2 yrs 8 mos)
**Documentation date:** 2026-11-21
**Status:** Retrospective project spec — reconstructs a buildable Aug 2019 – Mar 2022 system

---

## 1. Summary

This document specifies a **chest-radiograph triage and calibrated computer-aided detection (CAD) capability** for Siemens Healthineers: a system that ingests chest X-rays from the installed base, prioritizes the worklist by likelihood of actionable disease, localizes suspicious findings on the image, attaches a *site-calibrated* confidence to each finding, and keeps the radiologist as the diagnostic authority — delivered as a companion on syngo.via in the AI-Rad Companion lineage, India-first against a tuberculosis (TB) burden that is the largest in the world.

**Thesis:** Siemens Healthineers' durable advantage is not model capability — hyperscalers and pure-play imaging-AI vendors can match or beat any single architecture. It is the **installed base of scanners + clinical workflow integration (syngo.via / teamplay) + regulatory clearance and clinical trust + the de-identified imaging data that base produces** (§3.5 of the research file). This project monetises exactly that moat: it turns a chest X-ray already acquired on a Healthineers system into a triage and second-read signal that is cleared, workflow-native, and explainable — not a standalone black box bolted on beside the scanner.

**Why this, in this window:** Aug 2019 – Mar 2022 is the exact period when three things converged. (1) Siemens Healthineers' **AI-Rad Companion** expanded from CT into chest radiography. (2) COVID made chest-imaging triage AI both urgent and *regulatorily and clinically acceptable* as a worklist-prioritization aid rather than a diagnosis. (3) In **March 2021 the WHO endorsed computer-aided detection (CAD)** as an alternative to human reading of chest X-rays for TB screening — a guideline-anchored, India-relevant use case that did not exist before. The 2026 industrial-AI narrative (Eigen, ICX, €1B AI investment) is Siemens AG, not Healthineers; for Healthineers the descendant of this line is the expanded AI-Rad Companion / syngo.via AI portfolio, and this project is its 2019–2022 ancestor.

---

## 2. Problem Statement

### 2.1 The business problem

Siemens Healthineers' economics are tied to installed base and to the software and AI that ride on it (§3.5). Chest radiography is the highest-volume, most globally distributed, and — in India — most *public-health-relevant* exam in radiology. Three facts converge:

- **Volume.** Chest X-ray is the workhorse of radiology and of TB screening programs at a scale no other modality approaches. Triage value scales with volume.
- **Shortage of readers.** India has a well-documented radiologist shortage; in high-burden screening settings, a human reading every chest X-ray is not achievable. Prioritization — read the urgent ones first — is a real, measurable intervention.
- **The AI moat is workflow + clearance, not the model.** The research file's thesis for the industrial side is "domain data and OT integration, not model capability." The Healthineers analogue is "installed base + clinical workflow + regulatory trust, not model capability." A triage/CAD feature that ships *inside* syngo.via on the scanner's own images, as a cleared companion, is where that moat is monetised.

### 2.2 The five technical problems

This is not "train a chest X-ray classifier." Five hard problems stand between pixels and clinical value:

1. **Prevalence shift breaks calibration.** A model calibrated on a symptomatic hospital cohort is badly miscalibrated when deployed for *screening*, where disease prevalence is one or two orders of magnitude lower. A "0.9 probability of TB" in a clinic is not 0.9 in a screening camp. Per-site, per-prevalence calibration is mandatory, not cosmetic.
2. **Site and device heterogeneity (domain shift).** Fixed DR rooms, portable/mobile units, CR cassettes, pediatric vs. adult, and India-specific rural screening rigs produce very different image distributions. A model trained on one scanner class degrades on another.
3. **Localization and interpretability are the product.** A radiologist will not accept a probability. They need a heatmap that localizes the finding and a confidence that means something — and they must remain the decision-maker for medico-legal reasons. A black-box score is a non-starter.
4. **Label quality and scarcity.** Ground truth is largely radiologist reports (variable, unstructured, no biopsy for most). Definitive microbiological confirmation (sputum smear, culture, GeneXpert) exists for only a subset of TB cases. This is a weak-supervision problem before it is a modelling problem.
5. **Regulation and audit.** CE under the EU MDR (applicable from May 2021), FDA 510(k), and CDSCO each demand locked model versions, audit trails, and documented performance. This is a compliance surface as much as an ML surface.

### 2.3 Why this was buildable in Aug 2019 – Mar 2022

| Capability | Availability in window | Use in this project |
|---|---|---|
| 2D CNNs (DenseNet, ResNet) | Mature | Classification of findings |
| nnU-Net (self-configuring) | Preprint 2018/19, *Nature Methods* 2021 | Segmentation of findings / anatomy |
| Transfer learning (ImageNet) | Standard | Low-label regimes |
| Class imbalance | Focal loss (2017), hard-negative mining | Rare actionable findings |
| Calibration | Temperature scaling (2017), isotonic | Per-site probability calibration |
| Explainability | Grad-CAM (2016), attention maps | Localization heatmaps |
| Medical imaging framework | **MONAI (Dec 2019)** | DICOM, transforms, training |
| DICOM / 3D I/O | pydicom, SimpleITK | Ingestion and preprocessing |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | Airflow 1.10, **Kubeflow 1.0 (2020)** | Training pipelines |
| Multi-site learning | NVIDIA Clara (2019–2020) | Optional federated / harmonized training |
| Generative LLMs | GPT-3 (2020) — no imaging role | **Excluded** |

The period is well-matched: medical-imaging CNNs and nnU-Net are mature and *the* standard of the era, calibration and Grad-CAM are established, MONAI arrives in Dec 2019, and the WHO CAD-for-TB endorsement (Mar 2021) creates the regulatory/clinical demand. The constraint is not model novelty; it is **calibration, domain shift, and regulatory hardening** — precisely the problems this project is designed around.

---

## 3. Scope

### 3.1 In scope

**Modality and population**
- Chest radiography (PA / AP, adult primary; pediatric flagged as a separate profile)
- Fixed DR, portable/mobile, and CR acquisitions (device class is a first-class feature)

**Findings (triage / second-read)**
- TB-suggestive abnormalities — the primary India use case
- Pulmonary nodule, consolidation, pleural effusion, pneumothorax, cardiomegaly
- "Inadequate / cannot assess" as an explicit output state

**Outputs**
- Per-study triage category: routine / priority / urgent (worklist reordering)
- Finding localization heatmap overlaid on the image
- Site-calibrated confidence per finding (never a bare score)
- A structured finding list that maps into syngo.via for the radiologist
- Explicit abstention ("cannot assess — image quality / coverage")

**Platform**
- DICOM ingestion, de-identification, preprocessing, training, registry, serving, monitoring, audit
- Per-site calibration and per-site monitoring

### 3.2 Out of scope

- Autonomous diagnosis or auto-generated final reports (triage / decision-support only)
- CT and MR primary reading (adjacent modalities)
- Mammography / tomosynthesis (different modality and screening workflow)
- Theranostics dosimetry and response assessment (runner-up, §11)
- PACS / RIS replacement (syngo.via integrates with, does not replace)
- Screening-program administration (the health system owns it)

### 3.3 Non-goals

- **No autonomous diagnosis or auto-sign-off.** The radiologist reads, decides and signs. AI prioritizes and second-reads.
- **No uncalibrated score presented as a probability.** Every confidence is site-calibrated; an uncalibrated number is treated as a defect.
- **No black-box output.** Every prediction carries a localization and a rationale; this is a legal requirement, not a preference.
- **No cross-site training on raw PHI without governance.** Federation or per-site training only.

---

## 4. System Architecture (Aug 2019 – Mar 2022 buildable)

```
  ┌──────────────────────────────────────────────────────────┐
  │ Acquisition (installed base)                            │
  │   DR / portable / CR chest X-ray → DICOM                │
  │   syngo.via / PACS worklist                             │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │ Ingestion + de-identification                            │
  │   pydicom / SimpleITK → MONAI transforms                │
  │   PHI scrub, device class + acquisition metadata        │
  │   → versioned data store (per-site, per-device)         │
  └──────────────────────┬──────────────────────────────────┘
                         │
      ┌──────────────────▼──────────────────┐
      │  Inference core (per study)          │
      │   nnU-Net: lung/field + finding      │
      │     segmentation                     │
      │   DenseNet: multi-finding heads      │
      │   Grad-CAM: per-finding heatmaps     │
      │   → raw finding scores + maps        │
      └──────────────────┬──────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Calibration layer (the differentiator)                  │
  │   per-site / per-device temperature scaling              │
  │   per-prevalence isotonic on top                        │
  │   "cannot assess" gate (quality/coverage)                │
  │   → site-calibrated confidence per finding               │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Triage + presentation                                   │
  │   worklist category: routine / priority / urgent         │
  │   syngo.via overlay: heatmap + confidence + finding list │
  │   2 most-similar prior cases (reference)                 │
  │   explicit "cannot assess" where applicable              │
  └──────────────────────┬──────────────────────────────────┘
                         │
  ┌──────────────────────▼──────────────────────────────────┐
  │  Radiologist reads + signs                               │
  │   final report + BI-RADS-like / action code              │
  │   feedback: accept / adjust / reject (with reason)       │
  │   → labels (NLP over report + microbio linkage)          │
  │   → retrain + recalibrate (locked-model release)         │
  └─────────────────────────────────────────────────────────┘

  Training + eval ─► MONAI + nnU-Net ─► MLflow registry ─► Airflow/Kubeflow
  ─► site-held-out validation ─► reader study ─► regulatory-grade release
```

### 4.1 Component notes

**Ingestion and device class.** DICOM is the input and the label carrier. Device class (fixed DR / portable / CR), acquisition parameters and the site identifier are captured as features, not discarded metadata — because domain shift across exactly these dimensions is the dominant real-world failure mode (§5.3).

**Inference core.** nnU-Net (segmentation of lung fields and findings) plus a DenseNet multi-head classifier (per finding). This is the era-standard pairing and it is intentionally *not* novel — the novelty is calibration and workflow, not architecture.

**Calibration layer — the differentiator.** This is where the project earns its place. A global model is trained once, then **per-site temperature scaling and per-prevalence isotonic calibration** are fitted on local labelled data. The same image gets a different, correct probability at a hospital clinic and at a rural screening camp. This layer is the technical heart of the system and the analog of FleetHealth's cross-asset transfer layer.

**Triage and presentation.** Output is a worklist reorder plus a syngo.via overlay (heatmap + calibrated confidence + finding list + similar prior cases). The radiologist always reads the image; the AI never suppresses a study.

---

## 5. Data Strategy

### 5.1 Label sources

| Label | Source | Notes |
|---|---|---|
| Radiologist report | Structured + NLP-extracted findings | Abundant, weak, variable |
| Microbiological confirmation | Sputum smear / culture / GeneXpert | Gold standard for a TB subset |
| Histopathology | Biopsy / resection (few) | Strong but rare |
| Follow-up imaging / outcome | Prior and subsequent studies | Confirms or refutes a finding |
| COVID RT-PCR (2020–21) | Lab link | Period-specific, opportunistic |

### 5.2 The weak-label problem

Most studies have a report, not a biopsy. This must be stated honestly: the training signal is predominantly **NLP-extracted from free-text reports**, noisy and site-dependent, with a small microbiologically confirmed subset. Mitigations, in order of importance:

1. **NLP over reports** to extract findings and laterality, mapped to a controlled vocabulary.
2. **Microbiological linkage for the TB subset** — GeneXpert/smear/culture converts a subset into true gold-standard labels; weight them accordingly.
3. **Multi-reader adjudication for the evaluation set** — the *test* set is read by 2–3 radiologists so that reported performance is not measured against the same weak labels used for training.
4. **Hard-negative mining and focal loss** for the rare actionable findings.

### 5.3 Prevalence shift and calibration

The project's central technical risk, and the reason it must be handled explicitly. Disease prevalence differs by one to two orders of magnitude between a symptomatic hospital cohort and a screening population. Consequences:

- A model calibrated on the clinic is **confidently wrong** at the screening site.
- Therefore: per-site, per-prevalence calibration (§4.1); calibration *slope and intercept* reported per site; and site-held-out validation (§6.2) that measures how badly a model trained on one site transfers to another before any score is shown to a radiologist.

### 5.4 Multi-site governance and regulatory posture

- **Per-site data isolation;** no cross-site raw-PHI training without governance — federation (NVIDIA Clara) or per-site training only.
- **De-identification** at ingestion (DICOM tag scrub, burned-in annotation handling).
- **India DPDP Act** obligations respected as processor; some sites require on-premise only.
- **Locked model versions** with immutable prediction logs (model version, device class, calibration set) for audit.
- **Regulatory surfaces:** EU MDR (applicable May 2021), FDA 510(k), CDSCO — documentation and version control are first-class deliverables.

---

## 6. Evaluation

### 6.1 Metrics

| Metric | Definition | Target |
|---|---|---|
| **Sensitivity for actionable findings** | At a clinically agreed false-positive rate, per site | **≥ 0.85 (site-stratified)** |
| AUROC / AUPRC | Per finding, per site | Report per site |
| Calibration (ECE, slope) | Per site and per prevalence | **ECE ≤ 0.05; slope 0.8–1.25** |
| Localization | IoU of heatmap vs. radiologist boxes | Report per finding |
| Triage yield | % of actionable cases captured in the "urgent/priority" bucket | Report |
| Read-time reduction | Median radiologist read time, triage vs. baseline | **↓ 15% relative** |
| Radiologist acceptance | Fraction of AI localizations a reader agrees with | ≥ 0.70 |
| False-negative audit | Missed confirmed positives in shadow | Report exhaustively |
| Subgroup parity | Performance by age, sex, device class, portable vs. fixed | Max gap ≤ 5 pp |

**The headline metric is calibrated sensitivity at a clinically acceptable false-positive rate, measured per site.** An AUROC that is high on average but miscalibrated at a screening site causes direct patient harm. Everything else is diagnostic.

### 6.2 Evaluation protocol

- **Site-held-out validation.** Train on some sites, test on a *held-out site* — this is the domain-shift claim and it must be measured directly, not assumed from a random split.
- **Temporal split.** Train on earlier studies, test on later ones; random splits leak the future.
- **Subgroup and device-class reporting.** A model that works on fixed DR and fails on portable is a half-product.
- **Multi-reader multi-case (MRMC) reader study.** Radiologist acceptance is measured, not inferred.
- **Prospective silent (shadow) period.** Run silently alongside live reading for a full cycle; audit every false negative before any score is acted upon.

### 6.3 Error analysis

Every failure attributed to one of:

1. **Domain shift** (new site, new device class, portable vs. fixed)
2. **Label error** (report NLP mis-extracted the finding)
3. **Model error** (missed a rare or subtle finding)
4. **Calibration error** (confidently wrong probability — the most dangerous in a screening setting)
5. **Localization error** (right finding, wrong location on the image)
6. **Automation-bias-induced miss** (reader deferred to AI and missed what it got wrong)

Category 4 and category 6 are reviewed at every release. In healthcare, a confidently wrong calibrated score is worse than an abstention.

---

## 7. Human-in-the-Loop Design

**Radiologist sees per study:**
- Triage category (routine / priority / urgent) and the reason
- Heatmap overlaid on the image, with the finding named in plain language
- Site-calibrated confidence band (never a bare number) and a suggested action ("priority review — right upper zone consolidation, site-calibrated 78%")
- The two most similar prior cases and their outcomes
- An explicit "cannot assess — image quality/coverage" where the model abstains

**Radiologist remains the signer.** Final report and action code are theirs. The AI never suppresses a study, never auto-reports, never signs.

**Actions logged as labels:** accept / adjust / reject (with reason) / escalate. Every action becomes training data for the next locked release.

**Requirement:** the overlay must be readable at a glance, not effortful to interpret. If interpretation costs more than the reading it saves, it fails. **Automation bias is measured explicitly** (reader study), because a triage aid that radiologists over-trust becomes a liability.

---

## 8. Technology Stack (Aug 2019 – Mar 2022)

| Layer | Choice | Rationale |
|---|---|---|
| Language | Python 3.7 | Standard |
| Imaging framework | **MONAI (Dec 2019)** | DICOM, transforms, training |
| Segmentation | **nnU-Net** (self-configuring) | Era-standard medical segmentation |
| Classification | PyTorch 1.x, DenseNet / ResNet | Multi-finding heads |
| Imbalance | Focal loss, hard-negative mining | Rare actionable findings |
| Calibration | Temperature scaling, isotonic regression | Per-site, per-prevalence |
| Explainability | Grad-CAM, attention maps | Localization heatmaps |
| I/O | pydicom, SimpleITK | DICOM ingest / de-id |
| Multi-site | NVIDIA Clara (2019–2020) | Optional federation / harmonization |
| Experiment tracking | **MLflow 1.0 (Jun 2019)** | Registry, lineage |
| Orchestration | Airflow 1.10, **Kubeflow 1.0 (2020)** | Training pipelines |
| Serving | TensorFlow Serving, syngo.via integration | Inference at the reading surface |
| Deployment | Docker, Kubernetes | Standard |
| Monitoring | Prometheus / Grafana + DICOM-volume and drift dashboards | Site-level monitoring |

**Excluded deliberately:** GPT-family / any LLM (no role in this imaging modality, and not clinically validated in this window), any black-box model without localization, and any autonomous reporting. The latter two are hard product and regulatory requirements, not preferences.

---

## 9. Delivery Plan (phased to 2 yrs 8 mos)

### Phase 0 — Months 1–2: Foundations
- Select pilot sites: one high-burden TB screening setting + one hospital cohort
- Extract DICOM + reports; define "actionable findings" and the label vocabulary *with* radiologists
- Baseline: current report turnaround and read-time per study
- **Gate:** label definition and baseline signed off by clinical lead

### Phase 1 — Months 3–7: Data and preprocessing platform
- DICOM ingestion + de-identification; device-class capture; MONAI preprocessing
- NLP-over-reports label extraction + microbiological linkage for the TB subset
- nnU-Net segmentation baseline (lung fields, findings)
- **Gate:** features/labels reproducible from a tagged snapshot; de-id verified

### Phase 2 — Months 8–14: Detection and triage models
- nnU-Net segmentation + DenseNet multi-head classifier; focal loss; hard-negative mining
- Grad-CAM localization per finding
- **Gate:** sensitivity ≥ 0.80 at agreed false-positive rate on a random holdout

### Phase 3 — Months 15–22: Calibration and localization
- Per-site temperature scaling + per-prevalence isotonic; calibration slope/intercept per site
- IoU evaluation of heatmaps vs. radiologist boxes
- **Gate:** ECE ≤ 0.05 per site; localization IoU meets threshold per finding

### Phase 4 — Months 23–28: Site-held-out validation and domain adaptation
- Held-out site; harmonization / device-class adaptation
- "Cannot assess" handling for out-of-distribution and poor-quality studies
- **Gate:** site-held-out sensitivity within 5 pp of in-site; no silent miscalibration

### Phase 5 — Months 29–33: Reader study and silent deployment
- MRMC reader study; prospective silent run alongside live reading
- Automation-bias measurement; audit every false negative
- **Gate:** radiologist acceptance ≥ 0.70; read-time ↓ ≥ 15% relative

### Phase 6 — Months 34–38: Regulatory-grade hardening and integration
- Locked model versioning, immutable audit logs, syngo.via integration
- Documentation packages for CE (MDR) / FDA 510(k) / CDSCO
- **Gate:** audit trail complete; versioned rollback demonstrated

---

## 10. Risks and Mitigations

| Risk | Severity | Mitigation |
|---|---|---|
| Prevalence shift makes a clinic-calibrated model harm at a screening site | **Critical** | Per-site/per-prevalence calibration; site-held-out validation; calibration as a release gate |
| Domain shift across sites / devices (portable vs. fixed) | **Critical** | Device-class features; harmonization; site-held-out validation; subgroup parity gate |
| Automation bias — readers over-trust AI and miss its errors | High | Reader study measures both; AI presented as triage not truth; confidence always shown |
| Label noise (report NLP, no gold standard for most) | High | NLP + microbiological linkage for TB subset; adjudicated evaluation set; report label-quality sensitivity |
| Regulatory (EU MDR from May 2021, FDA, CDSCO) | High | Locked model versions; audit logs; documentation as first-class deliverable |
| PHI / India DPDP data governance | High | De-id at ingest; per-site isolation; federation option; on-prem option |
| Rare / long-tail findings | Medium | "Cannot assess" state; never overclaim on unseen patterns |
| Scope creep into autonomous diagnosis | Medium | Hard boundary — this service triages and second-reads; the radiologist decides |
| Post-COVID case-mix shift | Medium | Monthly drift monitoring; recalibration triggers |

---

## 11. What This Deliberately Is Not

- **Not** an autonomous diagnostic system. It prioritizes and second-reads; the radiologist reads and signs.
- **Not** CT or MR reading. Different modality, different workflow, different data.
- **Not** mammography or theranostics. Adjacent but distinct.
- **Not** a PACS replacement. It rides syngo.via; it does not replace it.
- **Not** a GPT/LLM play. The modality is 2D radiography; LLMs are irrelevant here and were not clinically validated in this window.

### Runner-up use cases (adjacent, same stack)

1. **Theranostics dosimetry and response assessment (PET/CT, Ga-68 / Lu-177).** Directly fits the "advanced Theranostics" line in the company profile (§3.5) and is far less crowded than chest radiography AI — but needs molecular-imaging data and a different clinical pathway.
2. **Neuro / stroke CT triage (large-vessel occlusion).** High clinical value, but crowded (Viz.ai, RapidAI) and a different modality.
3. **Mammography / breast screening AI.** Adjacent modality with its own screening workflow; reuses calibration and reader-study methods but not the chest data.

---

## 12. Provenance and Honest Caveats

- Company facts are drawn from `Siemens-Research.md` (research dated 2026-11-21) and describe the **2026** group: 319,000 employees, €83.4B revenue, four segments, Healthineers (€23.6B, 28.3% of revenue) being spun off. In Aug 2019 – Mar 2022, Healthineers had IPO'd (2018) and was majority-owned by Siemens Healthineers AG; the 2026 deconsolidation and the Eigen / ICX / €1B-AI industrial narrative are **Siemens AG, not Healthineers**, and postdate the tenure.
- **Entity distinction (critical for provenance).** Siemens Limited (India) (listed; NSE: SIEMENS) does **not** report Healthineers in its segments — its mix is Smart Infrastructure / Digital Industries / Mobility / Other (§10.1). Siemens Healthineers India is a **separate legal entity** (majority-owned by Siemens Healthineers AG). The sibling file `Siemens-India-FleetHealth-ProjectDoc.md` attributes Aug 2019 – Mar 2022 to **Siemens Limited (India)**; this file attributes the same window to **Siemens Healthineers India**. These are two different employers. **Resolve before publishing:** pick the entity that matches the actual legal employer for the tenure, split the window, or re-attribute the FleetHealth doc — and make CV / LinkedIn agree.
- **India clinical context is real and period-accurate:** India carries roughly a quarter to a third of the global TB burden; the national programme moved to NTEP in 2020; and WHO's consolidated TB screening guidelines (March 2021) endorsed CAD as an alternative to human reading of chest X-rays for TB screening — the guideline anchor for this project.
- **Technical period-accuracy:** nnU-Net (preprint 2018/19, *Nature Methods* 2021), MONAI (first release Dec 2019), temperature scaling (2017), Grad-CAM (2016), MLflow 1.0 (Jun 2019), Kubeflow 1.0 (2020), EU MDR applicable May 2021. AI-Rad Companion's expansion into chest radiography falls inside this window.
- The COVID (2020–2021) chest-triage AI wave is described as period *context*, not as a claim about this project.
- The author's tenure (Aug 2019 – Mar 2022) and function (Siemens Healthineers India, AI companion / syngo.via) were supplied by the author and are not independently verified.
- Financial and headcount figures are company-reported or third-party estimates and are unaudited in this analysis.
- This is a reconstruction. It specifies a system that *could* have been built with the tools of the time and that aligns with Siemens Healthineers' actual imaging-AI trajectory (AI-Rad Companion → syngo.via AI). It is not a claim about what was actually built.