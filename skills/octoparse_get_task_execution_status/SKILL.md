---
name: octoparse_get_task_execution_status
description: "Retrieves the current execution status of one or multiple Octoparse tasks. Use this to monitor task progress and state."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_task_execution_status"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_task_execution_status

## Overview

Retrieves the current execution status of one or multiple Octoparse tasks. Use this to monitor task progress and state.

[When to use]:
- MUST call when user asks "is task X running?", "what's the status of task Y?", "how is my scraper doing?"
- MUST call BEFORE startCloudTask to avoid starting an already-running task
- MUST call BEFORE stopCloudTask to verify task is actually running
- Call periodically when user wants to monitor long-running tasks
- Call after starting/stopping a task to confirm state change

[When NOT to use]:
- DO NOT call if user wants detailed task configuration (use getTaskInfoById instead)
- DO NOT call if user is searching for tasks (use searchTaskList instead)
- DO NOT call repeatedly in rapid succession (respect rate limits)

[Batch Capability]:
- This tool accepts MULTIPLE task IDs in one call
- BEST PRACTICE: When user asks about several tasks, batch them into one call
- More efficient than calling once per task

[Possible Status Values]:
- "Running": Task is currently executing
- "Stopped": Task has been stopped manually
- "Completed": Task finished successfully
- "Failed": Task encountered an error
- "Pending": Task is queued to run
- "Paused": Task is temporarily paused

[Examples]:
User: "Is task abc123 running?"
-> get_task_execution_status(taskIds: ["abc123"])

User: "Show me status of all my tasks"
-> 1. searchTaskList()
-> 2. get_task_execution_status(taskIds: [<all_ids>])

User: "Tell me about task 789"
-> If user wants configuration/details, use getTaskInfoById instead
-> If user wants execution status, use this tool

## Parameters

- **taskIds** (`array`) (required): REQUIRED: Array of task IDs to check status for. Must contain at least one ID. BEST PRACTICE: Batch multiple tasks in one call rather than calling repeatedly. Verify task IDs exist if unsure (use searchTaskList or getTaskInfoById).

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_execution_status

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.