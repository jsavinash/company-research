# Master Test Strategy

## 1. Test levels

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Preprocessing, calibration, triage logic | pytest |
| **Integration** | DICOM → segment → classify → calibrate → triage | pytest + test DICOM |
| **Evaluation (ML)** | Sensitivity, ECE, IoU, subgroup parity | Custom eval harness |
| **Adversarial** | Domain shift, prevalence shift, poor quality, rare findings | Golden datasets |
| **Reader study** | Radiologist acceptance (MRMC) | Reader study |
| **Shadow** | Silent run vs. live reading | Shadow deployment |

## 2. Test data

- **Golden datasets:** labeled chest X-rays (report + microbio).
- **Splits:** site-held-out (train some sites, test a held-out site), temporal (train earlier, test later).
- **Segments:** device class (fixed/portable/CR), age, sex.

## 3. Release gates

A release is blocked if:
- Any unit/integration test fails.
- Sensitivity < 0.80 on random holdout.
- ECE > 0.05 per site.
- Site-held-out sensitivity drops > 5 pp vs. in-site.
- Any subgroup gap > 5 pp.
- Any ungrounded nutritional/medical claim.
- Any black-box output without localization.

## 4. Test environments

| Env | Purpose |
|---|---|
| Local | Dev |
| Staging | Pre-prod with test DICOM |
| Prod | Shadow → canary |

## 5. Roles

- **Engineers:** unit + integration.
- **Data science:** evaluation + adversarial.
- **Clinical:** reader study + sign-off.
- **Regulatory:** audit.

## 6. Reporting

- CI dashboard.
- Eval reports on model PRs.