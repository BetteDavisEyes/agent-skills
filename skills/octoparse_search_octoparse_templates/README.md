# octoparse_search_octoparse_templates

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Searches the Octoparse template library by keyword and returns a list of matching templates with detailed information.

## Parameters

- **keyword** (string): Search keyword for templates. Use the exact platform/website name if user mentions one (e.g., 'Amazon', 'LinkedIn'). If omitted, returns popular templates. DO NOT fabricate keywords - use user's exact words.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: search_octoparse_templates

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com