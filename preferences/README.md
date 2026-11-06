# User Preference Layer

This directory separates personal presentation defaults from shared skill behavior.

## Activate a local preference file

1. Copy `user-preferences.template.md` to `user-preferences.md`.
2. Edit only the fields that are useful to you.
3. Keep `user-preferences.md` local. It is listed in the repository's `.gitignore` and should not be committed.

The template is not an active configuration. The skill loads `user-preferences.md` only when that file exists.

## Scope and priority

The preference layer may customize presentation defaults, including language, target format, heading depth, indentation, compression density, source display, highlighting, and tone.

It does not define content-analysis logic and cannot override:

- source integrity, factual boundaries, or copyright limits;
- the action explicitly requested for the current task;
- the zero-semantic-edit protection when the task is format-only;
- required content-structure or domain-module rules.

The current task's explicit instructions take priority over saved preferences. If no local preference file exists, use the skill defaults without asking the user to create one.
