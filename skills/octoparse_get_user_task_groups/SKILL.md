---
name: octoparse_get_user_task_groups
description: "Retrieves all task groups (folders/categories) that belong to the current user. Task groups are used to organize tasks."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_user_task_groups"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_user_task_groups

## Overview

Retrieves all task groups (folders/categories) that belong to the current user. Task groups are used to organize tasks.

[What are Task Groups]:
Task groups are organizational containers for tasks, similar to folders. They help users organize their scraping tasks by project, category, or any other criteria.

[When to use]:
- MUST call when user asks "what are my task groups", "show my folders", "list my task categories"
- MUST call BEFORE createTemplateTask if user wants to specify a group (get group ID)
- Call when user wants to organize tasks or move tasks between groups
- Call as a discovery tool when user is exploring their tasks

[When NOT to use]:
- DO NOT call if user wants task details (use getTaskInfoById)
- DO NOT call if user is searching for specific tasks (use searchTaskList)
- DO NOT call repeatedly - groups don't change frequently, cache the result

[What You Get]:
- Group ID: Numeric identifier (use with createTemplateTask, updateTemplateTask, searchTaskList)
- Group name: Human-readable name
- Task count: Number of tasks in each group

[Examples]:
User: "What task groups do I have?"
-> get_user_task_groups()

User: "Create a task"
-> Call this first if user wants to specify a group, or ask: "Which group should I put this task in?"

User: "Show me my Amazon tasks"
-> DO NOT call this tool first, call searchTaskList(keyWord: "Amazon") instead

## Parameters


## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_user_task_groups

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.