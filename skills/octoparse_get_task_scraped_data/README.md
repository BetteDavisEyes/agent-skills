# octoparse_get_task_scraped_data

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Retrieves scraped data from a task as a JSON structure. Gets data that hasn't been exported yet and returns it directly as a JSON array.

## Parameters

- **taskId** (string) (required): REQUIRED: The task ID to get data from. Task must have run at least once and collected data. Verify with getTaskStatus if unsure.
- **size** (integer): OPTIONAL: Number of records to retrieve per batch. Default 50, maximum 200. Only matters when getAll=true (determines batch size). Use 50-200 for normal requests.
- **getAll** (boolean): OPTIONAL: Whether to get all not-exported data. false (default) = get first batch only (quick preview), true = get ALL data (complete dataset). IMPORTANT: If false and you call again, you get NEXT batch (incremental).

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_scraped_data

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com