---
name: octoparse_search_user_task_list
description: "Searches the user's task list with flexible filtering options including keyword, group, status, and pagination. This is the primary tool for finding tasks."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "search_user_task_list"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_search_user_task_list

## Overview

Searches the user's task list with flexible filtering options including keyword, group, status, and pagination. This is the primary tool for finding tasks.

[When to use]:
- MUST call when user says "show my tasks", "find tasks", "list all tasks", "search for task X"
- MUST call when user references a task by name but you don't have the ID (e.g., "start my Amazon scraper")
- Call when user wants to filter tasks by group, status, or keyword
- Call when user wants to browse their tasks

[When NOT to use]:
- DO NOT call if you already have the task ID and want details (use getTaskInfoById)
- DO NOT call if user only wants execution status for known task IDs (use getTaskStatus)
- DO NOT call if user wants to create a task (use createTemplateTask)

[Parameter Guidelines]:
- keyWord (optional): Searches task names and descriptions. Case-insensitive. Leave empty to get all tasks.
- taskGroup (optional): Filter by specific task group/folder. Get group ID from getTaskGroups first.
- status (optional): Filter by execution status (e.g., "Running", "Stopped", "Completed").
- taskIds (optional): Fetch specific tasks by ID. More efficient than searching by keyword if you have IDs.
- pageIndex (optional, default: 1): Page number (1-based). Start with page 1.
- pageSize (optional, default: 20, max: 100): Number of tasks per page.

[Pagination Best Practices]:
- For first search: Use default pagination or pageSize=50
- Don't automatically fetch all pages - wait for user confirmation
- If user says "show all", loop through pages

[Examples]:
User: "Show my tasks"
-> search_user_task_list()

User: "Find my Amazon tasks"
-> search_user_task_list(keyWord: "Amazon")

User: "Show me running tasks"
-> search_user_task_list(status: "Running")

User: "What's task 123 doing?"
-> DO NOT call this tool, use getTaskStatus(["123"]) instead

## Parameters

- **taskGroup** (`string`): OPTIONAL: Task group ID to filter by. Get group IDs from getTaskGroups(). Leave empty to search all groups.
- **pageIndex** (`integer`): OPTIONAL: Page number (1-based). Default is 1. BEST PRACTICE: Start with page 1, ask user before fetching more.
- **pageSize** (`integer`): OPTIONAL: Number of tasks per page. Default is 20, maximum is 100. Use 50-100 for "show all tasks" requests.
- **keyWord** (`string`): OPTIONAL: Keyword to search in task names and descriptions. Case-insensitive. Leave empty to get all tasks.
- **status** (`string`): OPTIONAL: Filter by task execution status. Common values: "Running", "Stopped", "Completed", "Failed".
- **taskIds** (`array`): OPTIONAL: Array of specific task IDs to fetch. More efficient than keyword search if you have IDs.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: search_user_task_list

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.