# Glossary and Terminology

## Domain

| Term | Definition |
|---|---|
| **Triage** | Worklist prioritization by likelihood of actionable disease. |
| **CAD** | Computer-Aided Detection — a second-read aid for radiologists. |
| **AI-Rad Companion** | Siemens Healthineers' AI companion product family. |
| **syngo.via** | Siemens Healthineers' imaging software platform. |
| **Chest radiography** | Chest X-ray (PA/AP). |
| **DR / CR** | Digital Radiography / Computed Radiography. |
| **Portable / mobile** | Bedside/ward X-ray units (different image distribution). |
| **Finding** | An abnormality (nodule, consolidation, effusion, pneumothorax, cardiomegaly). |
| **Actionable finding** | A finding that changes clinical action (e.g., TB-suggestive). |
| **TB** | Tuberculosis — the primary India use case. |
| **Prevalence shift** | Disease prevalence differs by 1–2 orders of magnitude between clinic and screening. |
| **Domain shift** | Image distribution differs across sites/devices. |
| **Worklist** | The radiologist's queue of studies. |
| **Heatmap / Grad-CAM** | Localization overlay on the image. |
| **Reader study (MRMC)** | Multi-reader multi-case evaluation of radiologist acceptance. |
| **Shadow / silent deployment** | Running alongside live reading without affecting it. |

## Technical

| Term | Definition |
|---|---|
| **nnU-Net** | Self-configuring neural network for medical image segmentation. |
| **DenseNet / ResNet** | CNN architectures for classification. |
| **MONAI** | Medical Open Network for AI (Dec 2019). |
| **DICOM** | Digital Imaging and Communications in Medicine. |
| **pydicom / SimpleITK** | DICOM I/O and image processing. |
| **Temperature scaling** | Calibration by scaling logits. |
| **Isotonic regression** | Non-parametric calibration. |
| **ECE** | Expected Calibration Error. |
| **AUROC / AUPRC** | Discrimination metrics. |
| **IoU** | Intersection over Union (localization). |
| **Focal loss** | Loss for class imbalance. |
| **Hard-negative mining** | Training on difficult negatives. |
| **Grad-CAM** | Gradient-weighted Class Activation Mapping. |
| **NVIDIA Clara** | Medical imaging AI framework (federation). |
| **Federated learning** | Training across sites without pooling raw data. |

## Abbreviations

| Abbreviation | Expansion |
|---|---|
| CAD | Computer-Aided Detection |
| TB | Tuberculosis |
| DR / CR | Digital / Computed Radiography |
| DICOM | Digital Imaging and Communications in Medicine |
| MONAI | Medical Open Network for AI |
| ECE | Expected Calibration Error |
| AUROC | Area Under the Receiver Operating Characteristic |
| AUPRC | Area Under the Precision-Recall Curve |
| IoU | Intersection over Union |
| Grad-CAM | Gradient-weighted Class Activation Mapping |
| MRMC | Multi-Reader Multi-Case |
| PHI | Protected Health Information |
| DPDP | Digital Personal Data Protection (India) |
| MDR | Medical Device Regulation (EU) |
| CDSCO | Central Drugs Standard Control Organisation (India) |
| PACS | Picture Archiving and Communication System |
| SLA | Service Level Agreement |
| NFR | Non-Functional Requirement |
| ADR | Architecture Decision Record |