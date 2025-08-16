# Stage 3: Solution Definition & PRD

## Purpose
Define the solution scope, user stories, and success criteria for MVP and beyond.

## Required Inputs
- Validated problem and market from Stages 1-2
- {Constraints}
- {KeyMetricsNorthStar}

## Assets Produced
- Outcome-oriented PRD
- User Stories with Acceptance Criteria
- Non-functional Requirements
- Success Metrics

---

## Prompt

```
Create a concise PRD:
- Problem, goals, non-goals
- Scope v1 (MVP) vs v2 (post-MVP)
- 8–12 user stories with acceptance criteria (Gherkin style)
- Non-functional reqs: performance, security, privacy, availability, compliance
- Success metrics: activation, time-to-value, core action, retention, NPS

Output: PRD markdown + backlog table (Story | AC | Effort t-shirt | Risk)
```

---

## Gate Check Prompt

```
Flag any story that requires uncertain tech or third-party dependency. Propose spike tasks and success criteria for each spike.
```

---

## Success Metrics
- [ ] All user stories map to validated problems
- [ ] MVP scope achievable in <90 days
- [ ] Clear success metrics defined
- [ ] Non-functionals documented
- [ ] No unmitigated high-risk dependencies

## Common Pitfalls
- Feature creep in MVP
- Vague acceptance criteria
- Missing non-functional requirements
- Unrealistic scope for constraints

## Next Stage
Proceed to Stage 4: Architecture & Build/Buy/Partner