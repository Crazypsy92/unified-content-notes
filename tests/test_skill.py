"""Offline, dependency-free checks for the public skill package."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


class SkillPackageTests(unittest.TestCase):
    def test_skill_frontmatter_and_name(self):
        content = read("SKILL.md")
        self.assertTrue(content.startswith("---\n"))
        frontmatter = content.split("---", 2)[1]
        self.assertRegex(frontmatter, r"(?m)^name:\s*unified-content-notes\s*$")
        self.assertRegex(frontmatter, r"(?m)^description:")

    def test_three_actions(self):
        content = read("SKILL.md")
        for label in ("summarize", "explain", "format-only"):
            with self.subTest(action=label):
                self.assertIn(label, content)

    def test_relative_reference_links(self):
        content = read("SKILL.md")
        links = re.findall(r"\]\((references/[^)#]+\.md)\)", content)
        self.assertGreaterEqual(len(links), 3)
        for link in links:
            with self.subTest(link=link):
                self.assertTrue((ROOT / link).is_file())

    def test_example_heading_levels(self):
        for file in (ROOT / "examples").glob("*.md"):
            if file.name == "README.md":
                continue
            with self.subTest(file=file.name):
                text = file.read_text(encoding="utf-8")
                self.assertNotRegex(text, r"(?m)^#\s")
                self.assertRegex(text, r"(?m)^##\s")

    def test_format_only_preserves_nonformat_characters(self):
        source = read("examples/format-input.md")
        output = read("examples/format-only.md")

        def canonical(text):
            # The example's only permitted changes are Markdown heading and whitespace.
            return "".join(c for c in text if not c.isspace() and c != "#")

        self.assertEqual(canonical(source), canonical(output))

    def test_argument_summary_keeps_key_details(self):
        summary = read("examples/argument-summary.md")
        self.assertIn("180", summary)
        self.assertIn("20", summary)
        self.assertIn("每周做两次", summary)

    def test_same_source_has_distinct_summary_and_explanation(self):
        summary = read("examples/argument-summary.md")
        explanation = read("examples/argument-explanation.md")
        self.assertNotEqual(summary, explanation)
        self.assertIn("总结", read("examples/README.md"))
        self.assertIn("为什么", explanation)
        self.assertIn("不能断定", explanation)

    def test_story_examples_preserve_unresolved_ending(self):
        summary = read("examples/narrative-summary.md")
        explanation = read("examples/narrative-explanation.md")
        self.assertIn("没有交代学生是否收下伞", summary)
        self.assertIn("没有明确写她把伞交给了学生", explanation)

    def test_documentary_example_separates_evidence_levels(self):
        explanation = read("examples/documentary-explanation.md")
        self.assertIn("尚未证实", explanation)
        self.assertIn("居民", explanation)
        self.assertIn("材料边界", explanation)

    def test_carousel_example_preserves_order_and_source_boundaries(self):
        summary = read("examples/carousel-summary.md")
        for item in ("第1页", "第2页", "第3页", "第4页", "45 cm", "28 cm", "读者评论"):
            with self.subTest(item=item):
                self.assertIn(item, summary)

    def test_contribution_guide_has_workflow_and_checklist(self):
        guide = read("CONTRIBUTING.md")
        for item in ("Fork", "pull request", "Pull request checklist", "format only", "rights-cleared"):
            with self.subTest(item=item):
                self.assertIn(item.lower(), guide.lower())

    def test_repository_metadata(self):
        for name in ("README.md", "LICENSE", "CONTRIBUTING.md", ".gitignore"):
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file())


if __name__ == "__main__":
    unittest.main()
