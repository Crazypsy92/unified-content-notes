## Obsidian 技术八股与知识笔记排版参考

适用于嵌入式及相关工程技术，也适用于其他技术类面试知识库。目标是让笔记适合 Obsidian 长期阅读、快速检索和面试复习。**普通 Markdown 为主，背景色块为辅。**

## 标题与右侧大纲

统一使用以下结构：

```markdown
# 技术八股知识库

## 一、硬件与底层基础

### 1. DMA 为什么能降低 CPU 搬运数据的负担？

**核心回答：** DMA 是……

**工作原理：** ……

**工程案例：** ……

### 2. RTOS 中优先级反转是什么？

**核心回答：** ……
```

- 每道题 / 每个知识点只有一个 `###` 标题。
- 不使用 `####`、`#####` 等内部标题。
- “核心回答 / 原理 / 案例 / 追问 / 注意事项”使用加粗短语，不进入右侧大纲。
- 快速索引只列章节和题目。
- 章节数量不宜过多；先按知识体系分组，再按题目组织。
- 原题有价值时保留原始表述；重复题目可合并，但不得抹掉不同来源之间的技术差异。

## 面试回答的阅读顺序

每题优先呈现可口述的简洁回答，然后再展开机制。可按需使用：

```markdown
**核心回答：** 先给出 2～5 句直接回答，说明概念和作用。

**工作原理：** 按数据流、控制流、时序或状态变化解释关键机制。

**工程案例：** 用有来源的真实案例，或明确标记为“典型场景 / 示例”的工程例子说明。

**面试追问：**
- 追问一：……
- 回答要点：……

**易错点：** 指出容易混淆的概念、适用边界或版本差异。
```

这只是可选组织方式，不要求每道题都填满。简单概念可以一段讲清；复杂题目才需要展开。

## 普通正文优先，Callout 稀疏使用

推荐普通正文、列表和表格。不要每道题都重复一个 `[!abstract]` 核心回答色块。

Callout 只用于少量真正重要的信息：

```markdown
> [!warning] 工程风险
> Flash 擦写过程中掉电可能破坏当前数据，必须设计状态记录、冗余或恢复策略。
```

- 全篇 Callout 不超过题目数的 20%。
- 仅用于关键安全风险、跨题总结或必须单独提醒的边界。
- 不连续堆叠色块，不把每个例子和表格装进背景框。
- 不使用外部 CSS snippets 或硬编码色值；**仅关键技术文字允许受控的内联 `<span>` 同时设置主题色文字与浅背景**。Callout 仍使用 Obsidian 原生主题颜色，标准写法见下文。


## 技术重点的文字背景高亮

**默认启用主题色文字 + 浅背景**，借鉴情感观点文案的语义高亮，但不让整道题成为色块。优先突出可复述的关键句；普通段落、表格、代码与公式保持清爽。每题通常选 1～3 处，短题只选一句；**不要求每题凑满三色**。

| 语义色 | 内容 | 高亮判断 |
| --- | --- | --- |
| 蓝青色 | 核心回答、重要机制和明确结论 | 最值得直接记忆并口述的完整分句 |
| 绿色 | 工程案例、可验证现象、数据及事实证据 | 有来源和验证级别的具体依据 |
| 橙色 | 常见误区、版本差异、技术取舍和工程风险 | 决定结论适用范围的限定条件 |

**Obsidian HTML 写法：** 仅使用 Obsidian 主题变量。`--text-highlight-bg` 是回退背景；当阅读器支持 `color-mix()` 时，后一项使用与文字同色的半透明背景，适应深浅主题。内联样式不需要用户自行安装 CSS snippets。

~~~markdown
<span style="color: var(--color-cyan); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-cyan) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">可直接口述的核心结论</span>

<span style="color: var(--color-green); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-green) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">有依据的工程场景或可验证现象</span>

<span style="color: var(--color-orange); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-orange) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">技术风险、适用限制和常见误区</span>
~~~

**一题示例：**

~~~markdown
# 嵌入式面试八股

## 一、STM32 基础

### 1. DMA 为什么能减轻 CPU 负担？

**核心回答：** <span style="color: var(--color-cyan); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-cyan) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">DMA 配置完成后可在外设与存储器之间搬运数据，CPU 不必逐字节执行搬运指令。</span> CPU 仍负责初始化、事件处理和后续业务逻辑。

**工作原理：** CPU 设置传输方向、地址与长度，DMA 控制器在请求条件满足时使用系统总线传输。

**工程案例（典型场景）：** <span style="color: var(--color-green); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-green) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">串口接收结合 DMA 和缓冲区，可以减少 CPU 对逐字节数据搬运的参与。</span> 此处仅为教学示例，未声称硬件实测。

**易错点：** <span style="color: var(--color-orange); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-orange) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">DMA 并非没有总线开销，也不意味着 CPU 完全不处理接收流程。</span>
~~~

**兼容与边界：** 上述效果应在 Obsidian 的阅读视图或实时预览中查看；源码模式显示标签属于正常现象。若环境过滤内联样式，可用 Obsidian 原生 `==重点==` 实现单色背景；再不支持时降级为 `**加粗**`。不要使用硬编码色值、CSS snippets、整段背景或嵌套标签；不要把 `<span>` 包在公式、代码、表格、标题或链接中。只改格式任务除非明确授权，否则不新增高亮。

## 表格、代码与流程图

- 有明确对比维度时使用 Markdown 表格；原理解释和长案例放在表格外。
- 代码块注明 C / C++ / Python / Bash / 伪代码等语言；涉及 MCU、RTOS、SDK、LVGL、ROS 2 或汽车软件栈时标明适用平台与版本。
- 未经运行验证的代码示例不能标为“已编译 / 已测试”。
- 只有在表达状态机、数据流、系统链路确实更清晰时才使用 Mermaid，不为了装饰画图。
- 对汽车电子标准、诊断协议、机器人坐标系、算法指标等内容，保留版本、条件和适用范围。

## Obsidian MathJax

**行内公式：**

```markdown
ADC 的理想量化步长为 $V_{ref}/2^N$。
```

**块级公式：**

```markdown
$$
\Delta V=\frac{V_{ref}}{2^N}
$$
```

**完整示例：**

```markdown
PID 连续形式：

$$
u(t)=K_p e(t)+K_i\int_0^t e(\tau)\,\mathrm{d}\tau
+K_d\frac{\mathrm{d}e(t)}{\mathrm{d}t}
$$

其中 $e(t)$ 为误差，$K_p$、$K_i$、$K_d$ 分别为比例、积分和微分系数。
```

- 行内公式只用 `$...$`；块级公式只用独占一行的 `$$...$$`。
- 不使用 `\\(...\\)` / `\\[...\\]` 作为 Obsidian 笔记的默认定界符。
- 不把公式放入代码围栏；代码围栏中的公式只作为源码显示。
- 解释变量、单位、前提和适用范围，不孤立堆公式。

## 视觉验收清单

- [ ] 右侧大纲只出现文档标题、章节和题目。
- [ ] 每个题目没有内部 Markdown 子标题。
- [ ] 大部分内容是普通正文、列表和表格，不是连续色块。
- [ ] Callout 数量不超过题目数的 20%，且每个色块有明确价值。
- [ ] 代码示例标明语言与适用环境；未验证代码没有被声称为已运行。
- [ ] 数学公式在 Obsidian 阅读视图中正常渲染。
- [ ] 章节、题目和索引链接一致。
- [ ] 深色主题下有自然留白，长段落按完整意思拆分。
- [ ] 核心技术句有适度的蓝青 / 绿 / 橙色浅文字背景，颜色与语义一致，不将整题涂色；编辑和阅读视图下均检查排版。
- [ ] 使用主题变量，未混入硬编码色值；代码、公式、表格、链接和原始文字没有被高亮破坏。

## 交付前的实际渲染校验（防止出现“编辑模式正常、阅读模式坏掉”）

- **表格**：表格上下各留一个空行；表头后下一行必须是完整分隔行，例如 `| --- | --- |`，各行单元格列数一致。不要把表格前的 `**小标题：**` 与表格行粘连。应通过 Markdown 渲染器确认生成真正的表格节点。
- **块级公式**：独立一行写 `$$` 开始，独立一行写 `$$` 结束；公式前后空行。禁止 `**PID 公式：** $$` 这种同行开头。
- **标题**：每道原始题对应一个真正的 `###`，且在 Obsidian 大纲中可以找到；不要让公式、代码围栏或引用吞掉之后的标题。
- **原生文字背景**：技术八股优先 `==🔵核心结论==`、`==🟢工程证据==`、`==🟠重要风险==`，不强制外部 CSS；不同 Obsidian 版本可能显示为默认高亮，应以原生 `==关键短语==` 作为兼容后备。
- **面试内容**：要求面试增强时逐题检查追问有答案、案例有来源或明确标注示例，不能仅重排原始知识点。
