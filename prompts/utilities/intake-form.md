# Idea Intake Form & Utilities

## Structured Intake Form Prompt

Use this to generate a complete intake form for your project management system:

```
Generate an intake form for capturing product ideas with these fields:

Core Information:
- IdeaName: [text, required]
- OneLine: [text, max 100 chars, required]
- ICP: [text, required]
- Problem: [textarea, required]
- Alternatives: [textarea, "How is this solved today?"]

Assessment Fields:
- Urgency: [1-5 scale, "How urgent is this problem?"]
- Budget Authority: [yes/no/unknown]
- Success Metric: [text, "How will we measure success?"]
- Estimated Market Size: [dropdown: <$100M, $100M-$1B, $1B-$10B, >$10B]

Constraints:
- Timeline: [dropdown: <1 month, 1-3 months, 3-6 months, 6-12 months, >12 months]
- Budget: [text, "Available resources"]
- Team Size: [number]
- Required Compliance: [multiselect: GDPR, CCPA, HIPAA, SOC2, PCI, Other]

Strategic Context:
- Founder Goals: [multiselect: speed to revenue, strategic moat, defensibility, lifestyle business, acquisition target]
- Data Sensitivity: [high/medium/low]
- Key Stakeholders: [textarea]
- Moat Hypothesis: [textarea, "What makes this defensible?"]

Decision Criteria:
- Go Criteria: [textarea, "What would make this a clear yes?"]
- No-Go Criteria: [textarea, "What would make this a clear no?"]
- Key Risks: [textarea]

Return as:
1. JSON schema for form validation
2. HTML form template
3. Markdown template for documentation
```

---

## Repository/Documentation Scaffold Prompt

```
Generate a complete repository and documentation structure for {IdeaName}:

Create folder structure:
/docs
  - PRD.md
  - GTM.md  
  - AnalyticsPlan.md
  - Security.md
  - RiskRegister.md
  - Roadmap.md
  - Architecture.md

/product
  - user-stories.csv
  - acceptance-criteria.csv
  - feature-matrix.md
  - success-metrics.md

/gtm
  - messaging.md
  - positioning.md
  - competitor-analysis.md
  - sequences/
    - welcome.md
    - nurture.md
    - win-back.md
  - content-calendar.csv
  - sales-materials/
    - pitch-deck.md
    - one-pager.md
    - case-studies/

/ops
  - runbook.md
  - sla.md
  - changelog.md
  - incident-response.md
  - monitoring.md

/legal
  - privacy-policy-outline.md
  - terms-outline.md
  - compliance-checklist.md
  - ip-strategy.md

/research
  - customer-interviews/
  - market-research.md
  - user-personas.md
  - jobs-to-be-done.md

/analytics
  - tracking-plan.md
  - dashboard-specs.md
  - experiment-log.md
  - cohort-definitions.md

Create README.md with:
- Quick links table to all key documents
- Setup instructions
- Contribution guidelines
- Decision log

Output as shell commands to create structure.
```

---

## Quick Decision Matrix Generator

```
Create a decision matrix for {IdeaName} with these criteria:

Evaluation Dimensions:
1. Problem Severity (1-10)
2. Market Size (1-10)
3. Technical Feasibility (1-10)
4. Time to Market (1-10)
5. Competitive Advantage (1-10)
6. Team Fit (1-10)
7. Financial Viability (1-10)
8. Strategic Alignment (1-10)

Weight each dimension and calculate weighted score.
Compare against threshold of 7.0 for go/no-go.

Output as:
- Scoring table
- Weighted calculation
- Visual representation (ASCII chart)
- Recommendation with rationale
```

---

## Customer Interview Script Generator

```
Generate a customer interview script for {IdeaName}:

Opening:
- Introduction and permission to record
- Context setting (not selling, just learning)

Problem Discovery (5 questions):
- Questions that explore the problem space
- Avoid leading or suggesting solutions
- Focus on current behavior and spending

Solution Exploration (5 questions):
- How they solve this today
- What they've tried before
- Dream solution (magic wand question)

Willingness to Pay (3 questions):
- Current spend on alternatives
- Budget authority
- Payment preferences

Closing (2 questions):
- Who else should I talk to?
- Can I follow up with our solution?

Include:
- Follow-up probes for each question
- Red flag answers to watch for
- Note-taking template
```

---

## Competitor Analysis Framework

```
Analyze competitive landscape for {IdeaName}:

Direct Competitors:
- List 3-5 with:
  - Target segment
  - Pricing model
  - Key features
  - Strengths/Weaknesses
  - Market share estimate
  - Recent developments

Indirect Competitors:
- Alternative solutions
- DIY approaches
- Status quo/do nothing

Competitive Positioning:
- 2x2 matrix (choose relevant axes)
- Feature comparison table
- Pricing comparison
- GTM strategy comparison

Differentiation Opportunities:
- Underserved segments
- Feature gaps
- Pricing gaps
- Distribution gaps

Output as:
- Executive summary
- Detailed comparison tables
- Positioning recommendations
- Battle card for sales
```

---

## MVP Scope Cutter

```
Given the full PRD for {IdeaName}, ruthlessly cut to true MVP:

Apply these filters:
1. Must have for core value prop? Keep.
2. Can be done manually first? Cut.
3. Needed for first 10 customers? Keep.
4. Nice to have? Cut.
5. Requires integration? Cut unless critical.
6. Can use existing tool? Cut.

For each feature:
- Original: [Feature description]
- Decision: [Keep/Cut/Defer]
- Rationale: [Why]
- If Cut: [Workaround for v1]

Output:
- MVP feature list (max 5 items)
- Deferred to v2 list
- Cut completely list
- Time saved estimate
```

---

## Financial Model Generator

```
Create a simple financial model for {IdeaName}:

Revenue Assumptions:
- Pricing: ${Price} per {Unit}
- Customer acquisition: {N} per month
- Growth rate: {X}% monthly
- Churn rate: {Y}% monthly

Cost Structure:
- CAC: ${Amount}
- COGS: {%} of revenue
- Fixed costs: ${Monthly}
- Team costs: ${Monthly}

Calculate:
- Monthly revenue (months 1-24)
- Monthly costs
- Gross margin
- Contribution margin
- Break-even point
- Cash required to break-even
- LTV:CAC ratio over time

Output as:
- Key metrics summary
- Month-by-month table
- Sensitivity analysis (vary price, CAC, churn)
- Funding requirements
```

---

## Launch Readiness Checklist

```
Generate comprehensive launch checklist for {IdeaName}:

Product Readiness:
□ Core features tested
□ Edge cases handled
□ Performance acceptable
□ Security review complete
□ Accessibility check

Technical Readiness:
□ Production environment ready
□ Monitoring configured
□ Backup/restore tested
□ Rollback plan documented
□ Load testing complete

GTM Readiness:
□ Landing page live
□ Pricing page ready
□ Documentation complete
□ Sales materials ready
□ Support team trained

Legal Readiness:
□ Terms of service posted
□ Privacy policy posted
□ Compliance requirements met
□ IP protection filed
□ Contracts reviewed

Operational Readiness:
□ Support channels configured
□ SLAs defined
□ Escalation paths clear
□ Team communication plan
□ Success metrics dashboards

For each item, specify:
- Owner
- Due date
- Verification method
- Blocker status (yes/no)
```

---

## Quick Pivot Evaluator

```
Evaluate pivot options for {IdeaName} when hitting a gate failure:

Current State:
- Original hypothesis: {What you believed}
- What failed: {Specific failure point}
- Evidence against: {Data points}

Pivot Options Analysis:
1. Customer Segment Pivot
   - New segment: {Who}
   - Why better: {Rationale}
   - Evidence for: {Supporting data}

2. Problem Pivot
   - New problem: {What}
   - Same customers: {Yes/No}
   - Evidence: {Supporting data}

3. Solution Pivot
   - New approach: {How}
   - Same problem: {Yes/No}
   - Technical feasibility: {Assessment}

4. Business Model Pivot
   - New model: {What}
   - Impact on unit economics: {Analysis}

5. Channel Pivot
   - New channel: {Which}
   - CAC impact: {Estimate}

For each option provide:
- Effort required (1-10)
- Likelihood of success (1-10)
- Time to validate (weeks)
- Key risks

Recommendation: {Which pivot and why}
```

---

## Usage Instructions

1. **For Notion/Linear/Jira**: Use the Intake Form generator to create custom fields
2. **For GitHub**: Use the Repository Scaffold to set up your project
3. **For Decisions**: Run the Decision Matrix when evaluating opportunities
4. **For Research**: Use Interview Script for consistent customer discovery
5. **For Planning**: Use MVP Scope Cutter to stay lean
6. **For Launch**: Use the Readiness Checklist to ensure nothing is missed

Each utility prompt can be customized by adding more specific context about your industry, constraints, or requirements.