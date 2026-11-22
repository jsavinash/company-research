# Runbook — Database Failover

## When to use

- Snowflake or Databricks primary is unreachable / degraded.
- Replication lag exceeds threshold.
- Regional outage affecting the primary data store.

## Prerequisites

- Access to Databricks, Snowflake, and Terraform.
- On-call SRE + data platform engineer.

## Steps

1. **Confirm the incident**
   - Check status pages (Snowflake, Databricks, Azure).
   - Check Datadog dashboards for replication lag / error rate.

2. **Assess impact**
   - Which pipelines are affected? (forecast batch, copilot queries)
   - Is the replica healthy and current?

3. **Fail over**
   - **Snowflake → Databricks:**
     - Point the feature pipeline to the Databricks replica.
     - Update connection strings via Vault (no code change).
   - **Databricks → Snowflake/SageMaker:**
     - Switch forecast training/serving to the fallback.
   - **Promote replica:**
     - Promote the read replica to primary in the respective console.

4. **Degrade gracefully**
   - If data is stale, serve **last-good forecast** and mark "degraded" in the copilot.
   - Alert planners via status banner.

5. **Communicate**
   - Post to #incidents + status page.
   - Notify demand planning leadership if SLA at risk.

6. **Recover**
   - Once primary is healthy, reverse the failover.
   - Reconcile data (backfill gaps from retained logs / Time Travel).
   - Re-run affected forecast batches.

7. **Review**
   - Post-incident review within 48 h.
   - Update runbook with lessons learned.

## Rollback

- Revert connection strings to primary.
- Re-run reconciliation.

## Escalation

- Data platform on-call → Platform lead → Head of Data.