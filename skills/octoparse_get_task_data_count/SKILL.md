---
name: octoparse_get_task_data_count
description: "Retrieves the total count of collected data for a specific task. Use this to check how much data has been scraped without downloading all the data."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_task_data_count"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_task_data_count

## Overview

Retrieves the total count of collected data for a specific task. Use this to check how much data has been scraped without downloading all the data.

[When to use]:
- MUST call when user asks "how much data", "how many records", "data count", "how many rows"
- Call when user wants to check data volume before exporting
- Call when user wants to monitor scraping progress (how much data collected so far)
- Call when user wants to verify if task has collected any data
- Call to check if there's new data to export (use includeExported=false)

[When NOT to use]:
- DO NOT call if user wants the actual data (use export_task_scraped_data instead)
- DO NOT call if user wants task execution status (use get_task_execution_status instead)
- DO NOT call if user wants task configuration details (use get_task_detailed_info instead)

[Critical Parameters]:
- taskId (REQUIRED): The task ID to check data count for. User must provide this.
- includeExported (OPTIONAL, default: true): Controls which data to count
  * true = Count ALL data (both exported and not-exported) - Total data collected by task
  * false = Count ONLY not-exported data - New data available for export

[Understanding includeExported]:
When includeExported=true (default):
  - Returns TOTAL count of all data ever collected by this task
  - Use when user asks: "How much data in total?", "Total records", "All data count"

When includeExported=false:
  - Returns count of ONLY new/unexported data
  - Use when user asks: "How much new data?", "Unexported records", "Data ready to export"
  - This is data that hasn't been marked as exported yet

[What You Get]:
- total: Total number of data records matching the filter
- offset: Current offset (always 1 in this tool)
- restTotal: Remaining records after offset
- fileIds: Sample file IDs (only first file, used for verification)

[Self-Correction Scenarios]:

Scenario 1: Task doesn't exist
If API returns error "task not found" or similar:
- Return structured error with taskId
-

...

## Parameters

- **taskId** (`string`) (required): REQUIRED: The task ID to check data count for. Must be a valid existing task. User must provide this parameter.
- **includeExported** (`boolean`): OPTIONAL: Whether to include exported data in the count. Default is true (count all data). Set to false to count only unexported/new data. Use true when user asks about "total data" or "all data", use false when user asks about "new data" or "unexported data".

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_data_count

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.