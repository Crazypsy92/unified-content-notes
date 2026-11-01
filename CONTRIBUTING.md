# Contributing

Thanks for improving Unified Content Notes.

## Principles

1. Keep one entry point and three actions: **summarize, explain, format only**.
2. Preserve the user's requested operation. Never turn formatting into rewriting.
3. Do not invent missing facts, scenes, quotations, or scientific evidence.
4. Include or update a short, **original or rights-cleared** test example whenever behavior changes.
5. Avoid publishing other people's private conversations or copyrighted long-form scripts.
6. Keep the skill dependency-free and use Markdown where possible.

## A suggested pull request

- Describe the input type and the intended action.
- Show the failure (or missing coverage) in a short source/output pair.
- Modify `SKILL.md` only for global behavior; use `references/` for specific input structures and edge cases.
- Run `python3 -m unittest discover -s tests -v` and report the result.

## Language

English documentation is welcome. Chinese is the current default output language for the skill, and explicit user requests take precedence.
