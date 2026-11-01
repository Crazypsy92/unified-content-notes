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
- In long opinion pieces, a compact **claim / reasoning / examples** overview table is usually helpful. In stories and format-only work, avoid forcing a table.
- Favor **high-fidelity compression** over extreme brevity: preserve independent claims, meaningful counterexamples, numbers, key dialogue, and turning points.
- Avoid narrator-style commentary such as “the speaker says” when a clean standalone digest is requested.
- Never silently change the text in **format-only** mode.
- Distinguish verifiable facts, quotations, the original creator's claims, the user's own notes, and model-added interpretation.

Explicit instructions from the user take priority over these defaults.

## Examples

The `examples/` directory contains **newly written demonstration sources and outputs**, so this public repository does not republish long excerpts from other creators' videos, books, or users' private notes.

| Example | Demonstrates |
| --- | --- |
| [`argument-input.md`](examples/argument-input.md) → [`argument-summary.md`](examples/argument-summary.md) | Summarize a multi-point argument with numerical details |
| [`narrative-input.md`](examples/narrative-input.md) → [`narrative-summary.md`](examples/narrative-summary.md) | Preserve events, motivation, and a small reveal |
| [`format-input.md`](examples/format-input.md) → [`format-only.md`](examples/format-only.md) | Keep every non-format character unchanged |

Examples illustrate output *behaviors*, not mandatory templates.

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