---
name: octoparse-template-task
description: Create web scraping tasks using Octoparse's pre-defined templates. Handles multi-step workflows, parameter synchronization, and error self-correction. **IMPORTANT**: Requires Octoparse MCP server. If not configured or authorized, use `octoparse-mcp-setup` skill first.
---

## Overview

This skill enables the creation of complex web scraping tasks using Octoparse's pre-defined templates. It handles multi-step workflows, parameter synchronization between UI and backend, and provides error self-correction capabilities.

## When to use

Use this skill when the user wants to:
- Create a new web scraping task
- Use a template to scrape a specific platform (Amazon, eBay, etc.)
- Set up a scraper for a website
- "Create a scraper for X"
- "I need to get data from Y using a template"

## Instructions

### Pre-Flight Check: MCP Server Configuration (MANDATORY)

**Before using any Octoparse tools**, verify the MCP server is configured:

1. **Check if Octoparse MCP server exists** in the system
2. **If not configured**:
   - STOP the current workflow
   - **Check if `octoparse-mcp-setup` skill exists**:
     - If YES: Inform the user: "Octoparse MCP server needs to be configured first. Please use the `octoparse-mcp-setup` skill to complete the setup and authorization."
     - If NO: "The `octoparse-mcp-setup` skill is not installed. Downloading from GitHub..." → Download from `https://github.com/octoparse/agent-skills/tree/main/skills/octoparse-mcp-setup` and install
   - Do NOT proceed until configuration is complete
3. **If configured but tools fail**: The server may need authorization - direct user to `octoparse-mcp-setup`

### Stage 1: Template Discovery (MANDATORY)

NEVER create a task blindly. Always follow this protocol:

1. **Search Templates**: Call `search_octoparse_templates(keyword: "platform")`
   - Use the exact platform name (e.g., "Amazon", "eBay", "LinkedIn")
   - Read the `enDescription` to ensure it matches user needs
   - Note the `templateId`, `accountLimit`, and `runOn` properties

2. **Verify Compatibility**: Check user's account level
   - Call `get_user_account_info()` to get `currentAccountLevel`
   - Ensure user's level meets template's `accountLimit`
   - Warn user if upgrade is needed

### Stage 2: Schema Inspection

Call `get_template_details_by_id(templateId: ID)` to get:
- **prompts field**: Contains the "Instruction Manual" for this template
- **parameters list**: All required and optional parameters
- For each parameter, note:
  - `Id`: UI identifier
  - `ParamName`: Backend identifier
  - `ControlType`: Determines value format
  - `IsRequired`: Whether parameter is mandatory

### Stage 3: Parameter Analysis

**ControlType determines value format:**

| ControlType | Value Format | Example |
|-------------|--------------|---------|
| `MultiInput` | Array of strings | `["keyword1", "keyword2"]` |
| `TextInput` | String | `"search term"` |
| `NumberInput` | Number | `100` |
| `Checkbox` | Boolean | `true` |

**CRITICAL**: Even single values for MultiInput must be arrays: `["value"]` NOT `"value"`

### Stage 4: The "Double-Array" Synchronization Rule

Octoparse tasks FAIL if parameters aren't perfectly mirrored. Construct `userInputParameters` with:

```json
{
  "UIParameters": [
    {"Id": "param-id-1", "Value": ["keyword1"]},
    {"Id": "param-id-2", "Value": 100}
  ],
  "TemplateParameters": [
    {"ParamName": "SearchKeyword", "Value": ["keyword1"]},
    {"ParamName": "MaxPages", "Value": 100}
  ]
}
```

**Mapping Requirement**: For every parameter:
1. Find its `Id` (for UIParameters) and `ParamName` (for TemplateParameters)
2. Assign the SAME value to both
3. If one exists in UIParameters, its twin MUST exist in TemplateParameters

### Stage 5: Task Creation

Call `create_task_from_template` with:
- `templateId`: From Stage 1
- `taskName`: Descriptive name (ask user if not provided)
- `taskGroupId`: Optional - get from `get_user_task_groups()`
- `userInputParameters`: Properly constructed from Stage 4

## Error Self-Correction

| Error Message | Cause | Solution |
|---------------|-------|----------|
| "Parameter Mismatch" | Missing twin in one array | Re-scan schema, ensure both arrays have all parameters |
| "Invalid Format" | String passed to MultiInput | Wrap in array: `"value"` → `["value"]` |
| "Account Level Too Low" | Template requires higher tier | Check `accountLimit` vs user's level, suggest upgrade |
| "UIParameters is required" | Forgot to include UIParameters | Both arrays are mandatory |

## Example Workflow

**User**: "Create an Amazon scraper for 'mechanical keyboards'"

1. **Search**: `search_octoparse_templates(keyword: "Amazon")` → ID 293
2. **Inspect**: `get_template_details_by_id(templateId: 293)` → `MainKeys` (Id: "p-1", ControlType: "MultiInput")
3. **Analyze**: `MainKeys` is MultiInput, so value must be `["mechanical keyboards"]`
4. **Execute**:
```json
{
  "templateId": 293,
  "taskName": "Amazon - Mechanical Keyboards",
  "userInputParameters": {
    "UIParameters": [{"Id": "p-1", "Value": ["mechanical keyboards"]}],
    "TemplateParameters": [{"ParamName": "MainKeys", "Value": ["mechanical keyboards"]}]
  }
}
```

## Resources

- `search_octoparse_templates`: Find templates by keyword
- `get_template_details_by_id`: Get template schema and parameters
- `create_task_from_template`: Execute task creation
- `get_user_account_info`: Verify account level
- `get_user_task_groups`: Get available task groups for organization
