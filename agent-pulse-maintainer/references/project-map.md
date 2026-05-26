# Agent Pulse Project Map

## Package Shape

`agent-pulse` is a Python CLI package with optional web/API features. The package entrypoint is declared in `pyproject.toml` as `agent-pulse = "agent_pulse.cli:main"`.

Important modules:

- `agent_pulse/cli.py`: Click command group and subcommands.
- `agent_pulse/core.py`: Aggregates sessions from Hermes and local agent log sources.
- `agent_pulse/models/`: Dataclasses for sessions, projects, and dashboard stats.
- `agent_pulse/sources/hermes.py`: SQLite-backed Hermes source.
- `agent_pulse/sources/agent_logs.py`: Claude Code, Codex CLI, DeepSeek-TUI, OpenClaw, and generic JSONL parsing.
- `agent_pulse/pricing.py`: Model pricing database and cost breakdown logic.
- `agent_pulse/renderers/terminal.py`: Rich terminal dashboard and tables.
- `agent_pulse/web.py`: Self-contained web dashboard.
- `agent_pulse/api.py`: FastAPI app factory.
- `agent_pulse/mcp_server.py`: MCP stdio server and tool dispatch.
- `agent_pulse/doctor.py`, `scanner.py`, `health.py`: Diagnostics and discovery.
- `agent_pulse/forecast.py`, `leaderboard.py`, `optimizer.py`, `insights.py`: Analysis features.

## Change Patterns

Adding a CLI command usually requires:

1. Add or update focused implementation module if logic is more than simple wiring.
2. Register the command in `agent_pulse/cli.py`.
3. Support `--json` if the command exposes scriptable data.
4. Reuse `PulseConfig` and `_pulse_for_cli` unless the command has special startup needs.
5. Update documentation only after confirming the command exists in `main.commands`.

Adding a data source usually requires:

1. Parse into `Session` and `SessionStats`.
2. Add enable/disable config fields in `PulseConfig` if user-selectable.
3. Extend platform selection in `PLATFORM_CHOICES`, `AgentPulse._want_platforms`, diagnostics, and scanner output.
4. Keep parsing best-effort and resilient to malformed log entries.

Changing costs usually requires:

1. Update `MODEL_PRICING` and alias matching in `pricing.py`.
2. Verify cache read/write, reasoning, request, and search cost paths.
3. Confirm `models`, `top`, `status`, `summary`, `leaderboard`, `forecast`, `mcp`, and JSON renderers still agree.

## Windows Notes

PowerShell defaults can hide UTF-8 problems. Use:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```

Avoid shell heredocs written for Bash. In PowerShell, use `python -c "..."` for short snippets or create real files with `apply_patch`.
