# Load Balancing and Auto-Scaling

## 1. Load balancing

| Layer | Choice |
|---|---|
| **External** | Azure Front Door / Load Balancer |
| **Internal** | Kubernetes Service / Ingress |
| **Algorithm** | Round-robin / least-connections |
| **Health checks** | Liveness + readiness |

## 2. Auto-scaling

| Workload | Metric | Min/Max |
|---|---|---|
| **Copilot BFF** | CPU / RPS | 2 / 20 |
| **Forecast API** | Queue depth / CPU | 2 / 30 |
| **Agents** | Queue depth | 2 / 20 |
| **Gateway** | RPS | 2 / 10 |

## 3. HPA configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
spec:
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target: { type: Utilization, averageUtilization: 70 }
```

## 4. Scaling strategy

- **Horizontal** (scale out).
- **Vertical** (scale up) for stateful.
- **Cluster autoscaler** for nodes.

## 5. Load testing

- k6 / Locust.
- Peak: 300 concurrent.
- Validate HPA behavior.

## 6. Backpressure

- Queue limits.
- 429 + Retry-After.
- Graceful degradation.

## 7. Multi-region

- Active-passive (DR).
- Active-active (future).

## 8. Monitoring

- Latency, throughput, saturation.
- Alert on HPA events.

## 9. Related

- `03_high_availability_backups_and_dr.md`
- `Nestle-USA-DemandSensing-AIArchitect-UseCase/05-quality-and-verification/performance-and-load-reports.md`