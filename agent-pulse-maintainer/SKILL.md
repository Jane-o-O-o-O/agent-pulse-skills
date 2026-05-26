---
name: agent-pulse-maintainer
description: Maintain, extend, debug, and release the Agent Pulse Python project. Use when Codex works in the agent-pulse repository on CLI commands, log-source parsers, token/cost accounting, Rich terminal rendering, web/API/TUI/MCP features, packaging, CI, or release-readiness checks.
---

# Agent Pulse Maintainer

## Start Here

Use this skill for work on the `agent-pulse` repository. Prefer the existing package structure and keep changes narrow: most behavior belongs in `agent_pulse/`, and command wiring currently lives in `agent_pulse/cli.py`.

Before editing, inspect the worktree and the relevant module:

```powershell
git status --short --branch
rg "target_symbol_or_command" agent_pulse tests
```

If the user asks for broad project status, run:

```powershell
python scripts/check_agent_pulse.py E:\agent-pulse
```

## Project Map

Read `references/project-map.md` when changing unfamiliar areas. The key ownership boundaries are:

- CLI entrypoints: `agent_pulse/cli.py`
- Core aggregation: `agent_pulse/core.py`
- Local agent logs: `agent_pulse/sources/agent_logs.py`
- Hermes DB source: `agent_pulse/sources/hermes.py`
- Pricing and cost: `agent_pulse/pricing.py`
- Terminal UI: `agent_pulse/renderers/terminal.py`, `agent_pulse/tui.py`
- Web/API: `agent_pulse/web.py`, `agent_pulse/api.py`
- MCP: `agent_pulse/mcp_server.py`

## Development Rules

- Keep Unicode already used by the project, but run CLI checks with UTF-8 on Windows.
- Do not move large command blocks out of `cli.py` unless the user asks for refactoring; this project currently favors command co-location.
- Keep output formats backward-compatible. If JSON fields change, update every renderer, CLI path, and reference test expectation.
- Cost changes must update both `estimate_cost` behavior and display paths that use `estimate_session_cost_breakdown`.
- Data-source parsers must be tolerant of missing fields, malformed JSONL lines, and platform-specific usage aliases.
- Avoid network calls in tests and default CLI paths. Webhook and external API behavior should be mockable.

## Validation

Use the smallest useful check first, then broaden before finishing substantial edits.

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
python -m ruff check agent_pulse
python -m agent_pulse.cli --version
python -m agent_pulse.cli --help
python -m agent_pulse.cli demo --json --sessions 3 --days 2 --projects 1
```

If tests exist in the checkout, use a repository-local temp directory on Windows:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
python -m pytest -q --basetemp .pytest-tmp-run
```

## Known Local Issues

- The project uses emoji and box drawing. On Windows GBK terminals, `agent-pulse --help` can fail unless UTF-8 is enabled.
- The default pytest temp location can be inaccessible on this machine. Use `--basetemp .pytest-tmp-run`.
- The repository previously had duplicate `tui` command registration in `agent_pulse/cli.py`; check for duplicate Click command names when touching CLI wiring.
- Documentation may drift from reality. Verify command count, version, tests, and PyPI status instead of trusting README badges.

## Release Work

Read `references/release-checklist.md` before release, packaging, PyPI, GitHub Actions, or version-bump work.
