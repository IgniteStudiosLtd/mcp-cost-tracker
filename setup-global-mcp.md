# Setup Global MCP Cost Tracker

## Option 1: Global Configuration (Recommended)

Add this to your global Claude Code settings at `~/.config/claude/settings.json`:

```json
{
  "mcpServers": {
    "cost-tracker": {
      "command": "/Users/kingigilbert/Git-Hub/mcp-cost-tracker/mcp-cost-server",
      "args": []
    }
  }
}
```

## Option 2: Per-Project Configuration

For each project where you want cost tracking, add to `.claude/settings.json`:

```json
{
  "mcpServers": {
    "cost-tracker": {
      "command": "/Users/kingigilbert/Git-Hub/mcp-cost-tracker/mcp-cost-server",
      "args": []
    }
  }
}
```

## Available MCP Tools

Once configured, you'll have access to these tools in any Claude Code session:

- **`track_cost`**: Track session costs with parameters:
  - `cost` (required): Session cost in USD
  - `duration`: Session duration (e.g., "45m 30s")
  - `phase`: Development phase
  - `description`: Brief description of work
  - `project`: Project name

- **`get_cost_summary`**: Get total cost statistics

- **`get_cost_history`**: Get filtered cost history
  - `project`: Filter by project
  - `phase`: Filter by phase
  - `limit`: Limit results

- **`generate_dashboard`**: Generate updated HTML dashboard

## Usage Example

In any Claude Code session, you can now:

```
Use the track_cost tool to log this session with cost 2.50, duration "30m", phase "Development", description "Added new feature", project "MyProject"
```

## Benefits

- ✅ **Global Access**: Works from any project directory
- ✅ **Centralized Data**: All costs stored in single location
- ✅ **Automatic Tracking**: No need to manually run commands
- ✅ **Cross-Project Analytics**: Track costs across all your projects
- ✅ **Real-time Updates**: Dashboard updates automatically

## Testing the Setup

1. Start Claude Code in any project
2. Ask Claude to use the `get_cost_summary` tool
3. Use `track_cost` to log a session
4. Use `generate_dashboard` to update the web dashboard