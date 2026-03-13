---
name: octoparse_get_user_account_info
description: "Retrieves comprehensive account information for the authenticated Octoparse user, including account level, subscription status, balances, and binding accounts."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "get_user_account_info"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_get_user_account_info

## Overview

Retrieves comprehensive account information for the authenticated Octoparse user, including account level, subscription status, balances, and binding accounts.

[When to use]:
- MUST call when user asks "who am I", "my account", "my info", "my subscription", "my balance"
- Call as the FIRST step when user needs to verify their authentication status
- Call when user asks about account limits, permissions, or subscription details
- Call before operations that depend on account level (e.g., checking if user can create template tasks)

[When NOT to use]:
- DO NOT call repeatedly in the same conversation - cache the result
- DO NOT call if user is asking about task information (use getTaskInfoById instead)
- DO NOT call if user is asking about templates (use searchTemplates instead)

[Important Notes]:
- This tool requires authentication. If user is not authenticated, guide them to authenticate first.
- Account information includes sensitive data (masked email, balance) - handle with care
- The account level determines user permissions: Free(1), Basic(9), Standard(2), Professional(3), Enterprise(31), Enterprise Plus(4)
- If subscribe=false, subscription fields (packageKey, nextBillingDate) will be empty

[Key Field Descriptions]:
- googleAccount: Bound Google Account - Email address of the bound Google account
- microsoftAccount: Bound Microsoft Account - Email address of the bound Microsoft account
- appleAccount: Apple Account - Email address of the bound Apple account
- accountLevel: Account Level - Raw account level without validity check (1:Free;9:Basic;2:Standard;3:Professional;31:Enterprise;4:Enterprise Plus;110:Personal;120:Group;130:Business;140:BusinessMember)
- currentAccountLevel: Current Account Level - Current account level with validity check, shows Free if expired (1:Free;9:Basic;2:Standard;3:Professional;31:Enterprise;4:Enterprise Plus;110:Personal;120:Group;130:Business;140:BusinessMember)
- levelEffectivePeriod: Level Effective Period - Expiration date

...

## Parameters


## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: get_user_account_info

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.