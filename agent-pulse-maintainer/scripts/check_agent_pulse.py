"""Quick Agent Pulse repository status checker."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(repo: Path, args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        args,
        cwd=repo,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    return proc.returncode, proc.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".", help="Path to the agent-pulse repo")
    ns = parser.parse_args()
    repo = Path(ns.repo).resolve()

    checks = [
        ("git status", ["git", "status", "--short", "--branch"]),
        ("version", [sys.executable, "-m", "agent_pulse.cli", "--version"]),
        ("cli command count", [
            sys.executable,
            "-c",
            "from agent_pulse.cli import main; print(len(main.commands))",
        ]),
        ("ruff", [sys.executable, "-m", "ruff", "check", "agent_pulse"]),
        ("demo json", [
            sys.executable,
            "-m",
            "agent_pulse.cli",
            "demo",
            "--json",
            "--sessions",
            "1",
            "--days",
            "1",
            "--projects",
            "1",
        ]),
    ]

    failed = False
    for label, cmd in checks:
        code, output = run(repo, cmd)
        status = "OK" if code == 0 else f"FAIL {code}"
        print(f"== {label}: {status}")
        if output:
            print(output[:2000])
        if code != 0:
            failed = True
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
