"""
Skill loader for AI Agents.

Loads skill definitions from the skills directory and registry.
Supports multi-region endpoint resolution (OCTOPARSE_MCP_REGION=china|international).
"""

import json
import os
from pathlib import Path
from typing import Any, Optional

# Default paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SKILLS_DIR = PROJECT_ROOT / "skills"
DEFAULT_REGISTRY_PATH = PROJECT_ROOT / "registry" / "skills.json"


def get_invoke_endpoint(skill: dict[str, Any]) -> Optional[str]:
    """
    Resolve the MCP endpoint for a skill, supporting multi-region.

    Priority:
    1. OCTOPARSE_MCP_URL (or server-specific env) - explicit URL override
    2. OCTOPARSE_MCP_REGION - region choice (china | international)
    3. invoke.endpoint - default from skill definition

    Returns:
        The resolved endpoint URL, or None if not applicable.
    """
    invoke = skill.get("invoke", {})
    if invoke.get("type") != "mcp":
        return invoke.get("endpoint")

    server = invoke.get("server", "")
    region_env = invoke.get("regionEnv", "")
    endpoints = invoke.get("endpoints", {})
    default_region = invoke.get("defaultRegion", "international")

    # Explicit URL override (e.g. OCTOPARSE_MCP_URL)
    url_env_map = {"user-octoparse": "OCTOPARSE_MCP_URL"}
    url_env = url_env_map.get(server, "MCP_URL")
    explicit_url = os.environ.get(url_env)
    if explicit_url:
        return explicit_url

    # Region-based selection
    if endpoints and region_env:
        region = os.environ.get(region_env, default_region)
        return endpoints.get(region, endpoints.get(default_region, invoke.get("endpoint")))

    return invoke.get("endpoint")


def load_skill(skill_name: str, skills_dir: Optional[Path] = None) -> dict[str, Any]:
    """
    Load a skill definition by name.

    Args:
        skill_name: Name of the skill (e.g., 'crawl_page')
        skills_dir: Base directory for skills (default: project skills/)

    Returns:
        Skill schema dict with name, description, parameters, invoke

    Raises:
        FileNotFoundError: If skill does not exist
    """
    base = skills_dir or DEFAULT_SKILLS_DIR
    skill_path = base / skill_name / "skill.json"
    if not skill_path.exists():
        raise FileNotFoundError(f"Skill not found: {skill_name} at {skill_path}")

    with open(skill_path, encoding="utf-8") as f:
        skill = json.load(f)
    # Resolve endpoint for multi-region support
    endpoint = get_invoke_endpoint(skill)
    if endpoint and skill.get("invoke"):
        skill["invoke"] = {**skill["invoke"], "endpoint": endpoint}
    return skill


def load_skill_example(skill_name: str, skills_dir: Optional[Path] = None) -> dict[str, Any]:
    """Load example input for a skill."""
    base = skills_dir or DEFAULT_SKILLS_DIR
    example_path = base / skill_name / "example.json"
    if not example_path.exists():
        return {}

    with open(example_path, encoding="utf-8") as f:
        return json.load(f)


def load_registry(registry_path: Optional[Path] = None) -> dict[str, Any]:
    """
    Load the skills registry.

    Returns:
        Registry dict with version and skills list
    """
    path = registry_path or DEFAULT_REGISTRY_PATH
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def list_skills(registry_path: Optional[Path] = None) -> list[dict[str, Any]]:
    """
    List all available skills from the registry.

    Returns:
        List of skill metadata dicts (name, description, path)
    """
    registry = load_registry(registry_path)
    return registry.get("skills", [])
