# Stakeholders and Governance

## 1. Stakeholder map

| Stakeholder | Role | Interest | Influence |
|---|---|---|---|
| **Executive Sponsor** (VP Demand Planning) | Sponsor | Business outcomes | High |
| **Demand planners** (Frozen, Coffee) | Primary users | Usable, trustworthy forecasts | Medium |
| **RGM analysts** | Users | Causal attribution | Medium |
| **Supply planners** | Users | Store/banner numbers by lead time | Medium |
| **Data science** | Build | Model quality | High |
| **ML engineering** | Build | Platform reliability | High |
| **Platform / SRE** | Run | Availability, latency | Medium |
| **Security & compliance** | Govern | Privacy, audit | High |
| **Finance (RIG)** | Value | ROI reporting | Medium |
| **Enterprise Architecture** | Approve | Standards | High |

## 2. Governance structure

```
Steering Committee (Sponsor + Product Owner + Architect)
        │
Change Advisory Board (CAB)
        │
Delivery (Data Science, ML Eng, Platform, Security)
```

## 3. RACI (summary)

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Business case | Product Owner | Sponsor | Finance | Steering |
| Architecture | AI Solutions Architect | EA Board | Security | Steering |
| Model development | Data Science | DS Lead | Product | Steering |
| Platform ops | ML Eng / SRE | Platform Lead | Security | Product |
| Security & privacy | Security | CISO delegate | Legal | Steering |
| Go-live | Product Owner | Sponsor | All | Steering |

## 4. Decision rights

- **Scope / priority:** Product Owner + Sponsor.
- **Architecture:** AI Solutions Architect + EA Board.
- **Security exceptions:** Security & Compliance.
- **Data access:** Data owners + OPA policy.

## 5. Escalation

See `../07-security-compliance-and-users/end-user-and-support/support-escalation-matrix.md` (or the operations runbooks).