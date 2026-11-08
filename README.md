# Unified Content Notes

**One skill. Three actions. Structure-aware notes for almost any content.**

Unified Content Notes turns source material into clear, reusable Markdown. It supports short-form videos, Bilibili lectures, Xiaohongshu image posts, X threads, podcasts, articles, movies, novels, documentaries, tutorials, conversations, and personal stories **when the relevant source content is provided or actually accessible**.

It separates two decisions:

- **Action:** what the user wants done — summarize, explain, or format only.
- **Content structure:** how the material is organized — argument, narrative, dialogue, documentary, method, short copy, image carousel, or a mixture.

The skill uses a small entrypoint, shared core rules, optional domain modules, and a private user-preference overlay. It is one skill, not a separate prompt for every platform or topic.

> The skill instructions and default written output are in Chinese. This README is in English for easier public sharing. Users can request another output language or formatting style explicitly.

## What it does

| Action | Use it when you want to... | What changes |
| --- | --- | --- |
| **Summarize** | Condense a transcript, extract arguments, recap a story or work | Removes repetition while retaining independent claims, evidence, cases, and narrative turns |
| **Explain** | Understand why a claim works, how a process unfolds, or what a character's actions mean | Adds source-grounded reasoning and clearly distinguished interpretation |
| **Format only** | Make copied text or dialogue readable without rewriting | Preserves wording and event order; adjusts layout only |

## Architecture

SKILL.md is the entrypoint and routing contract. Rules are separated by responsibility:

~~~text
unified-content-notes/
├── SKILL.md
├── core/
│   ├── action-router.md
│   ├── structure-router.md
│   ├── source-boundaries.md
│   ├── transcript-cleanup.md
│   ├── technical-knowledge-notes.md
│   ├── markdown-style.md
│   ├── quality-check.md
│   ├── argument-analysis.md
│   ├── narrative-analysis.md
│   ├── knowledge-analysis.md
│   ├── dialogue-analysis.md
│   ├── method-notes.md
│   └── format-only.md
├── modules/
│   └── relationship-analysis.md
├── preferences/
│   ├── README.md
│   └── user-preferences.template.md
├── references/
│   ├── obsidian-argument-layout.md
│   ├── obsidian-technical-notes.md
│   ├── platform-and-source.md
│   └── legacy compatibility notes (old reference paths)
├── examples/
└── tests/
~~~

### Shared rules and specialized modules

- **Core rules** define common behavior once: action routing, source boundaries, Markdown style, and quality checks.
- **Content modules** define how a type of material should be organized.
- **Domain modules** add specialized analysis without copying their parent module. For example, relationship analysis extends the general argument-analysis module and adds behavior, needs, reciprocity, and relationship-boundary analysis, not a second writing template.
- **User preferences** are an optional third layer for presentation choices such as language, heading depth, paragraph indentation, density, and tone. The repository publishes a neutral template; a filled `preferences/user-preferences.md` is local-only and ignored by Git.
- **Optional references** are loaded only when a platform-specific input structure matters.

The three working layers are **Core → Modules → User Preferences**. Load shared core rules first, then only the content/domain modules needed for the task, and finally apply a local preference file if one exists. A child module must be read together with its declared parent. Preferences affect presentation defaults only; they cannot invent source facts, weaken source-integrity rules, or silently change a format-only task. The current task's explicit instructions take priority over saved preferences. Actual context savings depend on whether the agent supports reading referenced files on demand.

## Quick start

### Install as a local Codex skill

1. Download or clone this repository.
2. Copy the **entire repository folder** to your skills directory, for example:
   - Linux/macOS/WSL: ~/.agents/skills/unified-content-notes/
   - Windows: %USERPROFILE%\.agents\skills\unified-content-notes\
3. Verify that the folder contains SKILL.md, core/, modules/, preferences/, and references/.
4. Start a new Codex session if your client needs to refresh available skills.
5. Optional: copy `preferences/user-preferences.template.md` to `preferences/user-preferences.md` and edit it for your own writing preferences. This local file is ignored by Git and should not be committed.

Do not copy only SKILL.md; the entrypoint references the supporting files. The preference template is inactive until you create the local `user-preferences.md` file.

This is a **file-based prompt skill**, not a program or a ChatGPT plugin. Copying the repository does not automatically install it into a ChatGPT conversation or grant browsing, download, transcription, or OCR capabilities.

#### User preference layer

The optional third layer is for **your own presentation defaults**, not a second set of content-analysis rules:

1. Copy `preferences/user-preferences.template.md` to `preferences/user-preferences.md`.
2. Fill only the preferences that are useful to you; leave the rest at their defaults.
3. The skill reads this file only when it exists. The template itself is documentation, not an active configuration.
4. `preferences/user-preferences.md` is ignored by Git so personal settings are not accidentally published.

The preference layer may set output language, target format, heading depth, paragraph indentation, compression density, source-retention preference, highlighting preference, and tone. It cannot override source integrity, copyright boundaries, the requested action, or format-only protection. A specific instruction in the current request overrides a saved preference.

## Obsidian layout and usage

The **观点分析型** mode now uses the confirmed Obsidian reading structure by default when Obsidian is the target:

1. One original `##` heading **per topic**; known creator/platform consolidated into one source line.
2. `[!abstract]` claim/evidence/reasoning/conclusion table (usually four columns).
3. `[!summary]` high-fidelity condensed body. Important cases must retain their background, actions, original dialogue/numbers, responses/outcomes, and logic; remove repetition, **not** evidence.
4. Optional `[!tip]` personal insight and `[!note]` reasoning caveats; preserve source and author boundaries.
5. `[!quote]-` collapsed **original text** (if provided). Reflow paragraphs with two full-width leading spaces while preserving wording; do not reconstruct material unavailable from the source.

This uses native Obsidian Callouts and theme variables; no external CSS snippets or plugins are required. For non-Obsidian environments use ordinary Markdown tables and labels without changing the information requirements. [Exact Callout and highlighting syntax](references/obsidian-argument-layout.md).

#### Obsidian Callout troubleshooting and simplified originals

独立 Callout 之间务必保留**真正的空白源码行**，而不是单独的 `>` 行。后者仍属于前一张卡片，可能导致 `[!note]`、`[!quote]-` 在阅读视图中直接显示。运行：

~~~bash
python tests/check_obsidian_callouts.py your_output.md
# 可选（需安装 opencc-python-reimplemented）：
python tests/check_obsidian_callouts.py your_output.md --simplified
~~~

原始 ASR 默认保留，不把繁简转换、标点补充或段落重排说成逐字原文。若用户明确要求“校订口播 / 修正 ASR / 让原文可读”，读取 core/transcript-cleanup.md，输出折叠的「口播转录 · 断句校订版」：补标点、按语义分段、只改高置信度错词；无法确认的词句用“听辨存疑”标记。没有音频时必须注明“基于 ASR 文本校订，未核听音频”。原始 ASR 另存备份。

#### Semantic highlighting

For Obsidian **argument-analysis** summarize / explain outputs, semantic highlighting is applied to **both the condensed body and the folded original text**:

- **Cyan:** complete core claims, key judgments, and conclusions.
- **Green:** concrete cases, evidence, facts, numbers, and meaningful actions.
- **Orange:** reasoning turns, contrasts, counterexamples, qualifications, and risks.

Highlight meaningful phrases or complete clauses—not isolated nouns or random keywords. For a verbatim original, removing added <span> tags must recover the supplied source text. For an explicitly requested ASR reading edition, removing spans must recover the corrected reading text, while the untouched ASR source is retained separately. A single legend near the beginning of a long document is enough. Format-only mode does not add semantic highlights unless explicitly requested. The spans use Obsidian theme variables such as var(--color-cyan), not hard-coded colors.

**What relationship analysis adds:** It does not create another layout. When the source is about intimate relationships, it supplements the same structure with two-party behavior, expectations, communication, reciprocity, timelines, and uncertainty; a pure conversation or a personal story without an argument can instead use dialogue/narrative routing. See [relationship analysis](modules/relationship-analysis.md).

#### ASR transcript cleanup

When a spoken transcript arrives as one long, punctuation-free block, the skill can create a readable transcript edition without pretending to have verified the audio:

- Keep the raw ASR transcript untouched as a separate backup.
- Add punctuation and split paragraphs around complete ideas, examples, numbered points, transitions, and conclusions.
- Correct only high-confidence recognition errors; mark uncertain names, numbers, phrases, and cut-off endings instead of guessing.
- Label the result as a corrected reading edition, not a verbatim transcript. If no audio is available, state that the cleanup is text-based and has not been audio-checked.

**Example prompts:**

~~~text
$unified-content-notes 文案 + 观点分析型。Obsidian 排版：每个话题一个标题，表格+完整浓缩正文+折叠原文，案例不要遗漏。
$unified-content-notes 文案 + 情感观点分析。继承同样的 Obsidian 版式，额外分析双方行为、关系责任和边界，不要合并人物观点。
$unified-content-notes 把原文和已有观点分析稿逐话题融合，来源只出现一次，保留原文文字，仅重新分段。
$unified-content-notes 这是 ASR 口播，帮我校订原文：补标点、按语义分段、修正高置信错词；不确定处标记存疑，保留未处理 ASR 备份。
~~~

## Choose a mode

The skill routes by structure, not by website:

| Prompt mode | Use it for | Typical output |
| --- | --- | --- |
| **文案 + 观点分析型** | Relationship commentary, workplace opinions, social observations, personal-growth arguments | **Per-topic original title + claim/evidence/reasoning/conclusion table + case-rich condensed body + collapsible source when provided** |
| **文案 + 情感观点分析** | Relationship, communication, attraction, marriage, boundaries, and interpersonal conflict | **Inherits the above full layout**, then examines both parties' actions, needs, interaction, responsibility, and uncertainty |
| **文案 + 故事 / 经历型** | Real-life stories, relationship experiences, narrative posts | Event order, people, actions, key dialogue, emotional changes, and outcome |
| **文案 + 情侣对话型** | Chat logs and conflict conversations | Speaker labels and readable dialogue; analysis or rewrite only when requested |
| **文案 + 短文案 / 金句型** | Short quotes, captions, one-line opinions | Preserve original wording; group lightly when useful |
| **文案 + 方法 / 经验型** | Advice, communication methods, practical lessons, tutorials | Goal, principles, steps, examples, conditions, and limitations |
| **文案 + 个人感悟型** | First-person reflections and journals | Preserve first-person voice, uncertainty, and personal judgment |
| **作品 + 剧情 / 人物解读型** | Film, novel, documentary, or character analysis | Source facts and character actions first; interpretation grounded in evidence |
| **图文 + 多页卡片型** | Carousels, screenshots, slide-like posts | Preserve page order, text, numbers, and relationships |
| **混合型 / 自动判断** | Sources containing arguments, cases, dialogue, and practical advice | Route each section according to its actual structure |

### Important distinction

**情感观点分析 is not a second layout template.** It inherits the general argument-analysis structure and adds relationship-specific lenses. The title, required argument table, case-rich condensed narrative, folded original (when provided), and quality rules remain defined once in core/argument-analysis.md. Domain modules do not replace the core output layout.

## Copy-and-use prompts

~~~text
$unified-content-notes 总结这段视频口播，高保真浓缩，保留论点、论据和关键案例。
$unified-content-notes 文案 + 观点分析型，按通用观点分析结构整理。
$unified-content-notes 文案 + 情感观点分析，结合双方行为、对话和关系变化分析。
$unified-content-notes 梳理这部电影的剧情与人物转变，不要编造原作没有的场景。
$unified-content-notes 讲解这篇纪录片的证据链，区分事实、采访和推断。
$unified-content-notes 只改这篇小故事的 Markdown 排版，一个字也不要改。
~~~

Natural language works too. The prefix is useful where the skill loader supports explicit invocation.

## Default writing conventions

- Preserve the original title. If no title is supplied, do not pretend a new one is original.
- The highest heading level in generated notes is ##; use ### for subsections.
- Indent Chinese prose paragraphs with **two full-width spaces** (　　). Do not indent tables, Markdown lists, headings, or quotes.
- For the **argument-analysis mode**, always include a claim/evidence/reasoning/conclusion table and a fully readable condensed narrative with concrete cases; when original material is available, include it in a collapsible Obsidian Callout.
- Favor high-fidelity compression: remove repetition, not evidence.
- Keep the source's narrative perspective, concrete cases, and emotional force; avoid unnecessary narrator-style commentary. Each topic gets one ## heading; use Obsidian Callout labels, not subheadings, for the table, summary, notes and folded original.
- Never silently change wording in format-only mode.
- Distinguish verifiable facts, creator claims, quotations, user notes, and model-added interpretation.

Explicit user instructions take priority over defaults, subject to source integrity and format-only protection.

## Examples

The examples/ directory contains original demonstration sources and outputs. Examples illustrate behavior and trade-offs; they are not mandatory templates.

| Example | Demonstrates |
| --- | --- |
| [Argument input](examples/argument-input.md) → [summary](examples/argument-summary.md) / [explanation](examples/argument-explanation.md) | Same source, two actions; retains numeric details and separates analysis from source claims |
| [Case-rich argument input](examples/argument-case-input.md) → [analysis output](examples/argument-case-output.md) | Claim/evidence/reasoning table, analytical case expansion, and readable dialogue |
| [Narrative input](examples/narrative-input.md) → [summary](examples/narrative-summary.md) / [explanation](examples/narrative-explanation.md) | Event order, character motivation, reveal, and unresolved ending |
| [Documentary input](examples/documentary-input.md) → [explanation](examples/documentary-explanation.md) | Observation, interview statements, hypotheses, and missing evidence |
| [Carousel input](examples/carousel-input.md) → [summary](examples/carousel-summary.md) | Card order, numbers, and source boundaries |
| [Format input](examples/format-input.md) → [format-only](examples/format-only.md) | Preservation of non-layout characters |

## Boundaries

- A title or link alone does not provide the full video, book, or post.
- The skill does not download videos or bypass platform protections.
- Do not claim to have seen visuals when only a transcript was supplied.
- Source claims are not automatically true; fact-checking is separate unless requested.
- Summarize and analyze copyrighted works responsibly; do not reconstruct unavailable works as substitutes.

## Validation

The skill has no runtime dependencies. Run the offline checks with Python 3.9+:

~~~bash
python3 -m unittest discover -s tests -v

# Validate a generated technical knowledge note
python3 tests/check_technical_notes.py path/to/note.md
~~~

See CONTRIBUTING.md for the module design and contribution rules.


### Technical knowledge and interview notes

For technical knowledge bases and interview preparation, load `core/technical-knowledge-notes.md`. The scope is broader than embedded fundamentals: MCU / single-chip systems, RTOS, drivers, buses and protocols, LVGL / HMI, automotive electronics, industrial control, robotics, ROS 2, machine vision, embodied intelligence, and other engineering or computer-technology topics. This is a separate route from documentary / factual knowledge summaries.

The Obsidian layout uses one question heading per topic:

- `# Document title`
- `## Chapter`
- `### Original question`

No lower-level headings are generated inside a question. Use ordinary paragraphs, bold lead-ins, lists, code blocks, and comparison tables. Answers should be speakable in an interview and may include mechanisms, implementation trade-offs, realistic cases, common follow-ups, and boundaries as needed. Clearly separate general principles, platform-specific behavior, real project evidence, public examples, and hypothetical scenarios. Never invent first-person experience or test results. For Obsidian, native section Callouts now create screenshot-like colored content panels: `[!summary]` for core answers, `[!info]` for mechanisms and tables, `[!example]` for grounded engineering cases, and `[!question]` for interview follow-ups. Ordinary text keeps its theme color; usually only one short `==recall phrase==` is highlighted per question. Callout panels are separated by truly empty lines, and no external CSS or inline `<span>` coloring is needed. Formulas use MathJax `$...$` and `$$...$$`. See [the technical Obsidian layout](references/obsidian-technical-notes.md).
