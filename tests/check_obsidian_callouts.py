#!/usr/bin/env python3
"""Validate Obsidian Callout block boundaries and semantic-highlighting spans."""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys

CALLOUT = re.compile(r"^> \[!([a-z][a-z0-9_-]*)\]([+-]?)")
SPAN_OPEN = re.compile(r"<span\b[^>]*>")
SPAN_CLOSE = re.compile(r"</span>")

def validate(path: Path, simplified: bool) -> list[str]:
    errors = []
    source = path.read_text(encoding="utf-8-sig")
    lines = source.splitlines()
    count = 0
    quote = False
    for i, line in enumerate(lines):
        match = CALLOUT.match(line)
        if match:
            count += 1
            quote = match.group(1) == "quote"
            if i and lines[i-1].strip():
                errors.append(f"{path}:{i+1}: expected a real blank line before a new Callout; '>' is not a separator")
            if quote and match.group(2) != "-":
                errors.append(f"{path}:{i+1}: original-text Callout should use [!quote]-")
        elif quote and line.strip() and not line.startswith(">"):
            quote = False
        if quote and re.match(r"^>\s*(?:~{3,}|\x60{3,})", line):
            errors.append(f"{path}:{i+1}: code fence inside original quote prevents HTML highlighting")
    if not count:
        errors.append(f"{path}: no Obsidian Callout found")
    a, b = len(SPAN_OPEN.findall(source)), len(SPAN_CLOSE.findall(source))
    if a != b:
        errors.append(f"{path}: unbalanced spans: {a} opening, {b} closing")
    if simplified:
        try:
            from opencc import OpenCC  # pip install opencc-python-reimplemented
        except ImportError:
            errors.append("OpenCC missing for --simplified: install opencc-python-reimplemented or mark check NOT RUN")
        else:
            cv = OpenCC("t2s")
            for i, line in enumerate(lines):
                if cv.convert(line) != line:
                    errors.append(f"{path}:{i+1}: possible traditional Chinese in simplified copy")
    return errors

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--simplified", action="store_true",
                        help="Check simplified characters (requires OpenCC).")
    args = parser.parse_args()
    failed = False
    for path in args.files:
        if not path.is_file():
            print(f"FAIL missing: {path}", file=sys.stderr)
            failed = True
            continue
        errors = validate(path, args.simplified)
        for error in errors:
            print("FAIL " + error, file=sys.stderr)
        if not errors:
            print(f"PASS {path}: Callout boundaries / spans")
        failed = failed or bool(errors)
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
