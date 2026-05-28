# Agent Pulse Skills

[![skills.sh](https://skills.sh/b/Jane-o-O-o-O/agent-pulse-skills)](https://skills.sh/Jane-o-O-o-O/agent-pulse-skills)
[![Agent Pulse](https://img.shields.io/badge/skill-agent--pulse-2563eb)](agent-pulse/SKILL.md)
[![Package](https://img.shields.io/badge/package-agentpulse--cli-0f766e)](https://pypi.org/project/agentpulse-cli/)

Codex skill for using [Agent Pulse](https://github.com/Jane-o-O-o-O/agent-pulse) to inspect local AI-agent sessions, token usage, model costs, health, reports, and MCP tools.

This repository is a skill package. The actual Agent operating guide lives in [`agent-pulse/SKILL.md`](agent-pulse/SKILL.md).

## Install

Install from GitHub with the skills CLI:

```bash
npx skills add Jane-o-O-o-O/agent-pulse-skills
```

List the skills exposed by this repository:

```bash
npx skills add Jane-o-O-o-O/agent-pulse-skills --list
```

Manual local install:

```bash
git clone git@github.com:Jane-o-O-o-O/agent-pulse-skills.git
cd agent-pulse-skills
npx skills add .
```

## Runtime Requirement

The skill tells an agent how to use Agent Pulse, but the `agent-pulse` CLI must be installed separately:

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

## What Agents Use It For

| User asks about | Agent Pulse commands the skill points to |
| --- | --- |
| Recent usage | `status`, `top`, root dashboard JSON |
| Sessions and search | `session`, `search`, `diff`, `snapshot` |
| Models and cost | `models`, `leaderboard`, `optimize`, `budget` |
| Risk and health | `alerts`, `health`, `anomaly`, `forecast`, `score` |
| Trends and comparisons | `history`, `timeline`, `heatmap`, `compare`, `compare-projects`, `insights` |
| Sharing and integration | `report`, `export`, `export-html`, `metrics`, `web`, `api`, `mcp` |
| Setup and discovery | `doctor`, `scan`, `config`, `plugins`, `frameworks`, `completions` |

Supported source keys for `-P/--platform`:

```text
hermes, claude, codex, deepseek, openclaw, copilot, aider, qwen,
opencode, goose, cursor, antigravity, amp
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

## Included Files

```text
agent-pulse/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
`-- scripts/
    `-- run_agent_pulse_snapshot.py
```

The helper script runs a compact JSON-friendly snapshot:

```bash
python agent-pulse/scripts/run_agent_pulse_snapshot.py --hours 24 --days 7
```

It gathers diagnosis, current status, top cost sessions, model analytics, leaderboard, forecast, health, score, budget, and insights. Each subcommand has its own timeout so one slow local scan does not block the whole snapshot.

## Windows Notes

Agent Pulse prints emoji and box-drawing characters. Use UTF-8 output for reliable command execution:

```powershell
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
```

## Validation

Run the skill validator from the `skill-creator` skill:

```bash
python path/to/skill-creator/scripts/quick_validate.py path/to/agent-pulse
```

Expected result:

```text
Skill is valid!
```
