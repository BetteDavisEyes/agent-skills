# octoparse_get_task_data_count

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Retrieves the total count of collected data for a specific task. Use this to check how much data has been scraped without downloading all the data.

## Parameters

- **taskId** (string) (required): REQUIRED: The task ID to check data count for. Must be a valid existing task. User must provide this parameter.
- **includeExported** (boolean): OPTIONAL: Whether to include exported data in the count. Default is true (count all data). Set to false to count only unexported/new data. Use true when user asks about "total data" or "all data", use false when user asks about "new data" or "unexported data".

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_data_count

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com