"""Test screenshot-style native Obsidian technical note card layouts."""
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from check_technical_notes import validate

HEAD = "# 技术八股\n\n## 一、外设\n\n### 1. DMA 有什么作用？\n\n"
CARD = (
    "> [!summary] 核心回答 · 面试速记\n"
    "> DMA 减少逐字节数据搬运。\n"
    ">\n"
    "> **面试速记：** ==减少 CPU 搬运负担==\n\n"
    "> [!info] 原理、区别与应用\n"
    "> | 方式 | 作用 |\n"
    "> | --- | --- |\n"
    "> | DMA | 传输数据 |\n\n"
    "> [!example] 工程案例与验证边界\n"
    "> **示例：** 串口 DMA 接收。\n\n"
    "> [!question] 面试追问与回答\n"
    "> **完全不用 CPU 吗？** 不是。\n"
)

class TestTechnicalCallouts(unittest.TestCase):
    def check(self, content):
        with TemporaryDirectory() as folder:
            p = Path(folder) / "note.md"
            p.write_text(content, encoding="utf-8")
            return validate(p)

    def test_four_cards_per_question_pass(self):
        self.assertEqual([], self.check(HEAD + CARD))

    def test_adjacent_cards_need_real_blank_line(self):
        invalid = (HEAD + CARD).replace(
            "==减少 CPU 搬运负担==\n\n> [!info]",
            "==减少 CPU 搬运负担==\n>\n> [!info]",
        )
        self.assertTrue(any("truly blank" in err for err in self.check(invalid)))

    def test_many_inline_highlights_are_not_preferred(self):
        body = HEAD + CARD + "\n" + " ".join("==过度高亮==" for _ in range(12))
        self.assertTrue(any("too many inline highlights" in err for err in self.check(body)))

if __name__ == "__main__":
    unittest.main()
