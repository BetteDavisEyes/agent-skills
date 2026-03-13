# octoparse_update_existing_template_task

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Updates an existing template-based task with new parameters, name, or group assignment. This is for modifying tasks that have already been created.

## Parameters

- **taskId** (string) (required): REQUIRED: The ID of the task to update. Must be an existing task. Verify with getTaskInfoById first.
- **taskName** (string) (required): REQUIRED: The task name. Use current name from getTaskInfoById if not changing, or provide new name.
- **taskGroupId** (['string', 'number']) (required): REQUIRED: Task group ID. Use current value from getTaskInfoById if not changing group.
- **templateId** (integer) (required): REQUIRED: Template ID. MUST match current template (cannot change template for existing task). Get from getTaskInfoById.
- **templateType** (integer): REQUIRED: Template type, usually 1. Get from getTaskInfoById. Do NOT change unless you know what you're doing.
- **templateVersion** (integer) (required): REQUIRED: Current template version. Get from getTaskInfoById. If version mismatch, update will fail.
- **templateRegistrationId** (integer) (required): REQUIRED: Template registration ID. Get from getTaskInfoById. This identifies the specific template instance.
- **userInputParameters** (object) (required): REQUIRED: User input parameters object containing BOTH UIParameters and TemplateParameters arrays. CRITICAL: Both arrays are mandatory and parameters must be paired (every parameter in UIParameters must exist in TemplateParameters and vice versa). Get current parameters from getTaskInfoById, modify only what user wants to change while preserving all other parameters. If you modify a parameter value, you MUST update it in BOTH UIParameters and TemplateParameters to keep them paired. Do not omit any existing parameters or they will be lost.
- **templateVersionId** (integer) (required): REQUIRED: Template version ID. Get from getTaskInfoById.
- **urlSourceTaskId** (string): OPTIONAL: URL source task ID for task chaining. Preserve from getTaskInfoById if exists.
- **urlSourceTaskField** (string): OPTIONAL: URL source field. Preserve from getTaskInfoById if exists.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: update_existing_template_task

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com