---
name: agent-pulse
description: Use Agent Pulse to inspect AI agent activity, token usage, tool calls, model usage, cost, budgets, forecasts, reports, local log sources, health checks, and MCP tools. Use when the user asks to check how much AI agents have been used, what sessions ran, what models cost, whether spending is high, generate Agent Pulse reports, diagnose Agent Pulse setup, or expose Agent Pulse data to other agents.
---

# Agent Pulse

## Purpose

Use the installed `agent-pulse` CLI as the source of truth for local AI-agent activity. Prefer running commands and summarizing their output over reading the Agent Pulse source code.

Always enable UTF-8 on Windows before running commands because Agent Pulse output contains emoji and box drawing:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```

If `agent-pulse` is not on PATH, try running from the project checkout:

```powershell
python -m agent_pulse.cli --version
```

## Common Requests

Use this command selection table first:

| User wants | Run |
|---|---|
| Current status | `agent-pulse status --json` |
| Full dashboard | `agent-pulse --json` or `agent-pulse --no-banner` |
| Demo data | `agent-pulse demo --json` |
| Setup diagnosis | `agent-pulse doctor --json` |
| Recent sessions | `agent-pulse --json --hours 24 --limit 20` |
| Top expensive sessions | `agent-pulse top --sort cost --json` |
| Model cost analysis | `agent-pulse models --json` |
| Cost savings | `agent-pulse optimize --json` |
| Budget status | `agent-pulse budget --json` |
| Cost forecast | `agent-pulse forecast --json` |
| Health/CI check | `agent-pulse health --json` |
| Search sessions | `agent-pulse search "<query>" --json` |
| Export report | `agent-pulse export -f markdown` or `agent-pulse export-html` |
| MCP tools | `agent-pulse mcp --list-tools` |

If the installed command lacks an option, run `agent-pulse <command> --help` and adapt.

## Workflow

1. Start with `agent-pulse doctor --json` if the user asks why data is missing or setup may be broken.
2. Use JSON output whenever possible, then summarize the fields that matter: sessions, tokens, tools, model breakdown, source breakdown, estimated cost, warnings.
3. Use time filters for scoped questions:

```powershell
agent-pulse status --json --hours 24
agent-pulse --json --hours 168 --limit 50
```

4. Use platform filters when the user asks about a specific agent system:

```powershell
agent-pulse --json -P codex
agent-pulse --json -P claude
agent-pulse --json -P hermes
agent-pulse --json -P deepseek
agent-pulse --json -P openclaw
```

5. For cost questions, pair summary and model views:

```powershell
agent-pulse status --json --hours 24
agent-pulse models --json --hours 24
agent-pulse optimize --json
```

6. For trend questions, use forecast/history/compare:

```powershell
agent-pulse forecast --json
agent-pulse history --json
agent-pulse compare --json
```

## Interpreting Results

- Treat `total_cost_usd` as an estimate based on Agent Pulse's local model pricing table.
- Report both cost and token volume; low-cost models can still have very high token usage.
- Distinguish sources such as `codex`, `claude`, `hermes`, `deepseek`, and `openclaw`.
- Mention if `doctor` reports missing optional sources, missing `dev_root`, or optional web dependencies.
- If no sessions appear, check `doctor`, then try a wider time window such as `--hours 168`.

## Reports

For a short human-readable answer, run JSON commands and summarize.

For artifacts, prefer:

```powershell
agent-pulse report --period daily
agent-pulse export -f markdown
agent-pulse export-html
```

Do not invent exact savings or costs. Use the CLI output.

## MCP

Use MCP mode when the user wants other AI clients to query Agent Pulse:

```powershell
agent-pulse mcp --list-tools
agent-pulse mcp
```

When explaining MCP, mention that it exposes tools such as status, forecast, top sessions, model analytics, optimization, health, search, and leaderboard.

## Local Helper

This skill includes `scripts/run_agent_pulse_snapshot.py`, which runs a compact set of JSON-friendly Agent Pulse checks and prints a combined summary:

```powershell
python scripts/run_agent_pulse_snapshot.py
```
