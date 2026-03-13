#!/bin/bash
# Example: Run the MCP to Skills generator
#
# Prerequisites:
#   - MCP server accessible (default: https://mcp.octoparse.com)
#   - Python 3.9+ with requirements installed: pip install -r requirements.txt
#
# Usage:
#   ./run_generator.sh
#   MCP_URL=https://your-mcp-server.com ./run_generator.sh
#   MCP_AUTH_TOKEN="Bearer xxx" ./run_generator.sh

set -e
cd "$(dirname "$0")/.."

echo "agent-skills: Running MCP to Skills Generator"
echo "=============================================="

# Default MCP URL: use OCTOPARSE_MCP_REGION (china|international) or MCP_URL
# international: mcp.octoparse.com, china: mcp.bazhuayu.com
if [ -z "$MCP_URL" ]; then
  case "${OCTOPARSE_MCP_REGION:-international}" in
    china) export MCP_URL="https://mcp.bazhuayu.com" ;;
    *)    export MCP_URL="https://mcp.octoparse.com" ;;
  esac
fi

echo "MCP URL: $MCP_URL"
echo ""

python generator/mcp_to_skills.py --verbose

echo ""
echo "Done! Skills are in skills/"
echo "Registry updated at registry/skills.json"
