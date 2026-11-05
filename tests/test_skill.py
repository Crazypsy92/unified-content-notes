"""Offline, dependency-free checks for the modular skill package."""
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

    def test_three_actions_are_defined(self):
        content = read("core/action-router.md")
        for label in ("summarize", "explain", "format-only"):
            with self.subTest(action=label):
                self.assertIn(label, content)

    def test_entrypoint_is_compact_and_routes_to_core(self):
        content = read("SKILL.md")
        self.assertLess(len(content), 6500)
        for path in (
            "core/action-router.md",
            "core/structure-router.md",
            "core/source-boundaries.md",
            "core/markdown-style.md",
            "core/quality-check.md",
        ):
            with self.subTest(path=path):
                self.assertIn(path, content)
                self.assertTrue((ROOT / path).is_file())

    def test_all_skill_relative_module_links_exist(self):
        content = read("SKILL.md")
        links = re.findall(r"\]\(((?:core|modules|references)/[^)#]+\.md)\)", content)
        self.assertGreaterEqual(len(links), 8)
        for link in links:
            with self.subTest(link=link):
                self.assertTrue((ROOT / link).is_file())

    def test_relationship_module_declares_inheritance(self):
        content = read("modules/relationship-analysis.md")
        self.assertIn("../core/argument-analysis.md", content)
        self.assertIn("继承", content)
        self.assertIn("双方", content)
        self.assertIn("可观察行为", content)
        self.assertIn("适用范围", content)

    def test_domain_module_adds_rules_without_replacing_parent(self):
        content = read("modules/relationship-analysis.md")
        self.assertIn("不复制基础排版规范", content)
        self.assertIn("不再另造一套", content)

    def test_legacy_reference_files_are_compatibility_notes(self):
        expected = {
            "references/argument-analysis-layout.md": "../core/argument-analysis.md",
            "references/quality-and-format.md": "../core/markdown-style.md",
            "references/relationship-analysis.md": "../modules/relationship-analysis.md",
            "references/structure-router.md": "../core/structure-router.md",
        }
        for path, target in expected.items():
            with self.subTest(path=path):
                content = read(path)
                self.assertIn(target, content)
                self.assertIn("兼容", content)

    def test_format_only_has_zero_semantic_edit_guardrails(self):
        content = read("core/format-only.md")
        for phrase in ("不总结", "不润色", "不改变", "保真核对"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, content)

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
        self.assertIn("Summarize", read("examples/README.md"))
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

    def test_contribution_guide_documents_modular_workflow(self):
        guide = read("CONTRIBUTING.md")
        for item in ("inheritance", "parent", "core/", "modules/", "pull request"):
            with self.subTest(item=item):
                self.assertIn(item.lower(), guide.lower())

    def test_repository_metadata(self):
        for name in ("README.md", "LICENSE", "CONTRIBUTING.md", ".gitignore"):
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file())


if __name__ == "__main__":
    unittest.main()
