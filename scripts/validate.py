#!/usr/bin/env python3
"""Check this collection's portable packaging. Requires only Python 3.10+."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "general-learning-tutor",
    "math-tutor",
    "research-coach",
    "programming-tutor",
    "ai-engineering-tutor",
    "indengpt",
}
errors = []


def error(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def main():
    found = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if found != SKILLS:
        errors.append(f"Skill set differs: missing={SKILLS - found}, extra={found - SKILLS}")

    root_license = (ROOT / "LICENSE").read_text(encoding="utf-8")
    for name in sorted(SKILLS):
        folder = ROOT / "skills" / name
        entry = folder / "SKILL.md"
        if not entry.is_file():
            error(entry, "missing entrypoint")
            continue
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            error(entry, "missing YAML frontmatter")
            continue
        # These skills deliberately use only flat, unquoted scalar fields.
        fields = {}
        for line in match.group(1).splitlines():
            item = re.fullmatch(r"([a-z-]+): (.+)", line)
            if not item or item.group(1) in fields:
                error(entry, "invalid or duplicate flat frontmatter field")
                continue
            fields[item.group(1)] = item.group(2)
        if set(fields) != {"name", "description", "license"}:
            error(entry, "expected name, description, and license fields")
        if fields.get("name") != name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            error(entry, "invalid name or folder mismatch")
        description = fields.get("description", "")
        if not 1 <= len(description) <= 1024 or ": " in description:
            error(entry, "invalid plain-scalar description")
        if fields.get("license") != "MIT":
            error(entry, "expected MIT license")
        notice = folder / "LICENSE"
        if not notice.is_file() or notice.read_text(encoding="utf-8") != root_license:
            error(notice, "missing or different bundled license")

    required = [
        "README.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "LICENSE",
        "docs/examples.md", "docs/design-notes.md", "docs/behavioral-checks.md",
        ".github/workflows/validate.yml", ".github/pull_request_template.md",
        ".github/ISSUE_TEMPLATE/behavior-report.md", ".github/ISSUE_TEMPLATE/improvement.md",
    ]
    for name in required:
        if not (ROOT / name).is_file():
            errors.append(f"Missing repository file: {name}")

    # Guard against common private-source carryover, not an exhaustive secret scan.
    forbidden = re.compile(
        r"docs\.google\.com|drive\.google\.com|notion\.so|notion\.site|"
        r"[A-Za-z]:[\\/]+Users[\\/]|(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}|"
        r"Matt[’']s|I am Matt|GPT-6 Astra|2/4 initial transfer|5/5 recall",
        re.I,
    )
    text_files = [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts]
    for path in text_files:
        rel = path.relative_to(ROOT)
        if path.suffix not in {".md", ".yml", ".yaml", ".json"} and path.name != "LICENSE":
            continue
        text = path.read_text(encoding="utf-8")
        if "\ufffd" in text or "\x00" in text:
            error(path, "invalid text marker")
        if forbidden.search(text):
            error(path, "possible personal context or credential carryover")
        if rel.parts[0] == "skills" and re.search(r"humanres|scrapling|math-track|Matt-xyl", text, re.I):
            # Copyright attribution in bundled notices is intentional.
            if path.name != "LICENSE":
                error(path, "excluded or learner-specific dependency")
        if path.suffix != ".md":
            continue
        # Check Markdown file links outside code fences; external URLs aren't fetched.
        prose = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", prose):
            target = unquote(target.strip("<>"))
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (path.parent / parsed.path).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                error(path, f"broken or escaping local link: {target}")

    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(SKILLS)} skills; frontmatter, licenses, local links, and context guards checked.")
    print("Structural checks only; behavioral and learning outcomes require separate evaluation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
