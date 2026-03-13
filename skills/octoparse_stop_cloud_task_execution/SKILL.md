---
name: octoparse_stop_cloud_task_execution
description: "Stops a currently running task on Octoparse's cloud infrastructure. The task will cease execution immediately."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "stop_cloud_task_execution"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_stop_cloud_task_execution

## Overview

Stops a currently running task on Octoparse's cloud infrastructure. The task will cease execution immediately.

[When to use]:
- MUST call when user says "stop task", "halt task X", "cancel scraping", "pause task Y"
- Call when user wants to terminate a running task
- Call when user wants to stop a malfunctioning task

[Prerequisites]:
- Task must be currently running. Check with getTaskStatus first to avoid unnecessary API calls.
- Task must exist. If unsure, call getTaskInfoById to verify.

[When NOT to use]:
- DO NOT call if task is not running
- DO NOT call if user wants to start a task (use startCloudTask instead)

[IMPORTANT - Data Preservation]:
- Stopping a task does NOT delete collected data
- Data collected before stopping is still available
- Use saveNoExportedData to retrieve partial results after stopping
- Task can be restarted later with startCloudTask

[Examples]:
User: "Stop my Amazon scraper"
-> 1. searchTaskList(keyWord: "Amazon")
-> 2. getTaskStatus([<task_id>])
-> 3. stop_cloud_task_execution(taskId: <task_id>)

User: "Start task 456"
-> DO NOT call this tool, call startCloudTask instead

## Parameters

- **taskId** (`string`) (required): REQUIRED: The ID of the task to stop. Must be a currently running task. Verify task exists and is running with getTaskStatus first for best UX.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: stop_cloud_task_execution

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.