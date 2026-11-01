# Examples: Input → Output

All material in this directory is **original demonstration content** written for this project. The examples teach *behavior and trade-offs*; they are **not fixed templates** that every film, video, article, or story must follow. Source files are deliberately small enough to inspect.

The public instructions are in English. Chinese outputs demonstrate the skill's default writing conventions.

## Compare actions on the same source

| Request | Input | Expected output | What to inspect |
| --- | --- | --- | --- |
| Summarize an opinion piece | [argument-input.md](argument-input.md) | [argument-summary.md](argument-summary.md) | Retains distinct claims, the 180°C example, and an actionable practice plan |
| Explain the same opinion piece | [argument-input.md](argument-input.md) | [argument-explanation.md](argument-explanation.md) | Answers *why* rather than simply shortening; labels its interpretation |
| Summarize a short story | [narrative-input.md](narrative-input.md) | [narrative-summary.md](narrative-summary.md) | Keeps character motivation, event sequence and the final reveal |
| Explain the same story | [narrative-input.md](narrative-input.md) | [narrative-explanation.md](narrative-explanation.md) | Grounds an interpretation in specific actions instead of adding an invented backstory |
| Format without rewriting | [format-input.md](format-input.md) | [format-only.md](format-only.md) | Preserves every non-layout character while improving reading rhythm |

## More source structures

| Request | Input | Expected output | What to inspect |
| --- | --- | --- | --- |
| Explain a documentary excerpt | [documentary-input.md](documentary-input.md) | [documentary-explanation.md](documentary-explanation.md) | Separates observation, interview statements, hypotheses and missing evidence |
| Summarize a multi-image social post | [carousel-input.md](carousel-input.md) | [carousel-summary.md](carousel-summary.md) | Preserves card order and numbers; separates author content from a reader comment |

These last two samples are **textual stand-ins** for an audiovisual segment and a multi-image post, not proof that the skill can read media that was not actually supplied. They illustrate how to work with already accessible transcripts or card text.

## Reproduce the evaluation

1. Open an \`*-input.md\` file.
2. Ask your assistant to use \`$unified-content-notes\` and the indicated action.
3. Compare the new result with the corresponding example output for **information coverage and boundary awareness**, not exact wording.
4. For \`format-only\`, check non-whitespace character identity (also covered by the offline test).

\`\`\`bash
python3 -m unittest discover -s tests -v
\`\`\`

Automated tests check structure and a few deliberate invariants. They **cannot** establish full semantic fidelity, story quality, or media access. Add a source/output test pair when proposing a new content-specific rule.
