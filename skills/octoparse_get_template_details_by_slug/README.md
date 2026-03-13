# octoparse_get_template_details_by_slug

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Retrieves comprehensive details of a specific Octoparse template by its URL-friendly slug identifier.

## Parameters

- **slug** (string) (required): The URL-friendly slug identifier of the template (e.g., "amazon-product-scraper"). Must be lowercase with hyphens. Extract from URLs or use exact slug from searchTemplates results. DO NOT guess or fabricate slugs.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_template_details_by_slug

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com