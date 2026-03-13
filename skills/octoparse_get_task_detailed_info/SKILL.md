---
name: octoparse_get_task_detailed_info
description: "Retrieves comprehensive configuration and metadata of a specific task, including template info, parameters, group assignment, and creation details."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_task_detailed_info"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_task_detailed_info

## Overview

Retrieves comprehensive configuration and metadata of a specific task, including template info, parameters, group assignment, and creation details.

[What This Tool Returns]:
- Task configuration: Name, description, settings
- Template information: templateId, templateRegistrationId, templateVersion
- Task parameters: userInputParameters structure
- Organization: taskGroupId, folder assignment
- Metadata: Creation date, last modified, owner
- DO NOT confuse with execution status (use getTaskStatus for that)

[When to use]:
- MUST call when user asks "show me task X details", "what's in task Y?", "how is task Z configured?"
- MUST call BEFORE updateTemplateTask to get current configuration
- Call when user wants to see task parameters or template info
- Call when user wants to know which template a task uses
- Call to verify a task exists before other operations

[When NOT to use]:
- DO NOT call if user only needs execution status (use getTaskStatus instead)
- DO NOT call if user is searching for tasks (use searchTaskList instead)
- DO NOT call if user wants to start/stop task (check status with getTaskStatus first)

[Key Difference: Info vs Status]:
- get_task_detailed_info: Returns task CONFIGURATION (what it is)
- getTaskStatus: Returns task EXECUTION STATUS (what it's doing)

Example confusion:
User: "Is task 123 running?" -> Use getTaskStatus, NOT this tool
User: "What template does task 123 use?" -> Use THIS tool

[Examples]:
User: "Show me details of task abc123"
-> get_task_detailed_info(taskId: "abc123")

User: "What template is task 456 using?"
-> get_task_detailed_info(taskId: "456")

User: "Is task 789 running?"
-> DO NOT use this tool, use getTaskStatus(["789"]) instead

User: "I want to modify task xyz"
-> 1. get_task_detailed_info(taskId: "xyz")
-> 2. Modify necessary fields
-> 3. updateTemplateTask(...)

## Parameters

- **taskId** (`string`) (required): REQUIRED: The ID of the task to retrieve details for. Must be a valid, existing task ID. If unsure, search first with searchTaskList to find the task ID.

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_detailed_info

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.