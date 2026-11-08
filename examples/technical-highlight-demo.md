# 嵌入式技术八股 · Obsidian 排版示例

本文是教学示例，不代表在特定芯片或硬件上完成过实际测试。请在 Obsidian 阅读视图或实时预览中查看文字背景。

## 一、STM32 与实时系统

### 1. DMA 为什么能减轻 CPU 负担？

**核心回答：** <span style="color: var(--color-cyan); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-cyan) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">DMA 在配置完成后可以搬运外设与存储器之间的数据，CPU 不必逐字节执行数据拷贝指令。</span> CPU 仍然负责初始化、事件处理和应用层逻辑。

**工作原理：** CPU 配置传输方向、源地址、目的地址与长度；DMA 控制器在请求条件满足时访问系统总线并执行传输。

**工程案例（典型场景）：** <span style="color: var(--color-green); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-green) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">串口接收结合 DMA 和接收缓冲区，可减少 CPU 对逐字节数据搬运的参与。</span> 是否支持循环模式及具体配置应以芯片手册为准。

**易错点：** <span style="color: var(--color-orange); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-orange) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">DMA 不等于没有总线开销，也不意味着 CPU 完全不用处理中断或数据。</span>

### 2. RTOS 中的优先级反转是什么？

**核心回答：** <span style="color: var(--color-cyan); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-cyan) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">高优先级任务等待低优先级任务持有的共享资源，而中优先级任务又抢占低优先级任务，导致高优先级任务的等待时间进一步延长，这是典型的优先级反转。</span>

**工作原理：** 低优先级任务先获取互斥锁，高优先级任务随后请求同一把锁而阻塞；此时中优先级任务获得运行机会，可能推迟持锁者释放资源。

**解决思路：** 对适用场景使用支持优先级继承的互斥锁，并缩短临界区或持锁时间。

**易错点：** <span style="color: var(--color-orange); background-color: var(--text-highlight-bg); background-color: color-mix(in srgb, var(--color-orange) 16%, transparent); font-weight: 600; border-radius: 3px; padding: 0 0.15em;">优先级继承不能替代对死锁、资源竞争和最坏执行时间的分析。</span>
