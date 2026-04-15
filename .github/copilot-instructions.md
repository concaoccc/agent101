# Copilot Instructions for agent101

## Project Overview

This is a **teaching project** that builds a mini Claude Code agent step-by-step across 12 Jupyter notebooks. Each notebook introduces one new concept while preserving everything from previous notebooks. The reference implementation lives in `C:\Users\concao\code\learn-claude-code\`.

## Build & Run Commands

```sh
# Install all dependencies (including dev/jupyter)
uv sync --all-groups

# Launch Jupyter
uv run jupyter notebook
# Then open agent101.ipynb

# Add a new dependency
uv add <package>
uv add --group dev <package>   # dev-only (e.g., testing tools)
```

## Architecture

### Notebook Progression

The 12 notebooks form a **linear progression** — each builds on the previous:

1. **01–02 (Foundation):** Agent loop + tool dispatch — the core `while True` loop that calls the LLM, executes tools, and appends results.
2. **03–06 (Single-Agent):** Planning (TodoManager), context isolation (subagents), knowledge injection (skills), memory management (3-layer compression).
3. **07–08 (Persistence):** Disk-backed task graph with dependency resolution, background thread execution.
4. **09–12 (Multi-Agent):** Team coordination via JSONL message bus, request-response protocols, autonomous task claiming, git worktree isolation.

### Core Pattern (present in every session, adapted for Azure OpenAI)

```python
def agent_loop(messages):
    while True:
        response = client.chat.completions.create(
            model=MODEL, messages=[{"role": "system", "content": SYSTEM}] + messages, tools=TOOLS,
        )
        msg = response.choices[0].message
        messages.append(msg)
        if not msg.tool_calls:
            return
        for tool_call in msg.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)
            output = TOOL_HANDLERS[name](**args)
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": output})
```

### Key Abstractions Introduced Per Notebook

| Notebook | New Abstraction | Persisted State |
|----------|----------------|-----------------|
| 01 | `agent_loop()` | None |
| 02 | `TOOL_HANDLERS` dict, `safe_path()` | None |
| 03 | `TodoManager` class | In-memory |
| 04 | `run_subagent()` | None (isolated) |
| 05 | `SkillLoader` class | `skills/*/SKILL.md` |
| 06 | `micro_compact()`, `auto_compact()` | `.transcripts/` |
| 07 | `TaskManager` class | `.tasks/task_*.json` |
| 08 | `BackgroundManager` class | Thread queue |
| 09 | `MessageBus`, `TeammateManager` | `.team/inbox/*.jsonl` |
| 10 | Request-response FSM | Request tracker dicts |
| 11 | `scan_unclaimed_tasks()`, `claim_task()` | `.tasks/` (owner field) |
| 12 | `WorktreeManager`, `EventBus` | `.worktrees/index.json`, events.jsonl |

## Conventions

### Notebook Structure

All 12 sessions live in a single notebook (`agent101.ipynb`). Each session section follows this pattern:
1. **Markdown intro** — what this session teaches and how it builds on the previous one
2. **Concept explanation** — key ideas with diagrams/pseudocode
3. **Implementation cells** — working Python code, building incrementally
4. **Demo/test cells** — runnable examples that show the new feature in action
5. **Summary cell** — what was added, what's next

Sessions are separated by level-1 markdown headers (`# Session XX: Title`).

### Code Style

- All agent code uses the **OpenAI Python SDK** with **Azure OpenAI** (`openai.AzureOpenAI`)
- Environment config via `python-dotenv` — always load from `.env`
- Tool handlers are pure functions: `def run_<tool>(**kwargs) -> str`
- Path safety: use `safe_path(path, workspace)` before any file operation
- YAML frontmatter in skill files parsed with `pyyaml`

### Reference Material

- **Docs:** `C:\Users\concao\code\learn-claude-code\docs\en\s01-the-agent-loop.md` through `s12-worktree-task-isolation.md`
- **Code:** `C:\Users\concao\code\learn-claude-code\agents\s01_agent_loop.py` through `s12_worktree_task_isolation.py`
- **Full reference:** `C:\Users\concao\code\learn-claude-code\agents\s_full.py` (all 12 concepts combined)
- **Skills:** `C:\Users\concao\code\learn-claude-code\skills\` (agent-builder, code-review, mcp-builder, pdf)

When implementing a notebook, always consult both the corresponding doc (`sXX-*.md`) and source (`sXX_*.py`) from the reference repo.

### Dependencies

- `openai` — Azure OpenAI API client
- `python-dotenv` — `.env` file loading
- `pyyaml` — YAML frontmatter parsing (used from session 05+)
- `jupyter` + `ipykernel` — notebook runtime (dev group)

### Azure OpenAI Setup

This project uses Azure OpenAI (not the Anthropic SDK). The client is initialized as:

```python
from openai import AzureOpenAI
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
MODEL = os.getenv("AZURE_OPENAI_DEPLOYMENT")
```

The reference repo uses Anthropic's SDK with `client.messages.create()`. When adapting code, translate to OpenAI's `client.chat.completions.create()` format:
- Anthropic `system` param → OpenAI `messages[0]` with `role: "system"`
- Anthropic `stop_reason == "tool_use"` → OpenAI `finish_reason == "tool_calls"`
- Anthropic `content[].type == "tool_use"` → OpenAI `message.tool_calls[]`
- Anthropic `tool_result` messages → OpenAI `role: "tool"` messages
