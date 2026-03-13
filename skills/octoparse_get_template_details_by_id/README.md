# octoparse_get_template_details_by_id

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Retrieves comprehensive details of a specific Octoparse template by its numeric ID, including version information, user permissions, and runtime requirements.

## Parameters

- **templateId** (integer) (required): The numeric ID of the template to query. This should come from searchTemplates results. IMPORTANT: Must be a positive integer, NOT a string or slug.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_template_details_by_id

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com