# Installation Guide - Techyon Prompt Pack for Claude Code

## Quick Install (30 seconds)

### 1. Clone the Repository
```bash
git clone https://github.com/james-techyon/techyon-prompt-pack.git
cd techyon-prompt-pack
```

### 2. Install as Claude Code Subagent

#### Option A: Automatic Installation
```bash
# Run the installer script
./install-claude-code.sh
```

#### Option B: Manual Installation
```bash
# Create subagents directory if it doesn't exist
mkdir -p ~/.claude/subagents

# Create symbolic link
ln -s $(pwd) ~/.claude/subagents/techyon-biz-launcher

# Copy command configuration
cp claude-code-integration/commands.json ~/.claude/commands.json

# Make Python script executable
chmod +x claude-code-integration/new-biz-pitch.py
```

### 3. Verify Installation
```bash
# In Claude Code, type:
/new-biz-pitch --help
```

## Usage Examples

### Quick Validation (3 stages only)
```bash
/new-biz-pitch "AI Meeting Assistant" --quick
```

### Full Business Validation (all 12 stages)
```bash
/new-biz-pitch "ConstructHub" --full --b2b --saas
```

### Generate Investor Package
```bash
/new-biz-pitch "GreenTech Solution" --investor
```

### Using Aliases
```bash
# Short alias
/nbp "FoodDelivery" --quick --b2c

# Other available aliases
/pitch "MyIdea"
/validate "ProductConcept"
/idea "Innovation"
```

## Command Options

| Option | Description | Example |
|--------|-------------|---------|
| `--quick` | Run stages 1-3 only (problem, market, solution) | `/nbp "idea" --quick` |
| `--full` | Run all 12 stages (default) | `/nbp "idea" --full` |
| `--investor` | Focus on fundraising materials | `/nbp "idea" --investor` |
| `--b2b` | Optimize for B2B business model | `/nbp "idea" --b2b` |
| `--b2c` | Optimize for consumer products | `/nbp "idea" --b2c` |
| `--saas` | SaaS-specific optimizations | `/nbp "idea" --saas` |
| `--hardware` | Include hardware considerations | `/nbp "idea" --hardware` |
| `--stage N` | Start from specific stage (1-12) | `/nbp "idea" --stage 5` |
| `--output DIR` | Specify output directory | `/nbp "idea" --output ./my-outputs` |

## Output Structure

After running the command, you'll find:

```
outputs/
├── 00-orchestrator.json       # Master plan and PR/FAQ
├── stages/
│   ├── 01-problem.json        # Problem validation
│   ├── 02-market.json         # Market analysis
│   ├── 03-solution.json       # Solution definition
│   └── ...                    # Additional stages
├── gates/
│   ├── gate-1-results.json    # Go/no-go decisions
│   └── ...
├── assets/
│   ├── pitch-deck.md          # Investor pitch
│   ├── prd.md                 # Product requirements
│   ├── gtm-plan.md            # Go-to-market strategy
│   └── ...
└── INDEX.md                    # Links to all outputs
```

## Manual Usage (Without Claude Code)

You can also use the prompts directly with any LLM:

### 1. Start with the Orchestrator
Open `prompts/00-master-orchestrator.md` and copy the prompt into ChatGPT, Claude, or any LLM.

### 2. Work Through Stages
Navigate to `prompts/stages/` and run each stage sequentially.

### 3. Use Gate Checks
After each stage, use `prompts/gates/universal-gate-check.md` to evaluate progress.

### 4. Fill Templates
Use the templates in `templates/` for professional outputs.

## Configuration

### Customize Settings

Create `~/.claude/techyon-config.json`:
```json
{
  "default_mode": "full",
  "gate_strictness": "high",
  "auto_save": true,
  "output_format": "markdown",
  "stages": {
    "parallel": false,
    "skip_optional": false
  }
}
```

### Modify Stage Behavior

Edit `claude-code-integration/commands.json` to:
- Change default options
- Add custom stages
- Modify gate criteria
- Update output formats

## Troubleshooting

### Command Not Found
```bash
# Ensure the subagent is linked correctly
ls -la ~/.claude/subagents/
# Should show: techyon-biz-launcher -> /path/to/techyon-prompt-pack
```

### Permission Denied
```bash
# Make scripts executable
chmod +x claude-code-integration/new-biz-pitch.py
chmod +x install-claude-code.sh
```

### Output Directory Issues
```bash
# Ensure write permissions
mkdir -p outputs
chmod 755 outputs
```

## Advanced Usage

### Combine with Other Tools

```bash
# Generate idea, validate, then create GitHub repo
/new-biz-pitch "MyIdea" --quick && \
gh repo create my-idea --public && \
git init && git add . && git commit -m "Initial validation"
```

### Batch Processing

```bash
# Validate multiple ideas
for idea in "Idea1" "Idea2" "Idea3"; do
  /new-biz-pitch "$idea" --quick --output "./validations/$idea"
done
```

### Custom Workflows

Create your own workflow by combining stages:
```bash
# Just problem and market validation
/new-biz-pitch "Idea" --stages 1,2

# Skip to business model
/new-biz-pitch "Idea" --stage 5

# Only generate investor materials
/new-biz-pitch "Idea" --stage 12
```

## Integration with IDEs

### VS Code
Add to `.vscode/tasks.json`:
```json
{
  "label": "Validate Business Idea",
  "type": "shell",
  "command": "/new-biz-pitch",
  "args": ["${input:ideaName}", "--quick"],
  "inputs": [{
    "id": "ideaName",
    "type": "promptString",
    "description": "Enter your business idea"
  }]
}
```

### JetBrains IDEs
Add as External Tool:
- Program: `~/.claude/subagents/techyon-biz-launcher/new-biz-pitch.py`
- Arguments: `$Prompt$ --quick`
- Working directory: `$ProjectFileDir$`

## Updates

### Check for Updates
```bash
cd ~/.claude/subagents/techyon-biz-launcher
git pull origin main
```

### Subscribe to Updates
Watch the repository on GitHub:
https://github.com/james-techyon/techyon-prompt-pack

## Support

### Getting Help
- **Documentation**: Read this guide and README.md
- **Issues**: https://github.com/james-techyon/techyon-prompt-pack/issues
- **Discussions**: Use GitHub Discussions for questions

### Reporting Bugs
When reporting issues, include:
1. Command you ran
2. Error message (if any)
3. Claude Code version
4. Operating system

## Uninstall

### Remove the Subagent
```bash
# Remove symbolic link
rm ~/.claude/subagents/techyon-biz-launcher

# Remove command configuration (optional)
rm ~/.claude/commands.json

# Delete local repository (optional)
rm -rf /path/to/techyon-prompt-pack
```

## License

MIT License - Free for commercial and non-commercial use.

---

**Ready to validate your next big idea?** Type `/new-biz-pitch "Your Idea"` in Claude Code!