#!/bin/bash
# Run the MCP JSON to Skills generator (reads from local mcps folder)
#
# Prerequisites:
#   - Python 3.9+
#   - mcps folder with tool JSON descriptors (default: ~/.cursor/projects/.../mcps)
#
# Usage:
#   ./run_mcps_generator.sh
#   MCPS_DIR=/path/to/mcps ./run_mcps_generator.sh
#   ./run_mcps_generator.sh --merge   # Merge with existing skills (crawl_page, etc.)

set -e
cd "$(dirname "$0")/.."

echo "agent-skills: Running MCP JSON to Skills Generator"
echo "===================================================="

# MCPS_DIR can be set to override default
MCPS_DIR="${MCPS_DIR:-$HOME/.cursor/projects/Users-jiangxiyue-Documents-code-skieer-octorparse-mcp-skills/mcps}"
echo "MCPS dir: $MCPS_DIR"
echo ""

python3 generator/mcps_to_skills.py --merge --verbose

echo ""
echo "Done! Skills are in skills/"
echo "Registry updated at registry/skills.json"
