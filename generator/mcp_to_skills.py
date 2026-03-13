#!/usr/bin/env python3
"""
MCP to Skills Generator

Automatically converts MCP (Model Context Protocol) tools into AI Skills
that can be discovered and used by AI Agents.

Usage:
    python mcp_to_skills.py [--mcp-url URL] [--output-dir DIR] [--auth-token TOKEN]

Examples:
    python mcp_to_skills.py --mcp-url https://mcp.octoparse.com
    python mcp_to_skills.py --mcp-url https://mcp.example.com --auth-token "Bearer xxx"
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

import requests

# Default paths relative to project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SKILLS_DIR = PROJECT_ROOT / "skills"
DEFAULT_REGISTRY_PATH = PROJECT_ROOT / "registry" / "skills.json"


def fetch_mcp_tools(
    mcp_url: str,
    auth_token: Optional[str] = None,
    session_id: Optional[str] = None,
    timeout: int = 30,
) -> list[dict[str, Any]]:
    """
    Fetch tool list from MCP server via tools/list JSON-RPC endpoint.

    MCP uses JSON-RPC 2.0 over HTTP POST. The tools/list method returns
    all available tools with their schemas.

    Args:
        mcp_url: Base URL of the MCP server (e.g., https://mcp.octoparse.com)
        auth_token: Optional Bearer token for authentication
        session_id: Optional MCP session ID for stateful servers
        timeout: Request timeout in seconds

    Returns:
        List of tool definitions from the MCP server

    Raises:
        requests.RequestException: On network errors
        ValueError: If response format is invalid
    """
    url = mcp_url.rstrip("/")
    headers = {
        "Content-Type": "application/json",
    }
    if auth_token:
        headers["Authorization"] = auth_token if auth_token.startswith("Bearer ") else f"Bearer {auth_token}"
    if session_id:
        headers["Mcp-Session-Id"] = session_id

    payload = {
        "jsonrpc": "2.0",
        "id": "mcp-to-skills-generator",
        "method": "tools/list",
        "params": {},
    }

    response = requests.post(url, json=payload, headers=headers, timeout=timeout)
    response.raise_for_status()

    data = response.json()
    if "error" in data:
        raise ValueError(f"MCP server error: {data['error']}")

    result = data.get("result", {})
    tools = result.get("tools", [])

    if not isinstance(tools, list):
        raise ValueError(f"Expected tools list, got: {type(tools)}")

    return tools


def mcp_tool_to_skill(
    tool: dict[str, Any],
    mcp_url: str,
    skill_name: Optional[str] = None,
) -> dict[str, Any]:
    """
    Convert an MCP tool definition to a Skill schema.

    Args:
        tool: MCP tool definition (name, description, inputSchema)
        mcp_url: Base URL of the MCP server for invoke endpoint
        skill_name: Override skill name (default: use tool name)

    Returns:
        Skill schema conforming to the agent-skills format
    """
    name = skill_name or tool.get("name", "unknown")
    description = tool.get("description", "")
    input_schema = tool.get("inputSchema", {})

    # Extract parameters from MCP inputSchema (JSON Schema format)
    # MCP uses inputSchema with properties, required, etc.
    parameters = {}
    if isinstance(input_schema, dict):
        parameters = {
            "type": input_schema.get("type", "object"),
            "properties": input_schema.get("properties", {}),
            "required": input_schema.get("required", []),
            "additionalProperties": input_schema.get("additionalProperties", False),
        }
        # Remove empty/None values for cleaner output
        parameters = {k: v for k, v in parameters.items() if v is not None}

    base_url = mcp_url.rstrip("/")
    # MCP tools are invoked via tools/call - the endpoint is the MCP server URL
    invoke_endpoint = base_url

    return {
        "name": name,
        "description": description,
        "parameters": parameters,
        "invoke": {
            "type": "http",
            "endpoint": invoke_endpoint,
            "method": "tools/call",
        },
    }


def generate_example_input(parameters: dict[str, Any]) -> dict[str, Any]:
    """
    Generate example input from parameter schema.

    Creates placeholder values based on JSON Schema types.
    """
    example = {}
    properties = parameters.get("properties", {})
    required = set(parameters.get("required", []))

    for param_name, param_schema in properties.items():
        if not isinstance(param_schema, dict):
            continue

        param_type = param_schema.get("type", "string")
        param_desc = param_schema.get("description", "")

        if param_type == "string":
            if "url" in param_name.lower() or "url" in param_desc.lower():
                example[param_name] = "https://example.com"
            elif "keyword" in param_name.lower():
                example[param_name] = "example keyword"
            else:
                example[param_name] = "example_value"
        elif param_type == "integer" or param_type == "number":
            example[param_name] = param_schema.get("default", 1)
        elif param_type == "boolean":
            example[param_name] = param_schema.get("default", False)
        elif param_type == "array":
            example[param_name] = []
        elif param_type == "object":
            example[param_name] = {}
        else:
            example[param_name] = "example_value"

    return example


def write_skill_folder(
    skill: dict[str, Any],
    output_dir: Path,
    example_input: Optional[dict[str, Any]] = None,
) -> None:
    """
    Write skill definition to a folder under output_dir.

    Creates: {output_dir}/{skill_name}/skill.json, README.md, example.json
    """
    skill_name = skill["name"]
    skill_dir = output_dir / skill_name
    skill_dir.mkdir(parents=True, exist_ok=True)

    # skill.json - full schema
    skill_file = skill_dir / "skill.json"
    with open(skill_file, "w", encoding="utf-8") as f:
        json.dump(skill, f, indent=2, ensure_ascii=False)

    # README.md - human-readable description
    readme_content = f"""# {skill_name}

{skill.get("description", "No description available.")}

## Parameters

"""
    params = skill.get("parameters", {})
    properties = params.get("properties", {})
    required = set(params.get("required", []))

    for param_name, param_schema in properties.items():
        if isinstance(param_schema, dict):
            param_type = param_schema.get("type", "string")
            param_desc = param_schema.get("description", "")
            required_marker = " (required)" if param_name in required else ""
            readme_content += f"- **{param_name}** ({param_type}){required_marker}: {param_desc or 'No description'}\n"

    readme_content += f"""
## Invoke

- **Type**: {skill.get("invoke", {}).get("type", "mcp")}
- **Endpoint**: {skill.get("invoke", {}).get("endpoint", "")}
- **Method**: {skill.get("invoke", {}).get("method", "tools/call")}
"""

    readme_file = skill_dir / "README.md"
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(readme_content)

    # example.json - example input
    example = example_input or generate_example_input(params)
    example_file = skill_dir / "example.json"
    with open(example_file, "w", encoding="utf-8") as f:
        json.dump(example, f, indent=2, ensure_ascii=False)


def update_registry(skills: list[dict[str, Any]], registry_path: Path) -> None:
    """Update the skills registry file with all generated skills."""
    registry_path.parent.mkdir(parents=True, exist_ok=True)

    registry = {
        "version": "1.0",
        "skills": [
            {
                "name": s["name"],
                "description": s.get("description", "")[:200] + ("..." if len(s.get("description", "")) > 200 else ""),
                "path": f"skills/{s['name']}",
            }
            for s in skills
        ],
    }

    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert MCP tools to AI Skills",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    _default = (
        os.environ.get("MCP_URL")
        or ("https://mcp.bazhuayu.com" if os.environ.get("OCTOPARSE_MCP_REGION") == "china" else "https://mcp.octoparse.com")
    )
    parser.add_argument(
        "--mcp-url",
        default=_default,
        help="MCP server URL (default: $MCP_URL, or $OCTOPARSE_MCP_REGION=china for China)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_SKILLS_DIR,
        help=f"Output directory for skills (default: {DEFAULT_SKILLS_DIR})",
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=DEFAULT_REGISTRY_PATH,
        help=f"Path to skills registry JSON (default: {DEFAULT_REGISTRY_PATH})",
    )
    parser.add_argument(
        "--auth-token",
        default=os.environ.get("MCP_AUTH_TOKEN"),
        help="Bearer token for MCP authentication (or $MCP_AUTH_TOKEN)",
    )
    parser.add_argument(
        "--session-id",
        default=os.environ.get("MCP_SESSION_ID"),
        help="MCP session ID for stateful servers (or $MCP_SESSION_ID)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds (default: 30)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    try:
        if args.verbose:
            print(f"Fetching tools from {args.mcp_url}...")

        tools = fetch_mcp_tools(
            mcp_url=args.mcp_url,
            auth_token=args.auth_token,
            session_id=args.session_id,
            timeout=args.timeout,
        )

        if args.verbose:
            print(f"Found {len(tools)} tools")

        skills = []
        for tool in tools:
            skill = mcp_tool_to_skill(tool, args.mcp_url)
            skills.append(skill)
            example_input = generate_example_input(skill.get("parameters", {}))
            write_skill_folder(skill, args.output_dir, example_input)
            if args.verbose:
                print(f"  Generated skill: {skill['name']}")

        update_registry(skills, args.registry)
        if args.verbose:
            print(f"Updated registry: {args.registry}")

        print(f"Successfully generated {len(skills)} skills to {args.output_dir}")
        return 0

    except requests.RequestException as e:
        print(f"Error fetching MCP tools: {e}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        if args.verbose:
            raise
        return 1


if __name__ == "__main__":
    sys.exit(main())
