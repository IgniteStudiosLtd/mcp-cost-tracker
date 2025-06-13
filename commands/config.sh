#!/bin/bash
# Shared configuration for MCP Cost Tracker commands
# This file is sourced by all command scripts

# Determine the project root directory relative to this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export MCP_COST_TRACKER_HOME="$(dirname "$SCRIPT_DIR")"

# Define all paths relative to the project root
export CSV_FILE="$MCP_COST_TRACKER_HOME/data/costs.csv"
export WEB_DIR="$MCP_COST_TRACKER_HOME/web"
export HTML_FILE="$MCP_COST_TRACKER_HOME/web/costs.html"
export SRC_DIR="$MCP_COST_TRACKER_HOME/src"