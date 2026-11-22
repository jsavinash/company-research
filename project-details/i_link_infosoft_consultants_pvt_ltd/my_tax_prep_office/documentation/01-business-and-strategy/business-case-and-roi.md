# Business Case and ROI

## 1. The problem

MyTAXPrepOffice competes on flat, all-inclusive pricing and a 40-brand reseller channel. That model is structurally fragile in exactly one place: **accuracy during filing season**. Recurring negative themes include:

- Dependent classification errors (under-17 children flagged as college dependents)
- State credit miscalculation (NJ EIC, NJ Child Tax Credit)
- Missing state schedules (NJ SCH-HCC, federal Schedule 1-A)
- Weak diagnostics (HOH accepted without a qualifying dependent)

A meaningful share of these originate **upstream of the computation engine**: a mistyped date of birth, a misread K-1, a misclassified relationship, a TIN read from a poor scan.

## 2. The thesis

> The accuracy complaints are predominantly *bad-input* defects. Fixing extraction quality and making uncertainty explicit addresses the root cause rather than the arithmetic symptom.

## 3. The intervention

A **confidence-scored document extraction and eligibility-classification service** that:
- Converts uploaded tax source documents into structured field values.
- Attaches a calibrated confidence to every field.
- Routes low-confidence fields to a human review queue before commitment.

## 4. Value drivers

| Value driver | Mechanism | Beneficiary |
|---|---|---|
| **Fewer e-file rejections** | Better extraction → fewer bad-input defects | Preparers, compliance |
| **Reduced amended returns** | Catch defects before filing | Clients, preparers |
| **Faster review** | Review queue focuses only on uncertain fields | Preparers |
| **Auditability** | Every field has a confidence + provenance | Compliance |
| **Reusable corpus** | E-file acks/rejections/amendments → training labels | Data science |

## 5. Success criteria (business)

- **Downstream reject rate ↓ 50%** vs. baseline (the only business metric that matters).
- Field precision ≥ 0.98 on auto-filled fields.
- Auto-accept rate ≥ 0.80; review queue ≤ 0.20 fields/document.
- Median review time ≤ 8 s/field (or the system has failed regardless of accuracy).

## 6. ROI model

The ROI is dominated by **avoided rejections and amendments**, not by labor savings. Illustrative:
- Reduced rejection handling (staff time + client refunds delayed).
- Fewer amended returns (E&O exposure, reputational cost).
- Faster onboarding (free conversion + AI import as a differentiator).

> Replace with Advanced Tax Solutions' actual baselines before any business-case submission.

## 7. Risks to the business case

| Risk | Mitigation |
|---|---|
| Confidently wrong extraction | Calibration + mandatory review; track category-5 errors separately |
| Scan quality in the independent-preparer segment | Synthetic degradation; cloud OCR fallback |
| Review queue becomes the bottleneck | Efficiency gate ≤ 8 s/field; per-field thresholds |
| Label noise from ack-as-truth proxy | Human verification on stratified sample |
| Regulatory/PII exposure | Encryption, access logging, retention schedule |

See `../11_risk_analysis_and_mitigation.md` (in the main documentation set) for the full register.