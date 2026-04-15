---
name: code-review
description: "Guidelines for reviewing Python code: style, bugs, security."
---

# Code Review Skill

When reviewing Python code, check for:

## Style
- PEP 8 compliance (naming, spacing, line length)
- Consistent use of type hints
- Docstrings on public functions

## Bugs
- Off-by-one errors in loops
- Unclosed file handles (use context managers)
- Mutable default arguments

## Security
- No hardcoded secrets or API keys
- Input validation on user-supplied data
- Safe use of subprocess (no shell=True with user input)
