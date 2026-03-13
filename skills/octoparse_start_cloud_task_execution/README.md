# octoparse_start_cloud_task_execution

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Starts a scraping task on Octoparse's cloud infrastructure. The task will run on cloud servers and extract data according to its configuration.

## Parameters

- **taskId** (string) (required): REQUIRED: The ID of the task to start. Must be a valid, existing task ID. Verify with getTaskInfoById first. CRITICAL: If task uses a template with runOn=1, this call will fail - check template compatibility first.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: start_cloud_task_execution

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com