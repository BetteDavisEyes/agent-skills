# octoparse_create_task_from_template

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Creates a new scraping task based on an Octoparse template. This is the primary way to set up a new data extraction job.

## Parameters

- **templateId** (integer) (required): REQUIRED: The template ID to use for task creation. Must be a valid template ID obtained from searchTemplates or getTemplateView. Verify template exists before calling.
- **taskName** (string): OPTIONAL but RECOMMENDED: A descriptive name for the task. If not provided, system auto-generates a name. BEST PRACTICE: Always ask user for a meaningful name like "Amazon Product Scraper - Electronics".
- **taskGroupId** (integer): OPTIONAL: The task group ID to organize this task. Get available groups from getTaskGroups(). If omitted, task goes to default group. RECOMMEND: Ask user or use their most recent group.
- **userInputParameters** (object) (required): REQUIRED: User input parameters object containing BOTH UIParameters and TemplateParameters arrays. CRITICAL: Both arrays are mandatory and parameters must be paired (every parameter in UIParameters must exist in TemplateParameters and vice versa). Get parameter schema from getTemplateView before constructing this object. Example: {UIParameters: [{Id: "param-id", Value: "value"}], TemplateParameters: [{ParamName: "ParamName", Value: "value"}]}
- **urlSourceTaskId** (string): ADVANCED: Task ID to use as URL source for task chaining. Only use if user explicitly wants to chain tasks.
- **urlSourceTaskField** (string): ADVANCED: Field name from source task containing URLs. Required if urlSourceTaskId is provided.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: create_task_from_template

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com