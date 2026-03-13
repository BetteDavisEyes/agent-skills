# octoparse_search_user_task_list

> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)

Searches the user's task list with flexible filtering options including keyword, group, status, and pagination. This is the primary tool for finding tasks.

## Parameters

- **taskGroup** (string): OPTIONAL: Task group ID to filter by. Get group IDs from getTaskGroups(). Leave empty to search all groups.
- **pageIndex** (integer): OPTIONAL: Page number (1-based). Default is 1. BEST PRACTICE: Start with page 1, ask user before fetching more.
- **pageSize** (integer): OPTIONAL: Number of tasks per page. Default is 20, maximum is 100. Use 50-100 for "show all tasks" requests.
- **keyWord** (string): OPTIONAL: Keyword to search in task names and descriptions. Case-insensitive. Leave empty to get all tasks.
- **status** (string): OPTIONAL: Filter by task execution status. Common values: "Running", "Stopped", "Completed", "Failed".
- **taskIds** (array): OPTIONAL: Array of specific task IDs to fetch. More efficient than keyword search if you have IDs.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: search_user_task_list

**Multi-region** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com