"""Regression tests for Obsidian semantic backgrounds in technical interview notes."""
import tempfile
import unittest
from pathlib import Path
from check_technical_notes import validate

BASE = "# 面试笔记\n\n## 一、嵌入式基础\n\n### 1. DMA 有什么作用？\n\n"
VALID = '<span style="color: var(--color-cyan); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-cyan) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">DMA 降低 CPU 搬运负担。</span>'

class TestTechnicalSemanticHighlight(unittest.TestCase):
    def check(self, content):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "note.md"
            path.write_text(BASE + content + "\n", encoding="utf-8")
            return validate(path)

    def test_semantic_colored_background_passes(self):
        self.assertEqual([], self.check(VALID))

    def test_plain_markdown_remains_valid(self):
        self.assertEqual([], self.check("**核心回答：** DMA 执行数据搬运。"))

    def test_missing_background_fails(self):
        self.assertTrue(self.check('<span style="color: var(--color-cyan);">DMA。</span>'))

    def test_mismatched_semantic_background_fails(self):
        self.assertTrue(self.check(VALID.replace("var(--color-cyan) 16%", "var(--color-orange) 16%")))

    def test_hardcoded_color_fails(self):
        self.assertTrue(self.check(VALID.replace("color: var(--color-cyan);", "color: #00aacc;")))

    def test_unclosed_span_fails(self):
        self.assertTrue(self.check(VALID.replace("</span>", "")))

if __name__ == "__main__":
    unittest.main()
