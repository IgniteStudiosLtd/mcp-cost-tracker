#!/usr/bin/env python3
"""
Cost Tracker Core Module
Handles cost tracking functionality for Claude Code sessions.
"""

import csv
import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any

class CostTracker:
    """Core cost tracking functionality."""
    
    def __init__(self, data_dir: str = None):
        """Initialize the cost tracker."""
        if data_dir is None:
            # Default to the data directory relative to this file
            base_dir = Path(__file__).parent.parent
            data_dir = base_dir / "data"
        
        self.data_dir = Path(data_dir)
        self.csv_file = self.data_dir / "costs.csv"
        self.web_dir = Path(__file__).parent.parent / "web"
        
        # Ensure directories exist
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.web_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize CSV file if it doesn't exist
        self._init_csv_file()
    
    def _init_csv_file(self):
        """Initialize the CSV file with headers if it doesn't exist."""
        if not self.csv_file.exists():
            with open(self.csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([
                    'Date', 'Time', 'Project', 'Phase', 'Cost', 
                    'Duration', 'Description', 'Session_ID'
                ])
    
    def track_session(
        self, 
        cost: float, 
        duration: str = "", 
        phase: str = "General", 
        description: str = "", 
        project: str = "General"
    ) -> str:
        """
        Track a new cost session.
        
        Args:
            cost: Session cost in USD
            duration: Session duration (e.g., "45m 30s")
            phase: Development phase (e.g., "Development", "Testing")
            description: Brief description of work done
            project: Project name
        
        Returns:
            session_id: Unique session identifier
        """
        # Generate session ID
        timestamp = datetime.now()
        session_id = f"session_{int(timestamp.timestamp())}"
        
        # Format date and time
        date_str = timestamp.strftime("%Y-%m-%d")
        time_str = timestamp.strftime("%H:%M:%S")
        
        # Append to CSV file
        with open(self.csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                date_str, time_str, project, phase, cost,
                duration, description, session_id
            ])
        
        return session_id
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get cost summary statistics.
        
        Returns:
            Dictionary with summary statistics
        """
        if not self.csv_file.exists():
            return {
                "total_cost": 0.0,
                "session_count": 0,
                "average_cost": 0.0,
                "last_cost": 0.0
            }
        
        sessions = self._read_sessions()
        
        if not sessions:
            return {
                "total_cost": 0.0,
                "session_count": 0,
                "average_cost": 0.0,
                "last_cost": 0.0
            }
        
        costs = [float(session['Cost']) for session in sessions]
        total_cost = sum(costs)
        session_count = len(sessions)
        average_cost = total_cost / session_count if session_count > 0 else 0.0
        last_cost = costs[-1] if costs else 0.0
        
        return {
            "total_cost": round(total_cost, 2),
            "session_count": session_count,
            "average_cost": round(average_cost, 2),
            "last_cost": round(last_cost, 2)
        }
    
    def get_history(
        self, 
        project: Optional[str] = None, 
        phase: Optional[str] = None, 
        limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Get cost history with optional filtering.
        
        Args:
            project: Filter by project name
            phase: Filter by phase
            limit: Limit number of results
        
        Returns:
            List of session dictionaries
        """
        sessions = self._read_sessions()
        
        # Apply filters
        if project:
            sessions = [s for s in sessions if s['Project'] == project]
        
        if phase:
            sessions = [s for s in sessions if s['Phase'] == phase]
        
        # Apply limit
        if limit:
            sessions = sessions[-limit:]
        
        return sessions
    
    def _read_sessions(self) -> List[Dict[str, str]]:
        """Read all sessions from the CSV file."""
        if not self.csv_file.exists():
            return []
        
        sessions = []
        with open(self.csv_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            sessions = list(reader)
        
        return sessions
    
    def generate_dashboard(self) -> Path:
        """
        Generate HTML dashboard.
        
        Returns:
            Path to the generated HTML file
        """
        # Use the existing generate-dashboard script
        commands_dir = Path(__file__).parent.parent / "commands"
        script_path = commands_dir / "generate-dashboard"
        
        if script_path.exists():
            try:
                # Run the dashboard generation script
                result = subprocess.run(
                    [str(script_path)],
                    capture_output=True,
                    text=True,
                    check=True
                )
                print(f"Dashboard generation output: {result.stdout}")
                if result.stderr:
                    print(f"Dashboard generation warnings: {result.stderr}")
            except subprocess.CalledProcessError as e:
                print(f"Error generating dashboard: {e}")
                print(f"Script output: {e.stdout}")
                print(f"Script errors: {e.stderr}")
        
        return self.web_dir / "costs.html"
    
    def get_projects(self) -> List[str]:
        """Get list of unique projects."""
        sessions = self._read_sessions()
        projects = list(set(session['Project'] for session in sessions))
        return sorted(projects)
    
    def get_phases(self) -> List[str]:
        """Get list of unique phases."""
        sessions = self._read_sessions()
        phases = list(set(session['Phase'] for session in sessions))
        return sorted(phases)
    
    def export_data(self, format: str = "csv") -> Path:
        """
        Export cost data in specified format.
        
        Args:
            format: Export format ("csv", "json")
        
        Returns:
            Path to the exported file
        """
        if format == "csv":
            return self.csv_file
        
        elif format == "json":
            import json
            sessions = self._read_sessions()
            json_file = self.data_dir / "costs.json"
            
            with open(json_file, 'w') as f:
                json.dump(sessions, f, indent=2)
            
            return json_file
        
        else:
            raise ValueError(f"Unsupported export format: {format}")

def main():
    """Test the cost tracker functionality."""
    tracker = CostTracker()
    
    # Test tracking a session
    session_id = tracker.track_session(
        cost=2.75,
        duration="45m",
        phase="Development", 
        description="Test cost tracking functionality",
        project="MCP-Cost-Tracker"
    )
    print(f"Tracked session: {session_id}")
    
    # Test getting summary
    summary = tracker.get_summary()
    print(f"Cost summary: {summary}")
    
    # Test getting history
    history = tracker.get_history(limit=5)
    print(f"Recent sessions: {len(history)}")
    
    # Test generating dashboard
    dashboard_path = tracker.generate_dashboard()
    print(f"Dashboard generated: {dashboard_path}")

if __name__ == "__main__":
    main()