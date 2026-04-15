# agent101 — Build Mini Claude Code from Zero

A step-by-step Jupyter notebook tutorial that teaches you how to build a mini [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) agent from scratch, following the [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) curriculum.

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- An Anthropic API key (or compatible provider)

## Quick Start

```sh
# Clone and enter
git clone <repo-url>
cd agent101

# Install dependencies
uv sync --all-groups

# Set up your API key
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY

# Launch Jupyter
uv run jupyter notebook
# Then open agent101.ipynb
```

## Course Outline

All 12 sessions live in a single notebook (`agent101.ipynb`):

| # | Session | Topic |
|---|---------|-------|
| 01 | Agent Loop | The fundamental while-loop connecting LLM to tools |
| 02 | Tool Use | Multi-tool dispatch with file operations |
| 03 | TodoWrite | Planning layer with stateful task tracking |
| 04 | Subagent | Context isolation via child agents |
| 05 | Skill Loading | On-demand knowledge injection |
| 06 | Context Compact | 3-layer compression for long sessions |
| 07 | Task System | Persistent task graph with dependencies |
| 08 | Background Tasks | Async execution with daemon threads |
| 09 | Agent Teams | Multi-agent coordination via message bus |
| 10 | Team Protocols | Structured request-response handshakes |
| 11 | Autonomous Agents | Self-organizing task-claiming agents |
| 12 | Worktree Isolation | Git worktree isolation for parallel execution |

## Reference

Based on [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) by shareAI-lab.