# agent-skills

**Automatically convert MCP (Model Context Protocol) tools into AI Skills** that can be discovered and used by AI Agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## Specification Compliance

This project aligns with the [Agent Skills Specification (agentskills.io)](https://agentskills.io/specification), the open format maintained by Anthropic and adopted by Claude, Cursor, Apify, and others.

Each skill includes:
- **SKILL.md** — agentskills.io compliant (YAML frontmatter + Markdown instructions)
- **skill.json** — Tool schema for programmatic use (OpenAI/Anthropic function calling)
- **example.json** — Sample input

See [docs/SPEC_COMPARISON.md](docs/SPEC_COMPARISON.md) for spec comparison, [docs/MULTI_REGION.md](docs/MULTI_REGION.md) for multi-region config, [docs/PROJECT_EVALUATION.md](docs/PROJECT_EVALUATION.md) for project assessment.

## What are Skills?

**Skills** are standardized, discoverable capability definitions that AI Agents can use to extend their functionality. Each skill describes:

- **What** it does (name, description)
- **How** to call it (parameters with JSON Schema)
- **Where** to invoke it (HTTP/MCP endpoint)

Skills bridge the gap between MCP tools (which use JSON-RPC over HTTP) and agent frameworks (OpenAI, Anthropic, LangChain, etc.) that need tool schemas for function calling.

## How MCP Tools Convert to Skills

MCP servers expose tools via the `tools/list` JSON-RPC method (POST to the MCP server URL). Each tool has:

- `name` → Skill name
- `description` → Skill description  
- `inputSchema` → Skill parameters (JSON Schema)

The generator fetches this list, maps each tool to the skill schema format, and writes:

```
skills/
  {tool_name}/
    skill.json    # Full schema (name, description, parameters, invoke)
    README.md     # Human-readable docs
    example.json  # Example input
```

## Project Structure

```
agent-skills/
├── skills/              # Generated skill definitions
│   ├── crawl_page/      # Web crawling (from mcp_to_skills)
│   ├── octoparse_*/     # Octoparse MCP tools (16 skills)
│   └── ...
├── generator/            # MCP → Skills converters
│   ├── mcp_to_skills.py   # From JSON-RPC (live MCP server)
│   ├── mcps_to_skills.py  # From local mcps JSON files
│   └── validate_skills.py # Validate against agentskills.io spec
├── docs/
│   ├── SPEC_COMPARISON.md # Spec compliance comparison
│   └── MULTI_REGION.md    # Multi-region endpoint config
├── mcp/
│   └── server.json       # MCP Registry format (multi-region)
├── registry/             # Skills index
│   └── skills.json
├── sdk/                  # Python SDK for loading skills
│   ├── __init__.py
│   └── loader.py
├── examples/             # Usage examples
│   ├── agent_usage.py
│   ├── run_generator.sh      # For mcp_to_skills (live server)
│   └── run_mcps_generator.sh  # For mcps_to_skills (local JSON)
├── requirements.txt
└── README.md
```

## Skill Schema Format

```json
{
  "name": "crawl_page",
  "description": "Crawls a web page and returns its HTML content.",
  "parameters": {
    "type": "object",
    "properties": {
      "url": { "type": "string", "description": "The URL to crawl" }
    },
    "required": ["url"]
  },
  "invoke": {
    "type": "http",
    "endpoint": "https://mcp.octoparse.com"
  }
}
```

## How to Run the Generator

### Prerequisites

- Python 3.9+
- MCP server running and accessible

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Generator

```bash
# Default: fetches from https://mcp.octoparse.com
python generator/mcp_to_skills.py

# Custom MCP server
python generator/mcp_to_skills.py --mcp-url https://your-mcp-server.com

# With authentication
python generator/mcp_to_skills.py --mcp-url https://mcp.example.com --auth-token "Bearer YOUR_TOKEN"

# Verbose output
python generator/mcp_to_skills.py -v
```

### Environment Variables

| Variable | Description |
|----------|-------------|
| `MCP_URL` | MCP server URL (default: https://mcp.octoparse.com) |
| `MCP_AUTH_TOKEN` | Bearer token for authenticated MCP servers |
| `MCP_SESSION_ID` | Session ID for stateful MCP servers |

### Using the Shell Script

```bash
chmod +x examples/run_generator.sh
./examples/run_generator.sh
```

### From Local MCP JSON (mcps folder)

If you have MCP tool descriptors as JSON files (e.g. Cursor's mcps folder), use `mcps_to_skills.py`:

```bash
# Default: reads from ~/.cursor/projects/.../mcps
python3 generator/mcps_to_skills.py --merge -v

# Custom mcps path
MCPS_DIR=/path/to/mcps python3 generator/mcps_to_skills.py --merge

# Or use the shell script
chmod +x examples/run_mcps_generator.sh
./examples/run_mcps_generator.sh

# Generate spec-compliant names (hyphens instead of underscores)
python3 generator/mcps_to_skills.py --merge --spec-compliant
```

### Validate Skills

```bash
python3 generator/validate_skills.py
python3 generator/validate_skills.py --strict  # Require agentskills.io name format
```

| Variable | Description |
|----------|-------------|
| `MCPS_DIR` | Path to mcps folder (contains user-octoparse/, user-figma/, etc.) |
| `OCTOPARSE_MCP_URL` | Octoparse MCP server URL (overrides region) |
| `OCTOPARSE_MCP_REGION` | Region: `international` (mcp.octoparse.com) or `china` (mcp.bazhuayu.com) |

## How Agents Can Use Skills

### 1. Discover Skills

```python
from sdk import list_skills

skills = list_skills()
for s in skills:
    print(s["name"], s["description"])
```

### 2. Load a Skill

```python
from sdk import load_skill

skill = load_skill("octoparse_get_task_scraped_data")
# Use skill["parameters"] for tool schema
# Use skill["invoke"]["endpoint"] for MCP server URL
# Use skill["invoke"]["tool"] for MCP tool name (tools/call params.name)
```

### 3. Convert to Agent Tool Format

```python
# OpenAI / Anthropic function calling format
tool_schema = {
    "type": "function",
    "function": {
        "name": skill["name"],
        "description": skill["description"],
        "parameters": skill["parameters"],
    },
}
```

### 4. Invoke via MCP

When the agent decides to call a skill, invoke the MCP server:

```json
POST {skill.invoke.endpoint}
{
  "jsonrpc": "2.0",
  "id": "1",
  "method": "tools/call",
  "params": {
    "name": "crawl_page",
    "arguments": { "url": "https://example.com" }
  }
}
```

See `examples/agent_usage.py` for a complete example.

## Example Skills (Included)

### Web Crawling (from mcp_to_skills)
| Skill | Description |
|-------|-------------|
| `crawl_page` | Fetch raw HTML from a URL |
| `discover_urls` | Extract all links from a page |
| `extract_structured_data` | Scrape structured data via CSS selectors |
| `render_page` | Render JS-heavy pages with headless browser |

### Octoparse MCP (from mcps_to_skills)
| Skill | Description |
|-------|-------------|
| `octoparse_search_user_task_list` | Search/filter user's scraping tasks |
| `octoparse_start_cloud_task_execution` | Start a cloud scraping task |
| `octoparse_get_task_scraped_data` | Retrieve scraped data from a task |
| `octoparse_create_task_from_template` | Create task from template |
| ... | 12 more Octoparse skills |

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please open an issue or PR on GitHub.
