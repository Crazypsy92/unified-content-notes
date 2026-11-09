"""Checks for the optional humanistic reflection module."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


class HumanisticReflectionTests(unittest.TestCase):
    def test_module_covers_narrative_media(self):
        module = read("modules/humanistic-reflection.md")
        for phrase in ("小说", "电影", "剧集", "纪录片"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, module)

    def test_guided_path_moves_from_evidence_to_reflection(self):
        module = read("modules/humanistic-reflection.md")
        for phrase in ("具体场景", "人物的处境与选择", "社会环境", "人文问题", "不同立场", "艺术形式", "联系当下", "暂时判断"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, module)

    def test_interactive_mode_asks_one_question_per_turn(self):
        module = read("modules/humanistic-reflection.md")
        self.assertIn("每轮只提出 **一个核心问题**", module)
        self.assertIn("等用户回答后", module)
        self.assertIn("不设计考试式测验", module)

    def test_module_is_optional_and_preserves_format_only(self):
        module = read("modules/humanistic-reflection.md")
        self.assertIn("普通剧情总结", module)
        self.assertIn("format-only", module)
        self.assertIn("不强行升华", module)
        self.assertIn("不强制", module)

    def test_film_analysis_requires_audiovisual_evidence(self):
        module = read("modules/humanistic-reflection.md")
        self.assertIn("镜头景别", module)
        self.assertIn("剪辑", module)
        self.assertIn("只有用户提供画面 / 视频", module)
        self.assertIn("不能", module)

    def test_module_is_referenced_by_entrypoint_and_routes(self):
        for path in ("SKILL.md", "core/structure-router.md", "core/narrative-analysis.md", "modules/novel-analysis.md", "README.md"):
            with self.subTest(file=path):
                self.assertIn("humanistic-reflection.md", read(path))


if __name__ == "__main__":
    unittest.main()
