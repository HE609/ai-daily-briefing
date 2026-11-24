# 研究地图：空间智能与通用 AI（持续更新）

## 2026-11-24 地图快照

窗口为 2026-11-21 09:00—2026-11-24 09:00（北京时间），与 23 日成稿去重。已读到 23 日 arXiv 公告批次，多数新论文 20 日提交；公告、提交与资产日期分开。新增十一项：NoPeWorld、Zing-1.0、StereoVLM、场景几何审计、Ego4Gen、LS-MBPO、Round-Trip Check、RoboTrack、RoboCap-10k 技术报告、CoEvoBench、DeepMind 形式验证量子 Agent 官方发布。NoPeWorld 21 日工件公告和 COLMAP LoMa 镜像此前漏检，按 Retrieval Failure 回补；RoboCap 数据较早已有预告，DeepMind 论文 6 日首发，均不冒称本期新论文/数据首发。

| 问题分类 | 今日映射与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 持久世界与规则 | NoPeWorld 约束命令；Zing 由引擎维护状态 | 状态、意图、渲染和交互性缺少共同验收 | 状态事件日志与画面事件配对，测违规及误停 |
| 度量空间与 real-to-sim | StereoVLM 使用双目标定；激光扫描审计 Agent 场景 | 输入证据错误与未利用已有证据混杂 | 尺度/标定干预×误差报告×留出房间 |
| 4D 表征与动作 | Ego4Gen 从几何/运动 latent 映射控制 | oracle 未来、可解码性与实际预测闭环未完全分离 | 固定任务交换/打乱 latent，测控制因果贡献 |
| 规划与模型式 RL | Round-Trip 检查搜索漏洞；LS-MBPO 缩短想象链 | 搜索更多与预测更长都可能积累失败 | 搜索预算×rollout 长度，报告成功/回归和总计算 |
| 数据与人机对齐 | RoboTrack 调整运动点分布；RoboCap 统一度量标签 | 跟踪和标签精度是否改善策略尚缺等预算证据 | 分层注入接触/尺度/遮挡噪声，测下游动作收益 |
| Agent 与科研演化 | CoEvoBench 联动模型/harness；Lean 外部验收搜索 | 首轮收益难转持续改进，弱 verifier 易自证 | 冻结外部测试，联合测每轮新增成功、回归及总成本 |

工件与指标边界：NoPeWorld 已见11个预测头和归档，Collision 的74%→16%不能配上 Prediction 的约1%开销；完整系统需上游大模型及80—96GB显存。Zing 23.82FPS 为H200加两张H100的短序列吞吐，长交互首帧10.33秒；系统代码/权重未核验公开。Stereo 8B深度与2B控制分开；控制38.1%→42.4%来自仿真。场景审计仓库主要单房演示，HF仅占位，评测代码待发布；误差报告在同30房设计测试。Ego4Gen混合视频适配后Hard15.2%→26.4%，Easy46.6%→37.2%，专家未来latent实验另列。LS-MBPO跨硬件计时不能称同硬件八倍加速。Round-Trip在Wall原MPC仅0.88→0.89，需先诊断是否存在规划漏洞。

RoboTrack轻量权重约66MB，307段基准中42段需Ego-Exo4D原权限；15M是轨迹数，Warp非商用且约47GB显存。RoboCap目录可见但manual gate，未取得全量或验证10,000小时；4.5mm手误差是对齐后的9.2分钟留出集指标，非野外真值。CoEvoBench24h/4H20/100美元教师额度，31.23为加权分数非成功率；仓库承认Docker/GPU及final-eval仍有完整性缺口。DeepMind证明位于discoveries分支；改善是形式规范/成本模型下的量子程序资源，非现有硬件实测，部分比较需230GB以上RAM。所有headline结果均为作者/官方，本轮未训练、运行机器人或重查Lean证明。

下一轮追踪：NoPeWorld模式配平、误停与接触扩展；Zing可运行工件及状态—画面一致性；Stereo模型/基准与未见标定；场景审计完整评测和留出泛化；Ego4Gen真实预测闭环与latent更新回归；LS-MBPO代码、数据与同硬件计时；Round-Trip代码和动作和可识别条件；RoboTrack遮挡分层与下游控制；RoboCap访问/manifest与噪声—收益曲线；CoEvoBench部署/评测隔离及完整研究成本；Lean规范覆盖、经典成本和完整搜索日志。

建议阅读 NoPeWorld→场景几何审计→Round-Trip→RoboTrack→CoEvoBench。第一项验证优先50问题逐轮规划失败分解，或20段可访问视频遮挡跟踪。SceneRuler、Beyond Visual Fidelity、PhiJEPA、Skill-JEPA、LDS、Embodied-Harness、Search-RSI、PhysForce和γ-Scape已检索未展开，属于Selection。[当期晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-24/)。

## 2026-11-23 地图快照

本期窗口为 2026-11-20 09:00—2026-11-23 09:00（北京时间），与 22 日成稿去重。保留六项：Waddle-1、NAT/LeRobot、Tesla Reality View、Hy4、RoboColosseum 新结果、IsaacSwim。Tesla 22 日晚架构说明为正常新增，其早期上线以及其他漏检的资产/结果按 Retrieval Failure 回补；不把旧论文或晚到新闻当成新首发。

| 问题分类 | 今日映射与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 持久空间与生成界面 | Tesla 将共享视觉特征分成动作和视频支路 | 画面合理、三维状态正确、被动作利用仍未连通 | 同一表征的状态、渲染、控制三路干预审计 |
| 动作表示与在线执行 | NAT 让因果 token 前缀直接进入执行链 | 动作压缩误差、首动作延迟与控制收益缺少统一预算 | 同策略下测前缀长度、段间跳变和限时成功曲线 |
| 机器人 Agent 与经验 | Waddle 组合云端推理、本地策略、跨尝试上下文 | 单模型能力、记忆学习与调用次数贡献混杂 | 重置协议×记忆×预算的因子实验与留出任务迁移 |
| 跨本体评估 | RoboColosseum 新榜单，Robocurve 公布系统记录 | 评级、平均进度、完整成功和成本容易被混用 | 双评分与站点重采样，测排名与可靠性的分离 |
| 多模态基础模型 | Hy4 开放权重与稀疏推理工程 | 视觉问答、长程工具能力和研究自改进未共同验收 | 对齐 harness/帧数/计算量，建立可审计的科研 Agent 任务 |
| 物理环境与 real-to-sim | IsaacSwim 扩展水下批量仿真 | 近似水动力、真实参数与策略迁移仍有误差 | 系统辨识与跨求解器留出轨迹测试，连接到策略退化 |

近期共同趋势是把能力装进可执行系统和持续评测。真正的空缺是**条件与预算可追溯的因果证据**：改善来自模型、表征、工具、记忆还是更多尝试，必须分别验收。持续研究地图已保留此前几何、材料、视频表征、人类数据与自进化分支，本期新增上述连接，不删除历史证据状态。

工件边界：Waddle 核心 Agent 服务闭源，120 条记录可核对但调用/费用字段为空；81.4% 是平均进度，64/120 是完整成功。NAT 主分支、2.16GB 策略和 tokenizer 可见，权重早于本期，新增为 21 日合并；19ms 论文与约40ms集成测试分开。Tesla 为官方说明，无公开模型工件及独立端到端计时。Hy4 BF16/FP8/基座文件可见，训练配方不完整且自定义许可；RoboColosseum SO101评级1984不等于可靠完成，API显示22.13%完整成功，服务身份未独立审计。IsaacSwim代码/评测协议可见，数值为作者报告，未重跑。

下一轮：Waddle记忆重置与预算配平、原始视频重标和实际账单；NAT严格加载/归一化/前缀一致性与闭环消融；Tesla几何、遮挡、实际延迟和生成支路因果用途；Hy4匹配harness与完整训练数据；RoboColosseum站点重采样和接入身份；IsaacSwim基准原始日志、近似物理误差和策略迁移。阅读顺序 Waddle→NAT→Tesla→RoboColosseum→Hy4。[当期晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-23/)。

## 2026-11-22 地图快照

窗口为 2026-11-19 09:00—2026-11-22 09:00（北京时间），与 21 日成稿去重。最新可读 arXiv 公告仍为 20 日。Inkling 2 Mini 的 20 日官方发布按上一轮 Retrieval Failure 回补；WALL-WM 2.0 RoboDojo Preview 的 21 日晚真实权重上传属于正常新增。Direct3D-V3、World-delta、O²LaF、CauSyncVLA、PhyDEX 等来自窗口内既有候选池，保留原提交日期，属于 Selection 调整。

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 原生几何与空间资产 | Direct3D-V3 让 SDF 直接接受几何监督 | 细节提升、粗索引误差、材质与物理可用性仍分离 | 固定粗 mesh，测薄结构与未见视角，再检验接触可用性 |
| 持久世界与证据更新 | World-delta 区分观测与补全，限制局部写入 | 静态纠错与真实对象移动仍会混淆 | 纠错、保留、运动识别三目标的持续空间基准 |
| 视频与跨本体动作 | O²LaF 复用逆、正两种动力学先验；WALL 开放预览资产 | 可解码、视频迁移和真实执行未被共同证明 | 动作交换干预，加上统一闭环与版本接口验收 |
| 在线执行与时延 | CauSyncVLA 用已执行历史更新控制记忆 | 模型耗时、观测年龄、闭环响应、限时成功常被混用 | 固定时钟和 GPU 预算，测延迟扰动与控制退化曲线 |
| 物理推理与感知 | PhyDEX 暴露抓取鲁棒性和隐藏物理信息不足 | 感知失败与不可辨识参数会污染“物理推理”分数 | 固定抓取起点，分层提供历史、力觉与 oracle 物理量 |
| Agent 计算与演化 | Inkling 开放循环深度；SkillPlumber 使用指令覆盖 | 内部计算、诊断信息和重试成本仍未公平配平 | 同权重循环实验，以及覆盖信号的预算匹配消融 |

连续地图中的近期变化是：**视频生成、可执行状态、控制相关表示和评估协议正逐渐成为独立研究对象。** 这提供更清晰的因果拆分，但也要求在模块连接处做实验：好的 mesh 是否改善接触，好的 latent 是否改变策略，正确的指令诊断是否在留出任务上保留收益。表中的机会是基于今日证据的研究推断，尚不是已经验证的结论。


工件边界：Inkling 产品固定三轮，研究模型可变循环，后期训练不同，均已见约20GB权重。Direct3D-V3三档权重已见，粗模型/训练代码待发布，公开版DINOv3/Muon不能沿用论文分数。World-delta未核验到可跑工件；O²LaF代码/权重仍待发布。CauSyncVLA公开约97MB的LIBERO updater与代码，真机权重私有，5.04倍是模型容量而非闭环加速。PhyDEX约89%的失败在投掷前，官方项目404。SkillPlumber是同任务带verifier修复，重跑稳定性、等总成本与留出任务泛化应分别验收。WALL于21日22:42实际上传约24.13GB预览权重，尚无新版结果或匹配loader的验收证明。所有实验数字均为作者/官方，本轮未做训练、付费API基准、大权重下载或机器人复现。

下一轮追踪：Inkling同权重循环与等预算独立验证；Direct3D-V3粗索引/公开版统一评测；World-delta持续更新工件与真实运动识别；O²LaF动作干预和实际开放；CauSyncVLA时间戳/观测延迟与跨骨干接口；PhyDEX固定抓取与多信息条件；SkillPlumber完整prompts/轨迹与跨任务；WALL匹配loader、完整报告、动作归一化和固定初态闭环。SolarWM 20日训练提速公告已跟踪，尚未独立核验硬件与等质量计时。

最小验证优先级：十场景纠错×保留×真实运动 → 动作probe×交换干预×闭环 → 固定抓取的信息充分性 → 同权重循环与指令覆盖的预算消融。ScaleWorld、Streaming-AAA、PGX、Fast-JEPA、SpatialMem、TuringSpace、System-One RSI、TwinLab-Bench与自蒸馏记忆报告已检索未展开，属于Selection；StrideWorld与Tripo宣传按原日期去重。[当期晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-22/)。

## 2026-11-21 地图快照

窗口为 2026-11-18 09:05—2026-11-21 09:05（北京时间），与 11 月 20 日成稿去重。最新可读 arXiv 公告批次为 20 日，多数新增论文实际于 19 日 UTC 提交。WM^MLLM 的 18 日论文与实现按 Retrieval Failure 回补；Genie 4、WorldRuler、Phoenix、Z-sight、PhysResponse、LightHarness、Doppel、Grana、F³、AHE-Beta、CDF 与 Neon 未因窗口重叠而机械重列。本期判断是状态、可表达形变、材料响应、动作效应和评估器精度需要分别建模并用独立证据连接。

| 问题分类 | 今日工作与趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 持久空间与几何 | WM^MLLM 外部 revision/全景状态；Plan4D 从共享 latent 读出 RGB 与几何 | 确定性恢复、语义编辑、尺度精度与真实部署并不等价 | 状态不变量×请求成功×几何对策略贡献的三层审计 |
| 对象交互与 real-to-sim | PRIO 预训练线性形变基；MorphTwin 扩大 bulk/shear 响应 | 形变可表达性、材料可辨识性和物理求解器贡献混合 | 固定几何/材料/外力，分别测表示误差与留出刺激响应 |
| 动作与规则 | AFFECT 匹配动作扰动引起的视觉交叉矩；RIFT 用校准纠偏频率先验 | 预测美观、规则辨识和策略排序仍无共同保证 | 动作扰动×采样频率×校准充分性的统一受控基准 |
| 触觉与跨本体监督 | TacInno 学触觉剩余信息；Awaken-HI 保留原始人体运动 | 新监督、容量、数据规模和 retargeting 误差难分 | 固定资源和机器人数据，比较监督内容与形态差异 |
| 数据和视频分析 | HumanCOIN 意图代理与多频率同步；WeMM 原声音画理解 | 意图冗余、设备/音轨捷径和时间泄漏尚待排除 | 跨设备/操作者留出、音轨替换和时序偏移的配对实验 |
| Agent 诊断与演化 | AgentRoboCritic 局部意图归因；Sage 改变观察分辨率 | 自评偏置、诊断误差、选择噪声与总成本混杂 | 固定候选库和外部验收，联合测 rescues/regressions、迁移与成本 |

工件边界：WM^MLLM 会话引擎不包含视频模型/完整实验输出，首次播放中位 609.4 秒，程序 demo 不代表生成性能；Plan4D 项目代码入口占位，尚无本轮核验的完整工件。PRIO、MorphTwin、AFFECT、RIFT、Sage 未核验到官方可跑实现/完整数据与权重。TacInno 已见 tokenizer/策略权重与约 112 GB 仿真示范目录，部署仍需真实触觉输入；Awaken-HI 推理/权重仍 TODO，Awaken-Human 仅约 17 MB 单录制预览，不能称 50,000 小时全量开放。HumanCOIN 工具与多项门控数据目录可见，L1 gaze 多为推断，EEG 只覆盖 L3 500 小时，尚无意图监督提高策略成功率的证明。WeMM 已见 2B/35B-A3B 权重与模型实现，完整预训练语料未开放。AgentRoboCritic 已见代码、400 条人工测试集、12,844 训练/1,548 验证样本及 critic 权重；Overall Accuracy 67.75% 限制其作为终局验收器的可靠性。所有重点数字均为作者/官方报告，本轮未复现训练或真机。

下一轮追踪：WM^MLLM 完整协议/输出、端点检查误差与生成成功成本；Plan4D 代码/权重及未对齐尺度与闭环任务；PRIO 工件、材料条件与真实接触；MorphTwin 完整数据、材料真值和跨图响应复用；AFFECT 扰动数据、特征盲区和规划收益；RIFT 基准/实现、短校准与规则切换；TacInno 单任务 code/tactile-off 对照及真实部署；Awaken-Human 完整 manifest、代码/权重和等计算量 scaling；HumanCOIN 跨层小时数、同步误差与额外信息价值；WeMM 采帧/音轨/推理模式对照；AgentRoboCritic 跨 actor 和独立人工标注；Sage 完整轨迹、观察更新与固定目标选择偏差。

最小验证优先级：十场景状态/编辑双评分 → 三对象表示×材料交叉刺激 → 动作效应与规则先验的二维实验 → 多模态时间/音轨扰动 → 八候选×二十任务固定外部验收。Fast-JEPA、O²LaF、ActMem、PGX、PhyDEX、TwinLab-Bench、System-One RSI、World-delta 和 SceneAnything 已进候选池，未展开属于 Selection。[当期晨报](https://he609.github.io/ai-daily-briefing/reports/2026-11-21/)。

## 2026-11-20 地图快照

本期窗口为 2026-11-17 09:10—2026-11-20 09:10（北京时间），与 11 月 19 日去重。Genie 4 因 18 日产品开放、19 日 API 新入口重访；Neon、CDF 等未识别官方证据按 Retrieval Failure 回补。18 日论文保留原提交日期。核心判断是交互世界开放、可执行状态、控制表征和外部验收同时推进，但相互之间仍需独立实验连接。

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 持久交互世界 | Genie 4 开放 API；WorldRuler 维护规则、身份与离屏状态 | 视频连贯、可存取状态和真实物理仍分开验收 | 建立规则执行、首次可见、重访和接触的分层测试 |
| 空间与视频表征 | Phoenix 外部双教师；Z-sight 原生 token 未来 | 可解码、被动作读取与真实成功尚未完全解耦 | 同数据/容量下比较教师来源、未来目标和读取机制 |
| 可编辑空间重建 | LightHarness 用光照证据和程序输出场景 | 单视图外观能掩盖错误几何与材料 | 用留出光照、视角和对象插入测可辨识性 |
| 跨本体与人类数据 | Doppel 将身体渲染作为共同视觉接口 | 外参、身体模型和环境响应相互混杂 | 固定动作，交叉扰动标定、身体外观和接触条件 |
| 物理与进度评估 | PhysResponse 测参数/临界事件；Grana 测组合进度 | 参数正确、事件正确和奖励有效性没有共同真值 | 建立状态、事件、进度和策略收益的配对审计 |
| 经验与持续改进 | F³ 学何时注入；AHE-Beta 按需求验收 | 记忆增长与候选增加仍可能引入回归和选择偏差 | 固定候选池，用外部验收测 rescue/regression 与迁移 |
| 数据和 Agent 基础设施 | CDF 编排生成/检查；Neon 展示 harness 差异 | 自动质量分数、有效样本和总成本不等价 | 建立含失败重试、人工复核和下游收益的数据账本 |

本期工件边界：RuleVerse 的 manifest 是 upload_in_progress（103/168 分片），WorldRuler 模型页仍占位且推理代码待发布；Phoenix checkpoint 和多分支可见，但原始准备不全且正式配方 224 GPU；Z-sight 所链仓库 404；Doppel 权重约 33 GB overlay，依赖上游 Wan 且非商用；LightHarness CPU demo 是合成证据；Grana 未确认论文权重/全量训练数据；PhysResponse 补充材料和 F³ 工件待补；AHE-Beta 的 offline demo 不代表真实演化收益。所有模型/机器人数字仍为作者或官方结果，本轮未完整复现。

下一轮优先追踪：Genie 4 API 协议、延迟、价格和独立状态持久性测试；RuleVerse 全量清单与 WorldRuler 推理实现/权重；Phoenix 数据准备、跨基准 checkpoint 与小规模 encoder 对照；Z-sight 公开工件和未来 token 干预；PhysResponse 数据/补充材料及评估器误差；LightHarness 32 输入的等预算重建；Doppel 相机真值与接触/策略收益；Grana 奖励权重和失败恢复标注；F³ 经验库与配对续跑；AHE-Beta 留出任务、需求验收与演化总成本；CDF 自动过滤的物理误判及完整成本。

近期最小实验：十场景离屏规则/存档恢复；未来 token 内容×可信度四格；参数响应×临界事件×进度奖励；十视频三种增强的验收器盲点；八候选×二十任务的独立需求选择。保留历史快照，不把产品开放、文件存在、渲染质量或脚本 demo 升级为闭环成功。

## 2026-11-19 地图快照

本期按 2026-11-16 10:30—2026-11-19 10:30（北京时间）检索。相对 11 月 18 日成稿，仅在有新版本、代码/权重、基准结果或独立审计证据时重复；π⁴、RelayWAM、RFW-S、CWM2、FastFrames、ScaleVLA、HubEgo、Hidden Variables、Resolution、GPT-6.2 与 CloudRobo-WM1.2 没有新的足够强工件，因此不机械重列。本期横跨“可观测状态—可执行世界—未来信息读取—接触与跨本体接口—评估器分辨率”，核心新增是 RWM 独立审计和机器人原生长时交互接口。

| 问题分类 | 今日工作与趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 世界模型审计与不确定性 | RWM 同时测一步、长时 rollout、策略、剪枝和置信度 | 预测指标与策略成功的排序不稳定；覆盖率远离名义校准 | 建立 prediction→policy→calibration 三层统一审计协议，并跨本体复用 |
| 机器人原生长时视频 | DreamFAR 用接触关键帧、KV cache、流式 DiT 支撑分钟级交互 | 权重、真实闭环成功、数据许可证和低价硬件路径未完整开放 | 同一动作轨迹比较 10 秒视觉质量、60 秒状态漂移与策略成功 |
| VLA—Agent 工具接口 | InteractVLA 暴露几何目标/相机反馈；ForceHarness 暴露力与物理摘要 | 额外重规划、API 延迟、接口误差和成功率尚无统一成本账本 | 做 geometry/force 双接口的诊断、回退和成本一致性基准 |
| 4D 与跨本体动作 | TCP4D 用 TCP SE(3) 连接视频、场景与 retargeting | TCP 误差、接触约束和关节控制成功仍分离 | 人类视频→TCP→关节策略的三阶段留出评测 |
| 结构化空间与反应场景 | JointGV 纠正 scene graph 漂移；驾驶 WM 让背景车辆对 ego 反应 | 节点误差、渲染误差、规划风险和真实安全没有共同真值 | counterfactual scene edit×closed-loop policy×risk 的统一基准 |
| 手控交互视频 | LynnReal-Hand 将手动作与相机姿态作为交互视频条件 | MANO/FVD 与真实接触、物体动力学脱节 | 手轨迹扰动、身份保持、接触事件和机器人控制的联合评测 |
| Agent 自演化与评估器 | Self-Org 让模型自发组织学习循环；Resolution 研究选择器分辨率 | 候选生成、噪声、成本与 transfer 混在一起 | 固定候选池与留出机制，测“可检测的最小改进”曲线 |

本期优先验证：CPU 复现 RWM 的短/长时差异；用公开 sample 审计 DreamFAR 的延迟与状态漂移；冻结同一 VLA 做 InteractVLA/ForceHarness 双接口四格实验；用 20 段视频检查 TCP4D 的 TCP—接触—retargeting 链。保留历史快照，不把作者或官方报告自动升级为第三方验证。

## 2026-11-18 地图快照

本期按 2026-11-15 13:40—2026-11-18 13:40（北京时间）检索；以最近可核验的 11 月 15 日成稿去重，保留 16、17 日缺口。跨层问题是“状态是否可靠—信息是否被用到—改进是否能被测出”，不以预测、渲染或单一榜单代替闭环成功。

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 4D 状态与动态几何 | π⁴ 将几何、相机、尺度、轨迹统一 | 相机运动、物体运动与下游控制误差仍纠缠 | 固定场景和动作，分离几何漂移、轨迹误差与策略失败 |
| 可控生成与持久世界 | CWM2 显式状态；FastFrames 压缩响应链路 | 吞吐、响应、持久性和物理正确性尚未统一 | 同一代理世界比较状态误差、重访一致性和 p95 响应 |
| 可变形生成仿真 | RFW-S 将校准与留出刺激验证分开 | 材料真值、跨求解器与完整性指标不足 | 校准刺激×验证刺激×求解器的交叉物理协议 |
| 预测表征到动作 | RelayWAM 建立读取通道；ScaleVLA 扩大冻结骨干 | 可解码信息、因果使用和规模收益尚未分离 | 未来监督×读取结构×骨干规模的等预算消融 |
| 人类数据与机器人质量 | HubEgo 扩展熟练工作；Hidden Variables 审计采集 | 多样性、标定一致性与动作语义缺因果对照 | 环境留出×标定漂移×跨本体接口的迁移曲线 |
| Agent 与自演化 | Resolution 审计选择噪声；GPT-6.2 改善能力／成本 | 更强候选与更准选择器的贡献混在一起 | 固定候选池，比较模型升级和重复评估预算 |
| 原生 WAM 与开放边界 | WM1.2 强调异构监督和多推理模式 | 官方叙述、可下载工件与可比评测仍有距离 | 建立 observation／action mask／mode 的版本化验收契约 |

## 下一轮追踪

- 2026-11-18 新增：π⁴ 的 0.5B 共享几何／运动与公开非商用权重；RelayWAM 的未来信息因果使用；RFW-S 的 100,000 生成资产与 83,365 通过交集；CWM2／InvokerRender 推理代码权重；FastFrames 的解码器／KV 修复器；ScaleVLA 的 552B 冻结编码器；HubEgo 首批 10,124 小时；真实数据标定与遥操作隐藏变量；Resolution Hypothesis 的选择器噪声审计；GPT-6.2 官方发布；CloudRobo-WM1.2 从预告推进到正式发布。
- 工件优先补查：RelayWAM 的代码与策略；RFW-S 的实际下载、许可证、材料测量与跨求解器验证；CWM2 长演示质量策略、训练代码和对齐数据；FastFrames 在统一硬件下端到端延迟；ScaleVLA 完整策略与固定数据；HubEgo 分批内容与真实机器人迁移；Hidden Variables 的原始实验数据；Resolution 的完整候选池／轨迹；CloudRobo-WM1.2 权重、代码、许可与榜单协议。
- 近期最小验证：25 帧动态几何与相机重访；未来监督×读取结构四格；20 资产留出刺激；8 候选×20 任务重复评估。固定版本、硬件、种子、测试与成本账本，再谈跨层迁移或规模收益。

## 2026-11-15 地图快照

| 问题分类 | 今日工作与近期趋势 | 尚未解决的 gap | 可形成论文的机会 |
|---|---|---|---|
| 开放 WAM 与跨本体动作 | Praxis-1 把视频未来、动作 expert、DROID/YAM/SO-101 和 LeRobot 接口放入一个可下载包 | 27B 推理成本、动作 head、长时任务和真实硬件适配仍缺独立对齐 | 固定视频 backbone，比较 action head、LoRA、NVFP4 和 embodiment projection 对跨本体成功率与成本的独立贡献 |
| 可执行 4D 世界与生成式渲染 | WorldDraft 用代码构造世界、视频模型渲染外观，并分别计分 preservation、realization、persistence 和 leakage | renderer 分数与真实物理接触、策略成功和长期状态仍未连接 | 将 WorldDraft 指标与 Atlas/Spatial Foundry 的几何重访、接触预测和下游策略放进同一三层协议 |
| 物理语言与视频表征 | PhysCapBench 用 1,500 个序列和七个 physical dimensions 评估 caption 是否保留接触、事件和状态变化 | 可见信息、语言压缩、跨本体动作和真实控制之间缺少因果归因 | 建立 caption precision/recall → video latent quality → closed-loop success 的冻结模型链路 |
| Agent 验收与持久场景 | Reins 用 guarded chain、narrator、3D tools 和 scene twin 处理长时真机；Praxis-1 计划与快速策略形成互补 | API 延迟、旁观者误判、场景 twin 误差和外部副作用尚无统一成本账本 | 在 resettable harness 中统一记录 success、rollback、narrator lag、token、wall-clock、twin error 和 transfer |
| 世界模型规划与动作连续性 | Rethinking Actions 把 expert temporal structure 放进 GP prior，ActWorld-JEPA 把 latent future 放进 candidate reranking | 预测质量、动作连续性、候选覆盖和真实成功仍由不同指标表示 | 做 action history × future latent × planning budget 三因素冻结实验，并报告长时失败阶段 |
| 低算力 world-model RL | BlinkMimic 把 differentiable simulation、failure-directed reset 和 CUDA graph 压到单卡分钟级 | 单一动作库和仿真结果无法证明真实 humanoid 鲁棒性 | 统一 fit/tail/iteration 账本，跨 MuJoCo、Newton、Genesis 和不同动作库做可迁移性验证 |
| 证据与发布基础设施 | Praxis、WorldDraft、ActWorld、BlinkMimic 公开了不同层级的代码、权重、数据和评测脚本 | 论文、artifact、revision、runtime、seed、成本常常分散在不同页面 | 为 world model/VLA/agent 建立 provenance lockfile，要求每个数字绑定版本、输入、硬件和验收器 |

## 下一轮追踪

- 2026-11-15 新增：Praxis-1 的 SO-101/NVFP4/LeRobot artifacts；WorldDraft 的 48 executable worlds、432 paired cases、Apache-2.0 代码与 805 MB HF 数据；PhysCapBench 的 1,500 序列与七维物理标注；Reins 的 guarded chain/narrator/scene twin；Rethinking Actions 的 LG-DKGP 与五任务权重；ActWorld-JEPA 的 PC-JEPA/R³ 选择器和 NAVSIM/nuScenes artifacts；BlinkMimic 的单 RTX 4090 三分多钟配方。
- 优先补查：Praxis-1 SO-101 真机或硬件在环日志；WorldDraft 与真实接触或策略成功的桥接；PhysCapBench 数据 revision、许可证和 caption-to-policy 归因；Reins 代码及 narrator lag；Rethinking Actions 的真实机器人迁移；ActWorld-JEPA 的非官方 GPU 复跑；BlinkMimic 的多动作库和真机部署。

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
