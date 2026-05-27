# Agent Pulse Skills

[![skills.sh](https://skills.sh/b/Jane-o-O-o-O/agent-pulse-skills)](https://skills.sh/Jane-o-O-o-O/agent-pulse-skills)

Codex skill for using [Agent Pulse](https://github.com/Jane-o-O-o-O/agent-pulse) as a local AI-agent activity dashboard.

This repository contains a usage-focused skill named `agent-pulse`. It helps an agent run the `agent-pulse` CLI, inspect local sessions, summarize token usage, estimate cost, diagnose setup issues, and expose Agent Pulse data through MCP.

## What It Does

- Summarizes recent AI-agent activity from local Agent Pulse data.
- Checks sessions, tokens, tool calls, model usage, and estimated cost.
- Runs setup diagnostics with `agent-pulse doctor`.
- Uses JSON CLI output when available so answers are grounded in real local data.
- Helps generate reports, forecasts, budget checks, and model cost analysis.
- Lists MCP tools for connecting Agent Pulse to other AI clients.

## Included Skill

```text
agent-pulse/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── scripts/
    └── run_agent_pulse_snapshot.py
```

## Install

Install from GitHub with the skills CLI:

```bash
npx skills add Jane-o-O-o-O/agent-pulse-skills
```

The skill expects the `agentpulse-cli` Python package to be installed, which provides the `agent-pulse` command.

```bash
pip install agentpulse-cli
```

If you are developing from a local Agent Pulse checkout:

```bash
cd path/to/agent-pulse
pip install -e .
```

After installation, the command to run is still:

```bash
agent-pulse --version
```

## Manual Install

You can also clone this repository and install from the local checkout:

```bash
git clone git@github.com:Jane-o-O-o-O/agent-pulse-skills.git
cd agent-pulse-skills
npx skills add .
```

## Example Prompts

```text
Use $agent-pulse to summarize my AI agent usage in the last 24 hours.
```

```text
Use $agent-pulse to check which model cost the most this week.
```

```text
Use $agent-pulse to diagnose why my dashboard has no sessions.
```

```text
Use $agent-pulse to list the MCP tools Agent Pulse exposes.
```

## Snapshot Helper

The bundled helper runs a compact set of Agent Pulse checks:

```bash
python agent-pulse/scripts/run_agent_pulse_snapshot.py
```

It runs:

- `agent-pulse doctor --json`
- `agent-pulse status --json --hours 24`
- `agent-pulse models --json --hours 24`
- `agent-pulse forecast --json`
- `agent-pulse health --json`

## Windows Notes

Agent Pulse prints emoji and box-drawing characters. On Windows, use UTF-8 output for reliable command execution:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```

## Validation

List the skills exposed by this repository:

```bash
npx skills add Jane-o-O-o-O/agent-pulse-skills --list
```

Run the skill validator from the `skill-creator` skill in your local Codex skills installation:

```bash
python path/to/skill-creator/scripts/quick_validate.py path/to/agent-pulse
```

Expected result:

```text
Skill is valid!
```
