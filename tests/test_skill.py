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

    def test_platform_reference_is_optional_and_platform_specific(self):
        content = read("references/platform-and-source.md")
        self.assertIn("按需加载", content)
        self.assertIn("core/source-boundaries.md", content)
        for platform in ("抖音", "Bilibili", "小红书", "X / Twitter"):
            with self.subTest(platform=platform):
                self.assertIn(platform, content)

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

    def test_all_local_markdown_links_resolve(self):
        for file in ROOT.rglob("*.md"):
            content = file.read_text(encoding="utf-8")
            targets = re.findall(r"\]\(([^)]+\.md)(?:#[^)]*)?\)", content)
            for target in targets:
                if target.startswith(("http://", "https://")):
                    continue
                resolved = (file.parent / target).resolve()
                with self.subTest(file=file.relative_to(ROOT), target=target):
                    self.assertTrue(resolved.is_file())

    def test_argument_mode_defaults_to_full_obsidian_contract(self):
        argument = read("core/argument-analysis.md")
        style = read("core/markdown-style.md")
        entrypoint = read("SKILL.md")
        for required in (
            "一个 ##", "观点速览", "具体案例", "浓缩正文", "折叠原文",
            "论点", "论据", "论证", "完整原文"
        ):
            with self.subTest(requirement=required):
                self.assertIn(required, argument)
        self.assertIn("references/obsidian-argument-layout.md", entrypoint)
        self.assertIn("观点分析型每个话题仅一个", style)

    def test_relationship_extends_argument_instead_of_replacing_format(self):
        module = read("modules/relationship-analysis.md")
        for phrase in ("适用范围", "继承基础模块", "双方", "责任", "不再另造一套模板"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, module)
        self.assertIn("../core/argument-analysis.md", module)
        self.assertIn("纯故事 / 对话", module)
        self.assertIn("只改格式", module)

    def test_obsidian_layout_uses_native_renderable_callouts(self):
        layout = read("references/obsidian-argument-layout.md")
        for tag in ("[!info]", "[!abstract]", "[!summary]", "[!note]", "[!quote]-"):
            with self.subTest(tag=tag):
                self.assertIn(tag, layout)
        self.assertIn("> 　　", layout)
        self.assertIn("一个话题一个标题", layout)

    @staticmethod
    def _normalized_original(text):
        # Remove visual spans and paragraph-edge indentation, but preserve
        # meaningful spaces inside the original lines.
        text = re.sub(r"<span\b[^>]*>", "", text)
        text = text.replace("</span>", "")
        return "".join(line.strip(" \t\u3000\r") for line in text.splitlines())

    @staticmethod
    def _folded_original(output):
        marker = "> [!quote]- 原文记录 · 点击展开"
        if marker not in output:
            raise AssertionError("Missing folded source")
        folded = output.split(marker, 1)[1]
        folded = folded.split("\n---\n", 1)[0]
        lines = []
        for line in folded.strip("\n").splitlines():
            if line.startswith("> "):
                lines.append(line[2:])
            elif line == ">":
                lines.append("")
            elif not line.strip():
                lines.append("")
            else:
                raise AssertionError(f"Invalid Callout quote line: {line!r}")
        return "\n".join(lines)

    def test_canonical_argument_examples_have_complete_layout(self):
        pairs = (
            ("examples/obsidian-argument-input.md", "examples/obsidian-argument-output.md"),
            ("examples/argument-case-input.md", "examples/argument-case-output.md"),
            ("examples/relationship-argument-input.md", "examples/relationship-argument-summary.md"),
        )
        for source_path, output_path in pairs:
            with self.subTest(output=output_path):
                source = read(source_path)
                output = read(output_path)
                self.assertEqual(len(re.findall(r"(?m)^## ", output)), 1)
                self.assertNotRegex(output, r"(?m)^### ")
                for marker in ("> [!abstract] 观点速览",
                               "> [!summary] 浓缩正文",
                               "> [!quote]- 原文记录 · 点击展开"):
                    self.assertIn(marker, output)
                self.assertIn("> 　　", output)
                # A native Obsidian Callout table is part of the evidence structure.
                table_start = output.index("> [!abstract] 观点速览")
                table_end = output.index("> [!summary] 浓缩正文")
                table_lines = [line for line in output[table_start:table_end].splitlines()
                               if line.startswith("> |")]
                self.assertGreaterEqual(len(table_lines), 3)
                self.assertEqual(len(set(line.count("|") for line in table_lines)), 1)

                # The source's original ## heading and its consolidated source
                # attribution do not reappear in the folded text; all actual
                # prose/metadata other than the source label must survive.
                original_lines = source.splitlines()[1:]
                original_lines = [
                    line for line in original_lines if not line.startswith("来源：")
                ]
                expected = self._normalized_original("\n".join(original_lines))
                actual = self._normalized_original(self._folded_original(output))
                self.assertEqual(expected, actual)

    def test_condensed_body_keeps_unique_case_evidence(self):
        cases = (
            ("examples/obsidian-argument-output.md",
             ("小李", "周一", "两项", "小周", "已完成4项", "待验证2项", "阻塞4项")),
            ("examples/argument-case-output.md",
             ("项目上线", "半夜", "女朋友", "纪念日", "周末", "改期")),
            ("examples/relationship-argument-summary.md",
             ("在线", "甲", "乙", "告诉我一声", "临时加班", "改期")),
        )
        for path, expected_fragments in cases:
            out = read(path)
            body = out.split("> [!summary] 浓缩正文", 1)[1]
            body = body.split("\n> [!note]", 1)[0].split("\n> [!quote]-", 1)[0]
            with self.subTest(example=path):
                self.assertGreater(len(body), 200)
                for fragment in expected_fragments:
                    with self.subTest(fragment=fragment):
                        self.assertIn(fragment, body)

    def test_obsidian_semantic_highlighting_contract(self):
        argument = read("core/argument-analysis.md")
        layout = read("references/obsidian-argument-layout.md")
        style = read("core/markdown-style.md")
        quality = read("core/quality-check.md")
        readme = read("README.md")
        for phrase in (
            "浓缩正文和折叠原文",
            "蓝青色",
            "绿色",
            "橙色",
            "孤立名词",
            "format-only",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, argument + layout + quality + readme)
        self.assertIn("var(--color-cyan)", layout)
        self.assertIn("var(--color-green)", layout)
        self.assertIn("var(--color-orange)", layout)
        self.assertIn("语义高亮", style)
        self.assertIn("不使用硬编码色值", style)
        self.assertIn("argument-analysis", readme)
        self.assertIn("观点分析型", quality)

    def test_semantic_highlights_cover_both_body_and_original(self):
        pairs = (
            ("examples/obsidian-argument-input.md", "examples/obsidian-argument-output.md"),
            ("examples/argument-case-input.md", "examples/argument-case-output.md"),
            ("examples/relationship-argument-input.md", "examples/relationship-argument-summary.md"),
        )
        allowed = {"cyan", "green", "orange"}
        for source_path, output_path in pairs:
            source = read(source_path)
            output = read(output_path)
            body_start = output.index("> [!summary] 浓缩正文")
            body_end_candidates = [
                pos for marker in ("\n> [!note]", "\n> [!quote]-")
                if (pos := output.find(marker, body_start + 1)) >= 0
            ]
            body = output[body_start:min(body_end_candidates) if body_end_candidates else len(output)]
            original = self._folded_original(output)
            for region_name, region in (("condensed body", body), ("folded original", original)):
                tags = re.findall(
                    r'<span style="color: var\(--color-(cyan|green|orange)\); font-weight: 600;">',
                    region,
                )
                with self.subTest(example=output_path, region=region_name):
                    self.assertGreaterEqual(len(tags), 3)
                    self.assertEqual(set(tags), allowed)
                    self.assertEqual(
                        len(re.findall(r"<span\b", region)),
                        region.count("</span>"),
                    )
                    for tag in re.findall(r"<span\b[^>]*>", region):
                        self.assertRegex(
                            tag,
                            r'^<span style="color: var\(--color-(?:cyan|green|orange)\); font-weight: 600;">$',
                        )
            original_lines = source.splitlines()[1:]
            original_lines = [line for line in original_lines if not line.startswith("来源：")]
            self.assertEqual(
                self._normalized_original("\n".join(original_lines)),
                self._normalized_original(original),
            )
        self.assertNotIn("<span", read("examples/format-only.md"))

    def test_user_preference_layer_is_optional_and_local(self):
        entrypoint = read("SKILL.md")
        guide = read("preferences/README.md")
        template = read("preferences/user-preferences.template.md")
        contributing = read("CONTRIBUTING.md")
        ignore = read(".gitignore")
        self.assertIn("preferences/user-preferences.md", entrypoint)
        self.assertIn("template", entrypoint)
        self.assertIn("only when that file exists", guide)
        self.assertIn("cannot override", guide)
        self.assertIn("Output language", template)
        self.assertIn("Summary density", template)
        self.assertIn("Semantic highlighting", template)
        self.assertIn("current request", template.lower())
        self.assertIn("preferences/user-preferences.md", ignore)
        self.assertIn("local-only", contributing)
        self.assertIn("Core → Modules → User Preferences", read("README.md"))
        self.assertIn("presentation defaults only", guide)
        # A local preference file may exist on a user machine; it must remain ignored, not forbidden.

    def test_novel_module_extends_narrative_with_deep_reading_rules(self):
        module = read("modules/novel-analysis.md")
        entrypoint = read("SKILL.md")
        router = read("core/structure-router.md")
        for phrase in (
            "core/narrative-analysis.md",
            "35%—50%",
            "人物处境",
            "行动",
            "后果",
            "情绪变化",
            "值得回看的动人情节片段",
            "3—8",
            "原创转述",
            "不超过 25 个词",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, module)
        self.assertIn("modules/novel-analysis.md", entrypoint)
        self.assertIn("modules/novel-analysis.md", router)

    def test_novel_example_has_narrative_density_and_final_scene_collection(self):
        source = read("examples/novel-input.md")
        output = read("examples/novel-summary.md")
        self.assertIn("台风", source)
        self.assertGreater(len(output), 1800)
        self.assertIn("## 故事梗概", output)
        self.assertIn("## 人物与关系", output)
        self.assertIn("## 值得回看的动人情节片段", output)
        headings = re.findall(r"(?m)^## .+$", output)
        self.assertEqual(headings[-1], "## 值得回看的动人情节片段")
        self.assertGreaterEqual(len(re.findall(r"(?m)^\\*\\*片段[一二三四五六七八九十]+", output)), 3)
        for phrase in ("红围巾", "台风夜", "送他回家", "灯塔"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, output)

    def test_novel_route_is_distinct_from_general_narrative_route(self):
        router = read("core/structure-router.md")
        self.assertIn("小说深度阅读型", router)
        self.assertIn("一般故事 / 经历 / 影视作品型", router)
        self.assertIn("narrative-analysis.md", router)

    def test_repository_metadata(self):
        for name in ("README.md", "LICENSE", "CONTRIBUTING.md", ".gitignore"):
            with self.subTest(file=name):
                self.assertTrue((ROOT / name).is_file())


if __name__ == "__main__":
    unittest.main()
