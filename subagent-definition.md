# Techyon Prompt Pack - Claude Code Subagent

## Agent ID
`techyon-biz-launcher`

## Description
A specialized Claude Code subagent that systematically takes business ideas from concept to launch-ready status using a 12-stage validation framework with go/no-go gates.

## Version
1.0.0

## Author
James Techyon

## Capabilities
- **Problem Validation**: Customer discovery interview guides and evidence logging
- **Market Analysis**: TAM/SAM/SOM calculations and competitive positioning
- **Product Definition**: PRD generation with user stories and acceptance criteria
- **Business Modeling**: Unit economics, pricing strategy, and financial projections
- **GTM Planning**: Channel strategy, messaging frameworks, and sales assets
- **Launch Preparation**: Complete operational runbooks and support documentation
- **Fundraising**: Pitch decks, executive summaries, and investor materials

## Primary Use Cases
1. **Startup Validation**: Test new business ideas before investing resources
2. **Corporate Innovation**: Validate internal innovation projects
3. **Product Expansion**: Assess new product lines or market entries
4. **Pivot Decisions**: Evaluate pivot options when hitting roadblocks
5. **Investment Analysis**: Due diligence framework for investors

## Workflow

### Stage 1: Initialization
```yaml
trigger: User provides business idea
actions:
  - Collect required variables
  - Run master orchestrator
  - Generate PR/FAQ document
  - Create execution roadmap
outputs:
  - Working Backwards document
  - Stage-by-stage timeline
  - Success criteria
```

### Stage 2: Problem Discovery
```yaml
actions:
  - Generate interview questions
  - Create evidence log template
  - Build persona hypotheses
outputs:
  - 15-question interview guide
  - Customer persona cards
  - Evidence tracking system
gate: 70% problem validation required
```

### Stage 3: Market & Competition
```yaml
actions:
  - Calculate market size
  - Analyze competitors
  - Identify moat opportunities
outputs:
  - TAM/SAM/SOM analysis
  - Competitive matrix
  - Positioning strategy
gate: Defensible position identified
```

### Stage 4: Solution & Architecture
```yaml
actions:
  - Define MVP scope
  - Create technical architecture
  - Assess build vs buy options
outputs:
  - Product Requirements Document
  - System architecture diagram
  - Risk register
gate: Technical feasibility confirmed
```

### Stage 5: Business Model
```yaml
actions:
  - Design pricing structure
  - Calculate unit economics
  - Model financial projections
outputs:
  - Pricing & packaging strategy
  - LTV/CAC analysis
  - 24-month financial model
gate: Unit economics viable (LTV:CAC > 3:1)
```

### Stage 6: Go-To-Market
```yaml
actions:
  - Define acquisition channels
  - Create messaging framework
  - Build sales materials
outputs:
  - GTM plan
  - Email sequences
  - Sales scripts
  - Objection handlers
gate: CAC validated in tests
```

### Stage 7-12: Implementation
```yaml
actions:
  - Brand development
  - Legal compliance
  - Analytics setup
  - Launch planning
  - Investor materials
outputs:
  - Complete launch package
  - Operating procedures
  - Fundraising deck
```

## Command Interface

### Slash Command: `/new-biz-pitch`

```bash
/new-biz-pitch [idea_name] [options]
```

#### Options
- `--quick`: Run accelerated validation (stages 1-3 only)
- `--full`: Complete 12-stage process
- `--investor`: Focus on fundraising materials
- `--b2b`: Optimize for B2B business model
- `--b2c`: Optimize for consumer products
- `--saas`: SaaS-specific optimizations
- `--hardware`: Include hardware/manufacturing considerations

#### Examples
```bash
# Quick validation of a new idea
/new-biz-pitch "AI Meeting Assistant" --quick

# Full process for B2B SaaS
/new-biz-pitch "ConstructHub" --full --b2b --saas

# Investor-focused package
/new-biz-pitch "GreenTech Solution" --investor
```

## Integration Points

### Input Sources
- User prompts and idea descriptions
- Market research data
- Customer interview transcripts
- Competitive intelligence
- Financial constraints

### Output Formats
- Markdown documents
- CSV data files
- JSON configuration
- HTML templates
- Pitch deck slides

### Tool Dependencies
- File system operations (Read/Write)
- Web search for market data
- Git for version control
- GitHub for collaboration

## Configuration

### Default Settings
```json
{
  "stages": {
    "enabled": "all",
    "parallel_execution": false,
    "gate_strictness": "medium"
  },
  "outputs": {
    "format": "markdown",
    "include_templates": true,
    "auto_generate_structure": true
  },
  "validation": {
    "min_evidence_quality": 3,
    "require_financial_viability": true,
    "pivot_threshold": 2
  }
}
```

### Customization Options
Users can override defaults via:
```bash
/new-biz-pitch config set gate_strictness high
/new-biz-pitch config set stages.enabled "1,2,3,6"
```

## Success Metrics

### Performance KPIs
- **Validation Speed**: Complete Stage 1-3 in <2 hours
- **Asset Generation**: 30+ deliverables per full run
- **Decision Quality**: 80% correlation with market success
- **User Satisfaction**: Save 100+ hours vs manual process

### Quality Indicators
- Evidence-based gate decisions
- Comprehensive documentation
- Professional-grade outputs
- Actionable recommendations

## Error Handling

### Common Issues & Solutions

#### Insufficient Market Data
```yaml
problem: "Cannot calculate TAM/SAM/SOM"
solution: 
  - Prompt for industry reports
  - Use proxy metrics
  - Provide estimation framework
```

#### Weak Problem Validation
```yaml
problem: "Gate check fails at Stage 1"
solution:
  - Generate pivot options
  - Suggest adjacent problems
  - Provide re-interview guide
```

#### Technical Infeasibility
```yaml
problem: "Architecture not viable"
solution:
  - Explore partnership options
  - Reduce MVP scope
  - Identify technical spikes needed
```

## Best Practices

### Do's
- ✅ Complete each stage before proceeding
- ✅ Be honest at gate checks
- ✅ Document all assumptions
- ✅ Test with real customers early
- ✅ Keep MVP truly minimal

### Don'ts
- ❌ Skip problem validation
- ❌ Ignore negative signals
- ❌ Over-engineer solutions
- ❌ Delay customer contact
- ❌ Proceed without evidence

## Installation

### For Claude Code Users

1. **Clone the repository**:
```bash
git clone https://github.com/james-techyon/techyon-prompt-pack.git
```

2. **Install as subagent**:
```bash
cd ~/.claude/subagents
ln -s /path/to/techyon-prompt-pack techyon-biz-launcher
```

3. **Register slash command**:
Add to `~/.claude/commands.json`:
```json
{
  "commands": [
    {
      "name": "new-biz-pitch",
      "description": "Launch business idea validation workflow",
      "subagent": "techyon-biz-launcher",
      "aliases": ["nbp", "pitch", "validate"]
    }
  ]
}
```

## Examples & Case Studies

### Example 1: B2B SaaS Validation
```bash
/new-biz-pitch "ProjectHub" --b2b --saas
```
**Result**: Validated problem, $2.4B TAM, clear GTM path, raised $500K seed

### Example 2: Quick Pivot Assessment
```bash
/new-biz-pitch "FoodDelivery" --quick
```
**Result**: Failed Stage 1 gate, pivoted to B2B kitchen management, succeeded

### Example 3: Investor Package
```bash
/new-biz-pitch "GreenEnergy" --investor
```
**Result**: Generated complete pitch deck, financial model, and 6-pager

## Support & Updates

- **Repository**: https://github.com/james-techyon/techyon-prompt-pack
- **Issues**: Report bugs or request features via GitHub Issues
- **Updates**: Star/watch the repo for updates
- **Community**: Share success stories with #techyon-prompt-pack

## License

MIT License - Free for commercial and non-commercial use

---

*Turning sparks into shipped products, systematically.*