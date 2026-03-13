#!/usr/bin/env python3
"""
MCP JSON to Skills Generator

Reads MCP tool descriptors from local mcps folder (JSON files) and generates
AI Skills in the agent-skills format. Supports Octoparse, GitLens, and other
MCP servers that expose tools as JSON descriptor files.

Usage:
    python mcps_to_skills.py [--mcps-dir DIR] [--output-dir DIR]

Examples:
    python mcps_to_skills.py
    python mcps_to_skills.py --mcps-dir ~/.cursor/projects/.../mcps
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

# Default paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# mcps folder: try env, then common Cursor project path
_MCPS_ENV = os.environ.get("MCPS_DIR") or os.environ.get("CURSOR_MCPS_DIR")
DEFAULT_MCPS_DIR = Path(_MCPS_ENV) if _MCPS_ENV else Path.home() / ".cursor" / "projects" / "Users-jiangxiyue-Documents-code-skieer-octorparse-mcp-skills" / "mcps"
DEFAULT_SKILLS_DIR = PROJECT_ROOT / "skills"
DEFAULT_REGISTRY_PATH = PROJECT_ROOT / "registry" / "skills.json"

# Server name mapping (short prefix for skill names)
SERVER_PREFIX = {
    "user-octoparse": "octoparse",
    "user-figma": "figma",
    "user-eamodio.gitlens-extension-GitKraken": "gitlens",
}

# MCP server endpoint URLs
# Multi-region: Octoparse has international (mcp.octoparse.com) and China (mcp.bazhuayu.com)
# Override: OCTOPARSE_MCP_URL (single URL) or OCTOPARSE_MCP_REGION (china|international)
OCTOPARSE_ENDPOINTS = {
    "international": "https://mcp.octoparse.com",
    "china": "https://mcp.bazhuayu.com",
}
OCTOPARSE_DEFAULT_REGION = "international"

SERVER_ENDPOINTS = {
    "user-octoparse": os.environ.get("OCTOPARSE_MCP_URL")
    or OCTOPARSE_ENDPOINTS.get(
        os.environ.get("OCTOPARSE_MCP_REGION", OCTOPARSE_DEFAULT_REGION),
        OCTOPARSE_ENDPOINTS[OCTOPARSE_DEFAULT_REGION],
    ),
    "user-figma": os.environ.get("FIGMA_MCP_URL", ""),
    "user-eamodio.gitlens-extension-GitKraken": os.environ.get("GITLENS_MCP_URL", ""),
}

# Multi-region config for skills (aligns with MCP Registry variables.choices)
SERVER_ENDPOINTS_MULTI = {
    "user-octoparse": {
        "endpoints": OCTOPARSE_ENDPOINTS,
        "defaultRegion": OCTOPARSE_DEFAULT_REGION,
        "regionEnv": "OCTOPARSE_MCP_REGION",
    },
}


def load_server_metadata(mcps_dir: Path, server_id: str) -> dict[str, Any]:
    """Load SERVER_METADATA.json for a server."""
    meta_path = mcps_dir / server_id / "SERVER_METADATA.json"
    if meta_path.exists():
        with open(meta_path, encoding="utf-8") as f:
            return json.load(f)
    return {"serverIdentifier": server_id, "serverName": server_id}


def load_tools_from_server(mcps_dir: Path, server_id: str) -> list[dict[str, Any]]:
    """Load all tool JSON files from a server's tools/ directory."""
    tools_dir = mcps_dir / server_id / "tools"
    if not tools_dir.exists():
        return []

    tools = []
    for path in sorted(tools_dir.glob("*.json")):
        try:
            with open(path, encoding="utf-8") as f:
                tool = json.load(f)
            if isinstance(tool, dict) and "name" in tool:
                tools.append(tool)
        except (json.JSONDecodeError, OSError) as e:
            print(f"  Warning: skip {path.name}: {e}", file=sys.stderr)
    return tools


def to_spec_compliant_name(name: str) -> str:
    """Convert underscore name to agentskills.io compliant (lowercase + hyphens)."""
    return name.replace("_", "-").lower()


def mcp_json_tool_to_skill(
    tool: dict[str, Any],
    server_id: str,
    server_name: str,
    skill_name_prefix: Optional[str] = None,
    spec_compliant: bool = False,
) -> dict[str, Any]:
    """
    Convert MCP JSON tool descriptor to agent-skills format.

    MCP JSON format uses "arguments" (JSON Schema); agent-skills uses "parameters".
    """
    name = tool.get("name", "unknown")
    prefix = skill_name_prefix or SERVER_PREFIX.get(server_id, server_id.replace(".", "_"))
    skill_name = f"{prefix}_{name}" if prefix else name
    if spec_compliant:
        skill_name = to_spec_compliant_name(skill_name)

    description = tool.get("description", "")
    args_schema = tool.get("arguments", {})

    # Map "arguments" to "parameters"
    parameters = {}
    if isinstance(args_schema, dict):
        parameters = {
            "type": args_schema.get("type", "object"),
            "properties": args_schema.get("properties", {}),
            "required": args_schema.get("required", []),
            "additionalProperties": args_schema.get("additionalProperties", False),
        }
        parameters = {k: v for k, v in parameters.items() if v is not None}

    invoke = {
        "type": "mcp",
        "server": server_id,
        "tool": name,
    }
    endpoint = SERVER_ENDPOINTS.get(server_id, "")
    if endpoint:
        invoke["endpoint"] = endpoint
    # Multi-region support (MCP Registry style: variables.choices)
    multi = SERVER_ENDPOINTS_MULTI.get(server_id)
    if multi:
        invoke["endpoints"] = multi["endpoints"]
        invoke["defaultRegion"] = multi["defaultRegion"]
        invoke["regionEnv"] = multi["regionEnv"]

    return {
        "name": skill_name,
        "description": description,
        "parameters": parameters,
        "invoke": invoke,
        "_mcp_tool_name": name,  # Original MCP tool name for invoke
    }


def generate_example_input(parameters: dict[str, Any]) -> dict[str, Any]:
    """Generate example input from parameter schema."""
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
            elif "taskid" in param_name.lower() or "task_id" in param_name.lower():
                example[param_name] = "task_123"
            elif "directory" in param_name.lower():
                example[param_name] = "."
            else:
                example[param_name] = "example_value"
        elif param_type == "integer" or param_type == "number":
            example[param_name] = param_schema.get("default", 1)
        elif param_type == "boolean":
            example[param_name] = param_schema.get("default", False)
        elif param_type == "array":
            if "taskid" in param_name.lower():
                example[param_name] = ["task_123"]
            else:
                example[param_name] = []
        elif param_type == "object":
            example[param_name] = {}
        else:
            example[param_name] = "example_value"

    return example


def _skill_description_for_frontmatter(description: str, max_len: int = 1024) -> str:
    """Extract or truncate description for agentskills.io frontmatter (max 1024 chars)."""
    if not description:
        return "No description available."
    # Prefer first paragraph or first 500 chars as summary
    first = description.split("\n\n")[0].strip()
    if len(first) <= max_len:
        return first
    return first[: max_len - 3] + "..."


def _write_skill_md(
    skill: dict[str, Any],
    skill_dir: Path,
    server_id: str,
) -> None:
    """Write SKILL.md conforming to agentskills.io specification."""
    skill_name = skill["name"]
    params = skill.get("parameters", {})
    properties = params.get("properties", {})
    required = set(params.get("required", []))
    invoke = skill.get("invoke", {})
    full_desc = skill.get("description", "")

    # Frontmatter: spec requires name, description
    inv_type = invoke.get("type", "mcp")
    meta = {"invoke_type": inv_type}
    if inv_type == "mcp":
        meta["server"] = server_id or invoke.get("server", "")
        meta["mcp_tool"] = invoke.get("tool", "")
        if invoke.get("endpoint"):
            meta["endpoint"] = invoke.get("endpoint", "")
        if invoke.get("regionEnv"):
            meta["regionEnv"] = invoke.get("regionEnv", "")
    else:
        meta["endpoint"] = invoke.get("endpoint", "")

    frontmatter = {
        "name": skill_name,
        "description": _skill_description_for_frontmatter(full_desc),
        "license": "MIT",
        "compatibility": "Requires MCP server connection. Compatible with Cursor, Claude Code." if inv_type == "mcp" else "Requires HTTP endpoint. Compatible with agent frameworks.",
        "metadata": meta,
    }

    # Build body
    body_lines = [
        f"# {skill_name}",
        "",
        "## Overview",
        "",
        full_desc if len(full_desc) <= 2000 else full_desc[:2000] + "\n\n...",
        "",
        "## Parameters",
        "",
    ]
    for param_name, param_schema in properties.items():
        if isinstance(param_schema, dict):
            param_type = param_schema.get("type", "string")
            param_desc = param_schema.get("description", "")
            req_marker = " (required)" if param_name in required else ""
            body_lines.append(f"- **{param_name}** (`{param_type}`){req_marker}: {param_desc or 'No description'}")

    body_lines.extend([
        "",
        "## Invoke",
        "",
        f"- **Type**: {invoke.get('type', 'mcp')}",
    ])
    if invoke.get("type") == "mcp":
        body_lines.append(f"- **Server**: {invoke.get('server', '')}")
        body_lines.append(f"- **Tool**: {invoke.get('tool', '')}")
        if invoke.get("endpoints"):
            body_lines.append("")
            body_lines.append("**Multi-region endpoints** (set `OCTOPARSE_MCP_REGION` env):")
            for region, url in invoke.get("endpoints", {}).items():
                body_lines.append(f"- **{region}**: {url}")
            body_lines.append(f"- **Default**: {invoke.get('defaultRegion', 'international')}")
        elif invoke.get("endpoint"):
            body_lines.append(f"- **Endpoint**: {invoke.get('endpoint')}")
    else:
        body_lines.append(f"- **Endpoint**: {invoke.get('endpoint', '')}")
    body_lines.extend([
        "",
        "## Example",
        "",
        "See [example.json](example.json) for sample input.",
    ])

    # Build YAML frontmatter (no pyyaml dependency)
    def yaml_quote(s: str) -> str:
        escaped = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
        return f'"{escaped}"'

    fm_lines = ["---"]
    fm_lines.append(f"name: {skill_name}")
    fm_lines.append(f"description: {yaml_quote(frontmatter['description'])}")
    fm_lines.append(f"license: {frontmatter['license']}")
    fm_lines.append(f"compatibility: {frontmatter['compatibility']}")
    fm_lines.append("metadata:")
    for k, v in frontmatter["metadata"].items():
        vs = str(v) if v else ""
        fm_lines.append(f"  {k}: {yaml_quote(vs)}")
    fm_lines.append("---")
    content = "\n".join(fm_lines) + "\n\n" + "\n".join(body_lines)
    with open(skill_dir / "SKILL.md", "w", encoding="utf-8") as f:
        f.write(content)


def write_skill_folder(
    skill: dict[str, Any],
    output_dir: Path,
    example_input: Optional[dict[str, Any]] = None,
    server_id: Optional[str] = None,
) -> None:
    """Write skill definition to folder: skill.json, SKILL.md, README.md, example.json."""
    skill_name = skill["name"]
    skill_dir = output_dir / skill_name
    skill_dir.mkdir(parents=True, exist_ok=True)

    # Remove internal key before saving skill.json
    skill_for_json = {k: v for k, v in skill.items() if not k.startswith("_")}

    # skill.json
    with open(skill_dir / "skill.json", "w", encoding="utf-8") as f:
        json.dump(skill_for_json, f, indent=2, ensure_ascii=False)

    # SKILL.md (agentskills.io compliant)
    _write_skill_md(skill, skill_dir, server_id or skill.get("invoke", {}).get("server", ""))

    # README.md (kept for backward compatibility, links to SKILL.md)
    params = skill.get("parameters", {})
    properties = params.get("properties", {})
    required = set(params.get("required", []))
    readme_lines = [
        f"# {skill_name}",
        "",
        f"> Full specification: [SKILL.md](SKILL.md) (agentskills.io compliant)",
        "",
        _skill_description_for_frontmatter(skill.get("description", "")),
        "",
        "## Parameters",
        "",
    ]
    for param_name, param_schema in properties.items():
        if isinstance(param_schema, dict):
            param_type = param_schema.get("type", "string")
            param_desc = param_schema.get("description", "")
            req_marker = " (required)" if param_name in required else ""
            readme_lines.append(f"- **{param_name}** ({param_type}){req_marker}: {param_desc or 'No description'}")

    invoke = skill.get("invoke", {})
    readme_lines.extend([
        "",
        "## Invoke",
        "",
        f"- **Type**: {invoke.get('type', 'mcp')}",
        f"- **Server**: {invoke.get('server', '')}",
        f"- **Tool**: {invoke.get('tool', '')}",
    ])
    if invoke.get("endpoints"):
        readme_lines.append("")
        readme_lines.append("**Multi-region** (set `OCTOPARSE_MCP_REGION` env):")
        for region, url in invoke.get("endpoints", {}).items():
            readme_lines.append(f"- **{region}**: {url}")
    elif invoke.get("endpoint"):
        readme_lines.append(f"- **Endpoint**: {invoke.get('endpoint')}")
    with open(skill_dir / "README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(readme_lines))

    # example.json
    example = example_input or generate_example_input(params)
    with open(skill_dir / "example.json", "w", encoding="utf-8") as f:
        json.dump(example, f, indent=2, ensure_ascii=False)


def update_registry(skills: list[dict[str, Any]], registry_path: Path) -> None:
    """Update the skills registry."""
    registry_path.parent.mkdir(parents=True, exist_ok=True)
    registry = {
        "version": "1.0",
        "skills": [
            {
                "name": s["name"],
                "description": (s.get("description", "")[:200] + ("..." if len(s.get("description", "")) > 200 else "")),
                "path": f"skills/{s['name']}",
            }
            for s in skills
        ],
    }
    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convert MCP JSON tool descriptors to AI Skills",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--mcps-dir",
        type=Path,
        default=Path(os.environ.get("MCPS_DIR", str(DEFAULT_MCPS_DIR))),
        help="Path to mcps folder (default: $MCPS_DIR or ~/.cursor/projects/.../mcps)",
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
        help=f"Path to skills registry (default: {DEFAULT_REGISTRY_PATH})",
    )
    parser.add_argument(
        "--merge",
        action="store_true",
        help="Merge with existing skills (keep crawl_page, etc.); default is replace",
    )
    parser.add_argument(
        "--spec-compliant",
        action="store_true",
        help="Use agentskills.io compliant names (hyphens instead of underscores)",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbose output",
    )

    args = parser.parse_args()

    if not args.mcps_dir.exists():
        print(f"Error: mcps directory not found: {args.mcps_dir}", file=sys.stderr)
        return 1

    # Discover servers (directories with tools/)
    # Exclude GitLens - not Octoparse capability
    EXCLUDED_SERVERS = {"user-eamodio.gitlens-extension-GitKraken"}
    servers = [
        d.name
        for d in args.mcps_dir.iterdir()
        if d.is_dir() and (d / "tools").exists() and d.name not in EXCLUDED_SERVERS
    ]

    if not servers:
        print("No MCP servers with tools found.", file=sys.stderr)
        return 1

    if args.verbose:
        print(f"Found servers: {servers}")

    all_skills: list[dict[str, Any]] = []

    # Load existing skills for merge
    existing_skills = {}
    if args.merge and args.registry.exists():
        with open(args.registry, encoding="utf-8") as f:
            reg = json.load(f)
            for s in reg.get("skills", []):
                existing_skills[s["name"]] = s

    for server_id in sorted(servers):
        meta = load_server_metadata(args.mcps_dir, server_id)
        server_name = meta.get("serverName", server_id)
        tools = load_tools_from_server(args.mcps_dir, server_id)

        if args.verbose:
            print(f"  {server_id}: {len(tools)} tools")

        for tool in tools:
            skill = mcp_json_tool_to_skill(
                tool, server_id, server_name, spec_compliant=args.spec_compliant
            )
            all_skills.append(skill)
            example_input = generate_example_input(skill.get("parameters", {}))
            write_skill_folder(
                skill, args.output_dir, example_input, server_id=server_id
            )

    if args.merge and existing_skills:
        # Add back existing skills not from mcps (e.g. crawl_page)
        mcps_skill_names = {s["name"] for s in all_skills}
        for name, s in existing_skills.items():
            if name not in mcps_skill_names:
                all_skills.append({"name": name, "description": s.get("description", ""), "path": s.get("path", "")})
        # Re-sort: existing first, then new
        existing_names = set(existing_skills)
        all_skills.sort(key=lambda x: (0 if x["name"] in existing_names else 1, x["name"]))

    update_registry(all_skills, args.registry)

    # Add or update SKILL.md for any skill that has skill.json
    for skill_dir in args.output_dir.iterdir():
        if skill_dir.is_dir():
            has_json = (skill_dir / "skill.json").exists()
            if has_json:
                try:
                    with open(skill_dir / "skill.json", encoding="utf-8") as f:
                        s = json.load(f)
                    server = s.get("invoke", {}).get("server", "")
                    _write_skill_md(s, skill_dir, server)
                    if args.verbose:
                        print(f"  Updated SKILL.md for {skill_dir.name}")
                except Exception as e:
                    print(f"  Warning: could not add SKILL.md to {skill_dir.name}: {e}", file=sys.stderr)

    if args.verbose:
        print(f"Updated registry: {args.registry}")
    print(f"Successfully generated {len(all_skills)} skills to {args.output_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
