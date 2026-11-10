# 研究地图：空间智能与通用 AI（持续更新）

本地图按“感知与状态 → 转移预测 → 规划与执行 → 学习闭环 → 评测与基础设施”组织；每期快照保留历史判断，不把作者/官方报告自动当作独立验证。

## 2026-11-10 地图快照

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 人类经验与跨本体动作 | GR00T 2、MR0、HiPHI-Hand 将人类视频、UMI、机器人和手部 mocap 接到统一动作接口 | 人类视频数量、动作可执行性、形态接近度、后训练预算纠缠 | 固定机器人数据和参数预算，做 human-only / robot-only / joint future-action 的跨本体因果曲线 |
| 对象中心空间状态 | ObjectWorld 用完整物体流替代直接机器人动作，刚体和柔性物体共用接口 | 自动几何、隐藏表面和真实时间尺度误差还没有闭合 | 在同一控制器下比较 visible flow、full-object flow、goal pose，独立测 hidden-surface 和闭环成功 |
| 语言条件世界模型 | Tiresias 把指令、候选动作和视频想象放进 LCWM-Bench | 36 秒级想象成本与真实控制收益不匹配，unseen 域仍从 63 降到 51 | 训练小型 ranker/latent predictor，测想象预算、候选覆盖和真实任务成功的校准曲线 |
| 隐式空间预见与规划效率 | DexForesight 把世界预测蒸馏进策略；WARP-JEPA 把在线 GD 改成 amortized proposer | probe/仿真增益是否能转为接触和长时真实收益 | 对同一冻结 world model 做 explicit future、query alignment、amortized planning 三因素实验 |
| 视觉—触觉—动作对齐 | BAT-WAM 用连续 bridge 恢复缺失触觉，并把状态加入 WAM | 触觉预测、动作执行和传感器布局仍可能共变 | 同手型/跨手型、同物体/留出物体下，测 touch prediction 对控制的独立贡献 |
| 可执行空间推理 | Spatial Harness 用 physics engine 执行视角变换；DexBench 计划按 Object/Physics/Spatial 评测 | 估计状态错误、执行正确、任务成功尚未在同一协议中拆开 | 建立状态—执行—策略三层 benchmark，分别冻结位姿、物理和任务验收器 |
| Agent 与自演化 | REINS 把 LLM 规则 grounding、verification、memory consolidation 放进实时规划 | 记忆增长不等于权重能力增长，感知和真实控制仍被抽象 | 固定外部验收器，报告规则覆盖、LLM 调用率、完整成本与跨场景保留率 |
| 可复现性与基础设施 | MR0 的 manifest、WARP-JEPA 的 checkpoint contract、WorldFoundry 的 evidence-aware scorecard | 代码、权重、数据、环境和结果常来自不同 revision | 为 world model/VLA 建立 provenance lockfile，并对每个分数标注 artifact、runtime、seed 和成本 |

## 2026-11-09 地图快照

| 问题分类 | 今日工作与近期趋势 | 未解决 gap | 可形成论文的机会 |
|---|---|---|---|
| 空间表征进入基础模型 | SLA 以 OmniVGGT 对齐中间视觉 token，把空间监督放进 continual pre-training 与 post-training | 教师质量、标定缺失、数据混合和下游适配成本仍纠缠 | 固定 VLA 与数据预算，做空间对齐阶段、标定可用性、state dropout 的因子化曲线 |
| 世界模型后训练 | RoboImagine 用候选未来的语义/视觉反馈；WAM-Sim 用持久 memory 约束在线 RL | 预测指标、任务进度、策略排名和物理真实性尚未闭合 | 同一动作序列下，比较 semantic/visual/world-state 反馈对真实闭环成功的预测力 |
| 语义纠错与人机对齐 | OopsieRecover 将少量人类干预变成 gated correction cost，并迁移到新姿态/场景 | 语义点集难表达接触力、隐变量和候选动作缺失 | 统一纠正库并加入触觉/力反馈，测程序蒸馏到小 VLA 后的迁移 |
| Agent 评测与部署 | RoboARCade 分离策略选择、精细执行、记忆和错误成功声称；VFlash 关注生成式策略效率 | 仿真、接口和 API 版本改变总分，预测收益尚未闭合到真实控制 | 固定接口和价格，联合测候选预算、错误声称、world-model 预测与闭环成功 |
| 传感器现实性 | VisionSIM 把 event、SPAD、iToF、热成像测量过程放进仿真 | open-loop 传感器误差还没有接到长期控制失败 | 传感器参数扰动到抓取/导航失败的可追溯链 |

## 2026-11-08 地图快照

| 问题分类 | 今日材料与近期趋势 | 未解决 gap | 可形成论文的机会 |
|---|---|---|---|
| 可辨识状态与世界生成 | GPWM、Cosmos Interactive Simulation、MetricTrail、La-JEPA、Scientist World | 状态、生成、控制和外部验收仍被不同数据/模型共同改变 | 状态表示、预测指标和动作成功的等预算因果审计 |
| 空间数据与接触 | ToyBlocks、Cosmos SimBimanual、MetricTrail | 接触真值、动作契约和尺度/标定仍缺少统一报告 | 物理接触与视觉相似分开计分，做跨引擎复核 |
| 人机与跨本体 | GPWM、La-JEPA、ToyBlocks | 数据来源、动作形态和真实部署规模相互混合 | 固定本体差异与数据量，估计跨本体迁移曲线 |
| 自主科研与 Agent | Scientist World、Anthropic memory | 任务发现、实现器、记忆和验证器共同演化 | 冻结外部验收并报告完整成本、轨迹和未解锁样本 |

## 2026-11-07 地图快照

| 问题分类 | 今日工作与近期趋势 | 未解决 gap | 可形成论文的机会 |
|---|---|---|---|
| 持久空间与动态记忆 | Frameboy、PlayGen2；空间上下文与显式状态两路推进 | 重访一致、视野外动态、接触正确性缺少统一比较 | 同观测、同预算下比较像素递归与显式状态，并分离渲染错误 |
| 人类经验与跨本体对齐 | Open-HumanWAM、Liber-0；数据覆盖和动作锚点结合 | 数据小时数、动作精度、硬件接近和计算量相互混合 | 固定数据量与预算，估计动作标注质量及形态差异的迁移曲线 |
| 几何状态到动作 | Spatial-UMI-Dream，连接 UMI / WAM | 深度质量收益与标定、视角及接口转换贡献难分 | 深度尺度和外参受控扰动，区分几何推理与视觉捷径 |
| 视频表示的控制效用 | Motion-guided regularization，连接 JEPA / LeWM | 分布不塌缩仍可能忽略任务动态 | 任务状态与背景独立干预，以闭环后果检验潜变量 |
| 自改进与长期执行 | Criteria Exposure、BudgetMix、Anthropic memory | 验收适应、重试预算、记忆整理计算共同改变分数 | 冻结外部判据，联合报告预算曲线、记忆成本与跨任务保留 |
| 研究基础设施 | LeRobot 0.7、持续跟踪 Genie Sim / SimuGuard | 包可安装、资源可见与任务成功之间仍有距离 | 流式数据、动作转换和远端运行的语义一致性审计 |

## 下一轮追踪

- 2026-11-10 新增：GR00T 2 主代码/权重与 Human-1M-100K 的训练契约；MR0 固定 HF revision、Rollback/事件记忆复现；ObjectWorld 完整数据与 flow-to-action 代码；Tiresias 小预算 ranker/想象验证；DexForesight 真实遮挡和 query alignment；BAT-WAM 代码与 HTBench；WARP-JEPA held-out 任务与小 GPU 复现；REINS 感知噪声与外部成本；Spatial Harness 代码落地；RLWRLD DexBench 资源计划。
- 2026-11-09 新增：SLA 的完整训练代码/数据/权重闭合、OmniVGGT 教师和 state dropout 复现；RoboImagine 预测指标到闭环任务进度的桥接；OopsieRecover correction program 的触觉扩展；WAM-Sim memory 与 online RL 的独立归因；VisionSIM 传感器误差到控制失败链；RoboARCade 单任务成本与错误成功声称；VFlash TensorRT/算法收益分离。
- 2026-11-08 新增：GPWM 完整代码／权重／ParticleWorlds、视觉到粒子及噪声搜索的独立归因；ToyBlocks 完整数据验收、oracle 四组与接触真值；Cosmos 训练／观测接口、59D 动作契约及策略排名有效性。
- 2026-11-07 新增：Frameboy 低延迟与长期动态独立量化；PlayGen2 全图/局部状态审计及完整训练包；Open-HumanWAM 50K 上传完整性、Goal 后训练与 Vanilla 回合数协议；Spatial-UMI-Dream 预训练数据、深度扰动与动作转换；Liber-0 独立任务验收、精确动作数据占比与开放资源。

## 历史来源

- [2026-11-10 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-10/)
- [2026-11-09 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-09/)
- [2026-11-08 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-08/)
- [2026-11-07 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-07/)
- [2026-11-03 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-03/)
- [2026-11-01 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-01/)
