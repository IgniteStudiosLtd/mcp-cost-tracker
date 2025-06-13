#!/bin/bash
# MCP Cost Tracker Installation Script
# This script sets up permissions and provides installation guidance

set -e

echo "🚀 Setting up MCP Cost Tracker..."

# Make scripts executable
echo "📝 Setting script permissions..."
chmod +x commands/*
chmod +x mcp-cost-server

# Check if Python is available
echo "🐍 Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found. Please install Python 3.7+ first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Found Python $PYTHON_VERSION"

# Test core functionality
echo "🧪 Testing core functionality..."
if python3 src/cost_tracker.py > /dev/null 2>&1; then
    echo "✅ Core cost tracking works"
else
    echo "❌ Core functionality test failed"
    exit 1
fi

# Get the absolute path for MCP configuration
INSTALL_PATH=$(pwd)
echo ""
echo "📋 Installation Complete!"
echo ""
echo "Next steps:"
echo "1. Add this to your global Claude Code settings (~/.config/claude/settings.json):"
echo ""
echo '{
  "mcpServers": {
    "cost-tracker": {
      "command": "'$INSTALL_PATH'/mcp-cost-server",
      "args": []
    }
  }
}'
echo ""
echo "2. Test local commands:"
echo "   ./commands/costs    # Quick summary"
echo "   ./commands/tc       # Track new session"
echo "   ./commands/vc       # View dashboard"
echo ""
echo "3. Test MCP integration in any Claude Code session:"
echo "   Ask Claude to 'use the get_cost_summary tool'"
echo ""
echo "📖 For detailed setup instructions, see README.md"
echo "🐛 For issues, visit: https://github.com/YOUR_USERNAME/mcp-cost-tracker/issues"
echo ""
echo "Happy cost tracking! 💰"