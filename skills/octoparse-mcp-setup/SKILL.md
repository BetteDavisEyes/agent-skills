---
name: octoparse-mcp-setup
description: Configure and authorize the Octoparse MCP server. Use when the Octoparse MCP server is not configured or needs authorization. Handles OAuth 2.1 dynamic client registration and connection setup for all Octoparse skills.
---

## Overview

This skill handles the one-time setup required for all Octoparse skills. It configures the MCP server and completes OAuth 2.1 authorization with dynamic client registration.

## When to use

Use this skill when:
- Octoparse MCP server is not detected in the system
- User receives "MCP server not found" or connection errors
- Authorization is required before using Octoparse tools
- Any Octoparse skill fails due to missing MCP configuration

## Instructions

### Auto-Configuration Workflow

When this skill is triggered, follow these steps:

#### Step 1: Check Current MCP Status

First, verify if Octoparse MCP server is already configured:
- Check if `octoparse` MCP server exists in the system
- If already configured and authorized, inform user and exit

#### Step 2: Add MCP Server Configuration

If Octoparse MCP is not configured:

1. **Add the MCP server** using the appropriate configuration method:
   ```json
   {
     "mcpServers": {
       "octoparse": {
         "url": "https://mcp.octoparse.com"
       }
     }
   }
   ```

2. **Re-initialize the MCP connection** to apply the new configuration

3. **Confirm addition** - Verify the server now appears in the MCP server list

#### Step 3: OAuth 2.1 Authorization (Dynamic Client Registration)

**CRITICAL: Authorization must be completed before using any Octoparse tools.**

After MCP server configuration:

1. **Initiate authorization flow**:
   - Execute the `/mcp` command to open the MCP server selection menu
   - Instruct the user to select the "octoparse" server from the list

2. **Guide through OAuth flow**:
   - The system will automatically handle dynamic client registration
   - If a browser window opens, instruct the user to complete login in the browser
   - Wait for the authorization callback to complete

3. **Verify authorization**:
   - Attempt to call `get_user_account_info()` to confirm connection is working
   - If successful, authorization is complete

4. **Handle failures**:
   - If authorization fails, report the specific error
   - Do not proceed until authorization succeeds

### Completion Confirmation

Once setup is complete:
1. Confirm: "Octoparse MCP server is now configured and authorized"
2. Inform user they can now use other Octoparse skills
3. If this was triggered by another skill, signal that the original request can proceed

## Configuration Reference

### Required MCP Server

| Service | URL | Protocol |
|---------|-----|----------|
| Octoparse | `https://mcp.octoparse.com` | OAuth 2.1 with Dynamic Client Registration |

### Authorization Details

- **Protocol**: OAuth 2.1
- **Client Registration**: Dynamic (automatic)
- **User Action Required**: Browser login to Octoparse account
- **Scope**: Full Octoparse API access

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Cannot connect to MCP server" | Verify URL is correct: `https://mcp.octoparse.com` |
| "Authorization timeout" | Ask user to check browser and complete login |
| "Dynamic registration failed" | Retry authorization flow from Step 3 |
| "Already authorized" | Skip authorization, configuration is complete |

## Integration with Other Skills

This skill is a prerequisite for all Octoparse skills:
- `octoparse-template-task` - Creating scraping tasks
- `octoparse-task-control` - Starting/stopping tasks
- `octoparse-data-export` - Retrieving scraped data
- `octoparse-task-management` - Managing tasks and groups

**Other skills should check for MCP configuration and trigger this skill if missing.**
