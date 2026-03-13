---
name: octoparse_get_template_categories
description: "Retrieves all available template categories (kinds) in the Octoparse template library."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_template_categories"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_template_categories

## Overview

Retrieves all available template categories (kinds) in the Octoparse template library.

[When to use]:
- MUST call when user asks "what categories of templates are available"
- Call when user wants to browse templates by category (e.g., "show me e-commerce templates")
- Call when user asks "what types of templates do you have"
- Call as a discovery tool when user is exploring available templates

[When NOT to use]:
- DO NOT call if user is searching for specific templates (use searchTemplates instead)
- DO NOT call if user wants template details (use getTemplateView or getTemplateBySlug)
- DO NOT call repeatedly - categories rarely change, cache the result

[What You Get]:
- Category IDs and names (e.g., "E-commerce", "Social Media", "Real Estate")
- These IDs can be used to filter searchTemplates results (if filtering by category is needed)

[Examples]:
User: "What kinds of templates are there?"
-> Call get_template_categories()

User: "List all available template categories"
-> Call get_template_categories()

## Parameters


## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_template_categories

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.