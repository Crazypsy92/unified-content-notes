#!/usr/bin/env python3
"""Validate headings, sparse Callouts, theme-aware highlights, and Obsidian MathJax."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
import sys

def visible_lines(text: str) -> list[str]:
    out = []
    in_fence = False
    fence_char = chr(96)
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(fence_char * 3) or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return out

def validate(path: Path) -> list[str]:
    source = path.read_text(encoding="utf-8-sig")
    lines = visible_lines(source)
    errors: list[str] = []
    headings = [(i + 1, line) for i, line in enumerate(lines) if re.match(r"^#{1,6}\s", line)]
    question_heads = [(n, h) for n, h in headings if h.startswith("### ")]
    if any(h.startswith("####") for _, h in headings):
        errors.append("found level-4-or-deeper heading; each question must have only one title")
    for n, h in question_heads:
        if not re.match(r"^###\s+\d+[.、]", h):
            errors.append(f"line {n}: level-3 heading is not a numbered question: {h}")

    callout_count = sum(1 for line in lines if re.match(r"^> \[![a-z]", line))
    question_count = len(question_heads)
    max_callouts = question_count // 5
    if callout_count > max_callouts:
        errors.append(
            f"too many Callouts: {callout_count} for {question_count} questions "
            f"(maximum 20% = {max_callouts})"
        )

    visible = "\n".join(lines)
    # Inline code is literal text, not a rendered formula.
    tick = chr(96)
    inline_pattern = tick + r"+[^" + tick + r"]*" + tick + r"+"
    math_text = re.sub(inline_pattern, "", visible)
    if any(token in math_text for token in (r"\[", r"\(")):
        errors.append("found LaTeX bracket/parenthesis delimiters; use Obsidian $...$ / $$...$$")
    block_count = math_text.count("$$")
    if block_count % 2:
        errors.append(f"unbalanced block MathJax delimiters: {block_count} $$ tokens")
    inline_text = math_text.replace("$$", "")
    inline_dollars = len(re.findall(r"(?<!\\)\$", inline_text))
    if inline_dollars % 2:
        errors.append(f"unbalanced inline MathJax delimiters: {inline_dollars} $ tokens")

    # Allow semantic text/background spans, but forbid arbitrary styling.
    if re.search(r"cssclasses\s*:|<style\b|<script\b", source, re.I):
        errors.append("found CSS or script styling; only semantic inline highlights are supported")
    span_pattern = re.compile(r'<span\s+style="([^"]+)">([^<>]+)</span>', re.I | re.S)
    for match in span_pattern.finditer(visible):
        style = match.group(1)
        pieces = [piece.strip() for piece in style.split(";") if piece.strip()]
        for piece in pieces:
            if ":" not in piece:
                errors.append("malformed inline highlight style")
                continue
            prop = piece.split(":", 1)[0].strip().lower()
            if prop not in {"color", "background-color", "font-weight", "border-radius", "padding"}:
                errors.append("unsupported inline highlight CSS property: " + prop)
        color = re.search(r"(?:^|;)\s*color:\s*var\(--color-(cyan|green|orange)\)", style, re.I)
        background = re.search(r"background-color:\s*color-mix\(in srgb,\s*var\(--color-(cyan|green|orange)\)", style, re.I)
        if not color or not background or color.group(1).lower() != background.group(1).lower():
            errors.append("highlight must pair the semantic text color with a matching soft background")
        if not re.search(r"background-color:\s*var\(--text-highlight-bg\)", style, re.I):
            errors.append("highlight must provide the Obsidian theme background fallback")
        if re.search(r"#[0-9a-f]{3,8}\b|(?:rgb|hsl)a?\s*\(|url\s*\(|expression\s*\(", style, re.I):
            errors.append("highlight contains hard-coded colors or unsafe CSS")
    # Consume recognized spans and flag dangling/unapproved HTML styles.
    leftover = span_pattern.sub("", visible)
    if re.search(r"<span\b|</span\s*>|\bstyle\s*=", leftover, re.I):
        errors.append("malformed or unauthorized inline styling")
    if not question_heads:
        errors.append("no numbered question headings found")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args()
    failed = False
    for path in args.files:
        if not path.is_file():
            print(f"FAIL missing: {path}", file=sys.stderr)
            failed = True
            continue
        errors = validate(path)
        if errors:
            for error in errors:
                print(f"FAIL {path}: {error}", file=sys.stderr)
            failed = True
        else:
            print(f"PASS {path}: headings / Callout density / semantic highlights / MathJax")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
