# MCP Cost Tracker

A standalone MCP (Model Context Protocol) server for tracking Claude Code usage costs across all projects.

## Overview

This tool provides centralized cost tracking for Claude Code sessions with:
- **CSV database** for lightweight, portable storage
- **Interactive HTML dashboard** for data visualization
- **MCP server** for integration with Claude Code
- **Global command shortcuts** for easy access

## Features

- 📊 **Cost Tracking**: Log session costs, duration, phase, and descriptions
- 🌐 **Web Dashboard**: Interactive browser-based cost analysis
- 📈 **Analytics**: Total costs, averages, trends over time
- 🔍 **Search & Filter**: Find sessions by project, phase, or keywords
- 💾 **Portable Data**: Single CSV file with all cost history
- 🔗 **MCP Integration**: Use from any Claude Code project

## Quick Start

### 1. Setup
```bash
# Install dependencies (if any)
cd mcp-cost-tracker
npm install  # or pip install if Python dependencies exist
```

### 2. Usage
```bash
# Track a new session
/tc    # Interactive prompt for cost details

# View dashboard
/vc    # Opens web dashboard in browser

# Quick summary
/costs # Terminal one-liner: Last task | Project total | Global total
```

### 3. MCP Integration
```bash
# Start MCP server
python mcp_server.py

# Connect from Claude Code projects
# Add to .claude/settings.json:
{
  "mcpServers": {
    "cost-tracker": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

## File Structure

- `data/` - Cost tracking data storage
- `web/` - HTML dashboard and assets  
- `commands/` - Global command shortcuts
- `mcp_server.py` - MCP server implementation
- `cost_tracker.py` - Core cost tracking logic

## Data Storage

All cost data is stored in `data/costs.csv` with the following schema:

```csv
Date,Time,Project,Phase,Cost,Duration,Description,Session_ID
2025-06-12,21:30:00,MyProject,Development,2.83,45m,Added new feature,session_001
```

## Dashboard Features

- **Summary Cards**: Total cost, session count, averages
- **Interactive Table**: Sortable, searchable session history
- **Phase Filtering**: Group by development phase
- **Export Options**: Download data in various formats

## Global Commands

- `/tc` - Track costs (prompts for session details)
- `/vc` - View costs (opens dashboard)
- `/costs` - Quick cost summary

## Integration with Claude Code

This tool is designed to work seamlessly with Claude Code through MCP. It can:

1. **Automatically capture** Claude Code session costs
2. **Store centrally** across all your projects
3. **Provide insights** into development costs and patterns
4. **Export data** for accounting and budgeting

## Development

The tool is built with:
- **Python** for MCP server and core logic
- **HTML/CSS/JavaScript** for dashboard
- **CSV** for data storage
- **Bash scripts** for command shortcuts

## License

MIT License - Feel free to use and modify for your needs.