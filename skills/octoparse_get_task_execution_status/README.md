# octoparse_get_task_execution_status

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Retrieves the current execution status of one or multiple Octoparse tasks. Use this to monitor task progress and state.

## Parameters

- **taskIds** (array) (required): REQUIRED: Array of task IDs to check status for. Must contain at least one ID. BEST PRACTICE: Batch multiple tasks in one call rather than calling repeatedly. Verify task IDs exist if unsure (use searchTaskList or getTaskInfoById).

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_execution_status

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com