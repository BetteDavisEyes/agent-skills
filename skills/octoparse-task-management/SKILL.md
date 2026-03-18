---
name: octoparse-task-management
description: Navigate and audit the Octoparse workspace. Find tasks, understand their configuration, and organize them via groups.
---

## Overview

This skill provides a structured approach to finding tasks, understanding their configuration, and organizing them via task groups. It uses progressive discovery for ambiguous queries.

## When to use

Use this skill when the user wants to:
- Find a specific task they created
- List all their tasks
- Check task configuration or details
- Browse task groups/folders
- "Find my Amazon scraper"
- "Show me all tasks in the E-commerce group"
- "What's the ID of my eBay task?"
- "I can't find my task"

## Instructions

### Progressive Discovery Strategy

User queries are often vague. Apply this logic:

1. **Initial Search**: Call `search_user_task_list(keyWord: "query")`
   - If no exact match, try broader keywords
   - Use platform names ("Amazon", "eBay") or partial task names

2. **Ambiguity Resolution**: If multiple tasks return:
   - Present concise list with IDs and status
   - Ask for clarification OR proceed with most relevant if context is clear

3. **Deep Dive**: Once `taskId` is identified:
   - Call `get_task_detailed_info(taskId: ID)` for full context
   - Get template used, creation date, parameters, task group

### Organizational Context (Groups)

Octoparse uses folder-like structure called **Task Groups**:
- Before suggesting new task organization, call `get_user_task_groups()`
- If user mentions "folder" or "category", they mean `taskGroupId`
- Display group names when showing task lists for better context

### Precision Requirements

- ALWAYS use exact `taskId` (alphanumeric string) for downstream operations
- When displaying task lists, include:
  - Task name
  - Task ID
  - Status (Running/Stopped/Completed/Failed)
  - Group name (if available)

### Common Workflows

#### Finding a Lost Task

1. Try keyword search with platform name: `search_user_task_list(keyWord: "amazon")`
2. Try partial name match: `search_user_task_list(keyWord: "scraper")`
3. List all tasks if needed: `search_user_task_list()`
4. Once found, get detailed info: `get_task_detailed_info(taskId: "found-id")`

#### Auditing Task Configuration

1. Get task details: `get_task_detailed_info(taskId: ID)`
2. Examine:
   - `templateId`: Which template is used
   - `userInputParameters`: Current parameter values
   - `taskGroupId`: Where task is organized
   - `templateVersion`: Template version being used
3. Report configuration summary to user

#### Organizing Tasks

1. Get available groups: `get_user_task_groups()`
2. Present options to user with task counts
3. Use appropriate `taskGroupId` for task creation or updates

## Example Interactions

**User**: "I can't find my eBay scraper. What's its ID?"

1. `search_user_task_list(keyWord: "ebay")`
2. Find "eBay Product Scraper v2" with ID `task-abc-123`
3. Report: "Found it! The ID for 'eBay Product Scraper v2' is `task-abc-123` (Status: Stopped)"

**User**: "Show me all my tasks"

1. `search_user_task_list(pageSize: 50)` - get first page
2. If more tasks exist, ask if user wants to see all
3. Present formatted list with name, ID, status, group

**User**: "What's in my Retail group?"

1. `get_user_task_groups()` - find Retail group ID
2. `search_user_task_list(taskGroup: "retail-group-id")`
3. Present tasks in that group

## Resources

- `search_user_task_list`: Primary entry point for finding tasks
- `get_task_detailed_info`: Get full task configuration
- `get_user_task_groups`: Get workspace structure
