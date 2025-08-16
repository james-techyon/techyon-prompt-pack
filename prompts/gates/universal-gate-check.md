# Universal Gate Check System

## Purpose
Make data-driven go/no-go decisions at each stage to prevent sunk cost fallacy and maximize success probability.

---

## Rapid Make/Break Gate Prompt

Use this after completing any stage:

```
Given the latest outputs, return:
- Green if ≥2 independent high-quality signals (willingness-to-pay evidence, warm intros, pilot LOIs, repeated usage in prototype).
- Yellow if signals exist but are weak/uncertain; specify 2 highest-value tests next.
- Red if no strong signals; recommend kill or restart with new segment/job.

Always cite the exact evidence behind the color and the next irreversible step NOT to take.
```

---

## Stage-Specific Gate Criteria

### After Problem Discovery (Stage 1)
- **Green**: ≥70% validation rate, clear budget authority, current spend identified
- **Yellow**: 50-70% validation, needs more interviews or segment adjustment  
- **Red**: <50% validation, no budget, or wrong segment

### After Market Analysis (Stage 2)
- **Green**: TAM >$1B, clear competitive gap, defensible moat hypothesis
- **Yellow**: TAM $100M-1B, indirect competition, needs positioning work
- **Red**: TAM <$100M, dominated market, no clear differentiation

### After Solution Definition (Stage 3)
- **Green**: All stories achievable, no blocking dependencies, clear success metrics
- **Yellow**: 1-2 risky dependencies need spikes, scope needs trimming
- **Red**: Multiple blocking unknowns, scope too large, unclear success criteria

### After Architecture (Stage 4)
- **Green**: Proven stack, team expertise, fits constraints
- **Yellow**: 1-2 learning curves, slight timeline risk
- **Red**: Unproven tech, missing expertise, exceeds constraints

### After Business Model (Stage 5)
- **Green**: LTV:CAC >3:1, payback <12mo, gross margin >70%
- **Yellow**: Ratios are 2:1 to 3:1, improvable with scale
- **Red**: Unit economics don't work, no path to profitability

### After GTM Strategy (Stage 6)
- **Green**: CAC validated, 2+ channels working, clear sales process
- **Yellow**: Channels identified but untested, CAC estimates only
- **Red**: No clear customer acquisition path, CAC too high

### After Brand (Stage 7)
- **Green**: Name available, brand resonates, domain secured
- **Yellow**: Backup name needed, minor trademark concerns
- **Red**: Major trademark issues, brand doesn't resonate

### After Legal/Compliance (Stage 8)
- **Green**: All requirements addressed, no blockers
- **Yellow**: Minor legal review needed, manageable requirements
- **Red**: Major regulatory blockers, compliance too expensive

### After Analytics (Stage 9)
- **Green**: Clear metrics, instrumentation planned, dashboards designed
- **Yellow**: Some tracking gaps, needs refinement
- **Red**: No measurement strategy, can't track success

### After Delivery Plan (Stage 10)
- **Green**: Realistic timeline, resources secured, risks mitigated
- **Yellow**: Minor resource gaps, timeline tight but achievable
- **Red**: Major resource gaps, unrealistic timeline, unmitigated risks

### After Launch Prep (Stage 11)
- **Green**: All systems tested, team ready, rollback plan exists
- **Yellow**: Minor gaps, can launch with careful monitoring
- **Red**: Critical systems not ready, no support plan

---

## Decision Framework

### When to Proceed
- Green light from gate check
- Clear path to next milestone
- Resources available
- Team aligned

### When to Pivot
- Yellow light with specific issues
- Better opportunity identified
- Market feedback suggests adjustment
- Resource constraints force change

### When to Kill
- Red light on critical gates
- No viable pivot path
- Resources better deployed elsewhere
- Fundamental assumption invalidated

---

## Evidence Quality Scoring

Rate each piece of evidence 1-5:

**5 - Highest Quality**
- Money changed hands
- Signed LOI/contract
- Repeated product usage
- Unsolicited referrals

**4 - Strong Signal**
- Verbal commitment with specifics
- Detailed feedback with time investment
- Public endorsement
- Prototype engagement

**3 - Moderate Signal**
- Survey responses align
- Interest but no commitment
- Positive but generic feedback
- Waitlist signups

**2 - Weak Signal**  
- Polite interest
- "Would consider"
- No follow-through
- Low engagement

**1 - No Signal**
- No response
- Negative feedback
- Clear disinterest
- Wrong audience

---

## Gate Review Template

```markdown
## Stage: [Name]
## Date: [Date]
## Reviewer: [Name]

### Evidence Summary
- Signal 1: [Description] - Quality: [1-5]
- Signal 2: [Description] - Quality: [1-5]
- Signal 3: [Description] - Quality: [1-5]

### Gate Decision: [Green/Yellow/Red]

### Rationale
[2-3 sentences explaining decision]

### Next Actions
- If Green: [Next stage]
- If Yellow: [Specific tests needed]
- If Red: [Pivot or kill recommendation]

### Risks to Monitor
- [Risk 1]
- [Risk 2]
```