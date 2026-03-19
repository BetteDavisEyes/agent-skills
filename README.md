# Octoparse Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Claude Code skills for Octoparse web scraping platform. These skills provide workflow-oriented capabilities that orchestrate Octoparse MCP tools for task creation, management, control, and data export.

## Overview

This repository contains **6 workflow skills** for Claude Code that simplify Octoparse operations:

| Skill | Purpose | Key Features |
|-------|---------|--------------|
| **octoparse-mcp-setup** | Configure and authorize Octoparse MCP server | Auto-detect missing MCP, OAuth 2.1 authorization |
| **octoparse-template-task** | Create scraping tasks from templates | Template discovery, parameter validation, error correction |
| **octoparse-task-management** | Find and organize tasks | Progressive discovery, task groups, configuration audit |
| **octoparse-task-control** | Start/stop cloud tasks | Pre-run checks, batch operations, status monitoring |
| **octoparse-data-export** | Export scraped data | Incremental/full export, pagination, volume checks |
| **octoparse-link-template** | Design template chains | Multi-template workflows, data enrichment patterns |

## Quick Start

### Prerequisites

- Claude Code with skill support
- Octoparse account (for authorization)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/octoparse/agent-skills.git
cd agent-skills/skills
```

2. Copy skills to your Claude Code skills directory:
```bash
# Default location (may vary by system)
cp -r octoparse-* ~/.claude/skills/
```

### Usage

Once installed, simply ask Claude to perform Octoparse operations:

- "Create an Amazon product scraper"
- "Show me all my tasks"
- "Start my eBay scraper"
- "Export data from task abc123"

The skills will automatically handle MCP server configuration and authorization on first use.

## Skill Details

### octoparse-mcp-setup

**Purpose**: First-time setup and authorization for Octoparse MCP server.

**Auto-Configuration Flow**:
1. Detect if Octoparse MCP server is configured
2. If missing, automatically add via HTTP streamable transport
3. Initiate OAuth 2.1 authorization with dynamic client registration
4. Verify connection before proceeding

**Manual Trigger**: Use this skill explicitly if authorization expires.

### octoparse-template-task

**Purpose**: Create web scraping tasks using Octoparse's pre-defined templates.

**Workflow**:
1. Template Discovery - Search templates by platform (Amazon, eBay, etc.)
2. Schema Inspection - Get template parameters and requirements
3. Parameter Analysis - Validate input formats (MultiInput, TextInput, etc.)
4. Task Creation - Submit with synchronized UI/Template parameters

**Key Feature**: Automatic error correction for parameter mismatches.

### octoparse-task-management

**Purpose**: Navigate and audit the Octoparse workspace.

**Capabilities**:
- Find tasks by keyword, group, or status
- View detailed task configuration
- Browse task groups/folders
- Progressive discovery for ambiguous queries

**Example**: "Find my Amazon scraper" → searches, finds, reports task ID and status.

### octoparse-task-control

**Purpose**: Orchestrate task execution on Octoparse's cloud infrastructure.

**Features**:
- Pre-run compatibility checks (cloud vs local-only)
- Start/stop individual or batch tasks
- Status monitoring with state change confirmation
- Error handling for credits, rate limits, etc.

**Safety**: Validates `runOn` property before starting; rejects local-only tasks.

### octoparse-data-export

**Purpose**: Retrieve and process scraped data results.

**Modes**:
- **Incremental** (`getAll: false`) - Get only new/unexported records
- **Full Snapshot** (`getAll: true`) - Get all unexported data with pagination

**Best Practice**: Always check data volume before large exports; warn user if >10,000 records.

### octoparse-link-template

**Purpose**: Design template chains for complex data workflows.

**Use Cases**:
- Link listing templates to detail templates
- Enrich data across multiple sources (product + reviews + contact)
- Build multi-step scraping pipelines

**Reference**: Includes linking rules and stable template catalog in `references/`.

## MCP Server Configuration

All skills use the Octoparse MCP server:

```json
{
  "mcpServers": {
    "octoparse": {
      "url": "https://mcp.octoparse.com"
    }
  }
}
```

**Authorization**: OAuth 2.1 with Dynamic Client Registration (handled automatically by `octoparse-mcp-setup`).

## Project Structure

```
agent-skills/
├── skills/
│   ├── octoparse-mcp-setup/          # MCP configuration skill
│   │   └── SKILL.md
│   ├── octoparse-template-task/      # Task creation skill
│   │   └── SKILL.md
│   ├── octoparse-task-management/    # Task discovery skill
│   │   └── SKILL.md
│   ├── octoparse-task-control/       # Task execution skill
│   │   └── SKILL.md
│   ├── octoparse-data-export/        # Data retrieval skill
│   │   └── SKILL.md
│   └── octoparse-link-template/      # Template chaining skill
│       ├── SKILL.md
│       └── references/               # Linking rules and template catalog
│           ├── linking-rules.md
│           ├── output-inference-rules.md
│           └── stable-templates.json
├── LICENSE                           # MIT License
└── README.md                         # This file
```

## Specification

These skills follow the [Agent Skills Specification](https://agentskills.io/specification) format:

- **SKILL.md** - YAML frontmatter + Markdown instructions
- **references/** - Optional supplementary documentation

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please open an issue or PR on GitHub.
