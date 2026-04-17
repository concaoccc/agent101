# agent101 — Build a Mini Coding Agent from Zero

A hands-on Jupyter notebook that teaches you how to build a coding agent from scratch — one concept per session. Inspired by the [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) curriculum, adapted for **Azure OpenAI**.

By the end you'll have a working agent with tool use, subagents, context compression, persistent tasks, MCP integration, a permission system, and cross-session memory — all in a single notebook.

## Prerequisites

| Requirement | Notes |
|---|---|
| **Python 3.12+** | [python.org/downloads](https://www.python.org/downloads/) |
| **uv** | Fast Python package manager — [install guide](https://docs.astral.sh/uv/getting-started/installation/) |
| **Azure OpenAI access** | You need an endpoint URL, API key, and a deployed chat model (e.g. `gpt-4o`, `gpt-4.1`) |

> **Don't have Azure OpenAI?** Any OpenAI-compatible API works. Just set the endpoint and key in `.env`.

## Setup (Step by Step)

### 1. Clone the repo

```sh
git clone https://github.com/concaoccc/agent101.git
cd agent101
```

### 2. Install dependencies with uv

```sh
# Install uv if you don't have it (one-liner)
# Windows (PowerShell):
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# macOS / Linux:
# curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies (runtime + Jupyter)
uv sync --all-groups
```

This creates a `.venv` virtual environment automatically and installs:
- `openai` — Azure OpenAI SDK
- `python-dotenv` — loads `.env` config
- `pyyaml` — YAML parsing for skills/memory
- `jupyter` + `ipykernel` — notebook environment

### 3. Configure your Azure OpenAI credentials

```sh
# Copy the example env file
cp .env.example .env
```

Edit `.env` with your own values:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
AZURE_OPENAI_API_VERSION=2025-01-01-preview
```

| Variable | Where to find it |
|---|---|
| `AZURE_OPENAI_ENDPOINT` | Azure Portal → your OpenAI resource → Keys and Endpoint |
| `AZURE_OPENAI_API_KEY` | Same page — Key 1 or Key 2 |
| `AZURE_OPENAI_DEPLOYMENT` | Azure AI Studio → Deployments → your model's deployment name |
| `AZURE_OPENAI_API_VERSION` | Use `2025-01-01-preview` or check [API version docs](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference) |

> ⚠️ **Never commit `.env`** — it's already in `.gitignore`.

### 4. Launch Jupyter

```sh
uv run jupyter notebook
```

Open `agent101.ipynb` in your browser and run cells top-to-bottom, session by session.

### 5. (Optional) Jump to a specific session

Each session builds on the previous ones. Run the cells in order. If you want to start fresh from a tagged version:

```sh
git checkout S05   # jump to the state after Session 5
```

Available tags: `S01` through `S10`.

## Course Outline

All 10 sessions live in a single notebook (`agent101.ipynb`):

| # | Session | What You Build |
|---|---------|----------------|
| 01 | **Agent Loop** | The fundamental `while`-loop: LLM → tool call → result → repeat |
| 02 | **Tool Use** | Multi-tool dispatch (powershell, read, write, edit) |
| 03 | **TodoWrite** | Planning layer — in-memory task tracking with nag reminders |
| 04 | **Subagents** | Context isolation — child agents with fresh `messages=[]` |
| 05 | **Skill Loading** | Two-layer knowledge injection (system prompt + on-demand) |
| 06 | **Context Compact** | Three-layer compression for infinite sessions |
| 07 | **Task System** | File-based task graph with `blockedBy` dependencies |
| 08 | **MCP & Plugins** | External tool integration via Model Context Protocol |
| 09 | **Permission System** | Four-stage safety pipeline (deny → mode → allow → ask) |
| 10 | **Memory System** | Cross-session persistence with YAML frontmatter files |

## Project Structure

```
agent101/
├── agent101.ipynb        # The notebook — all 10 sessions
├── .env.example          # Template for Azure OpenAI config
├── .env                  # Your credentials (git-ignored)
├── pyproject.toml        # uv project config & dependencies
├── skills/               # Skill files loaded by S05
│   └── code-review/
│       └── SKILL.md
├── .memory/              # Memory store created by S10
├── .tasks/               # Task files created by S07
├── .transcripts/         # Compact transcripts from S06
└── .github/
    └── copilot-instructions.md
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `uv: command not found` | Install uv — see step 2 above |
| `ModuleNotFoundError: openai` | Run `uv sync --all-groups` to install dependencies |
| Notebook kernel not found | Run `uv run python -m ipykernel install --user --name agent101` |
| LLM returns JSON text instead of calling tools | The system prompt tells it to use function calling — restart kernel and re-run from top |
| `AZURE_OPENAI_API_KEY` error | Check your `.env` file has the correct key and endpoint |
| `openai.AuthenticationError` | Verify your API key is valid and the deployment name is correct |

## Reference

Inspired by [learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) by shareAI-lab. Adapted for Azure OpenAI with PowerShell as the shell tool.