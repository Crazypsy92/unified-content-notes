# Unified Content Notes

**One skill. Three actions. Structure-aware notes for almost any content.**

Unified Content Notes turns source material into clear, reusable Markdown. It handles short-form videos, Bilibili lectures, Xiaohongshu image posts, X threads, podcasts, articles, movies, novels, documentaries, tutorials, and personal stories **when the relevant source content is provided**.

Instead of creating a separate skill for each platform or genre, it first identifies **what you want done**, then adapts the output to **how the content is organized**.

> The skill instructions and default written output are in Chinese. This README is in English for easier public sharing. You can request another output language or formatting style explicitly.

## What it does

| Action | Use it when you want to... | What changes |
| --- | --- | --- |
| **Summarize** | Condense a long video transcript, extract arguments, recap a novel or movie | Removes repetition, organizes the logic, retains key evidence, examples, character arcs, and plot turns |
| **Explain** | Understand a complex idea, documentary claim, character decision, or narrative | Expands the *reasoning* and context while distinguishing source material from additional interpretation |
| **Format only** | Turn messy copied text, dialogue, or a short story into readable Markdown | **Preserves the wording and event order**; adjusts paragraphs, headings, spacing, and verified copy/paste artifacts only |

It routes content by structure rather than by website: **arguments, narrative, documentary/knowledge, procedures, conversations, image carousels, threads, and mixed forms**.

## Quick start

### Install as a local Codex skill

1. Download or clone this repository.
2. Copy the **entire repository folder** to your skills directory, for example:
   - Linux/macOS/WSL: `~/.agents/skills/unified-content-notes/`
   - Windows: `%USERPROFILE%\.agents\skills\unified-content-notes\`
3. Verify that the folder contains `SKILL.md` and `references/`.
4. Start a new Codex session if your client needs to refresh available skills.

The layout should look like this:

```text
~/.agents/skills/
└── unified-content-notes/
    ├── SKILL.md
    ├── references/
    │   ├── platform-and-source.md
    │   ├── quality-and-format.md
    │   └── structure-router.md
    └── ...
```

This is a **file-based prompt skill**, not a program or a ChatGPT plugin. Copying this repository does not automatically install it into a ChatGPT conversation or grant browsing, download, transcription, or OCR capabilities.

## Usage examples

```text
$unified-content-notes 总结这段视频口播，高保真浓缩，保留论点、论据和关键案例。
$unified-content-notes 梳理这部电影的完整剧情与人物转变，不要编造原片中没出现的场景。
$unified-content-notes 讲解这篇纪录片的论证过程，区分事实、采访者观点和推断。
$unified-content-notes 总结这组小红书图文，保留卡片顺序并融合图中的文字。
$unified-content-notes 只改这篇小故事的 Markdown 排版，一个字也不要改。
```

Natural language works too; the `$unified-content-notes` prefix is useful where the skill loader supports explicit invocation.

## Default writing conventions

- Preserve the **original title**. If no title is supplied, do not pretend a new one is original.
- The highest heading level in generated Markdown is `##`; use `###` for subsections.
- Indent Chinese prose paragraphs with **two full-width spaces** (`　　`). Do not indent tables, Markdown lists, headings, or quotes.
- For long opinion-led material with cases, use a **claim / source case or evidence / reasoning / takeaway** table, followed by analytical prose that expands each important case. Do not turn an argument into a light-novel or storybook retelling. Stories remain narrative; format-only work gets no added analysis table.

### Relationship opinion pieces: analytical layout, not story-style prose

For relationship and emotional-content material with several real-life examples, use the **claim-and-case analysis layout** by default:

1. State the article's central idea in direct language.
2. Add a compact table mapping each claim to its source case/evidence, reasoning, and conclusion.
3. Develop the body as a structured analytical essay. Give each major claim a clear subsection; present each important case with only the relevant context, actions, key dialogue, and outcome, then explain what the evidence supports.
4. Keep cases as evidence, not as light-novel scenes. Do not invent atmosphere, gestures, inner monologues, suspense, or dramatic endings.
5. Format meaningful couple dialogue in restrained Markdown quote blocks with clear speaker labels, followed immediately by analysis.
6. Use complete analytical paragraphs and a small number of meaningful headings. Avoid one-sentence-per-line fragmentation, excessive subheadings, and decorative formatting.

See [references/relationship-analysis.md](references/relationship-analysis.md) for the full Chinese writing and layout specification, and [the relationship analysis example](examples/relationship-argument-summary.md) for a worked sample.
- Favor **high-fidelity compression** over extreme brevity: preserve independent claims, meaningful counterexamples, numbers, key dialogue, and turning points.
- Avoid narrator-style commentary such as “the speaker says” when a clean standalone digest is requested.
- Never silently change the text in **format-only** mode.
- Distinguish verifiable facts, quotations, the original creator's claims, the user's own notes, and model-added interpretation.

Explicit instructions from the user take priority over these defaults.

## Opinion analysis and case-rich writing

For argument-led material—especially relationship commentary with several real-life examples—the default is an **analytical article with evidence**, not a storybook or light-novel retelling.

The expected layout is:

1. Preserve the original title and add source metadata only when available.
2. State the central idea directly in a short **Article thesis** section.
3. Add a compact **claim / source case or evidence / reasoning / takeaway** table.
4. Write the body as a structured analysis, using headings that express the argument (for example, “Why delayed communication creates uncertainty”), not literary scene titles.
5. Expand every important case in the body: context, observable facts, key dialogue, response or outcome, and what the case supports.
6. Compare cases when their differences help explain the argument.
7. Close with the actual takeaway and any necessary limits.

**Do not turn analytical material into a fictionalized narrative.** No invented atmosphere, inner monologue, gestures, suspense, or dialogue. Case detail is included to support reasoning, not to create a dramatic scene.

### Dialogue formatting

Original couple dialogue may be visually separated with speaker labels:

> **Partner A:** I can understand that you will be late, but why didn't you tell me earlier?
>
> **Partner B:** I thought I would finish soon, but it took longer than expected.

Follow the exchange with analysis. For longer conversations, a compact comparison table may help distinguish the actual wording, observable concern, and possible effect. Keep original dialogue separate from any newly suggested rewrite.

See [the argument-analysis layout guide](references/argument-analysis-layout.md) and the [case-rich example](examples/argument-case-output.md).

## Examples

The `examples/` directory contains **newly written demonstration sources and outputs**, so this public repository does not republish long excerpts from other creators' videos, books, or users' private notes.

| Example | Demonstrates |
| --- | --- |
| [Argument input](examples/argument-input.md) → [summary](examples/argument-summary.md) / [explanation](examples/argument-explanation.md) | Same source, two distinct actions; preserves 180°C / 20-minute details and separates analysis from source claims |
| [Case-rich argument input](examples/argument-case-input.md) → [analysis output](examples/argument-case-output.md) | Demonstrates a claim/evidence/reasoning table, analytical case expansion, and readable dialogue blocks without storybook prose |
| [Narrative input](examples/narrative-input.md) → [summary](examples/narrative-summary.md) / [explanation](examples/narrative-explanation.md) | Keeps event order, character motivation, the reveal, and the deliberately unresolved ending |
| [Documentary input](examples/documentary-input.md) → [explanation](examples/documentary-explanation.md) | Separates observation, expert statement, a resident's personal experience, plans, and missing evidence |
| [Carousel input](examples/carousel-input.md) → [summary](examples/carousel-summary.md) | Preserves card order, numeric examples, author additions, and reader comments as separate sources |
| [Format input](examples/format-input.md) → [format-only](examples/format-only.md) | Keeps every non-layout character unchanged |
| [Relationship argument input](examples/relationship-argument-input.md) → [analysis summary](examples/relationship-argument-summary.md) | Maps claims to cases, expands evidence in analytical prose, and formats dialogue without novel-style narration |

Examples illustrate output *behaviors*, not mandatory templates. See the [examples guide](examples/README.md) for the full input/output matrix and how to reproduce comparisons.

## Boundaries

- **Inputs matter:** a title or link alone does not give the skill access to the full video, book, or post. Supply transcripts, text, screenshots, notes, or accessible content.
- **It does not download videos or bypass platform protections.** Source acquisition and speech-to-text are separate workflows.
- **No fabricated evidence:** summaries must not claim to have seen visuals when only transcripts were provided, or invent plot details absent from the available material.
- **No automatic fact-checking:** source claims are not necessarily true. Request verification separately, and use reputable sources when available.
- **Rights matter:** summarize or analyze copyrighted content responsibly; do not reconstruct entire unavailable works or republish substantial third-party text without permission.
- **Not all inputs are fully tested:** complete films, novels, documentary audiovisual tracks, multi-image social posts, and large multi-author threads require more end-to-end evaluation.

## Contributing and validating

The skill is written in Markdown and requires **no runtime dependencies**. You can run lightweight repository checks with Python 3.9+:

```bash
python3 -m unittest discover -s tests -v
```

For improvements, submit one realistic, rights-cleared source/output example showing the failure, then adjust the smallest relevant rule (usually in `references/`). Keep the three actions distinct; avoid adding one new mode per platform.

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

Licensed under the [MIT License](LICENSE). Please replace the generic copyright-holder line if you prefer to publish under your own name or organization. Third-party materials mentioned in prompts or supplied by users retain their original rights.