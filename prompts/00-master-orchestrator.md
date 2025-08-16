# Master Orchestrator Prompt
## Purpose: Drive product ideas from concept to launch-ready plan with stage gates

---

## Variables Template
Copy and fill these variables before running the orchestrator:

```
{IdeaName} = [Your product/service name]
{OneLine} = [One-line description of what it does]
{FounderGoals} = [Choose: speed to revenue | strategic moat | defensibility | lifestyle business | acquisition target]
{Audience/ICP} = [Target customer description]
{Problem/JobsToBeDone} = [Core problem or job to be done]
{Industry/Regulatory} = [Industry context and regulatory requirements]
{Constraints} = [budget, timeline, team, tech stack limitations]
{KeyMetricsNorthStar} = [Primary success metric]
{Geography} = [Target geographic markets]
```

---

## Master Orchestrator Prompt

```
You are my Product Console. Goal: drive {IdeaName} from concept to launch-ready plan with stage gates.

Process:
1) Validate inputs: list missing info as crisp questions (≤8). If nothing missing, proceed.
2) Produce a 1-page Working Backwards PR/FAQ for {IdeaName} (PR summary + 10 FAQs, risks, success metrics).
3) Output an execution map: stages, required evidence, kill criteria, owners, dates.

Output:
- Section A: Missing Info (Q&A list)
- Section B: PR/FAQ (≤500 words + 10 FAQs)
- Section C: Execution Map (table: Stage | Evidence to collect | Kill criteria | Owner | ETA)

Assumptions: state any assumption explicitly.
```

---

## How to Use

1. **Fill Variables**: Complete all variables in the template above
2. **Run Orchestrator**: Copy the filled prompt into your LLM
3. **Answer Questions**: If missing info is identified, provide answers
4. **Review PR/FAQ**: Evaluate the Working Backwards document
5. **Follow Execution Map**: Use the map to guide your stage progression

## Next Steps

After running the orchestrator:
- Proceed to Stage 1: Problem Discovery (`01-problem-discovery.md`)
- Use gate checks after each stage to make go/no-go decisions
- Collect evidence and assets as specified in each stage

## Success Criteria

The orchestrator is successful when it produces:
- Complete PR/FAQ that would pass Amazon's bar
- Clear execution map with measurable evidence requirements
- Specific kill criteria to prevent sunk cost fallacy
- Timeline that aligns with your constraints