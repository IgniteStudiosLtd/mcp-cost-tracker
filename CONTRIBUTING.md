# Contributing to MCP Cost Tracker

Thank you for your interest in contributing to MCP Cost Tracker! This document provides guidelines and information for contributors.

## 🚀 Quick Start for Contributors

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
3. **Create** a feature branch: `git checkout -b feature-name`
4. **Make** your changes
5. **Test** your changes thoroughly
6. **Commit** with clear messages
7. **Push** to your fork
8. **Submit** a Pull Request

## 🛠 Development Setup

### Prerequisites
- Python 3.7+
- Claude Code (for testing MCP integration)
- Git

### Local Development
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/mcp-cost-tracker.git
cd mcp-cost-tracker

# Make scripts executable
chmod +x commands/*
chmod +x mcp-cost-server

# Test local functionality
./commands/costs
./commands/generate-dashboard
```

### Testing MCP Integration
```bash
# Test MCP server
python src/mcp_server.py

# Test core functionality
python src/cost_tracker.py
```

## 🎯 Types of Contributions

### 🐛 Bug Reports
- Use GitHub Issues with the "bug" label
- Include steps to reproduce
- Provide error messages and logs
- Specify your environment (OS, Python version, Claude Code version)

### ✨ Feature Requests
- Use GitHub Discussions for feature ideas
- Explain the use case and benefit
- Consider backward compatibility

### 📝 Code Contributions
- **Dashboard Improvements**: Enhance the web interface
- **MCP Tools**: Add new MCP server capabilities  
- **Data Export**: Add new export formats
- **Performance**: Optimize CSV handling or dashboard generation
- **Documentation**: Improve setup guides and examples

## 📋 Code Guidelines

### Python Code
- Follow PEP 8 style guidelines
- Use type hints where applicable
- Add docstrings for public functions
- Handle errors gracefully with try/catch blocks

### JavaScript (Dashboard)
- Use modern ES6+ features
- Keep functions focused and readable
- Comment complex logic
- Maintain responsive design

### Bash Scripts
- Use proper error handling
- Quote variables to prevent word splitting
- Add comments for complex operations
- Test on multiple platforms if possible

## 🧪 Testing Guidelines

### Before Submitting
1. **Test Local Commands**:
   ```bash
   ./commands/tc    # Test cost tracking
   ./commands/vc    # Test dashboard generation
   ./commands/costs # Test summary display
   ```

2. **Test MCP Integration**:
   - Start MCP server: `python src/mcp_server.py`
   - Test from Claude Code session
   - Verify all MCP tools work correctly

3. **Test Dashboard**:
   - Generate dashboard with test data
   - Verify sorting, filtering, and search
   - Test project total calculations
   - Check responsive design

### Test Data
Create test scenarios with:
- Multiple projects
- Different phases (Development, Testing, etc.)
- Various cost amounts and durations
- Edge cases (empty data, special characters)

## 📝 Commit Guidelines

### Commit Message Format
```
type(scope): brief description

Detailed explanation if needed

- List specific changes
- Reference issues: Fixes #123
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style/formatting
- `refactor`: Code restructuring
- `test`: Test additions/modifications
- `chore`: Build process or auxiliary tool changes

### Examples
```
feat(dashboard): add project cost filtering

- Add project total card that appears when filtering
- Update JavaScript to calculate project-specific costs
- Enhance CSS for better card layout

Fixes #45
```

## 🔍 Code Review Process

1. **Automated Checks**: Ensure all tests pass
2. **Manual Review**: Core maintainers review code quality
3. **Functionality Test**: Verify the feature works as described
4. **Documentation**: Check if documentation needs updates

## 📚 Documentation

### Required Documentation Updates
- Update README.md for new features
- Add examples for new MCP tools
- Update CLAUDE.md for development guidance
- Include setup instructions for new dependencies

### Style Guide
- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Keep installation steps up-to-date

## 🎉 Recognition

Contributors will be:
- Listed in the repository contributors
- Mentioned in release notes for significant contributions
- Invited to help with project direction and decisions

## ❓ Questions?

- **General Questions**: Use GitHub Discussions
- **Bug Reports**: Use GitHub Issues
- **Security Issues**: Email privately to maintainers

## 📄 License

By contributing to MCP Cost Tracker, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make MCP Cost Tracker better for the Claude Code community! 🚀