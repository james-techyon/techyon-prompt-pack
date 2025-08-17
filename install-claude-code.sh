#!/bin/bash

# Techyon Prompt Pack - Claude Code Installation Script
# Automatically configures the prompt pack as a Claude Code subagent

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Installation paths
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CLAUDE_DIR="$HOME/.claude"
SUBAGENTS_DIR="$CLAUDE_DIR/subagents"
COMMANDS_FILE="$CLAUDE_DIR/commands.json"

echo "================================================"
echo "Techyon Prompt Pack - Claude Code Installer"
echo "================================================"
echo ""

# Check if running from the repo directory
if [ ! -f "$SCRIPT_DIR/subagent-definition.md" ]; then
    echo -e "${RED}Error: Please run this script from the techyon-prompt-pack directory${NC}"
    exit 1
fi

# Create Claude directories if they don't exist
echo "1. Setting up Claude Code directories..."
mkdir -p "$SUBAGENTS_DIR"
echo -e "${GREEN}✓${NC} Directories created"

# Create symbolic link for subagent
echo ""
echo "2. Installing subagent..."
SUBAGENT_LINK="$SUBAGENTS_DIR/techyon-biz-launcher"

if [ -L "$SUBAGENT_LINK" ]; then
    echo -e "${YELLOW}⚠${NC} Subagent link already exists. Updating..."
    rm "$SUBAGENT_LINK"
fi

ln -s "$SCRIPT_DIR" "$SUBAGENT_LINK"
echo -e "${GREEN}✓${NC} Subagent installed at: $SUBAGENT_LINK"

# Install command configuration
echo ""
echo "3. Installing slash command..."

if [ -f "$COMMANDS_FILE" ]; then
    echo -e "${YELLOW}⚠${NC} Commands file exists. Creating backup..."
    cp "$COMMANDS_FILE" "${COMMANDS_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
fi

# Copy commands configuration
cp "$SCRIPT_DIR/claude-code-integration/commands.json" "$COMMANDS_FILE"
echo -e "${GREEN}✓${NC} Slash command '/new-biz-pitch' configured"

# Make Python script executable
echo ""
echo "4. Setting permissions..."
chmod +x "$SCRIPT_DIR/claude-code-integration/new-biz-pitch.py"
echo -e "${GREEN}✓${NC} Scripts made executable"

# Create outputs directory
echo ""
echo "5. Creating output directory..."
mkdir -p "$SCRIPT_DIR/outputs"
echo -e "${GREEN}✓${NC} Output directory ready"

# Verify installation
echo ""
echo "6. Verifying installation..."

# Check if subagent is accessible
if [ -L "$SUBAGENT_LINK" ] && [ -e "$SUBAGENT_LINK" ]; then
    echo -e "${GREEN}✓${NC} Subagent link is valid"
else
    echo -e "${RED}✗${NC} Subagent link failed"
    exit 1
fi

# Check if commands file exists
if [ -f "$COMMANDS_FILE" ]; then
    echo -e "${GREEN}✓${NC} Commands file installed"
else
    echo -e "${RED}✗${NC} Commands file missing"
    exit 1
fi

# Check if Python script is executable
if [ -x "$SCRIPT_DIR/claude-code-integration/new-biz-pitch.py" ]; then
    echo -e "${GREEN}✓${NC} Python script is executable"
else
    echo -e "${RED}✗${NC} Python script not executable"
    exit 1
fi

# Success message
echo ""
echo "================================================"
echo -e "${GREEN}Installation Complete!${NC}"
echo "================================================"
echo ""
echo "You can now use the following commands in Claude Code:"
echo ""
echo "  /new-biz-pitch \"Your Idea\" --quick"
echo "  /nbp \"Your Idea\" --full --b2b"
echo "  /pitch \"Your Idea\" --investor"
echo "  /validate \"Your Idea\" --saas"
echo ""
echo "Available aliases: /nbp, /pitch, /validate, /idea"
echo ""
echo "For help and options, use:"
echo "  /new-biz-pitch --help"
echo ""
echo "Documentation:"
echo "  - Quick Start: $SCRIPT_DIR/README.md"
echo "  - Installation: $SCRIPT_DIR/INSTALL.md"
echo "  - Templates: $SCRIPT_DIR/templates/"
echo ""
echo "Repository: https://github.com/james-techyon/techyon-prompt-pack"
echo ""
echo -e "${GREEN}Happy validating! 🚀${NC}"

# Optional: Test the command
echo ""
read -p "Would you like to test the installation? (y/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "Running test validation..."
    python3 "$SCRIPT_DIR/claude-code-integration/new-biz-pitch.py" "Test Idea" --quick --output "$SCRIPT_DIR/outputs/test"
    echo ""
    echo -e "${GREEN}✓${NC} Test completed. Check $SCRIPT_DIR/outputs/test/ for results."
fi

echo ""
echo "Installation log saved to: $SCRIPT_DIR/install.log"
echo "$(date): Installation completed successfully" >> "$SCRIPT_DIR/install.log"