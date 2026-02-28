#!/usr/bin/env python3
"""
Structural validation of an AI skills repository.
"""

import json
import re
import sys
from pathlib import Path
from typing import Optional


REPO_ROOT = Path(__file__).resolve().parent.parent

SKILLS = [
    "catalyst-mapping",
    "cio-qa-prep",
    "cross-asset-signals",
    "investment-memo",
    "scenario-analysis",
    "thematic-screening",
]

RULES = [f"{s}.mdc" for s in SKILLS]

COMMANDS = [
    "catalyst-map.md",
    "cio-qa-prep.md",
    "cross-asset.md",
    "investment-memo.md",
    "scenario-analysis.md",
    "thematic-screen.md",
]


def _parse_frontmatter(text: str) -> Optional[dict]:
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return None
    fm = {}
    lines = match.group(1).split("\n")
    key = None
    value_lines = []
    for line in lines:
        if line.strip() and not line.startswith(" ") and ":" in line and not key:
            if key:
                fm[key] = "\n".join(value_lines).strip().strip("'\"")
            key, _, rest = line.partition(":")
            key = key.strip()
            value_lines = [rest.strip().strip("'\"")] if rest.strip() else []
        elif key and (line.startswith(" ") or line.startswith(">") or line.strip().startswith("|")):
            value_lines.append(line)
        elif key:
            fm[key] = "\n".join(value_lines).strip().strip("'\"").lstrip(">").strip()
            key = None
            value_lines = []
            if line.strip() and ":" in line:
                key, _, rest = line.partition(":")
                key = key.strip()
                value_lines = [rest.strip().strip("'\"")] if rest.strip() else []
    if key:
        fm[key] = "\n".join(value_lines).strip().strip("'\"").lstrip(">").strip()
    return fm


def check_skill_frontmatter() -> tuple[bool, str]:
    ok = 0
    missing = []
    for skill in SKILLS:
        path = REPO_ROOT / "skills" / skill / "SKILL.md"
        if not path.exists():
            missing.append(path.name)
            continue
        text = path.read_text()
        fm = _parse_frontmatter(text)
        if fm and fm.get("name") and fm.get("description"):
            ok += 1
        else:
            missing.append(skill)
    return ok == 6, f"SKILL.md frontmatter valid ({ok}/6)" + (
        f" - missing: {', '.join(missing)}" if missing else ""
    )


def check_rule_frontmatter() -> tuple[bool, str]:
    ok = 0
    missing = []
    for rule in RULES:
        path = REPO_ROOT / "rules" / rule
        if not path.exists():
            missing.append(rule)
            continue
        text = path.read_text()
        fm = _parse_frontmatter(text)
        if fm and fm.get("description"):
            ok += 1
        else:
            missing.append(rule)
    return ok == 6, f"Rule frontmatter valid ({ok}/6)" + (
        f" - missing: {', '.join(missing)}" if missing else ""
    )


def check_command_files() -> tuple[bool, str]:
    ok = 0
    missing = []
    for cmd in COMMANDS:
        path = REPO_ROOT / "commands" / cmd
        if path.exists() and path.stat().st_size > 0:
            ok += 1
        else:
            missing.append(cmd)
    return ok == 6, f"Command files exist and non-empty ({ok}/6)" + (
        f" - missing: {', '.join(missing)}" if missing else ""
    )


REFERENCE_PATTERN = re.compile(r"Read `references/([^`]+)`")


def check_references() -> tuple[bool, str]:
    broken = []
    for skill in SKILLS:
        path = REPO_ROOT / "skills" / skill / "SKILL.md"
        if not path.exists():
            continue
        text = path.read_text()
        for m in REFERENCE_PATTERN.finditer(text):
            ref_path = REPO_ROOT / "skills" / skill / "references" / m.group(1).strip()
            if not ref_path.exists():
                broken.append(f"{skill}/{m.group(1)}")
    ok = len(broken) == 0
    return ok, f"References exist ({'all' if ok else len(broken) + ' broken'})" + (
        f" - {', '.join(broken)}" if broken else ""
    )


def check_symlinks() -> tuple[bool, str]:
    symlinks = [
        (REPO_ROOT / ".cursor" / "skills", "directory"),
        (REPO_ROOT / ".cursor" / "rules", "directory"),
        (REPO_ROOT / ".cursor" / "commands", "directory"),
        (REPO_ROOT / ".claude" / "skills", "directory"),
    ]
    broken = []
    for p, expected in symlinks:
        if not p.exists():
            broken.append(str(p.relative_to(REPO_ROOT)))
        elif not p.is_symlink():
            broken.append(f"{p.relative_to(REPO_ROOT)} (not symlink)")
        else:
            target = p.resolve()
            if not target.exists() or not target.is_dir():
                broken.append(str(p.relative_to(REPO_ROOT)))
    ok = len(broken) == 0
    return ok, f"Symlinks resolve ({4 - len(broken)}/4)" + (
        f" - broken: {', '.join(broken)}" if broken else ""
    )


def check_cursor_plugin() -> tuple[bool, str]:
    path = REPO_ROOT / ".cursor-plugin" / "plugin.json"
    try:
        if not path.exists():
            return False, "Cursor plugin manifest - file missing"
        data = json.loads(path.read_text())
        if not data.get("name"):
            return False, "Cursor plugin manifest - missing 'name' field"
        return True, "Cursor plugin manifest valid"
    except json.JSONDecodeError as e:
        return False, f"Cursor plugin manifest - invalid JSON: {e}"


def check_claude_plugin() -> tuple[bool, str]:
    path = REPO_ROOT / ".claude-plugin" / "plugin.json"
    try:
        if not path.exists():
            return False, "Cowork plugin manifest - file missing"
        data = json.loads(path.read_text())
        if not data.get("name"):
            return False, "Cowork plugin manifest - missing 'name' field"
        return True, "Cowork plugin manifest valid"
    except json.JSONDecodeError as e:
        return False, f"Cowork plugin manifest - invalid JSON: {e}"


def check_line_counts() -> tuple[bool, str]:
    over = []
    for skill in SKILLS:
        path = REPO_ROOT / "skills" / skill / "SKILL.md"
        if path.exists():
            n = sum(1 for _ in path.open())
            if n >= 500:
                over.append(f"{skill} ({n})")
    ok = len(over) == 0
    return ok, f"SKILL.md line counts under 500 ({'all' if ok else 'over: ' + ', '.join(over)})"


def check_gitignore_env() -> tuple[bool, str]:
    path = REPO_ROOT / ".gitignore"
    if not path.exists():
        return False, "Gitignore - .env not found (no .gitignore)"
    content = path.read_text()
    for line in content.splitlines():
        stripped = line.strip()
        if stripped == ".env" or stripped.startswith(".env") and not stripped.startswith("!.env"):
            return True, ".env in .gitignore"
    return False, "Gitignore - .env not in .gitignore"


def check_claude_commands_clean() -> tuple[bool, str]:
    dirty = []
    cmd_dir = REPO_ROOT / ".claude" / "commands"
    if not cmd_dir.exists():
        return False, "Claude commands clean - .claude/commands missing"
    for f in cmd_dir.glob("*.md"):
        text = f.read_text()
        if "@.cursor/" in text or "@.claude/" in text:
            dirty.append(f.name)
    ok = len(dirty) == 0
    return ok, f"Claude commands clean ({'ok' if ok else 'dirty: ' + ', '.join(dirty)})"


CURSOR_SKILLS_PATTERN = re.compile(r"@\.cursor/skills/([^\s)`]+)")


def check_cursor_commands_resolve() -> tuple[bool, str]:
    broken = []
    skills_dir = REPO_ROOT / "skills"
    for cmd in COMMANDS:
        path = REPO_ROOT / "commands" / cmd
        if not path.exists():
            continue
        text = path.read_text()
        for m in CURSOR_SKILLS_PATTERN.finditer(text):
            rel = m.group(1).strip().rstrip(")")
            target = skills_dir / rel
            if not target.exists():
                broken.append(f"{cmd}: {m.group(1)}")
    ok = len(broken) == 0
    return ok, f"Cursor commands @paths resolve ({'all' if ok else 'broken: ' + ', '.join(broken[:5])}{'...' if len(broken) > 5 else ''})"


def main() -> int:
    checks = [
        ("SKILL.md frontmatter", check_skill_frontmatter),
        ("Rule frontmatter", check_rule_frontmatter),
        ("Command files", check_command_files),
        ("References exist", check_references),
        ("Symlinks resolve", check_symlinks),
        ("Cursor plugin manifest", check_cursor_plugin),
        ("Cowork plugin manifest", check_claude_plugin),
        ("SKILL.md line counts", check_line_counts),
        ("Gitignore .env", check_gitignore_env),
        ("Claude commands clean", check_claude_commands_clean),
        ("Cursor commands @paths", check_cursor_commands_resolve),
    ]

    failed = []
    for name, fn in checks:
        passed, msg = fn()
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} {msg}")
        if not passed:
            failed.append(name)

    print()
    if failed:
        print(f"Summary: {len(failed)} check(s) failed - {', '.join(failed)}")
        return 1
    print("Summary: All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
