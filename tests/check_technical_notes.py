#!/usr/bin/env python3
"""Validate heading depth, sparse Callouts, and Obsidian MathJax in technical notes."""
from __future__ import annotations
import argparse
import math
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
    q_count = len(question_heads)
    max_callouts = max(1, math.ceil(q_count / 5))
    if callout_count > max_callouts:
        errors.append(f"too many Callouts: {callout_count} for {q_count} questions (limit {max_callouts})")
    visible = "\n".join(lines)
    if any(token in visible for token in (r"\[", r"\]", r"\(", r"\)")):
        errors.append("found bracket/parenthesis math delimiters; use Obsidian $...$ / $$...$$")
    block_count = visible.count("$$")
    if block_count % 2:
        errors.append(f"unbalanced block MathJax delimiters: {block_count} $$ tokens")
    inline_text = visible.replace("$$", "")
    inline_dollars = len(re.findall(r"(?<!\\)\$", inline_text))
    if inline_dollars % 2:
        errors.append(f"unbalanced inline MathJax delimiters: {inline_dollars} $ tokens")
    if re.search(r"<span\b|\bstyle\s*=|cssclasses\s*:", source, re.I):
        errors.append("found CSS/HTML styling; technical notes should use native Markdown and sparse Callouts")
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
            print(f"PASS {path}: headings / Callout density / MathJax")
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
