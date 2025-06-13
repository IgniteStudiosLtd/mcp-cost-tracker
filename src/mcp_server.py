#!/usr/bin/env python3
"""
MCP Cost Tracker Server
A Model Context Protocol server for tracking Claude Code usage costs.
"""

import asyncio
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add the src directory to the path for imports
sys.path.insert(0, str(Path(__file__).parent))

from cost_tracker import CostTracker

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MCPCostTrackerServer:
    """MCP server for cost tracking functionality."""
    
    def __init__(self, data_dir: str = None):
        """Initialize the MCP server."""
        if data_dir is None:
            # Default to the data directory relative to this file
            base_dir = Path(__file__).parent.parent
            data_dir = base_dir / "data"
        
        self.cost_tracker = CostTracker(data_dir)
        self.tools = {
            "track_cost": self._track_cost,
            "get_cost_summary": self._get_cost_summary,
            "get_cost_history": self._get_cost_history,
            "generate_dashboard": self._generate_dashboard,
        }
    
    async def _track_cost(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Track a new cost entry."""
        try:
            # Extract parameters
            cost = float(params.get("cost", 0))
            duration = params.get("duration", "")
            phase = params.get("phase", "General")
            description = params.get("description", "")
            project = params.get("project", "General")
            
            # Track the cost
            session_id = self.cost_tracker.track_session(
                cost=cost,
                duration=duration,
                phase=phase,
                description=description,
                project=project
            )
            
            return {
                "success": True,
                "session_id": session_id,
                "message": f"Cost ${cost:.2f} tracked successfully"
            }
        
        except Exception as e:
            logger.error(f"Error tracking cost: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _get_cost_summary(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get cost summary statistics."""
        try:
            summary = self.cost_tracker.get_summary()
            return {
                "success": True,
                "summary": summary
            }
        
        except Exception as e:
            logger.error(f"Error getting cost summary: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _get_cost_history(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Get cost history with optional filtering."""
        try:
            project = params.get("project")
            phase = params.get("phase")
            limit = params.get("limit", 100)
            
            history = self.cost_tracker.get_history(
                project=project,
                phase=phase,
                limit=limit
            )
            
            return {
                "success": True,
                "history": history
            }
        
        except Exception as e:
            logger.error(f"Error getting cost history: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def _generate_dashboard(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate HTML dashboard."""
        try:
            dashboard_path = self.cost_tracker.generate_dashboard()
            return {
                "success": True,
                "dashboard_path": str(dashboard_path),
                "message": "Dashboard generated successfully"
            }
        
        except Exception as e:
            logger.error(f"Error generating dashboard: {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP requests."""
        try:
            method = request.get("method")
            params = request.get("params", {})
            
            if method == "initialize":
                return {
                    "capabilities": {
                        "tools": {
                            "track_cost": {
                                "description": "Track a new Claude Code session cost",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "cost": {"type": "number", "description": "Session cost in USD"},
                                        "duration": {"type": "string", "description": "Session duration (e.g., '45m 30s')"},
                                        "phase": {"type": "string", "description": "Development phase"},
                                        "description": {"type": "string", "description": "Brief description of work done"},
                                        "project": {"type": "string", "description": "Project name"}
                                    },
                                    "required": ["cost"]
                                }
                            },
                            "get_cost_summary": {
                                "description": "Get cost summary statistics",
                                "inputSchema": {"type": "object", "properties": {}}
                            },
                            "get_cost_history": {
                                "description": "Get cost history with optional filtering",
                                "inputSchema": {
                                    "type": "object",
                                    "properties": {
                                        "project": {"type": "string", "description": "Filter by project"},
                                        "phase": {"type": "string", "description": "Filter by phase"},
                                        "limit": {"type": "integer", "description": "Limit number of results"}
                                    }
                                }
                            },
                            "generate_dashboard": {
                                "description": "Generate HTML cost dashboard",
                                "inputSchema": {"type": "object", "properties": {}}
                            }
                        }
                    }
                }
            
            elif method == "tools/call":
                tool_name = params.get("name")
                tool_params = params.get("arguments", {})
                
                if tool_name in self.tools:
                    result = await self.tools[tool_name](tool_params)
                    return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}
                else:
                    return {"error": f"Unknown tool: {tool_name}"}
            
            else:
                return {"error": f"Unknown method: {method}"}
        
        except Exception as e:
            logger.error(f"Error handling request: {e}")
            return {"error": str(e)}

def main():
    """Main entry point for the MCP server."""
    import argparse
    
    parser = argparse.ArgumentParser(description="MCP Cost Tracker Server")
    parser.add_argument(
        "--data-dir",
        type=str,
        help="Directory for cost tracking data"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8080,
        help="Port to run the server on"
    )
    
    args = parser.parse_args()
    
    # Create server instance
    server = MCPCostTrackerServer(data_dir=args.data_dir)
    
    logger.info(f"Starting MCP Cost Tracker server on port {args.port}")
    logger.info(f"Data directory: {server.cost_tracker.data_dir}")
    
    # For now, just run a simple test
    async def test_server():
        # Test tracking a cost
        test_request = {
            "method": "tools/call",
            "params": {
                "name": "track_cost",
                "arguments": {
                    "cost": 2.50,
                    "duration": "30m",
                    "phase": "Testing",
                    "description": "MCP server test",
                    "project": "MCP-Cost-Tracker"
                }
            }
        }
        
        result = await server.handle_request(test_request)
        print("Test result:", json.dumps(result, indent=2))
        
        # Test getting summary
        summary_request = {
            "method": "tools/call",
            "params": {
                "name": "get_cost_summary",
                "arguments": {}
            }
        }
        
        result = await server.handle_request(summary_request)
        print("Summary result:", json.dumps(result, indent=2))
    
    # Run the test
    asyncio.run(test_server())

if __name__ == "__main__":
    main()