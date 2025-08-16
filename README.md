# Techyon Industry Platformification Prompt Pack
### From Spark to Shipped: A Complete Product Launch System

## 🚀 Quick Start

This prompt pack is a comprehensive system for taking any product idea from initial concept through to launch-ready status. It includes 12 staged prompts, gate checks, templates, and utilities that work with any LLM (ChatGPT, Claude, Gemini, etc.).

### First Time Setup (2 minutes)
1. Open `prompts/00-master-orchestrator.md`
2. Fill in the variables template at the top
3. Copy the orchestrator prompt into your LLM
4. Follow the execution map it generates

## 📁 What's Included

```
techyon-prompt-pack/
├── prompts/
│   ├── 00-master-orchestrator.md     # Start here - generates your roadmap
│   ├── stages/                       # 12 stage-specific prompts
│   │   ├── 01-problem-discovery.md   # Validate the problem exists
│   │   ├── 02-market-competition.md  # Size opportunity & competition
│   │   ├── 03-solution-prd.md        # Define what you're building
│   │   ├── 04-architecture.md        # Technical decisions
│   │   ├── 05-business-model.md      # Pricing & unit economics
│   │   ├── 06-go-to-market.md        # Customer acquisition strategy
│   │   ├── 07-brand-experience.md    # Brand & UX design
│   │   ├── 08-legal-compliance.md    # Legal & regulatory
│   │   ├── 09-analytics.md           # Metrics & experimentation
│   │   ├── 10-delivery-plan.md       # Execution roadmap
│   │   ├── 11-launch-post-launch.md  # Launch operations
│   │   └── 12-investor-materials.md  # Fundraising assets
│   ├── gates/
│   │   └── universal-gate-check.md   # Go/no-go decision framework
│   └── utilities/
│       ├── intake-form.md            # Structured idea capture
│       └── repo-scaffold.md          # Documentation structure
├── templates/
│   ├── prd-template.md               # Product requirements document
│   ├── gtm-plan-template.md          # Go-to-market plan
│   └── pitch-deck-template.md        # Investor pitch deck
└── outputs/                           # Your generated artifacts go here
```

## 🎯 How It Works

### The Process
1. **Orchestrate**: Run the master orchestrator to validate your inputs and generate an execution map
2. **Execute**: Work through each stage sequentially, generating specific deliverables
3. **Gate Check**: After each stage, use the gate check to decide: proceed, pivot, or kill
4. **Iterate**: Based on gate outcomes, refine and continue or pivot strategically

### Stage Flow
```
Problem Discovery → Market Analysis → Solution Definition → Architecture
    ↓                                                          ↓
Gate Check ←────────────────────────────────────────────── Gate Check
    ↓                                                          ↓
Business Model → GTM Strategy → Brand → Legal/Compliance → Analytics
    ↓                                                          ↓
Gate Check ←────────────────────────────────────────────── Gate Check
    ↓                                                          ↓
Delivery Plan → Launch Prep → Investor Materials → 🚀 Ship It!
```

## 💡 Example Usage

### Scenario: B2B SaaS for Construction Management

1. **Fill Variables:**
```
{IdeaName} = ConstructHub
{OneLine} = Slack for construction sites with IoT sensor integration
{FounderGoals} = speed to revenue
{Audience/ICP} = Mid-size construction companies (50-500 employees)
{Problem/JobsToBeDone} = Coordination between office and field teams
{Industry/Regulatory} = Construction, OSHA compliance
{Constraints} = $50k budget, 3 months, 2-person team
{KeyMetricsNorthStar} = Weekly active projects
{Geography} = United States
```

2. **Run Orchestrator** → Get PR/FAQ and execution map

3. **Stage 1: Problem Discovery**
   - Output: Interview guide for 15 construction managers
   - Result: 73% validate communication as top-3 problem
   - Gate: GREEN - Proceed

4. **Stage 2: Market Analysis**
   - Output: TAM $2.4B, SAM $450M, SOM $15M
   - Result: Clear gap in mobile-first solutions
   - Gate: GREEN - Proceed

5. Continue through stages...

## 🎨 Deliverables You'll Generate

By completing all stages, you'll have:

### Strategic Assets
- ✅ Working Backwards PR/FAQ
- ✅ Product Requirements Document (PRD)
- ✅ Go-to-Market Plan
- ✅ 90-day Execution Roadmap

### Customer-Facing Assets
- ✅ Landing page copy and wireframes
- ✅ Pricing page content
- ✅ Email sequences (6 emails)
- ✅ Sales discovery script
- ✅ 10 objection handlers

### Operational Assets
- ✅ Analytics tracking plan
- ✅ Launch runbook
- ✅ Support documentation
- ✅ Legal compliance checklist

### Fundraising Assets
- ✅ One-pager executive summary
- ✅ 10-slide pitch deck
- ✅ 6-page narrative memo

## 🚦 Gate System

Each stage includes a gate check with three possible outcomes:

- **🟢 GREEN**: Strong signals, proceed to next stage
- **🟡 YELLOW**: Weak signals, run specific tests before proceeding
- **🔴 RED**: No viable path, pivot or kill

### Evidence Quality Scoring (1-5)
- **5**: Money changed hands, signed LOI
- **4**: Verbal commitment, detailed feedback
- **3**: Survey alignment, waitlist signups
- **2**: Polite interest, no commitment
- **1**: No response or negative feedback

## 📝 Pro Tips

### For Maximum Effectiveness
1. **Be Honest at Gates**: Don't fool yourself with weak signals
2. **Kill Fast**: Red gates save time and money
3. **Document Everything**: Use the templates provided
4. **Test Continuously**: Each stage should validate assumptions
5. **Stay Lean**: MVP means minimum - resist feature creep

### Common Pitfalls to Avoid
- ❌ Skipping problem validation
- ❌ Overestimating TAM
- ❌ Building before validating
- ❌ Ignoring unit economics
- ❌ Launching without metrics

### Time Estimates
- **Full Process**: 2-4 weeks of focused work
- **Each Stage**: 2-8 hours of deep work
- **Gate Checks**: 30 minutes of honest evaluation

## 🔧 Customization

### Adapting for Your Context

**For B2C Products:**
- Emphasize Stage 7 (Brand) and Stage 6 (GTM)
- Adjust ICP templates for consumer personas
- Focus on viral/organic growth channels

**For Enterprise:**
- Expand Stage 8 (Legal/Compliance)
- Add proof-of-concept stage before Stage 10
- Include procurement process in GTM

**For Hardware:**
- Add manufacturing/supply chain prompts
- Expand Stage 4 (Architecture) for physical design
- Include certification requirements

## 🤝 Contributing

This prompt pack is open for improvement. To contribute:
1. Test the prompts with real projects
2. Document what works/doesn't work
3. Suggest improvements via issues
4. Share success stories

## 📊 Success Metrics

Track your progress:
- [ ] Orchestrator run and variables defined
- [ ] 3+ stages completed
- [ ] First gate check passed
- [ ] MVP scope defined
- [ ] GTM strategy validated
- [ ] Launch plan created

## 🆘 Troubleshooting

### If the LLM gives generic outputs:
- Add more specific context in your variables
- Reference examples from your industry
- Ask for specific formats (tables, bullets, etc.)

### If you get stuck at a gate:
- Review the evidence quality scores
- Consider pivoting to an adjacent problem
- Run customer discovery interviews
- Reduce scope to increase speed

### If stages feel overwhelming:
- Start with just the orchestrator
- Focus on one stage at a time
- Use templates as starting points
- Skip non-critical stages initially

## 📚 Additional Resources

### Recommended Reading
- "The Mom Test" - Customer discovery
- "Working Backwards" - Amazon's PR/FAQ method
- "Crossing the Chasm" - B2B go-to-market
- "Hooked" - Product engagement

### Useful Tools
- **Figma/Excalidraw** - Wireframing
- **Typeform** - Customer surveys
- **Mixpanel/Amplitude** - Analytics
- **Stripe Atlas** - Company formation

## 📄 License

This prompt pack is provided as-is for commercial and non-commercial use. Attribution appreciated but not required.

---

**Ready to ship your idea?** Start with `prompts/00-master-orchestrator.md` and let's build something amazing.

*Created by Techyon Industries - Turning Ideas into Impact*