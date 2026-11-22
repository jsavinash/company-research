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
| **Intake API** | CPU / RPS | 2 / 20 |
| **Coaching API** | CPU / RPS | 2 / 20 |
| **Vector store** | CPU / memory | 2 / 6 |

## 4. HPA configuration

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

## 5. Scaling strategy

- **Horizontal** (scale out).
- **Vertical** (scale up) for stateful.
- **Cluster autoscaler** for nodes.

## 6. Load testing

- k6 / Locust.
- Peak: 200 concurrent.

## 7. Backpressure

- Queue limits.
- 429 + Retry-After.
- Graceful degradation.

## 8. Multi-region

- Active-passive (DR).
- Active-active (future).

## 9. Monitoring

- Latency, throughput, saturation.
- Alert on HPA events.