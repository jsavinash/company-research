# Integration and Data Strategy

## 1. Data sources

| Source | Type | Freshness | Notes |
|---|---|---|---|
| Chest X-ray (DICOM) | Imaging | Real-time | DR / portable / CR |
| Radiologist reports | Unstructured | Daily | NLP-extracted findings |
| Microbiological confirmation | Structured | Daily | Sputum smear / culture / GeneXpert (TB subset) |
| Histopathology | Structured | Occasional | Biopsy / resection (few) |
| Follow-up imaging | Imaging | Occasional | Confirms/refutes findings |
| COVID RT-PCR (2020–21) | Structured | Occasional | Period-specific |

## 2. Label sources

| Label | Source | Notes |
|---|---|---|
| Radiologist report | NLP-extracted | Abundant, weak, variable |
| Microbiological confirmation | GeneXpert/smear/culture | Gold standard for a TB subset |
| Histopathology | Biopsy | Strong but rare |
| Follow-up imaging | Prior/subsequent studies | Confirms/refutes |
| COVID RT-PCR | Lab link | Period-specific |

## 3. The weak-label problem

- Most studies have a report, not a biopsy.
- **NLP over reports** → findings + laterality → controlled vocabulary.
- **Microbiological linkage** for the TB subset → true gold-standard labels.
- **Multi-reader adjudication** for the evaluation set (test set read by 2–3 radiologists).
- **Hard-negative mining + focal loss** for rare findings.

## 4. Prevalence shift and calibration

- Disease prevalence differs 1–2 orders of magnitude between clinic and screening.
- A model calibrated on the clinic is **confidently wrong** at a screening site.
- **Per-site, per-prevalence calibration**; calibration slope/intercept reported per site; **site-held-out validation** measures transfer before any score is shown.

## 5. Multi-site governance and regulatory posture

- **Per-site data isolation;** no cross-site raw-PHI training without governance (federation via NVIDIA Clara, or per-site training).
- **De-identification** at ingestion (DICOM tag scrub, burned-in annotation handling).
- **India DPDP Act** obligations; some sites on-premise only.
- **Locked model versions** with immutable prediction logs (model version, device class, calibration set).
- **Regulatory surfaces:** EU MDR (May 2021), FDA 510(k), CDSCO.

## 6. Integration architecture

```
DICOM → pydicom/SimpleITK → MONAI → nnU-Net + DenseNet → calibration → syngo.via
Reports → NLP → labels
Microbio → linkage → gold labels
```

## 7. Integration with enterprise systems

| System | Purpose | Protocol |
|---|---|---|
| syngo.via / PACS | Worklist + overlay | DICOM / API |
| HIS / RIS | Orders, reports | HL7 / FHIR |
| Snowflake / Databricks | Data platform | SQL |
| Kubernetes | Serving | K8s API |

## 8. Data governance

- **Ownership:** Siemens Healthineers India (clinical) + compliance.
- **Lineage:** MONAI + MLflow.
- **Retention:** per policy.
- **Access:** per-site isolation + ABAC.