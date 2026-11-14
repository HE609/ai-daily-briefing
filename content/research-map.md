# 研究地图：空间智能与通用 AI（持续更新）

## 2026-11-14 地图快照

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 持久空间世界与可编辑场景 | Atlas 开放 Viewfinder、Chisel、API 和 splats-to-mesh；Spatial Foundry 把相机、几何、实例和场景编辑放入统一坐标 | 生成世界的几何一致性、物体持久性、物理接触和长期重访仍未统一计分 | 建立 camera-held / scene-held / object-edit 三联协议，联合测重投影、实例位姿、接触和策略成功 |
| 几何基础模型与 3D/4D 重建 | Kosmo-GFM 用 GFM、PoseEngine、KosmoWorld 连接学习先验、全局优化和 3DGS/4DGS | 深度、位姿、scene flow 和下游策略收益仍然分离 | 固定输入视图与优化预算，比较 geometry prior、bundle optimization、4D flow 对闭环导航的独立贡献 |
| 真实场景与物理 AI 数据 | Ropedia Xperience 2 用 LiDAR + HOMIE 生成 real-to-sim、重定向、虚拟遥操作和长时轨迹，首批 126 场景已上线 | 批次版本、腿部缺失、模型生成语言和静态场景假设会影响可迁移性 | 用同一场景做 human-only、retargeted、virtual teleop 三组数据，估计环境规模与行为规模的因果曲线 |
| 跨本体动作接口 | SALA 用语言软邻域对齐 latent action，EgoX 用统一 frame 和 dreaming 共享 dynamics | 语言描述、动作锚点、形态差异和真实接触尚未完全解耦 | 建立 action semantics、latent geometry、control success 三层跨本体 benchmark |
| 空间记忆与长时执行 | STVLA 将几何 token 放入 bounded temporal memory，ACE-CaP-0 将示范与仿真经验写入冻结代码 | 进度、记忆、程序和外部验收缺少统一成本账本 | 同一 VLA/agent 上比较 geometry memory、event memory、program memory 和重规划预算 |
| 局部未来表征与可控视频 | ProtoVis-Nav 用 projected local target feature 对齐 waypoint，BWM-Forge 用 Blender scene program 控制机器人视频 | 局部视觉想象和视频 realism 尚未证明可转成真实飞行或接触动作 | 用相同 motion、不同 camera 和 object edit 做 feature alignment、生成一致性与闭环成功的三层实验 |
| Agent 自演化与评估器 | ACE-CaP-0 的 demonstration/simulation on demand 与 Anthropic Anvil 的 attack-evaluate-fix loop 都把经验回写执行系统 | 评估器错误、外部副作用、长期成本和跨任务保留率仍缺统一协议 | 设计 resettable agent harness，联合记录 success、rollback、token、wall-clock、verifier error 和 transfer |
| 证据与发布基础设施 | Atlas 无权重但有 API，Ropedia 有数据批次与 license，SALA/EgoX/STVLA 论文和项目页先于代码 | 产品、论文、代码、权重、数据与第三方结果常来自不同版本 | 为 world model/VLA 建立 provenance lockfile，要求每个数字绑定 revision、artifact、runtime、seed 和成本 |

## 下一轮追踪

- 2026-11-14 新增：Atlas 11 月 12 日开放工具与 API；Spatial Foundry 5,280 个可编辑住宅场景；Kosmo-GFM 的 GFM/PoseEngine/KosmoWorld；Ropedia Xperience 2 首批 126 场景约 1.07 TB、CC BY-NC 4.0；SALA 的 2,678 小时人类视频与语言对齐 latent；EgoX 的 MXT+ 与 embodiment dreaming；STVLA 的几何 temporal memory；ACE-CaP-0 的冻结代码策略；ProtoVis-Nav 的公开 checkpoint 与 AirSim/UE4；BWM-Forge 的 Apache-2.0 Blender pipeline；Anthropic Anvil 的 evaluator-guided red-team。
- 优先补查 Atlas 的长期几何/物理一致性、Spatial Foundry 完整数据批次、Kosmo-GFM 代码与权重、Ropedia 坐标注册和许可证、SALA/EgoX/STVLA 的公开实现、ACE-CaP-0 的可运行代码、ProtoVis-Nav 的真实或硬件在环评测、BWM-Forge 的物理有效性、Anvil 的公开可审计替代协议。

本地图按“感知与状态 → 转移预测 → 规划与执行 → 学习闭环 → 评测与基础设施”组织。每期快照保留历史判断，不把作者或官方报告自动当作独立验证。

## 2026-11-13 地图快照

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 动作表征与世界模型接口 | OnlyAct 用 V-JEPA 2 抽取 scene-invariant latent action；BEHAVIOR WAM 方案用 stage、skill 和候选动作连接世界预测与执行 | action expressiveness、scene leakage、物理因果和真实动作可执行性仍由不同指标衡量 | 建立 action representation × scene invariance × counterfactual rollout 三层协议，并做跨本体留出 |
| 无动作人类视频与跨本体 | Ego Guidance 用 future visual state，DexSeed 用 grasp prior 与 physics rollout，将人类经验转成机器人训练信号 | 视频量、动作标签、手型差异、仿真接触和视觉多样性相互纠缠 | 固定机器人数据和计算预算，比较 raw action、future state、contact prior 三种接口的迁移曲线 |
| WAM 长时状态与推理预算 | BEHAVIOR WAM 方案使用 progress estimator、skill routing 和 rolling inpainting；ExRL 学习 execution length | stage、时间、动作候选和重规划成本缺少统一账本 | 做 stage semantics × execution length × refinement budget 三因素冻结 checkpoint 实验 |
| Agent safety 与闭环验收 | LEASH 把 task/action/commit 三个 gate 接到 RoboRisk 五类风险；One Policy 用冻结 practice session 路由 agent | reviewer 误判、外部副作用、练习成本和安全收益仍未长期闭合 | 构建 resettable agent-robot harness，统一报告 harm、safe success、API cost、rollback 和 transfer |
| 游戏与桌面数据 | Game-Enhanced 用事件和 foresight 预训练 InternVLA-A1.5 | 游戏事件与物理动作存在接口鸿沟，收益可能来自额外训练预算 | 做 events-only、foresight-only、联合目标和随机事件的等预算对照 |
| 记忆与任务进度 | Memory Clock 的 null-event 审计与 BEHAVIOR 的 stage estimator 都说明时间不能代替状态 | 无事件延迟、重复动作、隐藏状态和阶段边界缺少统一测试 | 把 null-event、hidden-memory、stage confusion、execution length 放入同一长时基准 |
| 工业 persistent world 与真实部署 | HolidayFactory 作为窗口外边界线索，LEASH 和 BEHAVIOR 提供可审计闭环基础设施 | 模拟器成功、持续作业 throughput、能耗和真实安全仍缺跨系统证据 | 建立 persistent-scene benchmark，要求重置前后任务顺序、接触、能耗和安全同时正确 |

## 下一轮追踪

- 2026-11-13 新增：OnlyAct 的 V-JEPA 2 action encoder、Apache-2.0 代码与 checkpoint；LEASH/RoboRisk 的 92+13 任务目录、3,312 仿真结果与 Hugging Face 数据集；ExRL 的 execution-length adapter、真实 π₀.₅ 适配和公开代码；DexSeed 的 25,270 物理 rollout 轨迹、代码待发布与真实 grasp demo；Ego Guidance 的 SPAR、975 小时过滤 Ego4D 与 Open-AoE scaling；BEHAVIOR WAM 第二名的 stage estimator/skill routing；Game-Enhanced 的 event/foresight 预训练；One Policy 的冻结 Astra practice route。

本地图按“感知与状态 → 转移预测 → 规划与执行 → 学习闭环 → 评测与基础设施”组织；每期快照保留历史判断，不把作者/官方报告自动当作独立验证。

## 2026-11-12 地图快照

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 物理可检验世界预测 | PAN 2 用结构化状态和视频模拟多步计划；NTT 用质量、姿态、速度与运动方程筛选候选动作 | 模拟画面、物理状态、候选排序和真实闭环仍由不同系统提供 | 建立状态—视频—动作三层基准，要求候选排序和中间接触同时正确 |
| 4D 场景与几何补全 | UGG 统一 RGB、深度、相机 ray map 与 test-time search | seed、caption、稀疏观测和几何真值的影响尚未分离 | 构建稀疏视角、隐藏表面、相机误差和下游策略的联合评测 |
| WAM 接口与推理预算 | MetaWAM 压缩 robot signals；Elastic-WAM 选择未来 refinement；Long-WAM 刷新长历史 checkpoint | 表示压缩、未来预测、动作成功和总墙钟缺少等预算归因 | 在同一 WAM 上做 latent interface × history × refinement budget 三因素实验 |
| 交互状态与动力学适配 | LaST0.5 引入 interaction-centric latent；Few-Shot Residual 用三回合修正部署动力学 | 预测误差、接触状态和现场特异性适配容易混在一起 | 用冻结 world model、质心/摩擦 shift 和真实回合分离三者贡献 |
| 记忆与任务进度 | Memory Clock 用 null event 证明时间采样会产生 phantom progress | 记忆索引、事件边界、延迟和可见状态缺少统一不变性测试 | 设计 null-event、hidden-memory、clock-scaling、event-index 四联协议 |
| 跨本体与人类经验 | CIALLO 用 intent codec 做本体校准；Ego Guidance 用无动作人类视频监督未来表示 | 形态差异、视觉先验、动作接口和数据质量仍相互纠缠 | 固定数据与计算预算，比较 intent、future representation、raw action 三种接口 |
| Agent 自演化与验收器 | FGSE 把 lesson 视作可证伪假设；PAN 2 让 Agent 比较模拟计划 | verifier 错误、probe 过拟合、外部副作用和长期成本未闭合 | 将临时状态、世界模拟、外部验收和回滚统一到同一长期基准 |

## 下一轮追踪

- 2026-11-12 新增：PAN 2 29B checkpoint、概念状态与视频生成接口、长计划失败和 GPU 成本；NTT physics control adapter 的论文、代码、动作候选与 OBJ3D 细节；UGG 30 GB 权重的跨 seed 几何复验；MetaWAM 三组 checkpoint 的真实推理和上游数据许可；Elastic-WAM 的代码与速度边界；Long-WAM 19.2 秒 checkpoint 的独立评测；Memory Clock 的跨模型 null-event 协议；CIALLO 的 one-record calibration 和 FGSE 的 verifier 复核。

## 2026-11-11 地图快照

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 动态空间世界与持久状态 | WanderBench 测源事件与动态重访，Compass 1 激活长时空间历史 | 可见外观、离屏事件和检索状态缺少共同真值 | 固定事件时间与相机路线，构建动态重访的状态级评测 |
| 可执行生成与仿真 | SoftPAT3D 生成可变形初始状态，Steel 支持异构批次 | 生成合法性、接触精度和下游学习收益尚需联合验证 | 同资产、同接触设置下比较生成流程与求解器对迁移的贡献 |
| 人类经验与跨模态动作 | SWAM 系统研究语言、视频、UMI 与机器人监督 | 数据质量、模态配比、算力和模型结构仍可能混杂 | 等数据等计算下估计标注细度和动作锚点的迁移曲线 |
| 跨传感器接触表示 | LingBot-Touch 复用冻结编码器，真实策略获得增益 | 几何标定、掌面覆盖和跨硬件误差尚未闭合 | 表示、布局和传感器物理的因子化留出测试 |
| 世界反馈与 Agent 学习 | RoboScript、Fable 5.2 将模型、工具和任务记忆连接 | 示范数量、世界交互和推理预算缺少统一记账 | 固定模型与工具，比较上下文、权重更新和两者组合的成本曲线 |
| 可靠部署与自演化基础设施 | Gemini 2.5 测物理约束，InfraRSI 验证系统改动 | 试点可靠性、验收器充分性和总成本仍需长期证据 | 独立验收器下做长期扰动、失败恢复和收益摊平评测 |

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

- 2026-11-11 新增：Gemini Robotics 2.5 工业统计与 ASIMOV 门槛；Steel 固定 Newton revision、reuse_kinematics、接触误差和训练墙钟；RoboScript rehearsal/API 总成本及真机部署代码；LingBot-Touch 4K 主表与公开编码器、全量数据；SWAM 主权重、UMI 和分批数据完整性；WanderBench 专属评分/视频包；SoftPAT3D 可执行资产；Compass 1 十二月交付；Fable 5.2 同预算机器人评测；InfraRSI 完整审计和许可。
- 2026-11-10 新增：GR00T 2 主代码/权重与 Human-1M-100K 的训练契约；MR0 固定 HF revision、Rollback/事件记忆复现；ObjectWorld 完整数据与 flow-to-action 代码；Tiresias 小预算 ranker/想象验证；DexForesight 真实遮挡和 query alignment；BAT-WAM 代码与 HTBench；WARP-JEPA held-out 任务与小 GPU 复现；REINS 感知噪声与外部成本；Spatial Harness 代码落地；RLWRLD DexBench 资源计划。
- 2026-11-09 新增：SLA 的完整训练代码/数据/权重闭合、OmniVGGT 教师和 state dropout 复现；RoboImagine 预测指标到闭环任务进度的桥接；OopsieRecover correction program 的触觉扩展；WAM-Sim memory 与 online RL 的独立归因；VisionSIM 传感器误差到控制失败链；RoboARCade 单任务成本与错误成功声称；VFlash TensorRT/算法收益分离。
- 2026-11-08 新增：GPWM 完整代码／权重／ParticleWorlds、视觉到粒子及噪声搜索的独立归因；ToyBlocks 完整数据验收、oracle 四组与接触真值；Cosmos 训练／观测接口、59D 动作契约及策略排名有效性。
- 2026-11-07 新增：Frameboy 低延迟与长期动态独立量化；PlayGen2 全图/局部状态审计及完整训练包；Open-HumanWAM 50K 上传完整性、Goal 后训练与 Vanilla 回合数协议；Spatial-UMI-Dream 预训练数据、深度扰动与动作转换；Liber-0 独立任务验收、精确动作数据占比与开放资源。

## 历史来源

- [2026-11-12 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-12/)
- [2026-11-11 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-11/)
- [2026-11-10 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-10/)
- [2026-11-09 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-09/)
- [2026-11-08 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-08/)
- [2026-11-07 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-07/)
- [2026-11-03 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-03/)
- [2026-11-01 晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-01/)
