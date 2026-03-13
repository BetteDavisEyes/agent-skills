---
name: octoparse_create_task_from_template
description: "Creates a new scraping task based on an Octoparse template. This is the primary way to set up a new data extraction job."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "create_task_from_template"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_create_task_from_template

## Overview

Creates a new scraping task based on an Octoparse template. This is the primary way to set up a new data extraction job.

[When to use]:
- MUST call when user says "create a task", "set up a scraper", "use template X to scrape Y"
- Call after user has selected a template (from searchTemplates) and wants to instantiate it
- Call when user wants to start scraping with a specific template

[CRITICAL - Prerequisites]:
Before calling this tool, you MUST:
1. Call getTemplateView(templateId) to get template details and required parameters
2. Call getUserInfo() to verify user's account level meets template's accountLimit
3. Call getTaskGroups() if user wants to specify a task group (optional but recommended for organization)

[When NOT to use]:
- DO NOT call if user wants to modify an existing task (use updateTemplateTask instead)
- DO NOT call if you don't have a valid templateId (search first with searchTemplates)
- DO NOT call if user's account level is insufficient (check accountLimit from getTemplateView)

[Parameter Guidelines]:
- templateId (REQUIRED): Must be a valid template ID from searchTemplates or getTemplateView
- taskName (optional): If not provided, system will auto-generate. BEST PRACTICE: Always ask user for a descriptive name
- taskGroupId (optional): If not provided, task goes to default group. RECOMMEND: Ask user or use result from getTaskGroups
- userInputParameters (REQUIRED): Complex parameter object for template customization. This is MANDATORY for all templates.

[CRITICAL - userInputParameters Structure]:
The userInputParameters field is REQUIRED and must contain BOTH UIParameters and TemplateParameters arrays.

**UIParameters** (REQUIRED):
- Purpose: UI-level parameters for displaying in Octoparse Desktop client
- Format: Array of objects with structure: [{Id: "param_id", Value: "param_value"}]
- Each parameter MUST have: Id (string) - parameter identifier from template schema
- Each parameter MAY have: Value (any) - the parameter value
- Example

...

## Parameters

- **templateId** (`integer`) (required): REQUIRED: The template ID to use for task creation. Must be a valid template ID obtained from searchTemplates or getTemplateView. Verify template exists before calling.
- **taskName** (`string`): OPTIONAL but RECOMMENDED: A descriptive name for the task. If not provided, system auto-generates a name. BEST PRACTICE: Always ask user for a meaningful name like "Amazon Product Scraper - Electronics".
- **taskGroupId** (`integer`): OPTIONAL: The task group ID to organize this task. Get available groups from getTaskGroups(). If omitted, task goes to default group. RECOMMEND: Ask user or use their most recent group.
- **userInputParameters** (`object`) (required): REQUIRED: User input parameters object containing BOTH UIParameters and TemplateParameters arrays. CRITICAL: Both arrays are mandatory and parameters must be paired (every parameter in UIParameters must exist in TemplateParameters and vice versa). Get parameter schema from getTemplateView before constructing this object. Example: {UIParameters: [{Id: "param-id", Value: "value"}], TemplateParameters: [{ParamName: "ParamName", Value: "value"}]}
- **urlSourceTaskId** (`string`): ADVANCED: Task ID to use as URL source for task chaining. Only use if user explicitly wants to chain tasks.
- **urlSourceTaskField** (`string`): ADVANCED: Field name from source task containing URLs. Required if urlSourceTaskId is provided.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: create_task_from_template

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.