# Article Refinement

A standalone writing-review skill bundled inside unified-content-notes.

## Scope

Review and refine existing academic writing, proposals, theses, technical documents, reports, and general prose. Four modes are supported: Audit, Light Edit, Structural Review, and Proofread.

## Install only this skill

~~~bash
git clone --filter=blob:none --no-checkout https://github.com/Crazypsy92/unified-content-notes.git
cd unified-content-notes
git sparse-checkout init --cone
git sparse-checkout set skills/article-refinement
git checkout main
~~~

Copy skills/article-refinement/ to your agent skills directory as article-refinement/. The skill is self-contained; it does not require the root unified-content-notes files.

## Invoke

~~~text
$article-refinement 审校这份开题报告，先指出问题，不要直接重写。
$article-refinement 轻量润色这段文字，保留术语、数据和参考文献。
~~~

This skill improves writing quality; it does not promise to evade AI detectors or guarantee AIGC scores.
