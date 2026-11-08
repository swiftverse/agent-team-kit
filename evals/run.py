#!/usr/bin/env python3
"""Tests the reviewer on drafts with known answers. Run after changing any agent.

Each file in evals/cases is named <case>.<EXPECTED>.md. All the facts are made up.
Usage: python3 evals/run.py [--model sonnet]
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
TOOLS = ["Read", "Glob", "Grep"]


def review(case: Path, model: list[str]) -> str:
    with tempfile.TemporaryDirectory(dir=EVALS, prefix="tmp-") as tmp:
        folder = Path(tmp)
        shutil.copy(EVALS / "brief.md", folder / "brief.md")
        shutil.copy(EVALS / "research.md", folder / "research.md")
        shutil.copy(case, folder / "draft.md")
        prompt = f"Review the run folder {folder.relative_to(ROOT)}. This run is an offline test."
        result = subprocess.run(
            ["claude", "-p", prompt, "--agent", "reviewer", *model,
             "--tools", ",".join(TOOLS), "--allowedTools", *TOOLS,
             "--permission-mode", "dontAsk", "--max-budget-usd", "1",
             "--no-session-persistence"],
            cwd=ROOT, capture_output=True, text=True, timeout=300)
    found = re.findall(r'"verdict"\s*:\s*"(PASS|REVISE)"', result.stdout)
    return found[-1] if found else "NO VERDICT"


def main() -> int:
    model = sys.argv[1:] if sys.argv[1:] else []
    cases = sorted((EVALS / "cases").glob("*.md"))
    passed = 0
    for case in cases:
        name, expected = case.name.removesuffix(".md").rsplit(".", 1)
        got = review(case, model)
        ok = got == expected
        passed += ok
        print(f"{'ok  ' if ok else 'FAIL'}  {name:<16} expected {expected:<7} got {got}", flush=True)
    print(f"{passed}/{len(cases)} passed")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    sys.exit(main())
