# Cost Tracking Quick Guide

## 📊 Check Current Costs
```bash
/costs
```
**Shows:** `Last task: $X.XX | Project total: $X.XX | Global total: $X.XX`

- **Last task**: Cost of most recent Claude Code session
- **Project total**: Total spent on this project (Recall)  
- **Global total**: Total spent across all projects

## 💰 Log Session Costs
```bash
/track-costs
```
**Prompts for:**
1. Session cost (e.g., `0.77`)
2. Duration (e.g., `45m 30s`)
3. Phase (e.g., `Development`, `Planning`, `Testing`)
4. Task description (e.g., `Added cost tracking system`)

**Updates:**
- `claude-costs.md` (this project)
- `~/.claude/global-costs.md` (all projects)

## 🔄 Typical Workflow
1. **Before starting work:** `/costs` (check current totals)
2. **Do your Claude Code work**
3. **After session ends:** Run `cost` command to see session cost
4. **Log the session:** `/track-costs` (enter the details)
5. **Quick check:** `/costs` (verify updated totals)

## 📁 Files Created
- **Project costs:** `claude-costs.md` (in project root)
- **Global costs:** `~/.claude/global-costs.md` (home directory)

## 💡 Tips
- Log costs immediately after each session while details are fresh
- Use consistent phase names (`Planning`, `Development`, `Testing`, `Debugging`)
- The global file tracks all your Claude Code usage across projects
- Both commands work from any directory