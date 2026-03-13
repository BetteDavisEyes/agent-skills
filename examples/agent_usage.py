#!/usr/bin/env python3
"""
Example: How AI Agents can use agent-skills

This example demonstrates:
1. Discovering available skills from the registry
2. Loading a skill definition
3. Invoking a skill via MCP/HTTP (conceptual - actual call depends on your agent framework)
"""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sdk import load_skill, load_registry, list_skills


def discover_skills():
    """Discover all available skills from the registry."""
    print("=== Discovering Skills ===\n")
    skills = list_skills()
    for skill in skills:
        desc = skill.get("description", "")[:80]
        print(f"  • {skill['name']}: {desc}{'...' if len(skill.get('description', '')) > 80 else ''}")
    return skills


def load_and_inspect_skill(skill_name: str):
    """Load a skill and show its schema for agent tool binding."""
    print(f"\n=== Loading Skill: {skill_name} ===\n")
    skill = load_skill(skill_name)
    print(f"Name: {skill['name']}")
    print(f"Description: {skill['description'][:200]}...")
    print(f"\nParameters (JSON Schema):")
    import json
    print(json.dumps(skill.get("parameters", {}), indent=2))
    print(f"\nInvoke: {skill.get('invoke', {})}")
    return skill


def build_agent_tool_schema(skill_name: str):
    """
    Convert a skill to OpenAI/Anthropic tool format for agent use.

    Most LLM agent frameworks expect tools in a specific format.
    This shows how to map skill schema to that format.
    """
    skill = load_skill(skill_name)
    # OpenAI/Anthropic tool format
    return {
        "type": "function",
        "function": {
            "name": skill["name"],
            "description": skill["description"],
            "parameters": skill.get("parameters", {}),
        },
    }


def main():
    print("agent-skills: Example Usage for AI Agents\n")
    print("=" * 50)

    # 1. Discover skills
    skills = discover_skills()
    if not skills:
        print("No skills found. Run the generator first.")
        return

    # 2. Load and inspect a specific skill (Octoparse)
    load_and_inspect_skill("octoparse_get_task_scraped_data")

    # 3. Build tool schema for agent
    print("\n=== Agent Tool Schema (OpenAI/Anthropic format) ===\n")
    tool_schema = build_agent_tool_schema("octoparse_get_task_scraped_data")
    import json
    print(json.dumps(tool_schema, indent=2))

    print("\n" + "=" * 50)
    print("To invoke a skill, the agent would:")
    print("  1. Call the MCP server at skill['invoke']['endpoint']")
    print("  2. Use method 'tools/call' with params.name = skill['invoke']['tool']")
    print("  3. Parse the JSON-RPC response")


if __name__ == "__main__":
    main()
