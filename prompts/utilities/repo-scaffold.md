# Repository Scaffold Generator

## Purpose
Quickly create a complete documentation structure for your product development project.

---

## Main Scaffold Prompt

```
Generate a repository structure for {IdeaName} with all necessary documentation:

## Shell Commands Version
Output as executable shell script:

#!/bin/bash
# Create directory structure for {IdeaName}

# Create main directories
mkdir -p docs product gtm ops legal research analytics outputs

# Create documentation files
touch docs/PRD.md
touch docs/GTM.md
touch docs/AnalyticsPlan.md
touch docs/Security.md
touch docs/RiskRegister.md
touch docs/Roadmap.md
touch docs/Architecture.md

# Create product files
touch product/user-stories.csv
touch product/acceptance-criteria.csv
touch product/feature-matrix.md
touch product/success-metrics.md

# Create GTM structure
touch gtm/messaging.md
touch gtm/positioning.md
touch gtm/competitor-analysis.md
touch gtm/content-calendar.csv
mkdir -p gtm/sequences
touch gtm/sequences/welcome.md
touch gtm/sequences/nurture.md
touch gtm/sequences/win-back.md
mkdir -p gtm/sales-materials
touch gtm/sales-materials/pitch-deck.md
touch gtm/sales-materials/one-pager.md
mkdir -p gtm/sales-materials/case-studies

# Create operations files
touch ops/runbook.md
touch ops/sla.md
touch ops/changelog.md
touch ops/incident-response.md
touch ops/monitoring.md

# Create legal files
touch legal/privacy-policy-outline.md
touch legal/terms-outline.md
touch legal/compliance-checklist.md
touch legal/ip-strategy.md

# Create research structure
mkdir -p research/customer-interviews
touch research/market-research.md
touch research/user-personas.md
touch research/jobs-to-be-done.md

# Create analytics files
touch analytics/tracking-plan.md
touch analytics/dashboard-specs.md
touch analytics/experiment-log.md
touch analytics/cohort-definitions.md

# Create README with links
cat > README.md << 'EOF'
# {IdeaName} Documentation

## Quick Links

| Category | Key Documents |
|----------|--------------|
| **Product** | [PRD](docs/PRD.md) \| [User Stories](product/user-stories.csv) \| [Roadmap](docs/Roadmap.md) |
| **Go-to-Market** | [GTM Plan](docs/GTM.md) \| [Messaging](gtm/messaging.md) \| [Positioning](gtm/positioning.md) |
| **Technical** | [Architecture](docs/Architecture.md) \| [Security](docs/Security.md) \| [Analytics](docs/AnalyticsPlan.md) |
| **Operations** | [Runbook](ops/runbook.md) \| [SLAs](ops/sla.md) \| [Monitoring](ops/monitoring.md) |
| **Legal** | [Privacy](legal/privacy-policy-outline.md) \| [Terms](legal/terms-outline.md) \| [Compliance](legal/compliance-checklist.md) |
| **Research** | [Personas](research/user-personas.md) \| [JTBD](research/jobs-to-be-done.md) \| [Market Research](research/market-research.md) |

## Project Status
- Stage: [Current Stage]
- Last Gate: [Result]
- Next Milestone: [Date]

## Team
- Product: [Name]
- Engineering: [Name]
- GTM: [Name]

EOF

echo "Repository structure created successfully!"
```

---

## Python Version

```python
# Repository scaffold generator for {IdeaName}

import os
from pathlib import Path

def create_project_structure(project_name):
    """Create complete project documentation structure"""
    
    # Define directory structure
    structure = {
        'docs': [
            'PRD.md',
            'GTM.md',
            'AnalyticsPlan.md',
            'Security.md',
            'RiskRegister.md',
            'Roadmap.md',
            'Architecture.md'
        ],
        'product': [
            'user-stories.csv',
            'acceptance-criteria.csv',
            'feature-matrix.md',
            'success-metrics.md'
        ],
        'gtm': {
            'files': [
                'messaging.md',
                'positioning.md',
                'competitor-analysis.md',
                'content-calendar.csv'
            ],
            'sequences': [
                'welcome.md',
                'nurture.md',
                'win-back.md'
            ],
            'sales-materials': {
                'files': [
                    'pitch-deck.md',
                    'one-pager.md'
                ],
                'case-studies': []
            }
        },
        'ops': [
            'runbook.md',
            'sla.md',
            'changelog.md',
            'incident-response.md',
            'monitoring.md'
        ],
        'legal': [
            'privacy-policy-outline.md',
            'terms-outline.md',
            'compliance-checklist.md',
            'ip-strategy.md'
        ],
        'research': {
            'files': [
                'market-research.md',
                'user-personas.md',
                'jobs-to-be-done.md'
            ],
            'customer-interviews': []
        },
        'analytics': [
            'tracking-plan.md',
            'dashboard-specs.md',
            'experiment-log.md',
            'cohort-definitions.md'
        ],
        'outputs': []
    }
    
    # Create directories and files
    for directory, contents in structure.items():
        if isinstance(contents, list):
            # Simple directory with files
            Path(directory).mkdir(exist_ok=True)
            for file in contents:
                Path(directory, file).touch()
        elif isinstance(contents, dict):
            # Nested structure
            create_nested_structure(directory, contents)
    
    # Create README
    create_readme(project_name)
    
    print(f"✅ Project structure for {project_name} created successfully!")

def create_nested_structure(base_path, structure):
    """Recursively create nested directory structure"""
    Path(base_path).mkdir(exist_ok=True)
    
    if 'files' in structure:
        for file in structure['files']:
            Path(base_path, file).touch()
    
    for key, value in structure.items():
        if key != 'files':
            sub_path = Path(base_path, key)
            sub_path.mkdir(exist_ok=True)
            if isinstance(value, list):
                for file in value:
                    Path(sub_path, file).touch()
            elif isinstance(value, dict):
                create_nested_structure(sub_path, value)

def create_readme(project_name):
    """Create README with quick links"""
    readme_content = f"""# {project_name} Documentation

## Quick Links

| Category | Key Documents |
|----------|--------------|
| **Product** | [PRD](docs/PRD.md) \| [User Stories](product/user-stories.csv) \| [Roadmap](docs/Roadmap.md) |
| **Go-to-Market** | [GTM Plan](docs/GTM.md) \| [Messaging](gtm/messaging.md) \| [Positioning](gtm/positioning.md) |
| **Technical** | [Architecture](docs/Architecture.md) \| [Security](docs/Security.md) \| [Analytics](docs/AnalyticsPlan.md) |
| **Operations** | [Runbook](ops/runbook.md) \| [SLAs](ops/sla.md) \| [Monitoring](ops/monitoring.md) |
| **Legal** | [Privacy](legal/privacy-policy-outline.md) \| [Terms](legal/terms-outline.md) \| [Compliance](legal/compliance-checklist.md) |
| **Research** | [Personas](research/user-personas.md) \| [JTBD](research/jobs-to-be-done.md) \| [Market Research](research/market-research.md) |

## Project Status
- Stage: [Current Stage]
- Last Gate: [Result]
- Next Milestone: [Date]

## Team
- Product: [Name]
- Engineering: [Name]
- GTM: [Name]
"""
    
    with open('README.md', 'w') as f:
        f.write(readme_content)

# Run the generator
if __name__ == "__main__":
    project_name = input("Enter project name: ")
    create_project_structure(project_name)
```

---

## Node.js Version

```javascript
// Repository scaffold generator for Node.js projects

const fs = require('fs').promises;
const path = require('path');

async function createProjectStructure(projectName) {
  const structure = {
    'docs': [
      'PRD.md',
      'GTM.md',
      'AnalyticsPlan.md',
      'Security.md',
      'RiskRegister.md',
      'Roadmap.md',
      'Architecture.md'
    ],
    'product': [
      'user-stories.csv',
      'acceptance-criteria.csv',
      'feature-matrix.md',
      'success-metrics.md'
    ],
    'gtm': {
      files: ['messaging.md', 'positioning.md', 'competitor-analysis.md', 'content-calendar.csv'],
      'sequences': ['welcome.md', 'nurture.md', 'win-back.md'],
      'sales-materials': {
        files: ['pitch-deck.md', 'one-pager.md'],
        'case-studies': []
      }
    },
    'ops': [
      'runbook.md',
      'sla.md',
      'changelog.md',
      'incident-response.md',
      'monitoring.md'
    ],
    'legal': [
      'privacy-policy-outline.md',
      'terms-outline.md',
      'compliance-checklist.md',
      'ip-strategy.md'
    ],
    'research': {
      files: ['market-research.md', 'user-personas.md', 'jobs-to-be-done.md'],
      'customer-interviews': []
    },
    'analytics': [
      'tracking-plan.md',
      'dashboard-specs.md',
      'experiment-log.md',
      'cohort-definitions.md'
    ],
    'outputs': []
  };

  // Create all directories and files
  for (const [dir, contents] of Object.entries(structure)) {
    await createDirectory(dir, contents);
  }

  // Create README
  await createReadme(projectName);
  
  console.log(`✅ Project structure for ${projectName} created successfully!`);
}

async function createDirectory(dirPath, contents) {
  await fs.mkdir(dirPath, { recursive: true });
  
  if (Array.isArray(contents)) {
    // Simple array of files
    for (const file of contents) {
      await fs.writeFile(path.join(dirPath, file), '');
    }
  } else if (typeof contents === 'object') {
    // Nested structure
    if (contents.files) {
      for (const file of contents.files) {
        await fs.writeFile(path.join(dirPath, file), '');
      }
    }
    
    for (const [subDir, subContents] of Object.entries(contents)) {
      if (subDir !== 'files') {
        await createDirectory(path.join(dirPath, subDir), subContents);
      }
    }
  }
}

async function createReadme(projectName) {
  const readmeContent = `# ${projectName} Documentation

## Quick Links

| Category | Key Documents |
|----------|--------------|
| **Product** | [PRD](docs/PRD.md) \\| [User Stories](product/user-stories.csv) \\| [Roadmap](docs/Roadmap.md) |
| **Go-to-Market** | [GTM Plan](docs/GTM.md) \\| [Messaging](gtm/messaging.md) \\| [Positioning](gtm/positioning.md) |
| **Technical** | [Architecture](docs/Architecture.md) \\| [Security](docs/Security.md) \\| [Analytics](docs/AnalyticsPlan.md) |
| **Operations** | [Runbook](ops/runbook.md) \\| [SLAs](ops/sla.md) \\| [Monitoring](ops/monitoring.md) |
| **Legal** | [Privacy](legal/privacy-policy-outline.md) \\| [Terms](legal/terms-outline.md) \\| [Compliance](legal/compliance-checklist.md) |
| **Research** | [Personas](research/user-personas.md) \\| [JTBD](research/jobs-to-be-done.md) \\| [Market Research](research/market-research.md) |

## Project Status
- Stage: [Current Stage]
- Last Gate: [Result]
- Next Milestone: [Date]

## Team
- Product: [Name]
- Engineering: [Name]
- GTM: [Name]
`;

  await fs.writeFile('README.md', readmeContent);
}

// Run if called directly
if (require.main === module) {
  const projectName = process.argv[2] || 'MyProject';
  createProjectStructure(projectName).catch(console.error);
}

module.exports = { createProjectStructure };
```

---

## Usage Instructions

### Option 1: Shell Script
```bash
# Save as create-structure.sh
chmod +x create-structure.sh
./create-structure.sh
```

### Option 2: Python
```bash
python repo_scaffold.py
# Enter project name when prompted
```

### Option 3: Node.js
```bash
node repo_scaffold.js "YourProjectName"
# Or add to package.json scripts
```

### Option 4: Manual
Copy the shell commands and run them directly in your terminal.

## Customization

Add or remove directories/files based on your needs:
- **For Hardware Products**: Add `/hardware` with BOM, CAD, testing docs
- **For ML Products**: Add `/models` with training, evaluation, deployment docs
- **For Mobile Apps**: Add `/mobile` with iOS, Android, release notes
- **For APIs**: Add `/api` with OpenAPI specs, SDK docs, integration guides

## Best Practices

1. **Keep Updated**: Update files as you progress through stages
2. **Version Control**: Commit after each major update
3. **Link Everything**: Use relative links between documents
4. **Stay Organized**: One concept per file
5. **Use Templates**: Start files with templates from this pack