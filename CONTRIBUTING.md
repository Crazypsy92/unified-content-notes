# Contributing to Unified Content Notes

Thank you for helping improve the skill. You do **not** need to be a programmer: a well-documented failure case or a clearer Markdown rule can be a valuable contribution.

## Project scope

Unified Content Notes is **one skill with three actions**, not a collection of per-platform prompts:

| Action | Goal | Must not do |
| --- | --- | --- |
| Summarize | Compress while retaining the main argument, evidence, cases, and narrative turns | Replace the source with generic advice |
| Explain | Make the source understandable through sourced reasoning and clearly marked interpretation | Invent quotes, causes, scientific proof, or unseen scenes |
| Format only | Improve Markdown layout while preserving wording and the original order | Paraphrase, silently correct spelling, or omit details |

The original user request controls which action runs. The platform (Douyin, Bilibili, Xiaohongshu, X, etc.) is a property of the input, **not** a fourth action.

## Ways to contribute

- **Report a failure:** provide the content type, desired action, short source, actual result, and expected result.
- **Add a test case:** contribute an original or rights-cleared input/output pair in \`examples/\`.
- **Improve a rule:** clarify a specific instruction in \`references/\`; keep \`SKILL.md\` focused on universal behavior.
- **Improve documentation:** fix an installation step, broken link, or misleading claim.
- **Improve validation:** extend the offline tests without adding required third-party dependencies.

## Get started

1. Fork this repository on GitHub.
2. Clone your fork and create a topic branch.
3. Make a focused change.
4. Add an example or update a test when changing behavior.
5. Run the offline checks.
6. Open a pull request against \`main\` explaining the change.

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/unified-content-notes.git
cd unified-content-notes
git checkout -b docs/better-documentary-explanations
python3 -m unittest discover -s tests -v
git add .
git commit -m "docs: clarify documentary explanation boundaries"
git push -u origin docs/better-documentary-explanations
\`\`\`

Open a pull request in the GitHub UI. Avoid pushing directly to \`main\` when collaborating.

## How to submit a useful example

Place the files inside \`examples/\`, for example:

\`\`\`text
examples/
├── documentary-input.md
└── documentary-explanation.md
\`\`\`

A good example has:

1. **An explicit task:** summarize, explain, or format only.
2. **Enough original source detail** to test important behavior, but no unnecessary length.
3. **Observable acceptance criteria**, such as keeping a numeric limit, preserving a twist, not confusing two speakers, or preserving non-layout characters.
4. **An output grounded in that source**, with no unexplained facts.
5. **A description in** \`examples/README.md\`: what the sample tests and what it does *not* prove.

Good original samples are better than reproducing copyrighted videos, film scripts, books, or private relationship conversations. Do not submit personal information, credentials, or sensitive unpublished material. If a case is adapted from a real incident, anonymize it and ensure you have the rights to share it.

### Action-specific checks

**Summarize:** verify all independent claims, key numbers, speaker viewpoints, illustrative cases, and important turning points. Remove redundant delivery, **not** supporting evidence.

**Explain:** separate the source's observations, the source's claims, and your added interpretation. If there is no reliable support for a causal link, state the uncertainty. For stories, preserve the difference between what a character knows and what readers later learn.

**Format only:** make no semantic changes. The original title, words, punctuation, dialogues, and chronology must remain unchanged. Layout-only characters and verified copy/paste artifacts may be cleaned. Compare canonicalized text, not merely word counts.

## Style and design guardrails

- Use **English** for public-facing project documentation and paths; the skill's default note output remains **Chinese** unless the user asks otherwise.
- Preserve source titles, use \`##\` as the highest generated-note heading, and indent Chinese prose paragraphs with two ideographic spaces.
- Avoid a mandatory table for short stories or formatting-only work.
- Keep optional templates in \`references/\`; do not create a new sub-skill for each content platform.
- Do not promise browsing, image-reading, transcription, full-film access, or other capabilities that the active assistant does not actually have.
- Maintain a distinction between the source, a user's personal annotations, and external interpretation.

## Pull request checklist

- [ ] The change addresses a concrete scenario.
- [ ] The requested action remains unambiguous.
- [ ] Any new example is original, licensed, or clearly redistributable.
- [ ] The output preserves required source facts, events, and details.
- [ ] Formatting-only outputs preserve non-format characters.
- [ ] Existing examples, documentation links, and tests still pass.
- [ ] No version number was added unnecessarily to the project name.

A short PR description can use:

\`\`\`markdown
## Problem
What content failed, and how?

## Change
Which rule/example/test did you update?

## Verification
- Command: python3 -m unittest discover -s tests -v
- Result:
- Manually checked example(s):

## Boundaries
What source information or capability was unavailable?
\`\`\`

## Maintainer review

We value **fidelity, useful explanation, and a readable result** over aggressive compression or fancy formatting. An automated check can catch structural errors; it cannot prove that a summary faithfully represents a whole movie or documentary. Reviewers should inspect the source/output pair.

## License and conduct

By submitting a contribution, you agree that it may be distributed under this project's MIT License. Respect other contributors, do not add material you do not have permission to publish, and address disagreements with examples rather than personal attacks.
