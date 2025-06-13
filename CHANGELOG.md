# Changelog

All notable changes to MCP Cost Tracker will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-12

### Added
- **Initial release** of MCP Cost Tracker
- **Session tracking** with sequential numbering (1, 2, 3...)
- **Interactive HTML dashboard** with sorting, filtering, and search
- **Project cost totals** when filtering by project
- **Global MCP server** for cross-project cost tracking
- **Command-line tools** (`/tc`, `/vc`, `/costs`) for quick access
- **CSV data storage** for lightweight, portable cost history
- **Professional packaging** with MIT license and comprehensive documentation

### Features
- **Core Functionality**:
  - Track session costs with duration, phase, and descriptions
  - Store data in CSV format with session numbers
  - Generate interactive web dashboard
  - Global MCP integration for any Claude Code session

- **Dashboard Features**:
  - Summary cards showing total cost, session count, averages
  - Sortable table with session numbers and cost data
  - Project and phase filtering with search capability
  - Dynamic project total calculation when filtering
  - Responsive design with modern UI

- **MCP Integration**:
  - `track_cost` tool for logging session costs
  - `get_cost_summary` tool for statistics
  - `get_cost_history` tool for filtered data retrieval
  - `generate_dashboard` tool for dashboard updates

- **Developer Experience**:
  - Simple installation with executable scripts
  - Clear documentation and setup instructions
  - Cross-platform compatibility (macOS, Linux, Windows)
  - Centralized configuration for all projects

### Technical Details
- **Languages**: Python 3.7+, HTML/CSS/JavaScript, Bash
- **Data Format**: CSV with structured schema
- **Architecture**: MCP server + local command tools + web dashboard
- **Dependencies**: Python standard library only

### Documentation
- Comprehensive README with installation guide
- MCP setup instructions for global configuration
- Contributing guidelines for community development
- GitHub issue templates for bug reports and feature requests
- Professional licensing under MIT License

---

## Development Notes

This changelog will be updated with each release. For upcoming features and planned improvements, see:
- [GitHub Issues](https://github.com/YOUR_USERNAME/mcp-cost-tracker/issues) for bug reports
- [GitHub Discussions](https://github.com/YOUR_USERNAME/mcp-cost-tracker/discussions) for feature ideas
- [ROADMAP.md](ROADMAP.md) for long-term development plans