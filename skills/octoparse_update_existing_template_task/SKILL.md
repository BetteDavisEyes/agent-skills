---
name: octoparse_update_existing_template_task
description: "Updates an existing template-based task with new parameters, name, or group assignment. This is for modifying tasks that have already been created."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "update_existing_template_task"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_update_existing_template_task

## Overview

Updates an existing template-based task with new parameters, name, or group assignment. This is for modifying tasks that have already been created.

[When to use]:
- MUST call when user says "update task X", "change task Y parameters", "modify task Z"
- Call when user wants to rename an existing task
- Call when user wants to move a task to a different group
- Call when user wants to change template parameters (e.g., different search keywords)

[When NOT to use]:
- DO NOT call if user wants to create a NEW task (use createTemplateTask instead)
- DO NOT call if user wants to start/stop a task (use startCloudTask/stopCloudTask)
- DO NOT call if user just wants to view task info (use getTaskInfoById)

[CRITICAL - Prerequisites]:
Before calling this tool, you MUST:
1. Call getTaskInfoById(taskId) to get current task configuration
2. Preserve all existing values that user doesn't want to change
3. Call getTemplateView(templateId) to verify template version and parameters if changing parameters

[IMPORTANT - All Parameters Required]:
Unlike createTemplateTask, this tool requires ALL parameters because it performs a complete update.

[CRITICAL - userInputParameters Structure]:
The userInputParameters field is REQUIRED and must contain BOTH UIParameters and TemplateParameters arrays.

**UIParameters** (REQUIRED):
- Purpose: UI-level parameters for displaying in Octoparse Desktop client
- Format: Array of objects with structure: [{Id: "param_id", Value: "param_value"}]
- Each parameter MUST have: Id (string) - parameter identifier from template schema
- Each parameter MAY have: Value (any) - the parameter value
- When updating: Get current UIParameters from getTaskInfoById, modify only what needs to change

**TemplateParameters** (REQUIRED):
- Purpose: Template-level parameters for actual scraping execution
- Format: Array of objects with structure: [{ParamName: "param_name", Value: "param_value"}]
- Each parameter MUST have: ParamName (string) - parameter name from template

...

## Parameters

- **taskId** (`string`) (required): REQUIRED: The ID of the task to update. Must be an existing task. Verify with getTaskInfoById first.
- **taskName** (`string`) (required): REQUIRED: The task name. Use current name from getTaskInfoById if not changing, or provide new name.
- **taskGroupId** (`['string', 'number']`) (required): REQUIRED: Task group ID. Use current value from getTaskInfoById if not changing group.
- **templateId** (`integer`) (required): REQUIRED: Template ID. MUST match current template (cannot change template for existing task). Get from getTaskInfoById.
- **templateType** (`integer`): REQUIRED: Template type, usually 1. Get from getTaskInfoById. Do NOT change unless you know what you're doing.
- **templateVersion** (`integer`) (required): REQUIRED: Current template version. Get from getTaskInfoById. If version mismatch, update will fail.
- **templateRegistrationId** (`integer`) (required): REQUIRED: Template registration ID. Get from getTaskInfoById. This identifies the specific template instance.
- **userInputParameters** (`object`) (required): REQUIRED: User input parameters object containing BOTH UIParameters and TemplateParameters arrays. CRITICAL: Both arrays are mandatory and parameters must be paired (every parameter in UIParameters must exist in TemplateParameters and vice versa). Get current parameters from getTaskInfoById, modify only what user wants to change while preserving all other parameters. If you modify a parameter value, you MUST update it in BOTH UIParameters and TemplateParameters to keep them paired. Do not omit any existing parameters or they will be lost.
- **templateVersionId** (`integer`) (required): REQUIRED: Template version ID. Get from getTaskInfoById.
- **urlSourceTaskId** (`string`): OPTIONAL: URL source task ID for task chaining. Preserve from getTaskInfoById if exists.
- **urlSourceTaskField** (`string`): OPTIONAL: URL source field. Preserve from getTaskInfoById if exists.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: update_existing_template_task

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.