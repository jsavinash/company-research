# User Help Center Guides

## 1. What is the chest triage / CAD?

It reads a chest X-ray already acquired on your system, prioritizes the worklist (routine / priority / urgent), localizes suspicious findings with a heatmap, and gives a **site-calibrated** confidence. You remain the diagnostic authority — it prioritizes and second-reads; you read and sign.

## 2. For radiologists

- **Worklist:** reordered by likelihood of actionable disease.
- **Per study:**
  - Triage category + reason.
  - Heatmap overlaid, finding named in plain language.
  - Site-calibrated confidence band + suggested action.
  - Two most similar prior cases + outcomes.
  - "Cannot assess" where the model abstains.

## 3. Understanding the confidence

| Confidence | Meaning |
|---|---|
| **High** | Strong evidence; prioritize |
| **Medium** | Review recommended |
| **Cannot assess** | Image quality/coverage insufficient — no confident read |

## 4. Troubleshooting

| Issue | Fix |
|---|---|
| Study not analyzed | Check DICOM feed / site connection |
| Heatmap unclear | Check image quality; report |
| Wrong finding | Adjust with reason; it becomes a label |
| Confidence seems off | Check calibration set for the site |

## 5. Best practices

- Always review the heatmap + confidence.
- Cross-check with your own judgment.
- Report domain-shift or calibration issues.