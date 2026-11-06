"""Offline checks for ASR transcript cleanup rules."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


class TranscriptCleanupTests(unittest.TestCase):
    def test_entrypoint_routes_asr_cleanup_on_demand(self):
        entry = read("SKILL.md")
        self.assertIn("core/transcript-cleanup.md", entry)
        self.assertIn("明确要求", entry)
        self.assertIn("format-only", entry)

    def test_asr_cleanup_separates_raw_and_reading_versions(self):
        cleanup = read("core/transcript-cleanup.md")
        for phrase in (
            "原始 ASR 备份",
            "校订阅读版",
            "高置信度",
            "听辨存疑",
            "未核听音频",
            "不得补齐",
            "format-only",
        ):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, cleanup)

    def test_source_integrity_and_argument_analysis_allow_explicit_asr_editing(self):
        boundaries = read("core/source-boundaries.md")
        argument = read("core/argument-analysis.md")
        self.assertIn("原始 ASR 备份", boundaries)
        self.assertIn("校订阅读版", boundaries)
        self.assertIn("口播转录 · 断句校订版", argument)
        self.assertIn("原始 ASR 单独备份", argument)

    def test_obsidian_layout_explains_paragraphs_and_transcript_label(self):
        layout = read("references/obsidian-argument-layout.md")
        self.assertIn("口播转录 · 断句校订版", layout)
        self.assertIn("不要把几十句挤成一段", layout)
        self.assertIn("听辨存疑", layout)

    def test_quality_check_catches_asr_monoblocks(self):
        quality = read("core/quality-check.md")
        self.assertIn("ASR 口播挤成一大段", quality)
        self.assertIn("原始 ASR 备份", quality)
        self.assertIn("不机械地一句一段", quality)


if __name__ == "__main__":
    unittest.main()
