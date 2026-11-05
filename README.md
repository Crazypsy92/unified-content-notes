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

## Choose a mode

The skill uses **two independent choices**:

- **Action** — what you want done: summarize, explain, or format only.
- **Content mode** — what kind of material it is: opinion, story, dialogue, short copy, method, personal reflection, and so on.

You can specify both, or simply name the content mode. If you only say “整理一下”, the skill infers the best fit from the source and defaults to high-fidelity summarization. Explicit instructions always take priority.

### Actions

| Action | Use it for | Result |
| --- | --- | --- |
| **Summarize / 高保真浓缩** | Condense while retaining the source's independent ideas and evidence | A readable, structured note; removes repetition, not essential reasoning |
| **Explain / 深度讲解** | Understand why a claim works, how a process unfolds, or what a character's actions mean | Source-grounded explanation with additional interpretation clearly distinguished |
| **Format only / 只改格式** | Improve Markdown readability without rewriting | Original wording and event order are preserved; no analysis or extra content is added |

### Content modes

| Prompt mode | Use it for | Typical output |
| --- | --- | --- |
| **文案 + 观点分析型** | Relationship commentary, opinion-led short videos, arguments about communication, attraction, marriage, boundaries, or personal growth | Original title + compact claim/evidence/reasoning table + high-fidelity analytical body; important cases are explained in the body, not merely listed in the table |
| **文案 + 故事 / 经历型** | Real-life stories, relationship experiences, narrative posts, personal anecdotes | Event order, people, actions, key dialogue, emotional changes, and outcome; no forced argument table |
| **文案 + 情侣对话型** | Chat logs, conflict conversations, date or relationship dialogue | Clear speaker labels and readable dialogue blocks; analysis or rewrite is added only when requested |
| **文案 + 短文案 / 金句型** | Short quotes, captions, one-line opinions, quote collections | Preserve original wording; group by theme when useful; do not inflate short lines into essays |
| **文案 + 方法 / 经验型** | Advice, communication methods, practical lessons, step-by-step experience | Problem, principle, steps, examples, conditions, and limitations |
| **文案 + 个人感悟型** | First-person reflections, journals, lessons learned, emotional processing | Preserve the writer's first-person voice, uncertainty, and personal judgment |
| **作品 + 剧情 / 人物解读型** | Film, novel, documentary, or character analysis | Plot facts and character actions first; interpretation is grounded in specific evidence |
| **图文 + 多页卡片型** | Xiaohongshu carousels, screenshot collections, slide-like posts | Preserve page order, text in each image, numbers, and relationships between cards |
| **混合型 / 自动判断** | A source that combines opinion, cases, dialogue, and practical advice | Route each section according to its actual structure instead of forcing one template |

### Copy-and-use prompts

Use these directly in Codex or a compatible agent:

> **文案 + 观点分析型：** 使用 $unified-content-notes，总结这份文案。按高保真浓缩处理，保留原始标题、独立论点、关键论据、案例、对话、数字、比喻和推理过程。表格用于总览，正文要把重要案例讲清楚；不要写成第三人称视频解析，也不要为了缩短篇幅删掉论证。

> **文案 + 故事型：** 使用 $unified-content-notes，整理这篇故事。保留人物关系、事件顺序、关键动作、对话、情绪变化和结局，不要强行改成观点分析或补写原文没有的细节。

> **文案 + 情侣对话型：** 使用 $unified-content-notes，把这段对话按说话人和轮次排版，保留原话。先不要改写；如需分析，再单独解释双方表达的需求和冲突点。

> **文案 + 短文案 / 金句型：** 使用 $unified-content-notes，保留原句和原始标题，按主题归类；不要把短句扩写成文章，不确定的来源标为未注明。

> **文案 + 方法 / 经验型：** 使用 $unified-content-notes，整理成方法笔记，保留步骤顺序、具体示例、参数、适用条件和注意事项。

> **文案 + 个人感悟型：** 使用 $unified-content-notes，整理这段个人感悟，保留第一人称、原有情绪和不确定之处，不要改写成第三人称大道理。

> **只改格式：** 使用 $unified-content-notes，只整理 Markdown 排版，不删字、不润色、不增加分析、不改变事件顺序。

### Automatic selection

You do not have to memorize the mode list. You can simply say:

> 使用 $unified-content-notes，你先判断这份材料属于什么类型，再按最合适的方式高保真整理。

The skill should infer the structure, avoid unnecessary clarification, and ask only when a missing detail would materially change the result.

## Default writing conventions

- Preserve the **original title**. If no title is supplied, do not pretend a new one is original.
- The highest heading level in generated Markdown is `##`; use `###` for subsections.
- Indent Chinese prose paragraphs with **two full-width spaces** (`　　`). Do not indent tables, Markdown lists, headings, or quotes.
- For opinion-led material, keep the original title, add the source once, use a compact claim/evidence/reasoning table, then write a high-fidelity body in the source's logical order. Preserve the cases and reasoning needed to support each claim; remove repetition, not evidence. Do not turn it into a third-person video report or a fictionalized story.

- Favor **high-fidelity compression** over extreme brevity: preserve independent claims, meaningful counterexamples, numbers, key dialogue, and turning points.
- Avoid narrator-style commentary such as “the speaker says” when a clean standalone digest is requested.
- Never silently change the text in **format-only** mode.
- Distinguish verifiable facts, quotations, the original creator's claims, the user's own notes, and model-added interpretation.

Explicit instructions from the user take priority over these defaults.

## Opinion analysis and case-rich writing

For argument-led material—especially relationship commentary with several real-life examples—the default is a **high-fidelity analytical article**, not a third-person video report and not a fictionalized story.

Use this natural sequence:

1. Preserve the original title.
2. Add the source once beneath the title, only when known.
3. Place a compact claim/evidence/reasoning table near the beginning. Keep it readable (normally no more than four columns).
4. Continue with the body in the source's argument order. Use only the logical subheadings needed to make the reasoning easy to follow; do not force repeated template headings such as “Article thesis”, “Body summary”, or “Final takeaway”.
5. Keep the original speaker's narrative perspective and emotional force. Do not mechanically convert every passage into first person or second person.
6. Expand important cases in the body: context, what happened, key actions or dialogue, response, outcome, and why the case supports the claim. The table cannot replace this.
7. Add a short boundary note only when a claim is overgeneralized, unsupported, or needs verification. Keep the user's own reflection separate and place it at the end when present.

**High-fidelity compression means removing repetition, not removing evidence.** There is no fixed word count or compression ratio. Preserve independent claims, meaningful examples, numbers, dialogue, analogies, counterexamples, and reasoning steps. If several cases support similar conclusions but contain different evidence, do not collapse them into one generic example.

Avoid narrator-style phrases such as “the author believes”, “the original text says”, “the speaker gives an example”, or “this article is about”. Write the claim or event directly. Attribution belongs in the source line unless distinguishing speakers or viewpoints is necessary.

Do not invent scene details, inner thoughts, gestures, dialogue, or outcomes. Do not turn argument-led material into a light novel or storybook. Conversely, do not reduce it to a bare list of claims: the body must retain enough evidence and explanation to stand on its own.

For visual quality, use coherent paragraphs, a restrained amount of bold text, a compact table, and a small number of meaningful subheadings. Avoid both a wall of text and a heading every few lines.

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