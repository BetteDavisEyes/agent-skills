---
name: octoparse_greet_user_and_introduce_octoparse
description: "Provides a warm greeting and comprehensive introduction to the Octoparse MCP Server capabilities."
license: MIT
compatibility: Requires MCP server connection. Compatible with Cursor, Claude Code.
metadata:
  invoke_type: "mcp"
  server: "user-octoparse"
  mcp_tool: "greet_user_and_introduce_octoparse"
  endpoint: "https://mcp.octoparse.com"
  regionEnv: "OCTOPARSE_MCP_REGION"
---

# octoparse_greet_user_and_introduce_octoparse

## Overview

Provides a warm greeting and comprehensive introduction to the Octoparse MCP Server capabilities.

[When to use]:
- MUST call when user explicitly greets (e.g., "hello", "hi octoparse", "what can you do")
- MUST call when user asks "what is this", "tell me about octoparse", or similar introductory questions
- Call as the FIRST interaction when user starts a new session without a specific task

[When NOT to use]:
- DO NOT call if user has a specific task request (e.g., "start task 123", "get my info")
- DO NOT call in the middle of an ongoing operation
- DO NOT call repeatedly in the same conversation

[Examples]:
User: "Hello Octoparse!"
-> Call greet_user_and_introduce_octoparse()

User: "What can this server do?"
-> Call greet_user_and_introduce_octoparse()

User: "Start task 456"
-> DO NOT call this tool, call startCloudTask instead

## Parameters


## Invoke

- **Type**: mcp
- **Server**: user-octoparse
- **Tool**: greet_user_and_introduce_octoparse

**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):
- **international**: https://mcp.octoparse.com
- **china**: https://mcp.bazhuayu.com
- **Default**: international

## Example

See [example.json](example.json) for sample input.