---
name: octoparse_get_task_scraped_data
description: "Retrieves scraped data from a task as a JSON structure. Gets data that hasn't been exported yet and returns it directly as a JSON array."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_task_scraped_data"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_task_scraped_data

## Overview

Retrieves scraped data from a task as a JSON structure. Gets data that hasn't been exported yet and returns it directly as a JSON array.

[When to use]:
- MUST call when user says "get data", "fetch task data", "show scraped results", "retrieve task results"
- Call after a task has completed or stopped running
- Call when user wants to see data without saving to file
- Call when user wants to process data programmatically

[IMPORTANT - Context Optimization]:
- CRITICAL: For large datasets, use small batch sizes (e.g., size=50) with multiple calls instead of retrieving all data at once
- RECOMMENDED: Retrieve data in small batches and store each batch separately to minimize context usage
- OPTIMAL: Use size=50 or smaller with getAll=false, then call multiple times to retrieve all data in small chunks
- BENEFIT: Smaller context usage improves performance and reduces memory consumption
- STRATEGY: Store each batch in separate variables, then merge all batches when complete for final processing

[When NOT to use]:
- DO NOT call if task hasn't run yet (no data to retrieve)
- DO NOT call if user wants to save data to file (use export_task_scraped_data instead)
- DO NOT call if user only wants to see task status (use getTaskStatus)

[IMPORTANT - "Not Exported" Concept]:
- Octoparse tracks which data has been exported to avoid duplicates
- This tool gets "not exported" data = new data since last export
- After export, data is marked as "exported" in Octoparse
- CRITICAL: If you retrieve data with getAll=false, then call again, you'll get DIFFERENT data (next batch)

[Parameter Guidelines]:
- taskId (required): The task to get data from. Task must have run at least once.
- size (optional, default: 50, max: 200): Number of records to retrieve per batch. Maximum 200 per request.
- getAll (optional, default: false): false = get first batch only, true = get ALL data (may require multiple internal requests).

[Interaction Between getAll and size]:
- getAll=false, size=50: Get fir

...

## Parameters

- **taskId** (`string`) (required): REQUIRED: The task ID to get data from. Task must have run at least once and collected data. Verify with getTaskStatus if unsure.
- **size** (`integer`): OPTIONAL: Number of records to retrieve per batch. Default 50, maximum 200. Only matters when getAll=true (determines batch size). Use 50-200 for normal requests.
- **getAll** (`boolean`): OPTIONAL: Whether to get all not-exported data. false (default) = get first batch only (quick preview), true = get ALL data (complete dataset). IMPORTANT: If false and you call again, you get NEXT batch (incremental).

## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_task_scraped_data

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.