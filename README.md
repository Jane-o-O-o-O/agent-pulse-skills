# Agent Pulse Skills

[![skills.sh](https://skills.sh/b/Jane-o-O-o-O/agent-pulse-skills)](https://skills.sh/Jane-o-O-o-O/agent-pulse-skills)

Codex skill for using [Agent Pulse](https://github.com/Jane-o-O-o-O/agent-pulse) as a local AI-agent activity, token, and cost dashboard.

## What This Skill Does

This repository contains a usage-focused skill named `agent-pulse`. It guides an agent to run the `agent-pulse` CLI, prefer JSON output, interpret local usage data, diagnose setup issues, and expose Agent Pulse data through reports, APIs, metrics, or MCP when requested.

The skill is intentionally an agent operating guide. It should not be treated as project documentation or a product roadmap.

## Source Keys

```text
hermes, claude, codex, deepseek, openclaw, copilot, aider, qwen,
opencode, goose, cursor, antigravity, amp
```

## Agent Workflows

- Use `status`, `top`, `models`, and the root dashboard command for usage summaries.
- Use `budget`, `alerts`, `health`, `anomaly`, `forecast`, and `score` for spending and risk checks.
- Use `history`, `timeline`, `heatmap`, `compare`, `compare-projects`, `leaderboard`, `diff`, `search`, `insights`, and `snapshot` for analysis.
- Use `report`, `export`, `export-html`, `metrics`, `web`, `api`, and `mcp` for sharing or integration.
- Use `doctor`, `scan`, `config`, `themes`, `completions`, `plugins`, `frameworks`, `demo`, and `tui` for setup, discovery, and local operation.

## Included Skill

```text
agent-pulse/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
`-- scripts/
    `-- run_agent_pulse_snapshot.py
```

## Install

Install from GitHub with the skills CLI:

```bash
npx skills add Jane-o-O-o-O/agent-pulse-skills
```

The skill expects the `agentpulse-cli` Python package to be installed:

```bash
pip install agentpulse-cli
agent-pulse --version
```

For local Agent Pulse development:

```bash
cd path/to/agent-pulse
pip install -e ".[web]"
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
Use $agent-pulse to compare Codex and Claude activity over the last 7 days.
```

```text
Use $agent-pulse to list the MCP tools Agent Pulse exposes.
```

## Snapshot Helper

The bundled helper runs a compact set of Agent Pulse checks:

```bash
python agent-pulse/scripts/run_agent_pulse_snapshot.py --hours 24 --days 7
```

It runs JSON-friendly checks for diagnosis, current status, top cost sessions, model analytics, leaderboard, forecast, health, score, budget, and insights.

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
