#!/usr/bin/env python3
"""Checks a finished run folder without using a model. Usage: check_run.py runs/<id>"""
import json
import re
import sys
from pathlib import Path

CLAIM = re.compile(r'^C(\d+): .+ \| https?://\S+ \| ".+"\s*$')


def check(run: Path) -> list[str]:
    problems = []
    if not (run / "brief.md").exists():
        problems.append("brief.md is missing")

    status = run / "status.md"
    first = status.read_text().splitlines()[0].strip() if status.exists() and status.read_text().strip() else ""
    if first not in ("DONE", "NEEDS_YOU"):
        problems.append("status.md must start with DONE or NEEDS_YOU")

    claims = set()
    research = run / "research.md"
    if research.exists():
        for n, line in enumerate(research.read_text().splitlines(), 1):
            if re.match(r"^C\d+:", line):
                match = CLAIM.match(line)
                if match:
                    claims.add(match.group(1))
                else:
                    problems.append(f"research.md line {n} needs a URL and a quote")

    draft = run / "draft.md"
    if draft.exists():
        for tag in sorted(set(re.findall(r"\[C(\d+)\]", draft.read_text())), key=int):
            if tag not in claims:
                problems.append(f"draft.md cites C{tag}, which is not in research.md")

    has_work = draft.exists() or (run / "build" / "NOTES.md").exists()
    if not has_work:
        problems.append("no draft.md or build/NOTES.md")

    if first == "DONE":
        review = run / "review.json"
        try:
            verdict = json.loads(review.read_text()).get("verdict")
        except (OSError, ValueError, AttributeError):
            verdict = None
        if verdict != "PASS":
            problems.append("status is DONE but review.json is not a PASS")
        if not (run / "final.md").exists():
            problems.append("status is DONE but final.md is missing")
        elif re.search(r"\[C\d+\]", (run / "final.md").read_text()):
            problems.append("final.md still has [C] tags")
    return problems


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    found = check(Path(sys.argv[1]))
    for problem in found:
        print("FAIL:", problem)
    print("OK" if not found else f"{len(found)} problem(s)")
    sys.exit(1 if found else 0)
