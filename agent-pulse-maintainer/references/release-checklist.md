# Agent Pulse Release Checklist

Use this checklist for version bumps, packaging, and public release readiness.

## Verify State

```powershell
git status --short --branch
$env:PYTHONUTF8='1'
$env:PYTHONIOENCODING='utf-8'
python -m ruff check agent_pulse
python -m agent_pulse.cli --version
python -m agent_pulse.cli --help
python -m agent_pulse.cli demo --json --sessions 3 --days 2 --projects 1
```

If tests are present:

```powershell
python -m pytest -q --basetemp .pytest-tmp-run
```

## Documentation Consistency

Check these values against live code, not memory:

```powershell
python -c "from agent_pulse.cli import main; print(len(main.commands)); print(sorted(main.commands))"
python -c "import agent_pulse; print(agent_pulse.__version__)"
```

Confirm README badges, changelog version, command count, model count, and test count match the current tree.

## Packaging

```powershell
python -m build
python -m pip install --force-reinstall dist\*.whl
agent-pulse --version
agent-pulse --help
```

## Release Risks

- PyPI links in README are only valid after the package exists on PyPI.
- GitHub Actions should not reference `tests/` if tests were removed from the repo.
- Emoji-heavy CLI output needs UTF-8 behavior documented or guarded on Windows.
- Duplicate Click command registrations can silently shadow earlier implementations.
