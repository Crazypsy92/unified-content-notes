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
        a = read("examples/format-input.md")
        b = read("examples/format-only.md")
        def canonical(s):
            return "".join(c for c in s if not c.isspace() and c != "#")
        self.assertEqual(canonical(a), canonical(b))

    def test_argument_keeps_key_details(self):
        summary = read("examples/argument-summary.md")
        self.assertIn("180", summary)
        self.assertIn("每周做两次", summary)

    def test_repository_metadata(self):
        for name in ("README.md", "LICENSE", "CONTRIBUTING.md", ".gitignore"):
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file())


if __name__ == "__main__":
    unittest.main()
