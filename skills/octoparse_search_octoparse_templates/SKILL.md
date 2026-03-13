---
name: octoparse_search_octoparse_templates
description: "Searches the Octoparse template library by keyword and returns a list of matching templates with detailed information."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "search_octoparse_templates"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_search_octoparse_templates

## Overview

Searches the Octoparse template library by keyword and returns a list of matching templates with detailed information.

[When to use]:
- MUST call when user asks to "find templates", "search templates", or "browse templates"
- MUST call when user mentions a specific website/platform and wants to scrape it (e.g., "Amazon template", "eBay scraper")
- Call when user asks "what templates are available" or "show me templates for X"

[When NOT to use]:
- DO NOT call if user already has a specific template ID and wants details (use getTemplateView instead)
- DO NOT call if user wants to create a task (use createTemplateTask after getting the template ID)
- DO NOT call if user asks about template categories (use getTemplateKinds instead)

[Parameter Guidelines]:
- keyword (optional): If provided, searches by keyword. If omitted or empty, returns popular/recommended templates.
- IMPORTANT: If user mentions a specific platform name (e.g., "Amazon", "Facebook"), use that as the keyword exactly.
- DO NOT fabricate or assume template availability - search first, then report results.

[Output Requirements]:
When presenting results, you MUST display ALL these fields for EACH template:
- id: Template identifier (required for creating tasks)
- enName: Template name
- slug: URL-friendly identifier
- pricePerData: Cost per data unit
- accountLimit: Required account level (check against user's current level from getUserInfo)
- enDescription: What the template does
- runOn: Where it can run (1=Local only, 2=Cloud only, 3=Both) - CRITICAL for startCloudTask

[Key Field Descriptions]:
- id: The unique identifier for the template
- slug: The URL-friendly slug for the template
- pricePerData: The price per unit of data
- prices: A JSON string representing different pricing tiers
- likes: The number of likes the template has received
- status: The status of the template (e.g., 1 for Published)
- kindIds: An array of category IDs for the template
- enName: The English name of the template
- e

...

## Parameters

- **keyword** (`string`): Search keyword for templates. Use the exact platform/website name if user mentions one (e.g., 'Amazon', 'LinkedIn'). If omitted, returns popular templates. DO NOT fabricate keywords - use user's exact words.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: search_octoparse_templates

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.