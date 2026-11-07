# Yunhe · 科研日报

[打开日报网站](https://he609.github.io/ai-daily-briefing/) · [固定最新一期入口](https://he609.github.io/ai-daily-briefing/latest/) · [研究地图](https://he609.github.io/ai-daily-briefing/map/) · [RSS](https://he609.github.io/ai-daily-briefing/feed.xml)

以网页阅读为主的中文科研日报。首页展示最新一期与精读顺序，历史归档支持全文搜索、主题和月份筛选；正文有章节目录、相邻日期、阅读进度与 Markdown 下载。手机和电脑使用同一个网址。

归档同时保留此前的 AI 前沿情报和后续的空间智能与通用 AI 晨报。只收录已保存的完整成稿，不为缺失日期补造内容。历史条目中的资源、证据与复现状态以当时成稿为准。本地附件链接不随网页发布。

## 每日发布

现有每日研究任务生成完整 Markdown 和研究地图后，运行下面的发布脚本。脚本只提交报告内容；每次 push 后，GitHub Actions 自动构建、检查并部署 GitHub Pages。

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/publish.py --source ..
```

默认从上一级工作目录导入 `科研晨报-YYYY-MM-DD.md`、早期的 `YYYY-MM-DD-自动化科研晨报-*.md` 与 `研究地图-持续更新.md`。已存在的 GitHub 早期日报直接保留。10 月 2 日仅有 Word 来源，已提取正文、表格与超链接归档。

发布脚本要求干净的 `main` 分支并只允许本仓库的远端；发生冲突时会停止，不会覆盖其他修改或强制推送。发布完成需要确认对应 commit 的 Pages 工作流成功。定时研究任务在本地运行，运行时电脑和桌面应用需要保持开启；GitHub 负责接到 push 后的部署。

## 本地预览与检查

```sh
.venv/bin/python scripts/sync_reports.py --source ..
.venv/bin/python scripts/build.py
.venv/bin/python scripts/check.py
.venv/bin/python -m http.server 8765 --bind 127.0.0.1 --directory public
```

检查覆盖报告日期、全文索引、所有本地链接和章节锚点、数学字体与订阅源。浏览器所需的脚本和字体随站点发布，无需外部 CDN。`site.json` 可设置站点信息及个别期数的首页标题摘要。报告也可选用 YAML front matter 设置 `headline`、`summary`、`topics`；不设置时从正文自动提取。

## 原始项目介绍

本仓库由he维护，旨在每日整理和分享AI领域的最新技术动态、顶会论文、产业新闻及前沿进展。内容聚焦于世界模型（World Model）、JEPA、具身智能（Embodied Intelligence）、空间智能（Spatial Intelligence）、视觉-语言模型（VLM）、空间推理、LLM可解释性等热门研究方向，覆盖AI理论、应用与跨模态智能的前沿探索。

**主要内容包括：**
- AI最新学术论文追踪与解读
- 具身智能、空间智能等核心领域的代表进展
- 业界创新技术及产品动态
- 产业融资与市场趋势分析
- 重点模型及多智能体系统、代码执行范式等解构
- AI for Science、AI+新应用案例

本简报坚持每日更新，便于AI行业研究者、学生和从业者快速把握前沿脉搏，获取有价值的信息参考。

---

Maintained by Yunhe Ni, this repository curates daily briefings on cutting-edge AI research, technology trends, top-conference papers, and industry news. Focus areas include World Models, JEPA, Embodied Intelligence, Spatial Intelligence, Vision-Language Models (VLM), Spatial Reasoning, and LLM Interpretability—covering both theoretical innovations and cross-modal, embodied AI applications.

**Highlights:**
- Tracking and interpreting the latest academic papers in AI
- Key progress in embodied intelligence, spatial intelligence, and related fields
- Spotlights on industry innovation, product trends, and funding
- In-depth breakdowns of state-of-the-art models, multi-agent systems, and code execution paradigms
- AI for Science, and new cross-domain applications

Daily updates enable researchers, students, and professionals in AI to keep pace with the latest advancements and gain actionable insights.

---
⚠️ 所有内容由AI自动生成，仅供研究与学习参考，不构成投资建议。
