#!/usr/bin/env python3
"""
Validate skills against agentskills.io specification.

Checks:
- SKILL.md exists with valid YAML frontmatter
- name: 1-64 chars, lowercase + hyphens only, matches directory
- description: 1-1024 chars, non-empty
- Optional fields: license, metadata, compatibility
"""

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SKILLS_DIR = PROJECT_ROOT / "skills"

NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NAME_MAX = 64
DESC_MAX = 1024


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Extract YAML frontmatter from SKILL.md. Returns (frontmatter_dict, body)."""
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    # Naive YAML parse for simple key: value
    fm = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line and not line.strip().startswith("#"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip("'\"").replace('\\"', '"').replace("\\n", "\n")
    return fm, parts[2].lstrip()


def validate_skill(skill_dir: Path, strict: bool = False) -> list[str]:
    """Validate a single skill. Returns list of error messages.
    strict: require agentskills.io name format (hyphens only)."""
    errors = []
    name = skill_dir.name

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing SKILL.md")
        return errors

    content = skill_md.read_text(encoding="utf-8")
    frontmatter, _ = parse_frontmatter(content)

    # name
    fm_name = frontmatter.get("name", "")
    if not fm_name:
        errors.append("Frontmatter missing 'name'")
    elif len(fm_name) > NAME_MAX:
        errors.append(f"name exceeds {NAME_MAX} chars")
    elif strict and not NAME_PATTERN.match(fm_name):
        errors.append("name must be lowercase letters, numbers, hyphens only (use --spec-compliant when generating)")
    elif fm_name != name:
        errors.append(f"name '{fm_name}' does not match directory '{name}'")

    # description
    desc = frontmatter.get("description", "")
    if not desc:
        errors.append("Frontmatter missing or empty 'description'")
    elif len(desc) > DESC_MAX:
        errors.append(f"description exceeds {DESC_MAX} chars")

    # skill.json exists
    if not (skill_dir / "skill.json").exists():
        errors.append("Missing skill.json")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate skills against agentskills.io spec")
    parser.add_argument("--skills-dir", type=Path, default=DEFAULT_SKILLS_DIR)
    parser.add_argument("-q", "--quiet", action="store_true", help="Only print failures")
    parser.add_argument("--strict", action="store_true", help="Require agentskills.io name format (hyphens only)")
    args = parser.parse_args()

    if not args.skills_dir.exists():
        print(f"Error: {args.skills_dir} not found", file=sys.stderr)
        return 1

    failed = 0
    for skill_dir in sorted(args.skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        errs = validate_skill(skill_dir, strict=args.strict)
        if errs:
            failed += 1
            print(f"{skill_dir.name}:")
            for e in errs:
                print(f"  - {e}")
        elif not args.quiet:
            print(f"{skill_dir.name}: OK")

    total = sum(1 for d in args.skills_dir.iterdir() if d.is_dir())
    print(f"\nValidated {total} skills, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
