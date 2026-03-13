---
name: Octoparse Task Control
description: Orchestrate the execution of scraping tasks on Octoparse's cloud infrastructure. Manage task lifecycle from pre-run checks to completion monitoring.
---

## Overview

This skill orchestrates the execution of scraping tasks on Octoparse's cloud infrastructure. It manages the complete task lifecycle including pre-run compatibility checks, starting/stopping tasks, and status monitoring.

## When to use

Use this skill when the user wants to:
- Start a scraping task
- Stop a running task
- Check if a task is running
- Run tasks in a group
- "Start task abc123"
- "Run my Amazon scraper"
- "Stop the eBay task"
- "Is my task still running?"
- "Execute everything in the Retail group"

## Instructions

### Pre-Run Compatibility Check (MANDATORY)

Before starting ANY task, verify it can run on cloud:

1. **Fetch Task Info**: `get_task_detailed_info(taskId: ID)`
2. **Check `runOn` Property**:
   - `runOn=1`: **LOCAL ONLY** - You CANNOT start this. Inform user they must use Octoparse Desktop Client.
   - `runOn=2` or `3`: **CLOUD SUPPORTED** - Proceed to start.
3. **Check Account**: Ensure user has sufficient credits via `get_user_account_info()`

### Execution Workflow

1. **Verify Current State**: `get_task_execution_status(taskIds: [ID])`
   - Don't start already `Running` tasks
   - Don't stop already `Stopped` tasks

2. **Execute Action**:
   - Start: `start_cloud_task_execution(taskId: ID)`
   - Stop: `stop_cloud_task_execution(taskId: ID)`

3. **Confirm State Change**:
   - Wait briefly or check status again
   - Verify state changed (e.g., Pending → Running)

### Error Handling

**"Insufficient Credits" (Error Code 4)**
1. Call `get_user_account_info()` to check balance
2. Explain situation: "Your account has X credits remaining. This task requires Y credits."
3. Suggest: purchasing more credits or waiting for renewal

**"Task Disabled" (Error Code 5)**
- Template is deprecated or task is locked
- Suggest checking web console or recreating with new template

**"Already Running" (Error Code 1)**
- Task is already executing, no action needed
- Report current status to user

**"Rate Limit Exceeded" (Error Code 6)**
- Too many concurrent tasks
- Suggest stopping some tasks or waiting

**"Task Not Found" (Error Code 3)**
- Verify task ID is correct
- Use `search_user_task_list` to find correct ID

### Batch Operations

For "run everything in X group" or "stop all running tasks":

1. Get relevant task IDs:
   - By group: `search_user_task_list(taskGroup: "group-id")`
   - By status: `search_user_task_list(status: "Running")`

2. Check current status of all tasks: `get_task_execution_status(taskIds: [id1, id2, ...])`

3. Filter to appropriate subset:
   - For start: only Stopped tasks
   - For stop: only Running tasks

4. Execute operations sequentially

5. Report summary:
   - Successfully started: X tasks
   - Already running: Y tasks
   - Failed: Z tasks (with reasons)

### Status Values

| Status | Meaning |
|--------|---------|
| Running | Task is currently executing |
| Stopped | Task has been manually stopped |
| Completed | Task finished successfully |
| Failed | Task encountered an error |
| Pending | Task is queued to run |

## Example Interactions

**User**: "Run task abc123"

1. `get_task_detailed_info("abc123")` → confirms `runOn=3`
2. `get_task_execution_status(["abc123"])` → confirms `Stopped`
3. `start_cloud_task_execution("abc123")` → returns `SUCCESS (0)`
4. Response: "Task abc123 has been started successfully on the cloud."

**User**: "Stop all my running tasks"

1. `search_user_task_list(status: "Running")` → get all running task IDs
2. `get_task_execution_status(taskIds: [id1, id2, id3])` → verify they're running
3. Loop through and call `stop_cloud_task_execution` for each
4. Report: "Stopped 3 tasks successfully."

**User**: "Is task xyz789 still running?"

1. `get_task_execution_status(["xyz789"])`
2. Report current status and any relevant details

## Resources

- `get_task_execution_status`: Check task status (batch capable)
- `start_cloud_task_execution`: Start a task on cloud
- `stop_cloud_task_execution`: Stop a running task
- `get_task_detailed_info`: Get task configuration including runOn property
- `get_user_account_info`: Check account balance for credit errors
- `search_user_task_list`: Find tasks for batch operations
