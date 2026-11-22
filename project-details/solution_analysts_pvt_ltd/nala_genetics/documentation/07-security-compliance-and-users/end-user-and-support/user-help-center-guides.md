# User Help Center Guides

## 1. What is variant triage?

MyTAXPrepOffice... (Nala CDS) can rank the variants in a patient's exome/genome for clinical review. For each variant it gives a triage score, a calibrated confidence, suggested ACMG evidence codes with provenance, and literature references. If evidence is insufficient, it says so (VUS) instead of guessing.

## 2. Uploading a VCF

1. Upload the germline VCF (WES/WGS) and select the gene panel.
2. The system annotates and triages each variant.
3. Results are ranked; high-priority variants appear first.

## 3. Reviewing a variant

- **Curator sees:** genomic/protein context, score + confidence, top features, suggested ACMG codes + evidence, literature excerpts, population frequencies.
- **Actions:** accept / override with reason / reject / mark insufficient.
- Every action becomes a training label.

## 4. Understanding confidence

| Confidence | Meaning |
|---|---|
| **High** | Strong evidence; prioritize |
| **Medium** | Review recommended |
| **Low / abstained** | Insufficient evidence (VUS) |

## 5. Troubleshooting

| Issue | Fix |
|---|---|
| Variant not annotated | Check panel membership; annotation release |
| Wrong classification | Override with reason; it becomes a label |
| Slow triage | Large VCF; try batch/off-peak |
| Conflicting ClinVar | Both assertions shown with review status |

## 6. Best practices

- Use the correct panel.
- Review high-priority variants first.
- Always record a reason when overriding.
- Report triage issues via support.