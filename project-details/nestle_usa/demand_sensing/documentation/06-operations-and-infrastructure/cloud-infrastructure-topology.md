# Cloud Infrastructure Topology

## 1. Cloud providers

| Provider | Role |
|---|---|
| **Microsoft Azure** | Primary: Entra ID, Fabric, Azure AI Foundry/OpenAI, Azure AI Search, AKS |
| **AWS** | Bedrock (fallback models), SageMaker (training), S3 (data lake) |
| **GCP** | Vertex AI (fallback), BigQuery (optional analytics) |
| **Databricks** | Lakehouse + Mosaic AI (Unity Catalog) |
| **Snowflake** | Warehouse (retailer data) + Cortex |

## 2. Topology diagram

```
                    ┌──────────────────────────────┐
                    │        Azure (primary)        │
                    │  Entra ID · Fabric · AKS      │
                    │  Azure AI Foundry/OpenAI      │
                    │  Azure AI Search              │
                    └───────────────┬──────────────┘
                                    │
        ┌───────────────────────────┼───────────────────────────┐
        │                           │                           │
┌───────▼────────┐        ┌─────────▼─────────┐       ┌─────────▼────────┐
│   Databricks   │        │     Snowflake     │       │   AWS (fallback) │
│ Unity Catalog  │        │  + Cortex         │       │ Bedrock/SageMaker│
│ Mosaic AI      │        │                   │       │ S3               │
└────────────────┘        └───────────────────┘       └──────────────────┘
        │                           │
        └─────────────┬─────────────┘
                      │
              ┌───────▼────────┐
              │  Neo4j (graph) │
              │  Kafka (stream)│
              │  Feast (store) │
              └────────────────┘
```

## 3. Kubernetes (AKS)

| Namespace | Workload |
|---|---|
| `copilot` | TypeScript/React front-end + BFF |
| `forecast-api` | FastAPI forecast service |
| `agents` | LangGraph agents + Temporal workers |
| `gateway` | AI gateway (Portkey/LiteLLM) |
| `data` | Ingestion, dbt runners |

## 4. Networking

- **VPC isolation** per environment.
- **Private endpoints** to Snowflake, Databricks, Azure services.
- **Egress control** via NAT + firewall.
- **mTLS** between services.

## 5. Data residency

- Data stays in **US regions** (compliance).
- Cross-region replication only for DR.

## 6. Environments

See `environments-and-secrets.md`.