# Unified Content Notes

**One skill. Three actions. Structure-aware notes for almost any content.**

Unified Content Notes turns source material into clear, reusable Markdown. It supports short-form videos, Bilibili lectures, Xiaohongshu image posts, X threads, podcasts, articles, movies, novels, documentaries, tutorials, conversations, and personal stories **when the relevant source content is provided or actually accessible**.

It separates two decisions:

- **Action:** what the user wants done — summarize, explain, or format only.
- **Content structure:** how the material is organized — argument, narrative, dialogue, documentary, method, short copy, image carousel, or a mixture.

The skill uses a small entrypoint, shared core rules, and optional domain modules. It is one skill, not a separate prompt for every platform or topic.

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
├── references/
│   ├── platform-and-source.md
│   └── legacy compatibility notes (old reference paths)
├── examples/
└── tests/
~~~

### Shared rules and specialized modules

- **Core rules** define common behavior once: action routing, source boundaries, Markdown style, and quality checks.
- **Content modules** define how a type of material should be organized.
- **Domain modules** add specialized analysis without copying their parent module. For example, relationship analysis extends the general argument-analysis module.
- **Optional references** are loaded only when a platform-specific input structure matters.

The entrypoint instructs compatible agents to load shared core rules, then only the content modules needed for the current task. A child module must be read together with its declared parent. This reduces duplicated instructions and avoids loading unrelated topic rules. Actual context savings depend on whether the agent supports reading referenced files on demand.

## Quick start

### Install as a local Codex skill

1. Download or clone this repository.
2. Copy the **entire repository folder** to your skills directory, for example:
   - Linux/macOS/WSL: ~/.agents/skills/unified-content-notes/
   - Windows: %USERPROFILE%\.agents\skills\unified-content-notes\
3. Verify that the folder contains SKILL.md, core/, modules/, and references/.
4. Start a new Codex session if your client needs to refresh available skills.

Do not copy only SKILL.md; the entrypoint references the supporting files.

This is a **file-based prompt skill**, not a program or a ChatGPT plugin. Copying the repository does not automatically install it into a ChatGPT conversation or grant browsing, download, transcription, or OCR capabilities.

## Choose a mode

The skill routes by structure, not by website:

| Prompt mode | Use it for | Typical output |
| --- | --- | --- |
| **文案 + 观点分析型** | Relationship commentary, workplace opinions, social observations, personal-growth arguments | Original title + compact claim/evidence/reasoning table when useful + analytical body |
| **文案 + 情感观点分析** | Relationship, communication, attraction, marriage, boundaries, and interpersonal conflict | General argument structure plus analysis of observable behavior, dialogue, expectations, interaction, and boundaries |
| **文案 + 故事 / 经历型** | Real-life stories, relationship experiences, narrative posts | Event order, people, actions, key dialogue, emotional changes, and outcome |
| **文案 + 情侣对话型** | Chat logs and conflict conversations | Speaker labels and readable dialogue; analysis or rewrite only when requested |
| **文案 + 短文案 / 金句型** | Short quotes, captions, one-line opinions | Preserve original wording; group lightly when useful |
| **文案 + 方法 / 经验型** | Advice, communication methods, practical lessons, tutorials | Goal, principles, steps, examples, conditions, and limitations |
| **文案 + 个人感悟型** | First-person reflections and journals | Preserve first-person voice, uncertainty, and personal judgment |
| **作品 + 剧情 / 人物解读型** | Film, novel, documentary, or character analysis | Source facts and character actions first; interpretation grounded in evidence |
| **图文 + 多页卡片型** | Carousels, screenshots, slide-like posts | Preserve page order, text, numbers, and relationships |
| **混合型 / 自动判断** | Sources containing arguments, cases, dialogue, and practical advice | Route each section according to its actual structure |

### Important distinction

**情感观点分析 is not a second layout template.** It inherits the general argument-analysis structure and adds relationship-specific lenses. The original title, source line, optional claim/evidence table, case expansion, and general quality rules remain defined only once in core/argument-analysis.md.

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
- For argument-led material, use a compact table when it improves navigation; keep the body complete and case-rich.
- Favor high-fidelity compression: remove repetition, not evidence.
- Keep the source's narrative perspective and emotional force; avoid unnecessary narrator-style commentary.
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
~~~

See CONTRIBUTING.md for the module design and contribution rules.
