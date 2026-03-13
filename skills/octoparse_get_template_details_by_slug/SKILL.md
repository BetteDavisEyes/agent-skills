---
name: octoparse_get_template_details_by_slug
description: "Retrieves comprehensive details of a specific Octoparse template by its URL-friendly slug identifier."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_template_details_by_slug"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_template_details_by_slug

## Overview

Retrieves comprehensive details of a specific Octoparse template by its URL-friendly slug identifier.

[CRITICAL - Best Practices]:
- The "prompts" field contains high-level template instructions.
- Individual parameters in the "parameters" field also contain embedded "Instruction" text (originally from the Remark field).
- You MUST follow ALL these instructions to ensure correct configuration. Think of these as the template's manual.
- Note: The "Remark" field itself is hidden from output, but its content is preserved in parameter descriptions.

[What is a Slug]:
A slug is a URL-friendly identifier like "amazon-product-scraper" or "linkedin-people-search". It's the human-readable version of a template ID, often used in URLs.

[When to use]:
- MUST call when you have a template slug (from searchTemplates or user provides a template URL)
- Call when user provides a template link/URL and you extract the slug from it
- Call when user refers to a template by its human-readable name and you need to convert it

[When NOT to use]:
- DO NOT call if you have a numeric template ID (use getTemplateView instead - it's more efficient)
- DO NOT call if you're searching by keyword (use searchTemplates instead)
- DO NOT guess slug names - if user mentions a template name, search first with searchTemplates

[Parameter Format]:
- slug: Must be a lowercase, hyphenated string (e.g., "amazon-product-scraper")
- IMPORTANT: Extract slug from template URLs like "https://octoparse.com/template/amazon-product-scraper"
- DO NOT use template names directly - slugs are specific identifiers

[Examples]:
User: "Show me details of template amazon-product-scraper"
-> Call get_template_details_by_slug(slug: "amazon-product-scraper")

User: "I want to use https://octoparse.com/template/linkedin-people-search"
-> Extract "linkedin-people-search" and call get_template_details_by_slug(slug: "linkedin-people-search")

User: "Show me template 12345"
-> DO NOT call this tool, call getTemplateView(templateI

...

## Parameters

- **slug** (`string`) (required): The URL-friendly slug identifier of the template (e.g., "amazon-product-scraper"). Must be lowercase with hyphens. Extract from URLs or use exact slug from searchTemplates results. DO NOT guess or fabricate slugs.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_template_details_by_slug

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.