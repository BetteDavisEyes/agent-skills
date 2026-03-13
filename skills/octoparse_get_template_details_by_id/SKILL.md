---
name: octoparse_get_template_details_by_id
description: "Retrieves comprehensive details of a specific Octoparse template by its numeric ID, including version information, user permissions, and runtime requirements."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_template_details_by_id"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_template_details_by_id

## Overview

Retrieves comprehensive details of a specific Octoparse template by its numeric ID, including version information, user permissions, and runtime requirements.

[CRITICAL - Best Practices]:
- The "prompts" field contains high-level template instructions.
- Individual parameters in the "parameters" field also contain embedded "Instruction" text (originally from the Remark field).
- You MUST follow ALL these instructions to ensure correct configuration. Think of these as the template's manual.
- Note: The "Remark" field itself is hidden from output, but its content is preserved in parameter descriptions.

[When to use]:
- MUST call when you have a template ID (from searchTemplates result) and need detailed information
- MUST call BEFORE createTemplateTask to verify template requirements and parameters
- Call when user asks "show me details of template X" where X is a number
- Call to check template's runOn property before attempting to start a cloud task

[When NOT to use]:
- DO NOT call if you have a slug instead of an ID (use getTemplateBySlug instead)
- DO NOT call if you're searching for templates (use searchTemplates instead)
- DO NOT call repeatedly for the same template ID in one conversation - cache the result

[CRITICAL - Template Compatibility Check]:
- Always check the "runOn" field: 1=Local only, 2=Cloud only, 3=Both
- If runOn=1, user CANNOT use startCloudTask and must use Octoparse desktop client
- Check "accountLimit" against user's account level (from getUserInfo)
- Check "minClientVersion" if user is running locally

[Examples]:
User: "Show me details of template 12345"
-> Call get_template_details_by_id(templateId: 12345)

User: "Can I run template 789 on cloud?"
-> First call get_template_details_by_id(templateId: 789), then check runOn field

User: "Find LinkedIn templates"
-> DO NOT call this tool, call searchTemplates(keyword: "LinkedIn") instead

## Parameters

- **templateId** (`integer`) (required): The numeric ID of the template to query. This should come from searchTemplates results. IMPORTANT: Must be a positive integer, NOT a string or slug.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_template_details_by_id

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.