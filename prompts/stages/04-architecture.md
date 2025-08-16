# Stage 4: Architecture & Build/Buy/Partner Decisions

## Purpose
Define technical architecture, evaluate build vs buy options, and identify key technical risks.

## Required Inputs
- PRD from Stage 3
- {Constraints} (especially tech stack and team)
- {Industry/Regulatory} requirements

## Assets Produced
- Architecture Options Analysis
- High-Level System Diagram
- Data Model
- Risk Register

---

## Prompt

```
Propose 2–3 architecture options (build/buy/partner). For each:
- Diagram (describe components + data flows)
- Pros/cons, costs, time-to-market, lock-in risk
- Minimal data model (core entities + key fields + relationships)
- Integration points and failure modes
- Security & privacy posture (authN/Z, data retention, PII handling)
- Risk register (top 10 risks + mitigations)

Recommend one option with rationale aligned to {Constraints} and {FounderGoals}.
```

---

## Gate Check Prompt

```
Evaluate technical feasibility:
- Red flag if >3 unproven technical dependencies
- Yellow flag if timeline extends beyond constraints
- Green if proven stack with team expertise
Recommend spike tasks for any red/yellow items.
```

---

## Success Metrics
- [ ] Architecture supports all functional requirements
- [ ] Total cost within budget constraints
- [ ] Time-to-market aligns with goals
- [ ] Security/compliance requirements met
- [ ] Team has expertise or clear learning path

## Common Pitfalls
- Over-engineering for scale too early
- Underestimating integration complexity
- Ignoring operational overhead
- Missing compliance requirements

## Next Stage
Proceed to Stage 5: Business Model & Pricing