---
name: octoparse_start_cloud_task_execution
description: "Starts a scraping task on Octoparse's cloud infrastructure. The task will run on cloud servers and extract data according to its configuration."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "start_cloud_task_execution"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_start_cloud_task_execution

## Overview

Starts a scraping task on Octoparse's cloud infrastructure. The task will run on cloud servers and extract data according to its configuration.

[When to use]:
- MUST call when user says "start task", "run task X", "begin scraping", "execute task Y"
- Call after user has created a task and is ready to collect data
- Call when user wants to resume a stopped task

[CRITICAL - Prerequisites and Limitations]:
Before calling this tool, verify:
1. Task exists: Call getTaskInfoById(taskId) to verify task exists
2. Template compatibility: Check template's runOn field from getTemplateView
   - runOn=1 (Local only): CANNOT use this tool -> Tell user they must use Octoparse desktop client
   - runOn=2 (Cloud only): OK to use this tool
   - runOn=3 (Both): OK to use this tool
3. User account: Call getUserInfo() to verify user has sufficient credits/balance
4. Task status: Don't start if already running (check with getTaskStatus first)

[When NOT to use]:
- DO NOT call if template's runOn=1 (local only) -> Will always fail
- DO NOT call if task is already running -> Check with getTaskStatus first
- DO NOT call if user wants to stop a task (use stopCloudTask instead)
- DO NOT call immediately after creating a task without asking user

[What Happens]:
- Task starts executing on cloud servers
- Returns StartTaskResult status code and lotNo (execution batch number)
- Task will run until completion or manual stop
- Data will be available via saveNoExportedData after task completes

[Possible Results]:
- SUCCESS (0): Task started successfully
- ALREADY_RUNNING (1): Task is already executing
- TASK_NOT_FOUND (3): Task ID doesn't exist
- INSUFFICIENT_CREDITS (4): User needs to top up balance
- TASK_DISABLED (5): Task is disabled or template is local-only
- RATE_LIMIT_EXCEEDED (6): Too many concurrent tasks
- USER_INSUFFICIENT_PERMISSION (10): Account level too low for this task

[Examples]:
User: "Start task abc123"
-> 1. getTaskInfoById("abc123")
-> 2. getTaskStatus(["abc123"])
-> 3. I

...

## Parameters

- **taskId** (`string`) (required): REQUIRED: The ID of the task to start. Must be a valid, existing task ID. Verify with getTaskInfoById first. CRITICAL: If task uses a template with runOn=1, this call will fail - check template compatibility first.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: start_cloud_task_execution

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.