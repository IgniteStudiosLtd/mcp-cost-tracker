# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) cost tracker that provides centralized cost tracking for Claude Code sessions across all projects. The system consists of:

- **Core Python modules**: `src/cost_tracker.py` (data management) and `src/mcp_server.py` (MCP protocol implementation)
- **CSV data storage**: Lightweight, portable cost tracking in `data/costs.csv`
- **Interactive web dashboard**: HTML/CSS/JavaScript dashboard in `web/costs.html`
- **Global command shortcuts**: Bash scripts in `commands/` directory for easy CLI access

## Development Commands

### Core Operations
```bash
# Test the cost tracker core functionality
python src/cost_tracker.py

# Test the MCP server (runs test scenarios)
python src/mcp_server.py

# Generate the web dashboard
./commands/generate-dashboard
```

### Global Commands (for end users)
```bash
# Track a new cost session (interactive prompt)
./commands/tc

# View costs dashboard (opens in browser)
./commands/vc

# Quick cost summary (terminal output)
./commands/costs
```

## Architecture

### Data Flow
1. **Cost Entry**: Sessions are tracked via `CostTracker.track_session()` which appends to CSV
2. **MCP Integration**: `MCPCostTrackerServer` exposes tools for Claude Code integration
3. **Dashboard Generation**: `generate-dashboard` script converts CSV to embedded JSON in HTML
4. **Data Access**: CSV serves as single source of truth, with methods to export to JSON

### Key Components

**CostTracker (`src/cost_tracker.py`)**:
- Core data management and CSV operations
- Methods: `track_session()`, `get_summary()`, `get_history()`, `generate_dashboard()`
- Handles CSV initialization, data validation, and dashboard generation

**MCPCostTrackerServer (`src/mcp_server.py`)**:
- Implements MCP protocol for Claude Code integration
- Exposes tools: `track_cost`, `get_cost_summary`, `get_cost_history`, `generate_dashboard`
- Async request handling with proper error management

**Command Scripts (`commands/`)**:
- Self-contained bash scripts with hardcoded paths to this repository
- `tc`: Interactive cost entry with user prompts
- `vc`: Dashboard viewer that auto-generates if needed
- `costs`: One-liner summary for terminal usage
- `generate-dashboard`: Converts CSV to embedded HTML with JavaScript

### Data Schema
CSV format: `Date,Time,Project,Phase,Cost,Duration,Description,Session_ID`

Each session gets a unique `session_ID` based on Unix timestamp.

## MCP Integration

The server runs on port 8080 by default and provides MCP tools for:
- Tracking session costs with structured parameters
- Retrieving cost summaries and filtered history
- Generating updated dashboards

To connect from Claude Code projects, add to `.claude/settings.json`:
```json
{
  "mcpServers": {
    "cost-tracker": {
      "url": "http://localhost:8080/mcp"
    }
  }
}
```

## File Structure Notes

- `data/costs.csv`: Single source of truth for all cost data
- `web/costs.html`: Generated dashboard (do not edit manually)
- Commands have absolute paths to `/Users/kingigilbert/Git-Hub/mcp-cost-tracker`
- All Python modules handle path resolution relative to their location