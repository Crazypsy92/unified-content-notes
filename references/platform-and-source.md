## 多平台输入结构参考（按需加载）

本文件只记录不同平台常见的信息组织形式和平台特有的遗漏风险。通用来源真实性、素材范围、ASR / OCR、外部核验与版权规则统一维护在 core/source-boundaries.md；不要在本文件重复定义。

只有当素材来自特定平台、包含多页图卡 / 线程 / 分 P、多作者回复，或用户要求核对平台内容结构时才加载。平台功能和界面可能变化，以下内容是识别参考，不是永久平台规则。

| 来源 | 常见信息单元 | 平台特有的遗漏 / 混淆风险 | 推荐提取顺序 |
| --- | --- | --- | --- |
| 抖音 | 口播、字幕、封面标题、情景对白、影视混剪、图文卡片、合集 | 开头钩子不等于核心观点；屏幕文字可能补充口播；课程引流不是论据 | 标题 / 画面文字 → 口播主线 → 案例 / 转折 → 结论 |
| Bilibili | 中长视频、分 P、章节、知识解释、教程、纪录片、专栏 / 动态 | 分 P 顺序、剪辑版与原片差异；公式 / 图表可能不在 ASR；弹幕不是主讲者观点 | 期数 / 时间戳 → 章节 → 画面与术语 → 论证 / 人物线 |
| 小红书 | 多图轮播、逐图说明、清单攻略、经验分享、视频笔记、正文和评论 | 首图可能只有标题；步骤、价格、前后对比可能在后续图片；评论可能是作者更正 | 原题 → 图片 1…N → 正文 → 作者补充 |
| X / Twitter | 单帖、回复链、thread、quote post、长文和多媒体附件 | 回复与主帖混淆；不同人的话被拼接；更新帖可能纠正旧说法 | 原发者 / 时间 → 线程顺序 → 引用原帖 → 附件 → 后续更正 |
| 其他 | 播客、直播回放、群聊、网页、PDF、扫描件、演讲稿 | 说话人、章节、图表和附件可能承担不同信息 | 章节 / 说话人 → 视听 / 图表 → 主体内容 |

## 官方资料入口（用于理解平台输入形式）

- 抖音开放平台内容分享与发布：https://partner.open-douyin.com/docs/resource/zh-CN/dop/ability/opensdk/content-management/share-and-publish-to-douyin
- B 站视频笔记说明：https://www.bilibili.com/read/cv10976550
- B 站专栏编辑器：https://member.bilibili.com/york/read-editor
- 小红书小工具文档：https://miniapp-sandbox.xiaohongshu.com/minitool/doc
- X 帖子类型：https://help.x.com/en/using-x/types-of-posts
- X 连续帖：https://help.x.com/en/using-x/create-a-thread

这些链接用于理解输入形式，不意味着每次处理都必须联网。
