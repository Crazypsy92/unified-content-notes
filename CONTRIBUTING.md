# Contributing to Unified Content Notes

Thank you for helping improve the skill. A documented failure case, a better example, or a clearer rule can be valuable; programming experience is not required.

## Project scope

Unified Content Notes is **one skill with three actions**:

| Action | Goal | Must not do |
| --- | --- | --- |
| Summarize | Compress while retaining independent claims, evidence, cases, and narrative turns | Replace the source with generic advice |
| Explain | Make the source understandable through grounded reasoning and clearly marked interpretation | Invent quotes, causes, scientific proof, or unseen scenes |
| Format only | Improve Markdown layout while preserving wording and order | Paraphrase, silently correct spelling, or omit details |

The platform is an input source, not an action or content genre.

## Module architecture

- SKILL.md is the entrypoint. Keep it concise and focused on routing, loading rules, and universal constraints.
- core/ contains shared rules and reusable content structures. Define each common rule once.
- modules/ contains domain-specific extensions. A module must state its parent (if any), its loading condition, and only the additional rules it contributes.
- preferences/ contains a neutral preference template and instructions. A user's filled user-preferences.md is local-only and must not be committed.
- references/ contains optional source/platform references and compatibility notes; it should not duplicate canonical rules.
- examples/ contains original or rights-cleared input/output pairs.
- tests/ contains dependency-free structural and behavior checks.

### Inheritance and loading rules

1. A specialized module must name its parent module explicitly.
2. Load the parent before the child. The child inherits the parent's general rules and adds only domain-specific analysis.
3. Do not copy common formatting, source-integrity, or quality rules into every module.
4. Load only the modules relevant to the current task; do not load every topic module by default.
5. A domain module may refine its domain-specific lens, but it cannot weaken source integrity or format-only protection.
6. User preferences are loaded only when a local preferences/user-preferences.md exists; the public template is not active by itself.
7. Preferences may customize presentation defaults only. They cannot override source integrity, copyright boundaries, the current task's explicit instructions, or format-only protection.
8. Do not create a new module for every platform or every keyword. Add a module only when it contains genuinely reusable rules that cannot fit cleanly in an existing core structure.

## Ways to contribute

- **Report a failure:** provide the content type, requested action, short source, actual result, and expected result.
- **Add a test case:** contribute an original or rights-cleared input/output pair in examples/.
- **Improve a shared rule:** update the smallest relevant file in core/.
- **Improve a domain-specific rule:** update the relevant file in modules/.
- **Adjust a user's defaults:** edit a local copy of preferences/user-preferences.template.md; do not commit personal preference files.
- **Improve source guidance:** update references/ only when the guidance is optional or platform-specific.
- **Improve documentation or validation:** update the README, contribution guide, or offline tests.

## Get started

1. Fork this repository on GitHub.
2. Clone your fork and create a topic branch.
3. Make a focused change.
4. Add or update an example / test when behavior changes.
5. Run the offline checks.
6. Open a pull request against main.

~~~bash
git clone https://github.com/YOUR_USERNAME/unified-content-notes.git
cd unified-content-notes
git checkout -b docs/improve-relationship-analysis
python3 -m unittest discover -s tests -v
git add .
git commit -m "docs: refine relationship analysis module"
git push -u origin docs/improve-relationship-analysis
~~~

## Example requirements

A good example has:

1. An explicit action: summarize, explain, or format only.
2. Enough source detail to test the intended behavior.
3. Observable acceptance criteria, such as retaining a numeric limit, preserving a twist, distinguishing speakers, or preserving non-layout characters.
4. An output grounded in that source.
5. A description in examples/README.md explaining what the sample tests and does not prove.

Prefer original demonstration content. Do not submit credentials, personal information, sensitive unpublished material, or copyrighted content you do not have permission to publish.

## Style and design guardrails

- Use English for public-facing project documentation and paths; the skill's default note output remains Chinese unless the user asks otherwise.
- Preserve source titles, use ## as the highest generated-note heading, and indent Chinese prose paragraphs with two ideographic spaces.
- Do not force tables on short stories or format-only work.
- Keep the three actions distinct and content modules structure-aware.
- Keep common rules in core files, domain-only rules in modules, and personal presentation defaults in the optional preferences layer.
- Do not commit preferences/user-preferences.md; it may contain personal settings.
- Do not promise browsing, downloading, transcription, OCR, or full-work access that the active assistant does not have.
- Distinguish source claims, user annotations, and external interpretation.

## Pull request checklist

- [ ] The change addresses a concrete scenario.
- [ ] The action and content structure remain distinct.
- [ ] Any specialized module declares its parent and loading condition.
- [ ] User preferences are optional, local-only, and cannot weaken invariants.
- [ ] Common rules are not duplicated across modules.
- [ ] Only relevant modules are loaded for a task.
- [ ] New examples are original, licensed, or redistributable.
- [ ] Source facts, events, and details are preserved.
- [ ] Format-only outputs preserve non-format characters.
- [ ] Existing examples, documentation links, and tests pass.
- [ ] No unnecessary version suffix was added to the project name.

## Suggested pull request description

~~~markdown
## Problem
What content failed, and how?

## Change
Which core rule, module, example, or test changed?

## Verification
- Command: python3 -m unittest discover -s tests -v
- Result:
- Manually checked example(s):

## Boundaries
What source information or capability was unavailable?
~~~

## Maintainer review

We value fidelity, useful explanation, and readable results over aggressive compression or decorative formatting. Automated tests can catch structural errors; they cannot prove that a summary faithfully represents a complete movie, novel, or documentary. Reviewers should inspect the source/output pair.

## License and conduct

Respect third-party rights and other contributors. Contributions are distributed under the repository's MIT License.
