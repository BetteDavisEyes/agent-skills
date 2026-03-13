# octoparse_get_task_detailed_info

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Retrieves comprehensive configuration and metadata of a specific task, including template info, parameters, group assignment, and creation details.

## Parameters

- **taskId** (string) (required): REQUIRED: The ID of the task to retrieve details for. Must be a valid, existing task ID. If unsure, search first with searchTaskList to find the task ID.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_detailed_info

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com