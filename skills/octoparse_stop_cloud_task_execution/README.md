# octoparse_stop_cloud_task_execution

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Stops a currently running task on Octoparse's cloud infrastructure. The task will cease execution immediately.

## Parameters

- **taskId** (string) (required): REQUIRED: The ID of the task to stop. Must be a currently running task. Verify task exists and is running with getTaskStatus first for best UX.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: stop_cloud_task_execution

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com