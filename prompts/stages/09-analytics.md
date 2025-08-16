# Stage 9: Analytics & Experimentation Framework

## Purpose
Design measurement system for tracking product health, user behavior, and experiment velocity.

## Required Inputs
- {KeyMetricsNorthStar}
- User stories from Stage 3
- GTM channels from Stage 6

## Assets Produced
- Metrics Framework
- Event Taxonomy
- Dashboard Specifications
- A/B Testing Plan
- Cohort Analysis Setup

---

## Prompt

```
Deliver:
- North Star + 3 input metrics
- Event schema (event → properties → when instrumented)
- Dashboard spec: tiles, formulas, refresh cadence
- A/B testing plan: primary metric, MDE assumption, sample size heuristic, guardrails
- Cohort analysis plan for retention & payback

Output as: tracking plan table + dashboard PRD.
```

---

## Gate Check Prompt

```
Analytics readiness check:
- Green if instrumentation plan covers all key user flows
- Yellow if some tracking gaps exist
- Red if no clear measurement strategy
Prioritize top 5 events to instrument first.
```

---

## Success Metrics
- [ ] North Star metric clearly defined
- [ ] Input metrics have causal relationship
- [ ] All critical events instrumented
- [ ] Dashboard live before launch
- [ ] A/B testing framework ready

## Common Pitfalls
- Tracking everything (analysis paralysis)
- Missing attribution tracking
- No baseline metrics before changes
- Ignoring qualitative data

## Next Stage
Proceed to Stage 10: Delivery Plan & Operating Cadence