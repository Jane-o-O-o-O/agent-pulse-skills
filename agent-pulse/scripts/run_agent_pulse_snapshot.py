"""Run a compact Agent Pulse usage snapshot."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys


def command_base() -> list[str]:
    if shutil.which("agent-pulse"):
        return ["agent-pulse"]
    return [sys.executable, "-m", "agent_pulse.cli"]


def run(args: list[str]) -> dict:
    env = os.environ.copy()
    env.setdefault("PYTHONUTF8", "1")
    env.setdefault("PYTHONIOENCODING", "utf-8")
    proc = subprocess.run(
        command_base() + args,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env,
        check=False,
    )
    raw = proc.stdout.strip()
    parsed = None
    if raw:
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            parsed = raw
    return {"command": " ".join(command_base() + args), "exit_code": proc.returncode, "output": parsed}


def main() -> int:
    snapshot = {
        "doctor": run(["doctor", "--json"]),
        "status_24h": run(["status", "--json", "--hours", "24"]),
        "models_24h": run(["models", "--json", "--hours", "24"]),
        "forecast": run(["forecast", "--json"]),
        "health": run(["health", "--json"]),
    }
    print(json.dumps(snapshot, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
