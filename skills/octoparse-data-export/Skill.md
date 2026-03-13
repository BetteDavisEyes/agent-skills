---
name: Octoparse Data Export
description: Retrieve and process data results from Octoparse tasks. Manages the transition from scraped data to usable information while respecting API limits and data synchronization states.
---

## Overview

This skill retrieves and processes scraped data from Octoparse tasks. It manages the critical transition from "scraped data" to "usable information" while respecting API limits and data synchronization states.

## When to use

Use this skill when the user wants to:
- Get/export scraped data from a task
- Check how much data was collected
- Download results as JSON
- "Get the results from my task"
- "How many records did my task find?"
- "Export data from task abc123"
- "Is there any data to export?"

## Instructions

### The "Audit Before Export" Rule

Never download data blindly. It consumes user "Export Credits" or marks data as "Exported".

1. **Check Readiness**: Call `get_task_execution_status`
   - Best to export when `Completed` or `Stopped`
   - Avoid exporting while task is `Running` (inconsistent data)

2. **Check Volume**: Call `get_task_data_count(taskId: ID, includeExported: false)`
   - This tells how much **NEW** data is waiting
   - Use `includeExported: true` to see total data ever collected

3. **User Consent**: If volume is huge (e.g., > 10,000 records):
   - Warn user: "This will export 15,000 records. Continue?"
   - Get confirmation before proceeding

### Data Synchronization Concepts

Octoparse tracks which records have been exported:

**Incremental Mode** (`getAll: false`):
- Gets only the next batch of new data
- Useful for recurring syncs
- Each call returns different data (next batch)

**Full Snapshot Mode** (`getAll: true`):
- Gets ALL unexported data
- Useful for one-time deep dives
- Automatically paginates through all data

**Count Options**:
- `includeExported: true` = Count all data ever collected
- `includeExported: false` = Count only new/unexported data

### Export Workflow

**Step 1: Check Task Status**
```
get_task_execution_status(taskIds: ["task-id"])
```
Verify task is not actively running.

**Step 2: Check Data Volume**
```
get_task_data_count(taskId: "task-id", includeExported: false)
```
See how much new data exists.

**Step 3: Get User Confirmation (for large exports)**
If count > 10,000 records, warn user and get confirmation.

**Step 4: Retrieve Data**
```
get_task_scraped_data(taskId: "task-id", size: 200, getAll: true)
```
- For preview: `getAll: false, size: 50`
- For full export: `getAll: true, size: 200`

**Step 5: Present Results**
Show data preview or save to file as requested.

### Processing Large Datasets

If user wants "All" data:
- Use `size: 200` (maximum allowed) to minimize API calls
- Use `getAll: true` to automatically paginate
- Be patient with very large results (can take time)

### Understanding Export State

- After `get_task_scraped_data`, data is marked as "exported" in Octoparse
- Subsequent calls with `getAll: false` return DIFFERENT data (next batch)
- Use `includeExported: false` in count to check for fresh data

## Example Interactions

**User**: "Did my task find anything new?"

1. `get_task_data_count(taskId: "123", includeExported: false)`
2. Response: "Yes! There are 452 new records ready to be exported. Would you like me to fetch them now?"

**User**: "Get all data from my Amazon task"

1. Find task: `search_user_task_list(keyWord: "Amazon")`
2. Check status: `get_task_execution_status(taskIds: ["task-id"])`
3. Get count: `get_task_data_count(taskId: "task-id", includeExported: false)`
4. If count < 10,000: proceed with `get_task_scraped_data(taskId: "task-id", size: 200, getAll: true)`
5. If count > 10,000: warn user and get confirmation
6. Return data summary or full results

**User**: "Show me a sample of the data"

1. `get_task_scraped_data(taskId: "task-id", size: 50, getAll: false)`
2. Present first 50 records as preview

**User**: "How much data has my task collected in total?"

1. `get_task_data_count(taskId: "task-id", includeExported: true)`
2. Report total count including previously exported data

## Batch Size Guidelines

| Scenario | Recommended Size |
|----------|-----------------|
| Quick preview | 50 |
| Normal export | 100-200 |
| Very large dataset | 200 (maximum) |

## Resources

- `get_task_data_count`: Check data volume before export
- `get_task_scraped_data`: Retrieve actual data as JSON
- `get_task_execution_status`: Verify task is not running
- `search_user_task_list`: Find task ID by name
