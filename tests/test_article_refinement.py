"""Structural checks for the independently callable article-refinement sub-skill."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "skills" / "article-refinement"


def read(relative):
    return (BASE / relative).read_text(encoding="utf-8")


class ArticleRefinementTests(unittest.TestCase):
    def test_standalone_entrypoint(self):
        content = read("SKILL.md")
        self.assertTrue(content.startswith("---\n"))
        self.assertIn("name: article-refinement", content)
        for mode in ("Audit", "Light Edit", "Structural Review", "Proofread"):
            self.assertIn(mode, content)

    def test_reference_links_resolve(self):
        content = read("SKILL.md")
        links = re.findall(r"\]\((references/[^)#]+\.md|examples/[^)#]+\.md)(?:#[^)]*)?\)", content)
        self.assertGreaterEqual(len(links), 4)
        for link in links:
            self.assertTrue((BASE / link.split("#", 1)[0]).is_file(), link)

    def test_academic_integrity_and_no_detector_evasion(self):
        content = "\n".join(path.read_text(encoding="utf-8") for path in BASE.rglob("*.md"))
        for phrase in ("不以规避 AIGC 检测为目标", "不编造", "不承诺", "作者确认"):
            self.assertIn(phrase, content)

    def test_protected_content_is_explicit(self):
        content = read("references/guide.md")
        for item in ("技术术语", "单位", "公式", "引用标记", "参考文献序号", "实验条件"):
            self.assertIn(item, content)

    def test_example_does_not_change_parameter(self):
        content = read("examples/revision-cases.md")
        self.assertIn("10 Hz", content)
        self.assertEqual(content.count("10 Hz"), 2)


if __name__ == "__main__":
    unittest.main()
