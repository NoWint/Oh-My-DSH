# Oh-My-DSH — DeepSeek Harness Plugin Ecosystem

> **Data source:** GitHub `dsh-plugin` topic + `deepseek-harness` keyword search, as of 2026-08-15
> **数据来源：** GitHub `dsh-plugin` topic + `deepseek-harness` 关键词搜索，截至 2026-08-15
> The `dsh-plugin` topic contains **2,300+** repositories; this is a curated subset organized by category and stars.
> `dsh-plugin` topic 共 **2,300+** 个仓库，以下为按类别和 Star 精选的子集。

> **🏆 The only automated, multi-source DSH plugin discovery engine on GitHub.**
> **GitHub 上唯一的多源自动化 DSH 插件发现引擎。**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](scripts/dsh_discovery.py)
[![Tests](https://img.shields.io/badge/Tests-72_passing-brightgreen.svg)](tests/)
[![Update Frequency](https://img.shields.io/badge/Update_Hourly-automated-orange.svg)](scripts/dsh_discovery.py)
[![Stars of deepseek-harness](https://img.shields.io/github/stars/deepseek-ai/deepseek-harness?label=deepseek--harness&style=social)](https://github.com/deepseek-ai/deepseek-harness)

---

## ⚡ Quick Start / 快速开始

```sh
# Clone & install the hourly discovery agent
git clone https://github.com/NoWint/Oh-My-DSH.git
cd Oh-My-DSH/Oh-My-DSH
cp .env.example .env   # add your GITHUB_TOKEN (optional but recommended)
chmod 600 .env
./scripts/install-hourly-discovery.sh install
```

That's it. Every hour the pipeline scans 6 data sources, validates plugins against evidence rules, and updates this README automatically.

> **只需一条命令**：克隆 → 复制 `.env` → 安装 LaunchAgent，之后全自动运行。

---

## 📊 Ecosystem at a Glance / 生态总览

| Metric / 指标 | Value / 数值 |
|---|---|
| `dsh-plugin` topic total / 话题总仓库数 | **2,700+** |
| Curated & validated entries / 精选收录 | **~647+** |
| Data sources scanned / 扫描数据源 | **6** (GitHub · GitLab · Hacker News · Lobsters · Stack Exchange · Reddit) |
| Update frequency / 更新频率 | **Hourly** (LaunchAgent, 3600s interval) |
| Validation classification / 验证分级 | **4-tier**: validated · probable · lead · rejected |
| Highest-starred plugin / 最高 Star 插件 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐ 1.9k |
| Primary languages / 主要语言 | TypeScript · JavaScript · Python |
| Categories covered / 覆盖类目 | **19** (see Table of Contents) |
| Last full scan / 最近扫描 | 2026-08-15 · **+22 new** resources across 9 categories, 16 star counts refreshed |

---

## 🏆 Why Oh-My-DSH? / 为什么选择我们

| Feature / 特性 | NoWint/Oh-My-DSH | LaplaceYoung/oh-my-dsh | like-study1/Oh-My-DSH | AdamPlatin123/awesome-dsh-plugins |
|---|:---:|:---:|:---:|:---:|
| Multi-source scanning / 多源扫描 | ✅ **6 sources** | ❌ GitHub only | ❌ GitHub only | ❌ GitHub only |
| Evidence-based validation / 证据验证 | ✅ 4-tier system | ❌ None | ❌ None | ❌ None |
| Auto-update / 自动更新 | ✅ **Hourly** | ❌ Manual | ✅ Every 8h | ❌ Manual |
| Cross-platform sources / 跨平台 | ✅ HN · RE · SE · Lobsters | ❌ | ❌ | ❌ |
| Bilingual (EN/ZH) / 双语 | ✅ | ❌ ZH only | ❌ ZH only | ❌ ZH only |
| Test suite / 测试套件 | ✅ **7 test files** | ❌ | ❌ | ❌ |
| GitOps safety / Git 操作安全 | ✅ lock + rollback | ❌ | ❌ | ❌ |
| Star count / Star 数 | ⭐ 4 | ⭐ 43 | ⭐ 16 | ⭐ 641 |

> **核心差异**：其他 oh-my-dsh 项目是**静态 README 列表**，Oh-My-DSH 是**活的发现引擎**——自动扫描、自动验证、自动更新目录。

---

## 📋 Table of Contents / 导航索引

- [⚡ Quick Start / 快速开始](#-quick-start--快速开始)
- [📊 Ecosystem at a Glance / 生态总览](#-ecosystem-at-a-glance--生态总览)
- [🏆 Why Oh-My-DSH? / 为什么选择我们](#-why-oh-my-dsh--为什么选择我们)
- [🤝 Contributing / 贡献](#-contributing--贡献)
- [🏠 Core / 核心](#-core)
- [📂 Awesome Lists / 精选列表](#-awesome-lists)
- [🖥️ Desktop Clients / 桌面客户端](#-desktop-clients)
- [⌨️ Terminal TUI / 终端 TUI](#-terminal-tui)
- [👁️ Vision & Multimodal / 视觉与多模态](#-vision--multimodal)
- [🌐 Browser & Web Enhancements / 浏览器与 Web 增强](#-browser--web-enhancements)
- [🛠️ Development Tools / 开发工具](#-development-tools)
- [🔧 Utility Toolkit / 实用工具集](#-utility-toolkit)
- [💬 Communications & IM Bridges / 通讯与 IM 桥接](#-communications--im-bridges)
- [🧠 Memory & Persistence / 记忆与持久化](#-memory--persistence)
- [🤖 Multi-Agent & Workflows / 多 Agent 与工作流](#-multi-agent--workflows)
- [🎨 Skins & Desktop Pets / 皮肤与桌宠](#-skins--desktop-pets)
- [🔔 Notifications & Status / 通知与状态](#-notifications--status)
- [📊 Data & Finance / 数据与金融](#-data--finance)
- [🎮 Entertainment / 娱乐与趣味](#-entertainment)
- [📚 Tutorials & Guides / 教程与手册](#-tutorials--guides)
- [🔌 Infrastructure / 基础设施](#-infrastructure)
- [🎙️ Voice & Audio / 语音与音频](#-voice--audio)
- [⚡ Skills & Methodologies / 技能与方法论](#-skills--methodologies)
- [🔬 Advanced & Experimental / 高级与实验性](#-advanced--experimental)
- [📥 Installation / 安装](#-installation--安装)

---

## 🏠 Core / 核心

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 92.4k | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | Official core: **Everything is a Plugin.** Plugin-based agent harness powered by [Cordis](https://github.com/cordiverse/cordis). / 官方核心：**万物皆可插件。** 基于 Cordis 的插件化 agent 框架。 |

---

## 📂 Awesome Lists / 精选列表

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 856 | [AdamPlatin123/awesome-dsh-plugins](https://github.com/AdamPlatin123/awesome-dsh-plugins) | Radar: auto-scans all dsh plugin candidates; verified ones moved to curated index. / 雷达：自动扫描所有 dsh 插件候选，经测试移入精选目录。 |
| ⭐ 1.32k | [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | Curated plugin list for DeepSeek Harness. / DeepSeek Harness 精选插件列表。 |
| ⭐ 384 | [0xsline/awesome-deepseek-harness](https://github.com/0xsline/awesome-deepseek-harness) | DSH ecosystem: curated plugins, tools & infrastructure from dsh-external/hub and public dsh-plugin topic. / DSH 生态精选：来自 dsh-external/hub 及公开 dsh-plugin topic 的插件、工具与基础设施。 |
| ⭐ 47 | [Alex-Yanggg/awesome-DSH-plugin](https://github.com/Alex-Yanggg/awesome-DSH-plugin) | Meticulously curated list of plugins, extensions, tools & dev resources for DSH. / 精心编排的 DSH 插件、扩展、工具与开发资源列表。 |
| ⭐ 32 | [libukai/awesome-deepseek-harness](https://github.com/libukai/awesome-deepseek-harness) | The Ultimate Guide to DeepSeek Harness: QuickStart, Resources, Plugins & Toolkit. / DeepSeek Harness 终极指南：快速入门、资源推荐、精选插件与实用工具。 |
| ⭐ 92 | [bruc3van/awesome-dsh-plugin](https://github.com/bruc3van/awesome-dsh-plugin) | Find your DSH plugin in 30 seconds — not just a list, tells you what problem it solves. / 30 秒找到适合你的 DSH 插件：不只是列表，告诉你解决什么问题。 |
| ⭐ 30 | [Dominic789654/awesome-deepseek-harness](https://github.com/Dominic789654/awesome-deepseek-harness) | Curated plugins, skills, MCP servers, orchestrators & UIs for DSH. / DSH 精选插件、Skills、MCP Server、Orchestrator 与 UI。 |
| ⭐ 44 | [LaplaceYoung/oh-my-dsh](https://github.com/LaplaceYoung/oh-my-dsh) | 700+ plugin ecosystem, registered only via extension seams, never modifying the agent-loop skeleton. / 700+ 插件生态，只通过扩展接缝注册，不修改 agent-loop 骨架。 |
| ⭐ 22 | [like-study1/Oh-My-DSH](https://github.com/like-study1/Oh-My-DSH) | Community-maintained Oh-My-DSH mirror: auto-synced dsh-plugin catalog every 8 hours. / 社区维护的 Oh-My-DSH 镜像：每 8 小时自动同步 dsh-plugin 生态精选。 |
| ⭐ 7 | [kejixiaoliang/awesome-dsh-plugins](https://github.com/kejixiaoliang/awesome-dsh-plugins) | DeepSeek Harness plugin curated directory — 14 categories, 280+ community plugins across MCP / Skill / TUI / Multi-Agent / Memory / Skins. / DSH 插件精选目录，14 类 280+ 社区插件，覆盖 MCP/Skill/TUI/多Agent/记忆/皮肤分类索引。 |
| ⭐ 11 | [zp-home/dsh-recommend](https://github.com/zp-home/dsh-recommend) | DSH plugin ecosystem transparent ranking: daily auto-scan of dsh-plugin topic, public scoring model, ranked lists, and static recommendation site. / DSH 插件生态透明排行：每日自动抓取 dsh-plugin 话题 + 公开评分模型 + 排行推荐插件与静态站。 |
| ⭐ 7 | [white0dew/awesome-dsh-plugins](https://github.com/white0dew/awesome-dsh-plugins) | Awesome DSH Plugins: a public GitHub directory for DSH plugins, install commands, and ecosystem tools. / DSH 插件公共 GitHub 目录，含安装命令与生态工具。 |
| ⭐ 4 | [billLiao/awesome-dsh-plugin](https://github.com/billLiao/awesome-dsh-plugin) | A curated list of plugins for DeepSeek Harness (dsh). / DeepSeek Harness 精选插件列表。 |
| ⭐ 5 | [YYTbit/awesome-dsh-bridges](https://github.com/YYTbit/awesome-dsh-bridges) | Bridge your favorite AI coding tools into DeepSeek Harness. / 将各 AI 编码工具桥接到 DSH。 |
| ⭐ 3 | [calderbuild/awesome-deepseek-harness](https://github.com/calderbuild/awesome-deepseek-harness) | Curated DeepSeek Harness resources: docs, concepts, packages, plugins, and write-ups. / DSH 精选资源：文档/概念/包/插件/写作。 |
| ⭐ 9 | [the-beating-light-of-the-nail/dsh-meme-hub](https://github.com/the-beating-light-of-the-nail/dsh-meme-hub) | The meme side of DeepSeek Harness — 贪玩蓝鲸/QQ2006/whale girls/mini-games curated tour. / DSH 梗文化精选：蓝鲸/QQ2006/鲸鱼娘/小游戏导览。 |
| ⭐ 2 | [uyq/awesome-dsh](https://github.com/uyq/awesome-dsh) | The community ecosystem and plugin directory for DeepSeek Harness. / DeepSeek Harness 社区生态与插件目录。 |
| ⭐ 2 | [cccakeee/awesome-dsh-plugins](https://github.com/cccakeee/awesome-dsh-plugins) | Evidence-led curated DSH plugin directory with verified loadable extensions. / 证据驱动的 DSH 插件精选目录：可验证加载的扩展。 |
| ⭐ 2 | [vvlife/awesome-deepseek-harness-plugins](https://github.com/vvlife/awesome-deepseek-harness-plugins) | Curated list of plugins, tools, skins, and extensions for DSH. / DSH 精选插件/工具/皮肤/扩展列表。 |
| ⭐ 1 | [HackSing/dsh-plugins](https://github.com/HackSing/dsh-plugins) | Bilingual, continuously maintained directory of DSH plugins. / 双语持续维护的 DSH 插件目录。 |
| ⭐ 1 | [tmstack/awesome-harness-plugins](https://github.com/tmstack/awesome-harness-plugins) | Awesome DeepSeek Harness Plugin. / DSH 精选插件。 |
| ⭐ 1 | [dshworks/awesome-dsh-themes](https://github.com/dshworks/awesome-dsh-themes) | Registry of DeepSeek Harness themes and --dsw-* token skins. / DSH 主题与 token 皮肤注册表。 |
| ⭐ 15 | [ZASENJC/dsh-plugins-store](https://github.com/ZASENJC/dsh-plugins-store) | Auto-collected static catalog site for GitHub dsh-plugin topic — auto-categorizes and indexes plugins. / 自动收录分类 GitHub dsh-plugin Topic 项目的静态目录网站。 |
| ⭐ 8 | [Noob-stupid/dsh-plugin-hub](https://github.com/Noob-stupid/dsh-plugin-hub) | DSH plugin management panel: one-click enable/disable + GitHub dsh-plugin marketplace with plugin details and one-click install. / DSH 插件管理面板：一键启用/停用 + GitHub dsh-plugin 插件市场，带插件详情与一键安装。 |
| ⭐ 2 | [loguhan/dsh-workshop](https://github.com/loguhan/dsh-workshop) | Steam Workshop–style plugin store for DeepSeek Harness Web UI: browse 850+ community plugins, rating, one-click install. / Steam Workshop 风格 DSH Web UI 插件商店：浏览 850+ 社区插件，评分排序，一键安装。 |
| ⭐ 2 | [imlishiyuan/deepseek-harness-zh-cn](https://github.com/imlishiyuan/deepseek-harness-zh-cn) | Chinese-first plugin for DeepSeek Harness — translates the entire Web UI and agent interaction flow into simplified Chinese. / DSH 中文优先插件：将完整 Web UI 和 Agent 交互流程本地化为简体中文。 |

---

## 🖥️ Desktop Clients / 桌面客户端

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 1.96k | [anywhere-labs/deepseek-harness-desktop](https://github.com/anywhere-labs/deepseek-harness-desktop) | Electron desktop app deeply adapted for macOS & Windows — best out-of-the-box DSH experience. / 深度适配 macOS 和 Windows 的 Electron 桌面端，最佳开箱即用体验。 |
| ⭐ 326 | [PM-Shawn/Abu-Cowork](https://github.com/PM-Shawn/Abu-Cowork) | Open-source alternative to Claude Cowork — local-first AI agent desktop app with self-evolving skills, multi-model, privacy-first, and multi-Harness roadmap. / 本地优先 AI Agent 桌面应用：自进化技能、多模型、隐私优先，支持多 Harness 路线图。 |
| ⭐ 159 | [dataelement/dsh-desktop](https://github.com/dataelement/dsh-desktop) | Desktop for DeepSeek Harness. / DeepSeek Harness 桌面客户端。 |
| ⭐ 76 | [myYangyunfan/dsh_desktop](https://github.com/myYangyunfan/dsh_desktop) | Windows desktop client — bundled Node.js + dsh CLI, one-click launch. / Windows 桌面客户端，内置 Node.js + dsh CLI，一键启动。 |
| ⭐ 52 | [ChisaAlter/Deepseek-Harness-Desktop](https://github.com/ChisaAlter/Deepseek-Harness-Desktop) | Electron desktop shell. / Electron 桌面壳。 |
| ⭐ 25 | [vibeinging/dsh-work](https://github.com/vibeinging/dsh-work) | Local-first AI workbench: Agent sessions + project files + data analysis + web research + MCP + Office. / Local-first AI 工作台：Agent 会话 + 项目文件 + 数据分析 + Web 研究 + MCP + Office。 |
| ⭐ 65 | [Ruler4396/dsh-launcher](https://github.com/Ruler4396/dsh-launcher) | Lightweight Windows launcher: silent autostart + WebView2 window. / 轻量 Windows 启动器：静默开机自启 + WebView2 窗口。 |
| ⭐ 18 | [bruc3van/dsh-desktop](https://github.com/bruc3van/dsh-desktop) | Community-maintained third-party desktop client; auto-reuses local official instance. / 社区维护非官方桌面客户端，自动复用本机官方实例。 |
| ⭐ 20 | [CCMu04/DSHDesktop](https://github.com/CCMu04/DSHDesktop) | Unofficial Windows desktop client. / 非官方 Windows 桌面客户端。 |
| ⭐ 11 | [sleep2agi/DeepSeek-Harness-Desktop](https://github.com/sleep2agi/DeepSeek-Harness-Desktop) | Unofficial community desktop shell. / 非官方社区桌面壳。 |
| ⭐ 6 | [omdsh-dev/deepseek-harness-desktop](https://github.com/omdsh-dev/deepseek-harness-desktop) | DSH desktop app. / DSH 桌面应用。 |
| ⭐ 5 | [ding7015869-alt/dsh-web-desktop](https://github.com/ding7015869-alt/dsh-web-desktop) | Windows desktop client — WebView2 + tray mode. / Windows 桌面客户端，WebView2 + 托盘模式。 |
| ⭐ 11 | [openguardrails/dsh-tui](https://github.com/openguardrails/dsh-tui) | Claude Code-style terminal UI for DeepSeek Harness agents, as an out-of-tree dsh plugin bundle. / DSH 插件 bundle：Claude Code 风格终端 UI。 |
| ⭐ 7 | [whitelonng/dshcode](https://github.com/whitelonng/dshcode) | Community desktop companion — one-click Electron app for macOS & Windows. / 社区桌面伴侣，一键 Electron 应用（macOS/Windows）。 |
| ⭐ 3 | [longyu065/dsh-desktop](https://github.com/longyu065/dsh-desktop) | Desktop shell — auto-installs dsh, native macOS tray, packaged macOS & Windows. / 桌面壳，自动安装 dsh，原生 macOS 托盘，打包 macOS & Windows。 |
| ⭐ 3 | [Void0312Aurora/dsh-desktop-electron](https://github.com/Void0312Aurora/dsh-desktop-electron) | Cross-platform Electron shell, tray-resident standalone window. / 跨平台 Electron 壳，tray 常驻独立窗口。 |
| ⭐ 5 | [RZX00/deepseek-harness-desktop](https://github.com/RZX00/deepseek-harness-desktop) | DeepSeek Harness Windows desktop build: Electron shell over dsh web profile, packaged as installer. / DSH Windows 桌面版：Electron 封装官方 Web 配置文件，打包为安装程序。 |
| ⭐ 2 | [SnowCrescenter-tech/dsh-desktop](https://github.com/SnowCrescenter-tech/dsh-desktop) | Native Windows desktop shell: frameless window / tray / native notifications / single-instance / auto-launch. / 原生 Windows 桌面壳：无边框窗口/托盘/原生通知/单实例/开机自启。 |
| ⭐ 2 | [chyra-moon/deepseek-harness-desktop](https://github.com/chyra-moon/deepseek-harness-desktop) | 1:1 replica of the official Web UI as a Windows desktop app. / 1:1 复刻官方 Web UI 的 Windows 桌面应用。 |
| ⭐ 2 | [zsyu9779/dsh-desktop](https://github.com/zsyu9779/dsh-desktop) | Unofficial Wails (Go) desktop shell wrapping the dsh web UI in Codex-style native app. / 非官方 Wails (Go) 桌面壳，Codex 风格原生应用。 |
| ⭐ 2 | [SnowCrescenter-tech/dsh-launcher](https://github.com/SnowCrescenter-tech/dsh-launcher) | One-click portable launcher — no Node.js, no pnpm, no CLI needed. / 一键便携启动器：免 Node.js/pnpm/CLI。 |
| ⭐ 2 | [HaoyueQin/deepseek-harness-desktop](https://github.com/HaoyueQin/deepseek-harness-desktop) | Native-feeling, always-on desktop shell wrapping the official dsh web UI. / 原生质感、常驻后台的桌面应用壳。 |
| ⭐ 1 | [KhanZou/Deepseek-Harness-as-Desktop](https://github.com/KhanZou/Deepseek-Harness-as-Desktop) | Codex-style desktop app: WebView2 shell, system tray, auto-start, toast, skin center. / Codex 风格桌面应用：WebView2 + 系统托盘 + toast + 皮肤中心。 |
| ⭐ 1 | [SZMY-haruhi/dsh-desktop-shell](https://github.com/SZMY-haruhi/dsh-desktop-shell) | Pure Electron shell for DeepSeek Harness — no bundled code, spawns npx @deepseek-ai/dsh@latest web, loads 127.0.0.1:3080, transparent to all plugins. / 纯 Electron 壳：不捆绑代码，调用 npx 启动 dsh web，加载 127.0.0.1:3080，对所有插件透明。 |
| ⭐ 1 | [KnCRJVirX/dsh-desktop](https://github.com/KnCRJVirX/dsh-desktop) | Electron desktop wrapper for DeepSeek Harness. / DeepSeek Harness 的 Electron 桌面封装。 |
| ⭐ 1 | [kyorakuyk/dsh-desktop](https://github.com/kyorakuyk/dsh-desktop) | Desktop shell for DSH. / DSH 桌面壳。 |
| ⭐ 1 | [czzzlq/deepseek-harness-desktop](https://github.com/czzzlq/deepseek-harness-desktop) | deepseek-harness desktop client. / deepseek-harness 桌面端。 |
| ⭐ 1 | [fengzhiyushui/dsh-desktop-window](https://github.com/fengzhiyushui/dsh-desktop-window) | Desktop window for DSH. / DSH 桌面窗口。 |
| ⭐ 1 | [Asaiuta/dsh-session-hub](https://github.com/Asaiuta/dsh-session-hub) | Aggregate and natively control multiple remote DSH servers' sessions from one official Web UI. / 多服务器 DSH 会话聚合与原生操控 — hub gateway + 官方 UI 桥接。 |
| ⭐ 1 | [tttnny/DSH-Launcher](https://github.com/tttnny/DSH-Launcher) | macOS menu bar app managing the DSH web service via launchd. / macOS 菜单栏应用，通过 launchd 管理服务。 |
| ⭐ 1 | [SeverusZh/dsh-notify-windows](https://github.com/SeverusZh/dsh-notify-windows) | Windows notification plugin. / Windows 通知插件。 |
| ⭐ 2 | [starf233-2/DeepSeek-Harness-Desktop](https://github.com/starf233-2/DeepSeek-Harness-Desktop) | DeepSeek Harness Desktop packages DeepSeek's agent harness into a double-clickable Windows portable. / DSH Windows 便携桌面包。 |
| ⭐ 2 | [TMLX1453/DeepSeek-Harness-Desktop](https://github.com/TMLX1453/DeepSeek-Harness-Desktop) | Codex-packaged DeepSeek Harness desktop client. / Codex 打包 DSH 桌面端。 |
| ⭐ 2 | [qingyu321/dsh-gui](https://github.com/qingyu321/dsh-gui) | DeepSeek Harness self-contained desktop GUI — Electron shell, iframe-embedded official webui, portable single exe + NSIS. / DSH 自包含桌面 GUI（Electron 壳，iframe 嵌入官方 webui，便携单 exe + NSIS 安装包）。 |
| ⭐ 1 | [zneoxlab/deepseek-harness-app](https://github.com/zneoxlab/deepseek-harness-app) | DeepSeek Harness Desktop — a native desktop app for DSH. / DSH 原生桌面应用。 |
| ⭐ 1 | [MoneShadow/DeepSeek-Harness-linux-](https://github.com/MoneShadow/DeepSeek-Harness-linux-) | Linux desktop DSH based on official WebUI — bundled vision plugin, 4 iterations. / 基于官方 WebUI 二改的 Linux 桌面端。 |
| ⭐ 1 | [Aetik-yue/whalecode](https://github.com/Aetik-yue/whalecode) | DeepSeek Harness WebUI desktop wrapper (Electron): one-click launch, auto-update, official whale icon. / DSH WebUI Electron 桌面封装：一键启动，自动更新。 |
| ⭐ 1 | [jenokagong-dotcom/dsh-webui-launcher](https://github.com/jenokagong-dotcom/dsh-webui-launcher) | One-click Windows launcher for DeepSeek Harness Web UI: auto-starts service, opens browser. / 一键 Windows 启动器。 |
| ⭐ 1 | [FUOQL/DeepSeek-Launcher](https://github.com/FUOQL/DeepSeek-Launcher) | Windows launcher for DeepSeek Harness Agent. / DSH Windows 启动器。 |
| ⭐ 1 | [qzhqzh/dsh-quickstart](https://github.com/qzhqzh/dsh-quickstart) | Desktop launcher for DeepSeek Harness — start dsh web with no console window and auto-open browser. / 无控制台窗口的 DSH 桌面启动器。 |
| ⭐ 1 | [Ning668819/dsh-desktop-shortcut](https://github.com/Ning668819/dsh-desktop-shortcut) | One-click desktop shortcut for DeepSeek Harness — starts dsh web and opens the browser. / 一键桌面快捷方式。 |
| ⭐ 1 | [ReachGa0/dsh-desktop](https://github.com/ReachGa0/dsh-desktop) | Electron desktop shell for DeepSeek Harness (dsh web) — standalone window without system tray. / DSH Electron 桌面壳（独立窗口）。 |
| ⭐ 1 | [SwordSifu/dsh-desktop](https://github.com/SwordSifu/dsh-desktop) | Electron desktop shell for DeepSeek Harness: bundled Node runtime, tray, system notifications, NSIS. / DSH Electron 桌面壳：bundled Node、托盘、系统通知。 |
| ⭐ 1 | [Kazama-Suichiku/dshcode](https://github.com/Kazama-Suichiku/dshcode) | DSHCode: a clean native-desktop coding agent forked from DeepSeek Harness — Tauri shell + cordis plugins. / DSHCode：Tauri 壳 + cordis 插件的原生桌面 Agent。 |
| ⭐ 1 | [LouisYang841/dsh-mini](https://github.com/LouisYang841/dsh-mini) | DeepSeek Harness 核心的便携引擎 + Termux 友好的终端编程 Agent CLI（pi 壳 + DSH 引擎，零运行时依赖）。 / DSH 核心便携引擎 + Termux 友好 CLI。 |
| ⭐ 1 | [wuxiaoji/Dsh_Desktop](https://github.com/wuxiaoji/Dsh_Desktop) | DSH desktop app packaged with Rust — easy for beginners to launch and update. / Rust 打包 DSH 桌面应用。 |
| ⭐ 1 | [o-Sakurajimamai-o/dsh-desktop](https://github.com/o-Sakurajimamai-o/dsh-desktop) | DeepSeek Harness Desktop/App. / DSH 桌面应用。 |
| ⭐ 1 | [MAXeaglet/dsh-plugin-manager](https://github.com/MAXeaglet/dsh-plugin-manager) | DSH plugin manager: desktop GUI + CLI, manage profiles, plugins and one-click start dsh web (Tauri 2 + Node CLI). / DSH 插件管理器：桌面 GUI + CLI。 |
| ⭐ 1 | [wulun811/dsh-rules-manager](https://github.com/wulun811/dsh-rules-manager) | Rules & commands manager for DeepSeek Harness: /rules command + settings panel + custom commands. / DSH 规则与命令管理器。 |
| ⭐ 0 | [jilian-dsh/dsh-rules-manager](https://github.com/jilian-dsh/dsh-rules-manager) | Rules & commands manager for DeepSeek Harness: /rules command + settings panel + custom commands. / DSH 规则与命令管理器。 |
| ⭐ 1 | [Uddoo/dsh-dashboard](https://github.com/Uddoo/dsh-dashboard) | Symphony-compatible Linear issue orchestrator and native operations dashboard for DeepSeek Harness. / Symphony 兼容 Linear 任务编排与操作面板。 |
| ⭐ 1 | [Baiyuscc13724-Max/deepseek-harness-desktop](https://github.com/Baiyuscc13724-Max/deepseek-harness-desktop) | Windows desktop app for DeepSeek Harness: installer, themes, in-app plugin marketplace, model routing. / DSH Windows 桌面应用：安装器、主题、内置插件市场、模型路由。 |
| ⭐ 1 | [XS-dev/dsh-start](https://github.com/XS-dev/dsh-start) | Cross-platform one-command launcher for the DeepSeek Harness Web UI. / DSH Web UI 跨平台一键启动器。 |
| ⭐ 1 | [mocchh/dsh-better-launcher](https://github.com/mocchh/dsh-better-launcher) | dsh start / stop / status — one-command lifecycle manager for DeepSeek Harness. / DSH 一键生命周期管理器（start/stop/status）。 |
| ⭐ 1 | [AdamPlatin123/dsh-zcf](https://github.com/AdamPlatin123/dsh-zcf) | dsh-zcf: DeepSeek Zero-Config Flow — one-command setup wizard for DeepSeek Harness. / DSH 零配置一键安装向导。 |
| ⭐ 1 | [bill9109/dsh-conversation-share](https://github.com/bill9109/dsh-conversation-share) | Share any paragraph of DSH conversation. / 分享任意 DSH 对话段落。 |
| ⭐ 25 | [ningbainb/deepseek-harness-desktop](https://github.com/ningbainb/deepseek-harness-desktop) | Lossless Windows desktop app for DeepSeek Harness: complete DSH Web UI, plugins, skins, and auto-update. / 完整功能 DSH Windows 桌面应用：Web UI、插件、皮肤完整保留，支持自动更新。 |
| ⭐ 2 | [bailang1218/deepseek-harness-desktop](https://github.com/bailang1218/deepseek-harness-desktop) | Community-maintained self-contained Tauri desktop distribution for DeepSeek Harness. / 社区维护自包含 Tauri 桌面版 DSH。 |
| ⭐ 0 | [sorsama/deepseek-harness-mobile](https://github.com/sorsama/deepseek-harness-mobile) | Android companion for DeepSeek Harness — chat, goals, approvals & notifications from your phone. / DSH Android 伴侣：手机远程聊天/目标/审批/通知。 |
| ⭐ 5 | [railgun0325/dsh-phone](https://github.com/railgun0325/dsh-phone) | Run DSH agents on your phone via Magisk root — native Android operation (screenshot/click/swipe/open apps) + mobile layout + WebView API. / 让 DSH agent 跑在手机里，通过 Magisk root 原生操作安卓系统（截图/点击/滑动/开应用）+ 移动端布局。 |
| ⭐ 5 | [Hotsteel2901/dsh-client-ui-mobile-adapt](https://github.com/Hotsteel2901/dsh-client-ui-mobile-adapt) | Your DSH web UI, rebuilt for the phone in your hand — responsive layout optimized for mobile developers. / 专为手机端重建的 DSH Web UI：响应式布局，面向移动端开发者。 |
| ⭐ 1 | [tengqi159/harness-mate](https://github.com/tengqi159/harness-mate) | Native macOS companion for DeepSeek Harness — research files, Appshot, scoped Computer Use, desktop-integrated workflow. / DSH 原生 macOS 伴侣：研究文件、Appshot、受限 Computer Use，桌面集成工作流。 |
| ⭐ 7 | [Lehhair/dsh-mobile](https://github.com/Lehhair/dsh-mobile) | DeepSeek Harness Android standalone app. / DSH Android 独立应用。 |
| ⭐ 6 | [Kelai141/dsh-mobile-apk](https://github.com/Kelai141/dsh-mobile-apk) | Android APK shell with WebView UI + Termux runtime snapshot — runs on device without root. / Android APK 壳：WebView UI + Termux 运行时，免 ROOT 可直接运行。 |
| ⭐ 2 | [qiannianhuanxiang/DSHA](https://github.com/qiannianhuanxiang/DSHA) | Android launcher for DeepSeek Harness with proot+Ubuntu, one-click setup without root or Termux. / DSH 安卓启动器：内置 proot+Ubuntu，免 ROOT 免 Termux 一键运行。 |
| ⭐ 1 | [thness/dsh-mobile](https://github.com/thness/dsh-mobile) | DeepSeek Harness Android — bundled Node.js runtime + official Web UI, standalone app out of the box. / DSH Android 版：内嵌 Node.js 运行时 + 官方 Web UI 开箱即用。 |
| ⭐ 1 | [Bernardxu123/dsh-mobile-gate](https://github.com/Bernardxu123/dsh-mobile-gate) | LAN mobile gateway for DSH: first-visit approval, per-device tokens, rate limiting, mobile layout. / DSH 局域网手机网关：本机审批、设备令牌、限流、手机端适配。 |


| ⭐ 5 | [majiayu000/dsh-desk](https://github.com/majiayu000/dsh-desk) | Installable Tauri desktop distribution for DeepSeek Harness with bundled runtime — one-click setup, no Node.js needed. / 可安装 Tauri 桌面版 DSH：内置运行时，一键部署无需 Node.js。 |
| ⭐ 1 | [Nexus-Aethra/DSHBox](https://github.com/Nexus-Aethra/DSHBox) | Manage multiple DSH versions in isolated containers: version switching without conflicts, clean environment per project. / DSH 容器化管理：在隔离容器中运行多个 DSH 版本，零冲突切换。 |
---

## ⌨️ Terminal TUI / 终端 TUI

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 883 | [ccch1mneyyy/dsh-TUI](https://github.com/ccch1mneyyy/dsh-TUI) | Claude Code-style fullscreen interactive terminal: pixel whale header, streaming thought display, double-Esc rollback, TPS gauge. npm one-click install. / Claude Code 风格全屏交互终端：像素鲸鱼顶栏、思考流式展开、双击 Esc 回滚、TPS 仪表，npm 一键安装。 |
| ⭐ 133 | [huiliyi37/dsh-tianshu-tui](https://github.com/huiliyi37/dsh-tianshu-tui) | TianShu TUI + harness workflow with TDD and evidence-gate support. / 天枢 TUI + harness 工作流，支持 TDD 与证据门。 |
| ⭐ 75 | [pulseaiclub/phi](https://github.com/pulseaiclub/phi) | Coding Agent from pi — ∞ providers, sub-agents, hashline edits, permission gate, deepseek-tui. / pi 风格的 Coding Agent，∞ providers，sub-agents，hashline 编辑，权限门控，deepseek-tui。 |
| ⭐ 6 | [compforge/baton](https://github.com/compforge/baton) | Terminal-native workspace for Codex, Claude Code, and DeepSeek Harness — durable cross-harness sessions. / 终端原生工作区：支持 Codex/Claude Code/DSH 的跨 harness 持久会话。 |
| ⭐ 6 | [chen-001/dsh-grok-tui](https://github.com/chen-001/dsh-grok-tui) | Use dsh via Grok-build's TUI. / 通过 Grok-build 的 TUI 使用 dsh。 |
| ⭐ 11 | [dsh-tui/dsh-tui](https://github.com/dsh-tui/dsh-tui) | Claude Code-style terminal UI as an out-of-tree dsh plugin bundle. / Claude Code 风格终端 UI（out-of-tree bundle）。 |
| ⭐ 4 | [gxinxing/deepseek-harness-tui](https://github.com/gxinxing/deepseek-harness-tui) | Terminal-native interactive TUI built with Ink + React for terminals. / 终端原生交互式 TUI，基于 Ink + React for terminals。 |
| ⭐ 2 | [openma-ai/deepseek-harness-tui](https://github.com/openma-ai/deepseek-harness-tui) | TUI plugin for DeepSeek Harness. / DSH TUI 插件。 |
| ⭐ 2 | [orriduck/dsh-tui](https://github.com/orriduck/dsh-tui) | Small session-aware terminal UI for DeepSeek Harness. / 小型 session-aware 终端 UI。 |
| ⭐ 2 | [ccch1mneyyy/dsh-working-activity](https://github.com/ccch1mneyyy/dsh-working-activity) | Real-time model work status bar: playful thinking copy, running tools, turn summary, self-narration. / 实时模型工作状态行：俏皮思考文案、工具运行、回合总结。 |
| ⭐ 8 | [blissito/ghostycode](https://github.com/blissito/ghostycode) | DeepSeek V4 terminal coding agent & constitutional harness — Rust TUI with MCP, sub-agents, session persistence, evidence-driven verification. / DeepSeek V4 终端编码 agent 与宪法式 harness，Rust TUI + MCP + 子代理。 |
| ⭐ 0 | [liang7878/deepseek-harness-tui](https://github.com/liang7878/deepseek-harness-tui) | Standalone, themeable TUI for the official DeepSeek Harness engine — one-command npx, prebuilt runtime. / DSH 独立可主题化终端 TUI，一键 npx 运行。 |

---

## 👁️ Vision & Multimodal / 视觉与多模态

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 1.2k | [liustack/modlens](https://github.com/liustack/modlens) | First vision plugin for DeepSeek Harness — paste an image, get structured JSON evidence (OCR, layout, semantics). / DSH 首个视觉插件：粘贴图片 → 结构化 JSON（OCR、布局、语义）。 |
| ⭐ 62 | [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router) | Eyes for text-only DSH agents: built-in free vision chain (no key) + pixel-level tools (Q&A, grounding, OCR, SVG trace, screenshots). / 纯文本 DSH Agent 的视觉眼睛：内置免费视觉链（无需 key）+ 像素级工具。 |
| ⭐ 9 | [linenxi-ctrl/dsh-vision](https://github.com/linenxi-ctrl/dsh-vision) | External vision model adapter: circle-whale button, auto screenshot+OCR, multi-protocol adaptive, zero-config install (auto-downloads Node.js). / 外挂识图适配器：圆形鲸鱼按钮、自动截图+OCR、多协议自适应，零配置一键安装。 |
| ⭐ 4 | [poiuyjie/dsh-vision-opencode](https://github.com/poiuyjie/dsh-vision-opencode) | OpenCode-style vision plugin for DSH — paste images directly, auto-routed to configured vision model. / OpenCode 风格 DSH 视觉插件：直接贴图，自动路由到配置的视觉模型。 |
| ⭐ 2 | [Terry12138qy/dsh-vision](https://github.com/Terry12138qy/dsh-vision) | Vision plugin for text-only DeepSeek: Qwen 3.5-Omni-Plus primary, falls back to GLM-4.6V-Flash automatically. / 纯文本 DeepSeek 识图插件：Qwen 3.5-Omni-Plus 为主，自动降级到 GLM-4.6V-Flash。 |
| ⭐ 2 | [libinyam/dsh-vision-provider](https://github.com/libinyam/dsh-vision-provider) | Config-only vision bundle: drop a config file and connect any OpenAI-compatible VLM endpoint. / 配置式视觉插件：仅需配置文件即可接入任意 OpenAI 兼容 VLM。 |
| ⭐ 1 | [zouyuanqing/dsh-vision-primitives](https://github.com/zouyuanqing/dsh-vision-primitives) | Native interactive visual-reasoning plugin: precise pixel grounding (SOM grid), image QA, and screenshot capture. / 原生交互式视觉推理插件：精确像素定位（SOM 网格）、图片问答、截图捕获。 |
| ⭐ 1 | [yan5236/slcatwujian-dsh-vision-plugin](https://github.com/yan5236/slcatwujian-dsh-vision-plugin) | Vision bridge for text-only primary models: auto-connects configured vision model, pixel-coordinate descriptions, vision_ask follow-up tool. / 纯文本主模型的视觉桥接：自动连接配置的视觉模型，像素坐标描述，vision_ask 追问工具。 |
| ⭐ 1 | [ximengxiaolan/dsh-vision-bridge](https://github.com/ximengxiaolan/dsh-vision-bridge) | Composer-attached images are auto-described by an OpenAI-compatible vision model and handed to text-only model. / 编辑器附加图片经 OpenAI 兼容视觉模型自动描述后传递给纯文本模型。 |
| ⭐ 1 | [superclaude1/dsh-vision-android](https://github.com/superclaude1/dsh-vision-android) | Multimodal vision (OpenAI-compatible) + Android ADB UI automation plugin for DeepSeek Harness. / DSH 多模态视觉（OpenAI 兼容）+ Android ADB UI 自动化插件。 |
| ⭐ 1 | [2472786266-spec/deepseek-hsrness-devkit](https://github.com/2472786266-spec/deepseek-hsrness-devkit) | DSH DevKit: multimodal gallery + multi-agent supervision console — dynamic Cordis plugin with visual tooling. / DSH 开发套件：多模态图库 + 多 Agent 监督控制台（动态 Cordis 插件）。 |
| ⭐ 802 | [Anionex/agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit) | Vision toolkit for text-only models — image Q&A, long-screenshot OCR, UI restoration, GUI automation. / 纯文本模型的视觉工具箱：多图理解、OCR、UI 还原、GUI 自动化。 |
| ⭐ 348 | [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit) | DSH-native integration: image Q&A, long-screenshot OCR, UI restoration, grounding, pixel diff, Artifacts. / DSH-native 集成：图片问答、长截图 OCR、UI 还原、grounding、pixel diff、Artifacts。 |
| ⭐ 13 | [Anionex/dsh-computer-use](https://github.com/Anionex/dsh-computer-use) | Accessibility-first macOS computer control: fresh observations, stale-state rejection, scoped permissions, safe input. / macOS Accessibility 电脑控制：新鲜观测、过期拒绝、安全输入。 |
| ⭐ 19 | [william-jin-cmu/dsh-vision](https://github.com/william-jin-cmu/dsh-vision) | Add vision to text-only DeepSeek: view_image tool bridging any OpenAI-compatible VLM (4 vendors, 10 models). / 给纯文本 DeepSeek 加视觉：view_image 桥接任意 OpenAI 兼容 VLM（4 厂商 10 模型）。 |
| ⭐ 17 | [oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision) | Near-native image understanding for DeepSeek Harness. / 接近原生的图像理解。 |
| ⭐ 11 | [zhouwumu2-lab/dsh-vision-fix](https://github.com/zhouwumu2-lab/dsh-vision-fix) | Temporary fork: fix dsh.plugin.json in files. / PR 临时 fork：修复 dsh.plugin.json。 |
| ⭐ 4 | [Flyvhidbwo/dsh-vision-proxy](https://github.com/Flyvhidbwo/dsh-vision-proxy) | DeepSeek brain + auto image recognition: attached images trans-coded via Qwen VLM before sending. / DeepSeek 大脑 + 自动识图，附加图片经 Qwen VLM 转译。 |
| ⭐ 3 | [huashenglian/dsh-her-eyes](https://github.com/huashenglian/dsh-her-eyes) | Auto-invokes VLM for visual analysis in DSH. / 自动调用 VLM 进行视觉分析的 DSH 插件。 |
| ⭐ 3 | [moduqishi/GrassVison](https://github.com/moduqishi/GrassVison) | Seamless vision augmentation via OpenAI-compatible API — auto routes to vision models. / 无感添加视觉能力，OpenAI 兼容 API 自动转交给视觉模型。 |
| ⭐ 2 | [Favio8/dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye) | DeepEye vision plugin: image description, OCR, VQA, UI layout, clipboard analysis. / DeepEye 视觉插件：图片描述/OCR/VQA/UI 布局/剪贴板分析。 |
| ⭐ 1 | [hawkongz/doubao-vision-dsh](https://github.com/hawkongz/doubao-vision-dsh) | Desktop Doubao CDP bridge: let text-only models see chat images. / 桌面豆包 CDP 桥接：让纯文本模型看见聊天图片。 |
| ⭐ 1 | [Spirit4471/multimodal-bridge](https://github.com/Spirit4471/multimodal-bridge) | Multimodal bridge: Qwen-VL vision + Qwen-Image generation for text-only models. / 多模态桥：Qwen-VL 视觉理解 + Qwen-Image 图像生成。 |
| ⭐ 1 | [Yuuz12/dsh-vision-helper](https://github.com/Yuuz12/dsh-vision-helper) | Vision helper solution for DeepSeek Harness. / DSH 视觉辅助方案。 |
| ⭐ 1 | [TiankunDai/dsh-vision-LMstudio](https://github.com/TiankunDai/dsh-vision-LMstudio) | Call locally-loaded LM Studio vision models via DSH. / 通过 DSH 调用 LM Studio 本地视觉模型。 |
| ⭐ 1 | [Scorp1o117/dsh-tool-vision](https://github.com/Scorp1o117/dsh-tool-vision) | External vision model plugin for DeepSeek Harness. / 外置视觉模型插件。 |
| ⭐ 1 | [sjscy05/deepseek-harness-vision-plugin](https://github.com/sjscy05/deepseek-harness-vision-plugin) | Vision plugin for DeepSeek Harness. / DSH 视觉插件。 |
| ⭐ 1 | [ZhuXinAI/sidesight](https://github.com/ZhuXinAI/sidesight) | CLI-first vision sidecar: analyze screenshots, diagrams, charts, UI diffs with multimodal models. / CLI-first vision sidecar：截图/图表/UI diff 分析。 |
| ⭐ 1 | [akqwpeter-prog/dsh-media-skills](https://github.com/akqwpeter-prog/dsh-media-skills) | Paste images straight into chat: free vision model + image reading/generation skill. / 贴图直读生图 Skill。 |
| ⭐ 0 | [czczstc-lang/dsh-vision-plugins](https://github.com/czczstc-lang/dsh-vision-plugins) | Delegated vision plugin for DSH: text-only primary model can see images (auto-calls vision model on paste); multimodal models bypass directly. / DSH 委托式识图插件：纯文本主模型也能看图，粘贴图片自动调用视觉模型识别，多模态模型原生直通。 |
| ⭐ 7 | [Yts1919/dsh-vision-complete](https://github.com/Yts1919/dsh-vision-complete) | Eyes and ears for DeepSeek — image viewing / OCR / object detection / video understanding / speech transcription / screenshot reading, one-click install. / 给 DeepSeek 补上「眼睛和耳朵」的多模态视觉插件：看图/OCR/物体检测/视频理解/语音转写/截图直读，一键安装。 |
| ⭐ 2 | [shinegeer/dsh-vision-window](https://github.com/shinegeer/dsh-vision-window) | Enables single-modal AIs to recognize images: paste screenshots into the window, configure a multimodal AI, auto-recognizes and archives. / 单模态 AI 识图窗口：粘贴截图到窗口，配置多模态 AI，自动识图并归档。 |

| ⭐ 2 | [kbpoyo/dsh-image-bridge](https://github.com/kbpoyo/dsh-image-bridge) | DSH plugin: let text-only models see images — paste directly in web UI, no path needed; multimodal models route natively with zero skill binding. / DSH 插件：让纯文本模型也能看图，Web 端直接贴图无需指定路径；多模态模型原生直通，零 skill 绑定。 |
| ⭐ 1 | [chang416/deepsee](https://github.com/chang416/deepsee) | Vision + smart model routing for DeepSeek Harness: Gemini sees, DeepSeek codes. / DSH 视觉与智能模型路由：Gemini 识图，DeepSeek 编码。 |


---

## 🌐 Browser & Web Enhancements / 浏览器与 Web 增强

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 2.3k | [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw) | Local-first cross-platform AI content discovery agent (Bilibili, XHS, Douyin, YouTube, X, Zhihu, Reddit) — supports DSH plugin. / 本地优先跨平台 AI 内容发现 Agent，支持 DSH 插件。 |
| ⭐ 99 | [Lum1104/dsh-browser](https://github.com/Lum1104/dsh-browser) | Chrome sidebar extension: let DSH operate your browser directly — no vision capabilities required. / Chrome 侧边栏扩展：DSH 直接操作浏览器，无需视觉能力。 |
| ⭐ 2 | [wqty123/dsh-browser](https://github.com/wqty123/dsh-browser) | Shared real browser plugin for DeepSeek Harness — persistent profile with human-in-the-loop login and safe agent browser tools. / DSH 共享真实浏览器插件：持久化登录态 + 人审登录 + 安全浏览器工具。 |
| ⭐ 2 | [Tianyu209/dsh-browser-companion](https://github.com/Tianyu209/dsh-browser-companion) | Personal DSH browser plugin: persistent profile, visible window, human-in-the-loop login, and safe agent browser tools. / 个人 DSH 浏览器插件：持久化配置、可见窗口、人审登录与安全浏览器工具。 |
| ⭐ 1.9k | [zhu1090093659/dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) | Web UI plugin & skin collection: task board, Git graph, right panel, mobile UI, pet, live token stats, skin center. / Web UI 插件与皮肤合集：任务板、Git 图、右侧面板、移动端 UI、宠物、token 统计、皮肤中心。 |
| ⭐ 709 | [omdsh-dev/DSH-better-sidebar](https://github.com/omdsh-dev/DSH-better-sidebar) | Complete sidebar workspace: third-party tab extensions, file editing, terminal, Git, sub-agents. / 完整侧边栏工作台：三方 Tab 扩展、文件编辑/终端/Git/子代理。 |
| ⭐ 82 | [liustack/modsearch](https://github.com/liustack/modsearch) | Web search plugin: ask the web or X, get structured JSON evidence with citations. / Web 插件：Ask the web or X，返回结构化 JSON 证据（搜索、引用）。 |
| ⭐ 24 | [hanelalo/browser-bridge](https://github.com/hanelalo/browser-bridge) | Let your agent truly操控 your browser window like a human. / 让 Agent 像人一样操控浏览器窗口。 |
| ⭐ 7 | [CanglongCl/dsh-web-review](https://github.com/CanglongCl/dsh-web-review) | Web preview & element annotation — AI modifies frontend code based on visual feedback. / 网页预览与元素批注，让 AI 根据可视化反馈直接修改前端源码。 |
| ⭐ 6 | [tonyd2wild/DeepSeek-Harness-Web-Tools](https://github.com/tonyd2wild/DeepSeek-Harness-Web-Tools) | Free, keyless web_search and web_fetch backed by DuckDuckGo. / Keyless web_search / web_fetch，DuckDuckGo 驱动。 |
| ⭐ 3 | [titanwings/dsh-better-browser](https://github.com/titanwings/dsh-better-browser) | Let DSH agents use your signed-in browser via Kimi WebBridge — 13 webbridge_* tools. / 通过 Kimi WebBridge 让 Agent 使用已登录浏览器，13 个 webbridge_* 工具。 |
| ⭐ 13 | [Fisfzy/ego-browser](https://github.com/Fisfzy/ego-browser) | ego-lite browser for AI agents: 13 structured ego_* tools, CDP control, task isolation. / ego-lite 浏览器接入 HARNESS：13 个结构化 ego_* 工具，CDP 控制。 |
| ⭐ 2 | [TYEclipse/dsh-webfetch](https://github.com/TYEclipse/dsh-webfetch) | Web page reader: fetch URL, extract Markdown/plain text + link inventory, zero runtime deps. / 网页读取：fetch URL + 提取 Markdown/纯文本 + 链接清单。 |
| ⭐ 2 | [TYEclipse/dsh-netdoctor](https://github.com/TYEclipse/dsh-netdoctor) | Network diagnostics: DNS lookup, ICMP ping, TCP port check, TLS cert check, traceroute, public IP. / 网络诊断工具箱：DNS/ping/TCP/TLS/traceroute/IP。 |
| ⭐ 1 | [YJSoooooo/dsh-chrome](https://github.com/YJSoooooo/dsh-chrome) | Chrome profile bridge: control an existing signed-in Chrome profile through chrome_repl. / Chrome profile bridge：通过 chrome_repl 操控已登录 Chrome。 |
| ⭐ 1 | [RealAlexandreAI/dsh-cloudflare-browser-run](https://github.com/RealAlexandreAI/dsh-cloudflare-browser-run) | CF Browser Run web tools (markdown/screenshot/pdf) for DeepSeek Harness. / CF Browser Run web 工具（markdown/screenshot/pdf）。 |
| ⭐ 1 | [crayonlu/dsh-web-search-tavily](https://github.com/crayonlu/dsh-web-search-tavily) | Tavily-backed web search provider for DSH — no DeepSeek API key required. / Tavily web search 提供商，无需 DeepSeek API Key。 |
| ⭐ 1 | [crayonlu/dsh-web-search-firecrawl](https://github.com/crayonlu/dsh-web-search-firecrawl) | Firecrawl-backed web search provider for DSH. / Firecrawl-backed web search 提供商。 |
| ⭐ 1 | [RealAlexandreAI/dsh-all-search](https://github.com/RealAlexandreAI/dsh-all-search) | AnySearch web search provider for DeepSeek Harness. / AnySearch web search provider。 |
| ⭐ 1 | [cnChenKai/dsh-web-search-brave](https://github.com/cnChenKai/dsh-web-search-brave) | Brave Search-backed WebSearchProvider for DeepSeek Harness (ctx.web). / Brave Search 驱动的 DSH web search 提供商。 |
| ⭐ 1 | [cnChenKai/dsh-web-search-tavily](https://github.com/cnChenKai/dsh-web-search-tavily) | Tavily-backed WebSearchProvider for DeepSeek Harness (ctx.web) — keyless mode, no API key required. / Tavily 驱动的 DSH web search 提供商，keyless 模式无需 API Key。 |
| ⭐ 1 | [BruceWu1126/dsh-web-background](https://github.com/BruceWu1126/dsh-web-background) | Web UI background customization plugin. / Web UI 背景自定义。 |
| ⭐ 1 | [0xsline/dsh-spotlight](https://github.com/0xsline/dsh-spotlight) | Keyboard-first command palette for DeepSeek Harness Web. / 键盘优先命令面板。 |
| ⭐ 1 | [PangYiMing/dsh-browser-control](https://github.com/PangYiMing/dsh-browser-control) | Browser control plugin (CDP/Playwright) for DSH. / 浏览器控制插件（CDP/Playwright）。 |
| ⭐ 1 | [zhbdream/dsh-feishu-bridge](https://github.com/zhbdream/dsh-feishu-bridge) | Feishu → local DeepSeek Harness Agent bridge via bot API. / 飞书 → 本机 DeepSeek Harness Agent 桥接。 |
| ⭐ 1 | [PangYiMing/dsh-mobile-control](https://github.com/PangYiMing/dsh-mobile-control) | Mobile device control plugin (ADB/iOS) for DSH. / 手机控制插件（ADB/iOS）。 |
| ⭐ 1 | [MashedPotato817/dsh-tool-browser](https://github.com/MashedPotato817/dsh-tool-browser) | Native browser automation tools for DSH, powered by Playwright + Edge. / Playwright + Edge 原生浏览器自动化工具。 |
| ⭐ 4 | [anweat/dsh-web-search-pro](https://github.com/anweat/dsh-web-search-pro) | Enhanced persistent web search plugin for DeepSeek Harness: multi-engine search, SQLite-backed results, cross-session continuity. / DSH 增强持久化网络搜索：多引擎搜索、SQLite 结果存储、跨会话延续。 |
| ⭐ 7 | [Clizo1209/dsh-playwright-browser](https://github.com/Clizo1209/dsh-playwright-browser) | Playwright browser automation for DeepSeek Harness — snapshot-first, accessibility-tree aware, SSRF-safe navigation. / DSH Playwright 浏览器自动化：首屏快照、无障碍树感知、SSRF 安全导航。 |
| ⭐ 2 | [AHGGG/dsh-side-chat](https://github.com/AHGGG/dsh-side-chat) | Codex-style Side Chat for DSH — select text, ask follow-up questions in a focused side conversation. / DSH Codex 风格侧边对话：选中文本后在专注侧栏提问，主对话不受干扰。 |

---

## 🛠️ Development Tools / 开发工具

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 46 | [Lyn-77/ProMentor](https://github.com/Lyn-77/ProMentor) | AI coding mentor skill: scan project arch, generate step-by-step chapters, auto grading, AI Code Review. / AI 编程导师 Skill：扫描架构、生成阶梯 Chapter、自动判题、AI Code Review。 |
| ⭐ 112 | [omdsh-dev/dsh-at-file](https://github.com/omdsh-dev/dsh-at-file) | Codex-style @file mentions: search workspace files in the composer and attach contents to prompts. / Codex-style @file mentions：在 composer 中搜索文件并附加内容到 prompt。 |
| ⭐ 39 | [btspoony/mstar-harness](https://github.com/btspoony/mstar-harness) | Skill-driven Harness/Loop Engineering Workflow Agent Plugin. / Skill-driven Harness/Loop Engineering Workflow Agent 插件。 |
| ⭐ 54 | [icetomoyo/dsh_workflow](https://github.com/icetomoyo/dsh_workflow) | UltraCode mode: generatable, savable, governable, observable, restorable workflow layer for DSH. / UltraCode 模式：可生成/保存/治理/观察/恢复的 Workflow 层。 |
| ⭐ 38 | [omdsh-dev/dsh-open-in-vscode](https://github.com/omdsh-dev/dsh-open-in-vscode) | Open DSH workspace directories directly in VS Code from the web GUI. / 从 Web GUI 直接在 VS Code 中打开工作区目录。 |
| ⭐ 24 | [Anionex/dsh-turn-rewind](https://github.com/Anionex/dsh-turn-rewind) | Rewind conversation and workspace state, powered by a persistent Change Ledger. / 对话和代码状态回退，基于持久化 Change Ledger。 |
| ⭐ 18 | [omdsh-dev/dsh-custom-tool](https://github.com/omdsh-dev/dsh-custom-tool) | Create and manage sandboxed JS tools with a Monaco editor and model-driven tool lifecycle. / 沙箱 JS 工具管理：Monaco 编辑器 + 模型驱动工具生命周期。 |
| ⭐ 50 | [csyangwen/dsh-memory-evolve](https://github.com/csyangwen/dsh-memory-evolve) | Cross-session long-term memory + background self-evolution: five-track memory, git branch awareness, skill manager. / 跨会话长期记忆 + 后台自我进化：五轨记忆、git 分支感知、技能管理器。 |
| ⭐ 16 | [Moeblack/dsh-message-edit](https://github.com/Moeblack/dsh-message-edit) | Branch-based message editing: reroll, retry, version timeline. / 分支式消息编辑：reroll、retry、版本时间线。 |
| ⭐ 5 | [Zhenyu98/dsh-context-doctor](https://github.com/Zhenyu98/dsh-context-doctor) | Context injection audit: token cost of AGENTS.md / skills / tool schemas, duplicate & conflict detection. / 上下文注入审计：AGENTS.md / 技能 / 工具 schema 的 token 成本。 |
| ⭐ 4 | [FlashingChen/dsh-worktree](https://github.com/FlashingChen/dsh-worktree) | Codex-style permanent git worktrees: worktree_create/list/remove agent tools. / Codex-style permanent git worktrees：create/list/remove 工具。 |
| ⭐ 4 | [happyren/dsh-agent-messaging](https://github.com/happyren/dsh-agent-messaging) | Cross-session agent-to-agent messaging: address another session by name and deliver to inbox. / 跨会话 Agent 间消息传递：按名称寻址，投递到对方收件箱。 |
| ⭐ 18 | [Nwflower/dsh-chat-import](https://github.com/Nwflower/dsh-chat-import) | Import history from Claude Code, Codex, Reasonix and continue in DSH. / 从 Claude Code / Codex / Reasonix 导入历史消息。 |
| ⭐ 9 | [cpj-dev/dsh-plugin-cc](https://github.com/cpj-dev/dsh-plugin-cc) | Bridge DeepSeek-Harness into Claude Code for review, critique, delegation, and session import. / 桥接 DSH 至 Claude Code：审查、质疑、委派、会话导入。 |
| ⭐ 4 | [KitDoesIt/dsh-compaction-instant](https://github.com/KitDoesIt/dsh-compaction-instant) | LLM-free lossless compaction engine for DeepSeek Harness. / 无 LLM 无损压缩引擎。 |
| ⭐ 3 | [codeAnqiang-ma/dsh-superpowers](https://github.com/codeAnqiang-ma/dsh-superpowers) | Superpowers methodology as a DeepSeek Harness plugin. / Superpowers 方法论作为 DSH 插件。 |
| ⭐ 2 | [wuxiangru915/dsh-review-loop](https://github.com/wuxiangru915/dsh-review-loop) | Incremental diff reviewer: checkpoint incremental queue + review injection into agent. / 增量代码审查：checkpoint 队列 + 审查意见注入。 |
| ⭐ 2 | [Elaina-real/dsh-tiered-approval](https://github.com/Elaina-real/dsh-tiered-approval) | Tiered auto-review: static-rule safety net + LLM reviewer + human fallback. / 分级自动审核：静态规则 + LLM + 人工兜底。 |
| ⭐ 2 | [Drifter-yh/dsh-tool-policy](https://github.com/Drifter-yh/dsh-tool-policy) | Declarative deny-by-default tool policy plugin. / 声明式 deny-by-default 工具策略。 |
| ⭐ 2 | [shuguang1994/project-blueprint](https://github.com/shuguang1994/project-blueprint) | One command to make any project AI-agent-ready: adaptive tech stack detection, auto AGENTS.md generation. / 一键让项目具备 AI 开发能力：自适应技术栈检测 + AGENTS.md 生成。 |
| ⭐ 2 | [MashedPotato817/dsh-git-plugin](https://github.com/MashedPotato817/dsh-git-plugin) | Git workflow plugin: slash commands + read-only git tools. / Git workflow 插件：slash 命令 + 只读 git 工具。 |
| ⭐ 2 | [kingjly/dsh-plugin-builder](https://github.com/kingjly/dsh-plugin-builder) | Agent Skill that turns a capability into an installable DSH plugin. / 把能力做成可安装 dsh 插件的 Agent Skill。 |
| ⭐ 2 | [PerryLink/dsh-plugin-guide](https://github.com/PerryLink/dsh-plugin-guide) | Everything you need to build DSH plugins: official docs archive, Cordis primer, 15-repo deep-dive. / DSH 插件构建完全指南：EN/ZH 文档 + Cordis 入门。 |
| ⭐ 2 | [kaziii/dsh-github-connector](https://github.com/kaziii/dsh-github-connector) | GitHub connector: one-click connect, create/review/merge PRs from the conversation. / GitHub 连接器：一键连接，创建/审查/合并 PR。 |
| ⭐ 1 | [PangYiMing/dsh-bisect-debug](https://github.com/PangYiMing/dsh-bisect-debug) | Bisect bugs (code/boundary/commit) to find root cause. / 二分法定位 bug 根因（代码/边界/commit）。 |
| ⭐ 1 | [CrazyShout/dsh-ssh-remote](https://github.com/CrazyShout/dsh-ssh-remote) | SSH remote workspaces: browse/read/write remote files, run remote commands. / SSH 远程工作区：浏览/读写远程文件，运行远程命令。 |
| ⭐ 1 | [Simon314620/dsh-turn-index](https://github.com/Simon314620/dsh-turn-index) | Sidebar conversation turn index plugin. / 侧边栏对话轮次索引插件。 |
| ⭐ 1 | [zhouzhencheng07/dsh-tavily-search](https://github.com/zhouzhencheng07/dsh-tavily-search) | Free keyless Tavily web search tool. / 免费 keyless Tavily web search 工具。 |
| ⭐ 1 | [qingtian3a/dsh-event-auditor](https://github.com/qing3a/dsh-event-auditor) | Event stream audit panel: observe event types, dispatch patterns, counts, recent events. / 事件流审计面板：观察事件类型/分发模式/计数/最近事件。 |
| ⭐ 1 | [xilin3/dsh-prompt-persona](https://github.com/xilin3/dsh-prompt-persona) | Edit system prompt from Settings page with live preview. / 从设置页编辑 system prompt，实时预览。 |
| ⭐ 1 | [Jesse-njx/dsh-cowork](https://github.com/Jesse-njx/dsh-cowork) | Read + write office documents & notebooks (xlsx, pdf, docx, pptx, ipynb) + MCP server. / Office 文档读写：xlsx/pdf/docx/pptx/ipynb + MCP server。 |
| ⭐ 2 | [651002/codex-eyes-hands](https://github.com/651002/codex-eyes-hands) | Codex CLI as text-only DSH agent eyes & hands — image viewing, file reading, drawing, execution supervision, dual-channel failover. / 专为 DSH 打造：把本机 Codex CLI 变成纯文本 Agent 的眼睛和手——看图/读文件/画图/监督执行/双通道容灾。 |
| ⭐ 1 | [realalexandreai/dsh-atuin](https://github.com/realalexandreai/dsh-atuin) | Record dsh user prompts into atuin shell history. / 记录 dsh user prompts 到 atuin shell 历史。 |
| ⭐ 1 | [tyler-wang3141/dsh-open-in-finder](https://github.com/tyler-wang3141/dsh-open-in-finder) | One-click open-in-Finder icon in session header. / 一键 open-in-Finder 图标。 |
| ⭐ 1 | [lin-cheng-lab/dsh-reloader](https://github.com/lin-cheng-lab/dsh-reloader) | One-click reload: say "reload" after installing a plugin to auto-restart. / 一键重启：装完插件说一句 reload 自动重启生效。 |
| ⭐ 1 | [lehhair/dsh-split-panes](https://github.com/lehhair/dsh-split-panes) | Split panes for DSH. / 分割面板。 |
| ⭐ 1 | [ShawnSiao/dsh-credentials-keychain](https://github.com/ShawnSiao/dsh-credentials-keychain) | OS-backed credential provider for DeepSeek Harness. / OS-backed 凭据 provider。 |
| ⭐ 1 | [dyuan311/dsh-openai-codex-oauth](https://github.com/dyuan311/dsh-openai-codex-oauth) | ChatGPT subscription OAuth for the openai-codex provider in DSH. / ChatGPT subscription OAuth for openai-codex provider。 |
| ⭐ 1 | [Yan-Zero/dsh-codex](https://github.com/Yan-Zero/dsh-codex) | Use your ChatGPT subscription in DSH through OpenAI's Codex sign-in flow. / 通过 OpenAI Codex 登录流程使用 ChatGPT 订阅。 |
| ⭐ 12 | [bugmaker2/dsh-plugin-template](https://github.com/bugmaker2/dsh-plugin-template) | Template for DeepSeek Harness plugin development. / DSH 插件开发模板。 |
| ⭐ 6 | [w2112515/dsh-plugin-development](https://github.com/w2112515/dsh-plugin-development) | Portable Agent Skill for developing and auditing DSH plugins: scaffolding, test tiers, and optional profile-installable DSH bundle adapter. / 可移植 Agent 技能：DSH 插件开发、审计脚手架，含可选 DSH bundle 适配器。 |
| ⭐ 7 | [omdsh-dev/dsh-plugin-skills](https://github.com/omdsh-dev/dsh-plugin-skills) | Agent skills for building and testing DSH plugins — from scaffolding a new plugin package to choosing the right test tiers, entirely inside an agent session. / 构建和测试 DSH 插件的 Agent 技能：从脚手架新建插件包到选择正确测试层级，完全在 Agent 会话内完成。 |
| ⭐ 1 | [hccccc01333/dsh-excel-chat](https://github.com/hccccc01333/dsh-excel-chat) | Talk to Excel in DeepSeek Harness: create, edit, repair, and verify spreadsheets by chat. / 通过对话创建、编辑、修复和验证 Excel 表格。 |
| ⭐ 1 | [pingfanfan/dsh-learn](https://github.com/pingfanfan/dsh-learn) | Agent-maintained Chinese DeepSeek Harness learning, evidence, labs and ecosystem growth system. / Agent 维护的中文 DSH 学习、证据、实验与生态成长系统。 |
| ⭐ 4 | [huguangyu666/dsh-plugin-session-import](https://github.com/huguangyu666/dsh-plugin-session-import) | DeepSeek Harness plugin: import claude-code / codex / reasonix / zcode sessions. / DSH 插件：从 Claude Code / Codex / Reasonix / zcode 导入会话历史。 |
| ⭐ 2 | [Mreate/dsh-cc-import](https://github.com/Mreate/dsh-cc-import) | Import conversations into Claude Code with CLAUDE.md recognition and basic session features. / 将高质量对话导入 Claude Code，支持 CLAUDE.md 识别与基础功能扩展。 |
| ⭐ 1 | [jLeon-account/dsh-client-usage](https://github.com/jLeon-account/dsh-client-usage) | Real-time session-level API token usage & cost estimate, peak/off-peak pricing support. / 实时会话级 API token 用量与估算费用，峰谷计价适配。 |
| ⭐ 2 | [sunshine-lang/dsh-plugin-template](https://github.com/sunshine-lang/dsh-plugin-template) | Ready-to-publish DSH plugin skeleton: bundle format, tool DSL, config, tests, and a scaffold script. / 开箱即用 DSH 插件骨架：bundle 格式/工具 DSL/配置/测试脚手架。 |
| ⭐ 0 | [HHHEEEWWW/dsh-mcp-console](https://github.com/HHHEEEWWW/dsh-mcp-console) | MCP management panel for DeepSeek Harness Web UI (Settings → MCP): add/edit/remove MCP servers directly. / DSH Web UI MCP 管理面板：在设置页直接增删改 MCP 服务器。 |
| ⭐ 1 | [fly3366/DeepJIT](https://github.com/fly3366/DeepJIT) | JIT compiler plugin for DSH: compiles recurring agent workflows into hot skills and flow templates. / DSH JIT 编译器插件：将重复 Agent 工作流编译为热技能和工作流模板。 |
| ⭐ 1 | [CSY656/dsh-worktree](https://github.com/CSY656/dsh-worktree) | Git worktree filesystem isolation for DSH subagents — each child works in its own worktree; clean ones auto-remove, dirty ones are kept for review. / DSH 子代理工作树隔离：每个子代理独立 worktree，干净则自动清理，脏的保留审查。 |
| ⭐ 6 | [left0ver/dsh-file-review](https://github.com/left0ver/dsh-file-review) | Review files an agent just changed: diff viewer with inline side-by-side comparison. / Agent 修改文件审查：内联并排 diff 查看器。 |
| ⭐ 1 | [harryopo/dsh-remote-ide](https://github.com/harryopo/dsh-remote-ide) | SSH Remote IDE for DSH: connect via SSH and the IDE goes remote — explorer browses remote workspace, edit files directly. / DSH SSH 远程 IDE：连接后工作区远程化，直接编辑远程文件。 |
| ⭐ 1 | [Whning0513/deepseek-protocol-doctor](https://github.com/Whning0513/deepseek-protocol-doctor) | Checks DeepSeek tool loops, reasoning_content, strict schemas, and captured SSE. Also works as a DSH plugin. / 检测 DeepSeek 工具循环、reasoning_content、严格 schema 和捕获 SSE，同时作为 DSH 插件运行。 |
| ⭐ 1 | [MicroMilo/upstream-radar](https://github.com/MicroMilo/upstream-radar) | Always-on vulnerability and breaking-change impact monitoring for DeepSeek Harness plugins. / DSH 插件漏洞与破坏性变更持续监控。 |
| ⭐ 1 | [LJninse/dsh-open-in-ide](https://github.com/LJninse/dsh-open-in-ide) | Auto-detect local IDEs from DSH Web UI and open current workspace folder in one click. / 从 DSH Web UI 一键检测本地 IDE 并打开当前工作区。 |
| ⭐ 3 | [sandbaseai/deepseek-harness-handbook](https://github.com/sandbaseai/deepseek-harness-handbook) | Agent-first, multilingual handbook for DeepSeek Harness: quickstarts, architecture, safety, troubleshooting. / DSH Agent 优先多语言手册：快速入门、架构、安全与故障排查。 |
| ⭐ 1 | [JayZz210l/deepseek-harness-for-ide](https://github.com/JayZz210l/deepseek-harness-for-ide) | Bring DeepSeek Harness into JetBrains IDE: agent conversations, tool approval, goals, plans, sub-agents and workflows — one API key config. / 把 DeepSeek Harness 完整搬进 JetBrains IDE：智能体对话、工具审批、目标与计划、子智能体与 Workflow。 |
| ⭐ 2 | [poplarity/dsh-science-workbench](https://github.com/poplarity/dsh-science-workbench) | Reproducible science workbench plugin: agent-driven cells, inline figures with feedback/rerun, manifest provenance, environment snapshots. / 可复现科学工作台：Agent 驱动单元格、内联图表反馈重跑、清单溯源与环境快照。 |
| ⭐ 1 | [mervyn-teo/dsh-plugin-terminal](https://github.com/mervyn-teo/dsh-plugin-terminal) | Real PTY terminal in a VS Code-style collapsible footer panel for DeepSeek Harness Web. / DSH Web 端 VS Code 风格可折叠底部面板中的真实 PTY 终端。 |
| ⭐ 1 | [mbj733/dsh-edit-resend](https://github.com/mbj733/dsh-edit-resend) | Edit sent messages and resend — stop an in-flight reply, edit, and re-send from within DSH. / DSH 内编辑已发送消息并重新发送：中止正在进行的回复，编辑后重发。 |
| ⭐ 0 | [ideasir/dsh-zip](https://github.com/ideasir/dsh-zip) | ZIP file processing plugin for DeepSeek Harness: create, extract, list, and manage ZIP archives. / DSH ZIP 文件处理插件：创建/解压/列出/管理 ZIP 归档。 |
| ⭐ 4 | [BiBoyang/dsh-eval-harness](https://github.com/BiBoyang/dsh-eval-harness) | Regression eval harness for DeepSeek Harness: YAML-driven agent benchmark with PASS/WARN/FAIL gates and baseline comparison. / DSH 插件评测工具：YAML 用例驱动真实 agent 回归评测 + baseline 对比 PASS/WARN/FAIL 门禁。 |
| ⭐ 2 | [akira399/dsh-plugin-publisher](https://github.com/akira399/dsh-plugin-publisher) | DSH plugin development and GitHub publish workflow skill: develop, verify, publish and marketplace visibility (consent-gated). / DSH 插件开发与 GitHub 发布工作流技能：开发、验证、发布及市场曝光（需授权）。 |
| ⭐ 2 | [KHG420/git-worktree](https://github.com/KHG420/git-worktree) | Bind every DSH conversation to its own isolated git worktree + branch — parallel agents work on one repo without interference. / 每个 DSH 会话绑定独立 git worktree 与分支，并行 Agent 互不干扰。 |
| ⭐ 2 | [DfsyJian/dsh-snapshot](https://github.com/DfsyJian/dsh-snapshot) | Automatic file snapshots with a sidebar timeline and settings card. / 自动文件快照，侧边栏时间线与设置卡片。 |
| ⭐ 3 | [Civitasv/dsh-plugin-diff-review](https://github.com/Civitasv/dsh-plugin-diff-review) | Diff Review Plugin for DeepSeek Harness — inline change review before agent commit. / DSH 差异审查插件：Agent 提交前内联审查变更。 |
| ⭐ 2 | [anweat/dsh-plugin-dev-guide](https://github.com/anweat/dsh-plugin-dev-guide) | DSH plugin development & publishing guide: from first plugin to auto-publish to the community. / DSH 插件开发与发布指南：从零到自动发布到社区。 |


| ⭐ 7 | [WYH66666666/DSH-Transparent-UI-Plugin](https://github.com/WYH66666666/DSH-Transparent-UI-Plugin) | Transparent UI plugin for DSH Web: glass-morphism panels and translucent overlays with configurable opacity. / DSH Web 透明 UI 插件：玻璃态面板与半透明覆盖层，支持透明度配置。 |
| ⭐ 3 | [Inspireason/dsh-plugin-organizer](https://github.com/Inspireason/dsh-plugin-organizer) | DSH plugin organizer: categorize, filter and manage your plugin collection from the Web UI. / DSH 插件整理工具：分类、筛选和管理工作区插件集合。 |
| ⭐ 1 | [beijingwahw/dsh-companion](https://github.com/beijingwahw/dsh-companion) | DeepSeek Companion: conversation export (MD/PDF/JSON/PNG long image) + context handoff summary for seamless agent switching. / DSH 伴侣插件：对话智能导出（MD/PDF/JSON/PNG 长图）+ 上下文交接摘要。 |
---

## 🔧 Utility Toolkit / 实用工具集

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 15 | [omdsh-dev/dsh-toolkit](https://github.com/omdsh-dev/dsh-toolkit) | Zero-dependency toolkit: time / encoding / json / calculator / csv / regex / markdown / diff / stat / schema. / 零依赖工具包：time/encoding/json/calculator/csv/regex/markdown/diff/stat/schema。 |
| ⭐ 17 | [omdsh-dev/dsh-plugin-check](https://github.com/omdsh-dev/dsh-plugin-check) | Plugin health check: scan manifest protocol / patch format / build traps / hub listing status. / 插件健康检查：扫描清单协议/patch格式/构建陷阱/hub收录状态。 |
| ⭐ 35 | [vlln/plugin-registry](https://github.com/vlln/plugin-registry) | Plugin ecosystem infrastructure: browser panel for official repo plugins + make-dsh-plugin skill. / 插件生态基建：浏览器面板管理官方 repo 插件 + make-dsh-plugin skill。 |
| ⭐ 5 | [fakechris/dsh-harness-ops](https://github.com/fakechris/dsh-harness-ops) | DSH ops toolbox: A/B dual-slot upgrades, guardian daemon, one-command self-healing doctor. / DSH 运维工具箱：A/B 双槽升级、守护进程、一键自愈。 |
| ⭐ 3 | [omdsh-dev/dsh-tool-turbo](https://github.com/omdsh-dev/dsh-tool-turbo) | Per-round reasoning_effort optimizer: auto-downgrades tool-call reasoning for simple chains. / Per-round reasoning_effort 优化器：简单工具链自动降级思考。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-encoding](https://github.com/omdsh-dev/dsh-tool-encoding) | base64/url/hex/md5/sha/UUID encoding/decoding toolkit. / base64/url/hex/md5/sha/UUID 编解码工具。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-time](https://github.com/omdsh-dev/dsh-tool-time) | Strict ISO 8601 parsing, IANA timezone conversion, UTC calendar math. / ISO 8601 / IANA 时区 / UTC 日历运算。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-markdown](https://github.com/omdsh-dev/dsh-tool-markdown) | HTML↔Markdown conversion, GFM table normalization, TOC generation. / HTML↔Markdown / GFM 表格 / 目录生成。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-stat](https://github.com/omdsh-dev/dsh-tool-stat) | Descriptive statistics / percentiles / frequency distribution / correlation analysis. / 描述统计 / 百分位数 / 相关性分析。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-json](https://github.com/omdsh-dev/dsh-tool-json) | JMESPath subset queries, zero-dependency recursive descent parser. / JMESPath 子集查询。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-diff](https://github.com/omdsh-dev/dsh-tool-diff) | Text/JSON/CSV/Markdown structured comparison + unified diff. / 文本/JSON/CSV/Markdown 结构化比较与 unified diff。 |
| ⭐ 2 | [hyqhyq3/dsh-mcp-manager](https://github.com/hyqhyq3/dsh-mcp-manager) | MCP Server manager: Settings → MCP page, OAuth PKCE + dynamic client registration. / MCP Server 管理：Settings → MCP 页 + OAuth PKCE。 |
| ⭐ 2 | [gxpppp/dsh-search-mcp](https://github.com/gxpppp/dsh-search-mcp) | Replace built-in web search with MCP servers (Tavily/Brave/Exa/Perplexity/DuckDuckGo). / 替换内置 web search 为 MCP 服务器。 |
| ⭐ 3 | [PerryLink/dsh-mcp-panel](https://github.com/PerryLink/dsh-mcp-panel) | Read-only runtime management panel for the official DSH MCP client: status, tools, errors, reconnect counts, controlled patch suggestions (Apache-2.0). / 官方 DSH MCP 客户端只读运行时管理面板：状态/工具/错误/重连计数/受控补丁建议。 |
| ⭐ 2 | [Ericwong5021/dsh-kanban](https://github.com/Ericwong5021/dsh-kanban) | Task board plugin for DeepSeek Harness Web UI. / DSH Web UI 任务看板插件。 |
| ⭐ 2 | [MorGogh/widget-dock](https://github.com/MorGogh/widget-dock) | Draggable widget panel: balance, tokens, stats, commands, goal, cost. / 可拖拽 widget 面板（余额/token/统计/命令/目标/费用）。 |
| ⭐ 1 | [fff122/dsh-prompt-presets](https://github.com/fff122/dsh-prompt-presets) | Local reusable prompt presets for DeepSeek Harness. / 本地可复用 prompt 预设。 |
| ⭐ 1 | [fff122/dsh-task-checklist](https://github.com/fff122/dsh-task-checklist) | Local task checklist plugin for DeepSeek Harness. / 本地任务清单插件。 |
| ⭐ 1 | [omdsh-dev/dsh-pet-corner](https://github.com/omdsh-dev/dsh-pet-corner) | Pet corner: floating pet, keyless pet-image proxy, favorites. / 宠物角：悬浮宠物 + keyless 宠物图代理。 |
| ⭐ 1 | [omdsh-dev/dsh-fun-weather](https://github.com/omdsh-dev/dsh-fun-weather) | Weather tab and weather-following themes powered by Open-Meteo. / 天气标签 + 天气跟随主题（Open-Meteo 驱动）。 |
| ⭐ 1 | [omdsh-dev/sandbox-mxc](https://github.com/omdsh-dev/sandbox-mxc) | Microsoft cross-platform sandbox support. / 微软跨平台沙盒支持。 |
| ⭐ 1 | [omdsh-dev/Qwen-MM-Plugins](https://github.com/omdsh-dev/Qwen-MM-Plugins) | Qwen multimodal plugins support. / Qwen-MM-Plugins 支持。 |
| ⭐ 1 | [omdsh-dev/dsh-auto-chess](https://github.com/omdsh-dev/dsh-auto-chess) | Auto-chess plugin for DSH Web: human vs AI or dual-AI match. / DSH Web 自走棋插件：人机对战或双 AI 对弈。 |
| ⭐ 1 | [omdsh-dev/ex-setting](https://github.com/omdsh-dev/ex-setting) | DSH settings extension. / DSH 设置扩展。 |
| ⭐ 1 | [moduqishi/dsh-open-in-finder](https://github.com/moduqishi/dsh-open-in-finder) | One-click open-in-Finder icon in session header. / 一键 open-in-Finder 图标。 |
| ⭐ 1 | [schhaohao/dsh-file-explorer](https://github.com/schhaohao/dsh-file-explorer) | File explorer for DSH. / DSH 文件浏览器。 |
| ⭐ 1 | [zimixvx/dsh-archive-manager](https://github.com/zimixvx/dsh-archive-manager) | Archive manager for DSH. / DSH 归档管理器。 |
| ⭐ 1 | [detpecca/DSH-Wiki](https://github.com/detpecca/DSH-Wiki) | DSH Wiki. / DSH Wiki。 |
| ⭐ 1 | [echo-escape/dsh-workbench](https://github.com/echo-escape/dsh-workbench) | Plugin and skill showcase & sharing collection. / 插件与技能展示分享集合。 |
| ⭐ 1 | [Sanqi-normal/dsh-webui-market-plugin](https://github.com/Sanqi-normal/dsh-webui-market-plugin) | DSH Web GUI community plugin market — browse awesome-dsh-plugin.com and one-click install. / DSH Web GUI 社区插件市场，一键安装。 |
| ⭐ 1 | [ZgblKylin/dsh-gui](https://github.com/ZgblKylin/dsh-gui) | Tauri GUI with integrated DeepSeek Harness and plugin bundles. / DSH Tauri GUI：集成 DeepSeek Harness 与插件包。 |
| ⭐ 3 | [ZgblKylin/dsh-terminal](https://github.com/ZgblKylin/dsh-terminal) | Terminal plugin for DeepSeek Harness. / DSH 终端插件。 |
| ⭐ 2 | [Fro2en12/dsh-download-progress](https://github.com/Fro2en12/dsh-download-progress) | DSH web plugin: download progress panel for AI-generated artifacts. / DSH Web 插件：AI 产物下载进度面板。 |
| ⭐ 2 | [ZrSiO4-y/dsh-explorer](https://github.com/ZrSiO4-y/dsh-explorer) | VS Code-style file explorer for DeepSeek Harness: sidebar file tree + multi-tab preview (code/image/PDF/audio/video/zip). / DSH VS Code 风格文件浏览器：侧边栏文件树 + 多标签预览（代码/图片/PDF/音视频/ZIP）。 |
| ⭐ 1 | [flaqai/deepeseek-harness-guide](https://github.com/flaqai/deepeseek-harness-guide) | Guide for development with DeepSeek Harness. Building plugin for DeepSeek Harness Project. / DSH 插件开发指南。 |
| ⭐ 1 | [sliverp/DeepSeek-harness-qqbot](https://github.com/sliverp/DeepSeek-harness-qqbot) | QQ Bot text and image channel plugin for DeepSeek Harness. / QQ Bot 文本与图片频道插件。 |
| ⭐ 1 | [radres/dsh-plugin-call-me](https://github.com/radres/dsh-plugin-call-me) | Your DSH agent rings your actual phone: it asks out loud, you answer out loud, and the conversation continues via voice. / DSH Agent 拨打你的真实手机：语音询问、语音接听、语音继续对话。 |
| ⭐ 1 | [omdsh-dev/dsh-lark](https://github.com/omdsh-dev/dsh-lark) | Lark/Feishu IM bot channel for DeepSeek Harness: chats drive agents, replies and approvals return. / 飞书 IM Bot 通道：聊天驱动 Agent，回复/审批返回。 |
| ⭐ 1 | [springbrand-lab/dsh-oauth-mcp-client](https://github.com/springbrand-lab/dsh-oauth-mcp-client) | OAuth 2.1 Streamable HTTP MCP client plugin for DeepSeek Harness. / OAuth 2.1 Streamable HTTP MCP 客户端插件。 |
| ⭐ 7 | [LiangYin233/dsh-provider-model-configurator](https://github.com/LiangYin233/dsh-provider-model-configurator) | Advanced model configurator: apply pi-ai preset model context, output limits, and reasoning tiers to custom providers in one click. / DSH 高级模型配置器：将 pi-ai 预设模型的上下文、输出上限、推理挡位一键应用到自定义提供商。 |
| ⭐ 1 | [x118111/prompt-optimizer](https://github.com/x118111/prompt-optimizer) | Dynamic plugin: adds ✨ optimize-prompt button to chat composer — context-aware LLM rewriting with model fallback and visible errors. / 动态插件：为对话输入框添加提示词优化按钮，支持上下文感知改写与模型降级。 |
| ⭐ 1 | [ZSeven-W/dsh-openpencil](https://github.com/ZSeven-W/dsh-openpencil) | OpenPencil design preview and editing plugin for DSH. / OpenPencil 设计预览与编辑插件。 |
| ⭐ 26 | [HiWhaleW/dsh-toolbox](https://github.com/HiWhaleW/dsh-toolbox) | Local-first DSH plugins for product research, context routing, plugin preflight, and compatibility monitoring. / 本地优先 DSH 插件：产品调研、上下文路由、插件预检与兼容性监控。 |
| ⭐ 25 | [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) | Context insight dashboard: shows what the model's context window contains — token budget, source breakdown, and pressure indicators. / 上下文洞察看板：展示模型上下文窗口构成——token 预算、来源分解与压力指标。 |
| ⭐ 4 | [lire1131/dsh-undo-plugin](https://github.com/lire1131/dsh-undo-plugin) | Snapshot & rollback your plugin/skin/settings configs. Auto-save on change, undo/redo stack. / 插件/皮肤/设置配置快照回滚：变更自动保存，支持撤销/重做。 |
| ⭐ 3 | [hccccc01333/dsh-report-html](https://github.com/hccccc01333/dsh-report-html) | Generate self-contained interactive HTML reports from Markdown, tables, charts, China province maps. / 从 Markdown/表格/图表生成本地交互 HTML 报告，含中国省份地图。 |
| ⭐ 3 | [lsz-asd/dsh-plugin-session-delete](https://github.com/lsz-asd/dsh-plugin-session-delete) | Delete DSH sessions from the UI: header danger button + sidebar session-row menu item. / 从 UI 删除 DSH 会话：顶栏危险按钮 + 侧边栏会话行菜单。 |
| ⭐ 3 | [zhangzheng25/dsh-token-monitor](https://github.com/zhangzheng25/dsh-token-monitor) | Token usage & conversation stats as a native settings page — today / 7d / 30d views. / 原生设置页 token 用量与对话统计，支持今日/7 天/30 天视图。 |
| ⭐ 1 | [Awu12277/dsh-stock-watch](https://github.com/Awu12277/dsh-stock-watch) | A-share real-time stock watch plugin — foldable popup in DSH Web top-right corner for your watchlist. / A股自选股实时行情盯盘插件：DSH Web 右上角可折叠弹窗。 |
| ⭐ 2 | [Make0209/dsh-usage-stats](https://github.com/Make0209/dsh-usage-stats) | GitHub-style usage heatmap + token/cache-hit/account balance dashboard + workspace alias management. / GitHub 风格用量热力图 + Token/缓存命中/账户余额看板 + 工作区别名管理。 |
| ⭐ 2 | [hrhgit/deepseek-harness-plugin-manager](https://github.com/hrhgit/deepseek-harness-plugin-manager) | Web plugin manager for DSH: inspect, search, group, enable, and disable Cordis plugins from Settings. / DSH Web 插件管理器：从设置页检查/搜索/分组/启停 Cordis 插件。 |
| ⭐ 2 | [daybreak33167-commits/dsh-subscriptions](https://github.com/daybreak33167-commits/dsh-subscriptions) | Drives Cursor models through the official DeepSeek SDK within DSH sessions. / 通过官方 SDK 在 DSH 会话中驱动 Cursor 模型。 |
| ⭐ 2 | [Acidmoon/DIzzy-DSH](https://github.com/Acidmoon/DIzzy-DSH) | Collection of DSH utility plugins: usage tracking, session helpers, and quality-of-life improvements. / DSH 实用插件合集：用量追踪/会话辅助/生活质量提升。 |
| ⭐ 2 | [w769721503/dsh-plugin-store](https://github.com/w769721503/dsh-plugin-store) | DSH plugin store: browse, search, filter, and one-click install dsh-plugin ecosystem plugins. / DSH 插件商店：浏览/搜索/筛选并一键安装 dsh-plugin 生态插件。 |
| ⭐ 2 | [hellosky983/dsh-qrcode](https://github.com/hellosky983/dsh-qrcode) | Offline QR code (SVG/PNG/ASCII) and barcode (Code128/EAN-13) generator — no network, no API key. / 离线二维码（SVG/PNG/ASCII）和条形码（Code128/EAN-13）生成器，无需网络与 API Key。 |
| ⭐ 1 | [causebefore/dsh-pomodoro](https://github.com/causebefore/dsh-pomodoro) | Pomodoro timer plugin for DSH Web: configurable focus/break durations, sidebar entry, draggable floating panel. / DSH Web 番茄钟插件：可配置专注/休息时长，侧栏入口，可拖动浮动面板。 |
| ⭐ 1 | [wellorbetter/dsh-plugin-window-stats](https://github.com/wellorbetter/dsh-plugin-window-stats) | All-session progress & token overview: real-time refresh, cache hits, context usage, click-to-jump. / 全会话进度与 Token 总览：实时刷新、缓存命中、上下文占用、点击直达。 |
| ⭐ 1 | [AcidGr/dsh-web-lan-access](https://github.com/AcidGr/dsh-web-lan-access) | LAN access plugin for DeepSeek Harness Web UI — exposes the web service to local network. / DSH Web UI 局域网访问插件：将 Web 服务暴露到本地网络。 |
| ⭐ 1 | [Suxeca/dsh-plugin](https://github.com/Suxeca/dsh-plugin) | Session switch panel plugin (Ctrl+K / Ctrl+[ ]) + plugin development template for DSH. / DSH 会话切换面板插件（Ctrl+K/Ctrl+[ ]）+ 插件开发模板。 |
| ⭐ 1 | [ziyou979/dsh-llm-oauth](https://github.com/ziyou979/dsh-llm-oauth) | OAuth / subscription-plan LLM providers (Grok, GitHub Copilot, OpenAI Codex) for DeepSeek Harness. / DSH OAuth/订阅计划 LLM 提供商：Grok、GitHub Copilot、OpenAI Codex。 |
| ⭐ 1 | [Miku196/dsh-tokensave](https://github.com/Miku196/dsh-tokensave) | Token-saving plugin for DeepSeek Harness: optimizes context to reduce token consumption. / DSH Token 节省插件：优化上下文以降低 token 消耗。 |
| ⭐ 1 | [Max-Samson/dsh-usage-chart](https://github.com/Max-Samson/dsh-usage-chart) | Real-time Token usage, cost estimates, per-round charts, and peak/off-peak pricing for DeepSeek Harness. / DSH 实时 Token 用量、费用估算、每轮图表及峰谷计价。 |
| ⭐ 1 | [cute-baobao/dsh-usage-meter](https://github.com/cute-baobao/dsh-usage-meter) | Per-model daily token usage recorder (input/output/cache hits) with a Web GUI dashboard. / 按模型每日 Token 用量记录器（输入/输出/缓存命中），带 Web 看板。 |
| ⭐ 1 | [sharkymew/dsh-utility-tools](https://github.com/sharkymew/dsh-utility-tools) | Drag-and-drop any file into chat + selected text引用 for DeepSeek Harness conversations. / DSH 对话工具插件：拖拽任意文件进入对话 + 选中文本引用。 |
| ⭐ 1 | [awesome-dsh-plugin/dsh-find-plugin](https://github.com/awesome-dsh-plugin/dsh-find-plugin) | Find DSH plugins inside the agent — live GitHub dsh-plugin topic search, star-ranked. / 会话内搜索发现 DSH 插件：GitHub dsh-plugin 主题实时搜索。 |
| ⭐ 87 | [dsh-market/dsh-market](https://github.com/dsh-market/dsh-market) | The plugin market inside DeepSeek Harness — browse, search, one-click install. / DSH 内置插件市场：浏览、搜索、一键安装。 |
| ⭐ 1 | [TheYoungChen/dsh-plugin-market](https://github.com/TheYoungChen/dsh-plugin-market) | DeepSeek Harness plugin market — browse, search & install dsh-plugin topic plugins. / DSH 插件市场：浏览/搜索/安装。 |
| ⭐ 1 | [angel-heart/dsh-browser-agent](https://github.com/angel-heart/dsh-browser-agent) | Give DSH agents a real browser: browser-pro preset + 15 browser_* tools with persistent login. / 给 DSH Agent 真实浏览器：browser-pro 预设 + 15 个 browser_* 工具，持久化登录态。 |
| ⭐ 11 | [LX2000WASD/dsh-web-plugin-manager](https://github.com/LX2000WASD/dsh-web-plugin-manager) | One-click plugin management in Web UI: view, start/stop, install/uninstall, env management, plugin marketplace. Covers both bundle and non-bundle plugins. / Web UI 一键管理 DSH 插件：查看、实时启停、安装/卸载、环境管理、插件市场，bundle 与非 bundle 全覆盖。 |
| ⭐ 1 | [AwesomeHou/dsh-plugin-marketplace](https://github.com/AwesomeHou/dsh-plugin-marketplace) | Live-syncs the GitHub dsh-plugin topic (1800+ repos) into a searchable, paginated settings tab with one-click install and agent tools (market_search / market_install). / 实时同步 GitHub dsh-plugin topic（1800+ 仓库）到可搜索分页设置页，支持一键安装和 agent 工具。 |
| ⭐ 4 | [mishibeikejie/zat-dsh-engine](https://github.com/mishibeikejie/zat-dsh-engine) | Visual plugin marketplace for DeepSeek Harness — browse, search and install community plugins. / DSH 可视化插件市场：浏览、搜索和安装社区插件。 |
| ⭐ 10 | [Ericwong5021/deepseek-plugin-store](https://github.com/Ericwong5021/deepseek-plugin-store) | Independent community plugin store for DeepSeek Harness: discover, install, and submit verified plugins, tools, and extensions. / DSH 独立社区插件商店：发现、安装和提交经过验证的插件、工具与扩展。 |
| ⭐ 9 | [joejojoking-cloud/dsh-file-explorer](https://github.com/joejojoking-cloud/dsh-file-explorer) | File explorer plugin for DeepSeek Harness: file tree, preview, markdown, syntax highlighting, in-panel editing, VS Code integration. / DSH 全局文件资源管理器：文件树/预览/高亮/内联编辑/VS Code 集成。 |
| ⭐ 4 | [xiongjiamu/dsh-atomgit](https://github.com/xiongjiamu/dsh-atomgit) | AtomGit plugin bundle for DeepSeek Harness: atomgit-skills workflows + ag CLI + platform-hosted package registry. / AtomGit 插件包：DSH atomgit-skills 工作流 + ag CLI + 平台托管包注册表。 |
| ⭐ 3 | [fly233338/dsh-overleaf](https://github.com/fly233338/dsh-overleaf) | Connect Overleaf projects to DeepSeek Harness via OverleafMCP and MCP tools. / 通过 OverleafMCP 和 MCP 工具将 Overleaf 项目接入 DSH。 |
| ⭐ 3 | [LeemanCheung/dsh-token-usage](https://github.com/LeemanCheung/dsh-token-usage) | Persistent token usage records and dashboard for DeepSeek Harness. / DSH 持久化 token 用量记录与仪表板。 |
| ⭐ 1 | [tanf1ng/dsh-tool-hackernews](https://github.com/tanf1ng/dsh-tool-hackernews) | Hacker News tool suite (hn_top_stories, hn_search, hn_item) for DeepSeek Harness agents. / DSH Agent Hacker News 工具套件。 |
| ⭐ 3 | [Xenia0922/dsh-opencode-go-usage](https://github.com/Xenia0922/dsh-opencode-go-usage) | OpenCode Go usage floating dashboard for DSH: quota, per-request cost, model/source distribution. / DSH OpenCode Go 用量悬浮仪表盘：配额、逐请求成本、模型/来源分布。 |
| ⭐ 2 | [Yi-111-a/dsh-jingling](https://github.com/Yi-111-a/dsh-jingling) | DSH plugin collection bundle — a curated set of practical plugins for everyday DeepSeek Harness workflows. / DSH 插件合集 bundle：精选日常 DSH 实用插件集合。 |


| ⭐ 3 | [slywalker2006/dsh-passwords](https://github.com/slywalker2006/dsh-passwords) | Password management plugin for DSH: login gateway, at-rest encryption, secure credential storage. / DSH 密码管理插件：登录网关、静默加密、安全凭证存储。 |
| ⭐ 2 | [PerryLink/dsh-skill-pack-security](https://github.com/PerryLink/dsh-skill-pack-security) | Security-audit skill pack for DSH: 8 agent skills for secret scanning, compliance checks, and vulnerability detection. / DSH 安全审计技能包：8 个 agent 技能用于密钥扫描、合规检查与漏洞检测。 |
| ⭐ 3 | [030611/dsh-telemetry-redactor](https://github.com/030611/dsh-telemetry-redactor) | Fail-closed telemetry redaction for DSH: auto-redacts sensitive fields during session export-copy for privacy. / DSH 遥测数据脱敏插件：会话导出时自动脱敏敏感字段，保护隐私。 |
| ⭐ 1 | [kongxiangyiren/dhs-theme-plugin](https://github.com/kongxiangyiren/dhs-theme-plugin) | DSH theme management plugin: browse, install, and switch UI themes from Settings page. / DSH 主题管理插件：浏览/安装/切换 UI 主题。 |
| ⭐ 1 | [wanghui040127-ui/deepseek-harness-account](https://github.com/wanghui040127-ui/deepseek-harness-account) | Standalone account plugin for DeepSeek Harness: balance display, usage stats, and local token dashboard. / DSH 独立账户插件：余额显示、用量统计与本地 token 看板。 |
---

## 💬 Communications & IM Bridges / 通讯与 IM 桥接

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 36 | [omdsh-dev/dsh-notification](https://github.com/omdsh-dev/dsh-notification) | Desktop notifications: per-outcome controls + include/exclude keyword rules. / 桌面通知：按结果类型控制 + include/exclude 关键词规则。 |
| ⭐ 24 | [Chinesezjc/dsh-interconnect](https://github.com/Chinesezjc/dsh-interconnect) | Cross-instance message/event handoff plugins for DSH. / 跨实例消息/事件交接插件。 |
| ⭐ 10 | [whiteguo233/dsh-openbiliclaw](https://github.com/whiteguo233/dsh-openbiliclaw) | OpenBiliClaw DSH plugin: persistent 4th column with 22 Agent Bridge tools. / OpenBiliClaw DSH 插件：常驻第四栏，22 个 Agent Bridge 工具。 |
| ⭐ 6 | [LoserFox/telegram](https://github.com/LoserFox/telegram) | Telegram Bot API bridge: long polling, per-chat sessions, HTML formatting. / Telegram Bot API 桥接：长轮询、per-chat 会话、HTML 格式化。 |
| ⭐ 4 | [bill9109/dsh-web-ui-notify](https://github.com/bill9109/dsh-web-ui-notify) | DSH desktop notification reminder. / DSH 桌面通知提醒。 |
| ⭐ 4 | [MuziIsabel/dsh-win-notify](https://github.com/MuziIsabel/dsh-win-notify) | Windows toast notification + sound on task completion. / Windows toast 通知 + 声音（任务完成时）。 |
| ⭐ 3 | [wssfk12138/dsh-wechat-notify](https://github.com/wssfk12138/dsh-wechat-notify) | WeChat notification via ClawBot channel: task done / decision needed. / 微信通知：通过 ClawBot 通道主动推送任务完成/需决策消息。 |
| ⭐ 3 | [yyh-001/dsh-companion](https://github.com/yyh-001/dsh-companion) | Companion mode: SOUL persona + Hermes long-term memory, optional QQ channel. / 陪伴模式：SOUL 人格 + Hermes 长期记忆，可选 QQ 通道。 |
| ⭐ 3 | [william-jin-cmu/dsh-companion](https://github.com/william-jin-cmu/dsh-companion) | Persistent desktop assistant: global hotkey, scheduled automation, quick replies, plugin marketplace. / 常驻桌面助手：全局唤起、定时自动化、快捷回复、插件市场。 |
| ⭐ 3 | [BiBoyang/dsh-im-bridge](https://github.com/BiBoyang/dsh-im-bridge) | IM bridge (WeChat/iLink v0.1, DingTalk/Feishu/Telegram reserved). / IM 桥接（微信/iLink v0.1，钉钉/飞书/Telegram 预留）。 |
| ⭐ 2 | [imetn/dsh-lark-bridge](https://github.com/imetn/dsh-lark-bridge) | Bidirectional Lark/Feishu controller for DeepSeek Harness. / 飞书/Lark 双向控制桥接。 |
| ⭐ 2 | [Roy-oss1/dsh-lark](https://github.com/Roy-oss1/dsh-lark) | Lark/Feishu IM bot channel: chats drive agents, replies and approvals return as messages. / 飞书 IM Bot 频道：聊天驱动 Agent，回复/审批以消息和卡片返回。 |
| ⭐ 1 | [YYTbit/dsh-plugin-claude-bridge](https://github.com/YYTbit/dsh-plugin-claude-bridge) | Bridge Claude Code skills and config into DeepSeek Harness. / Claude Code 技能/配置桥接到 DSH。 |
| ⭐ 1 | [YYTbit/dsh-plugin-opencode-bridge](https://github.com/YYTbit/dsh-plugin-opencode-bridge) | Bridge OpenCode skills and config into DeepSeek Harness. / OpenCode 技能/配置桥接到 DSH。 |
| ⭐ 1 | [YYTbit/dsh-plugin-pi-bridge](https://github.com/YYTbit/dsh-plugin-pi-bridge) | Bridge Pi Agent skills and config into DeepSeek Harness. / Pi Agent 技能/配置桥接到 DSH。 |
| ⭐ 1 | [YYTbit/dsh-plugin-codex-bridge](https://github.com/YYTbit/dsh-plugin-codex-bridge) | Bridge Codex skills and config into DeepSeek Harness. / Codex 技能/配置桥接到 DSH。 |
| ⭐ 1 | [wingoo/codex-plugin-dsh](https://github.com/wingoo/codex-plugin-dsh) | Use local Codex App Server as a model provider in DeepSeek Harness. / 使用本地 Codex App Server 作为模型提供商。 |
| ⭐ 1 | [banana770/dsh-qq-bridge](https://github.com/banana770/dsh-qq-bridge) | QQ Bot <-> DeepSeek Harness bridge: bidirectional text chat via QQ channel (Node.js 22). / QQ 机器人 <-> DSH 双向对话桥接。 |
| ⭐ 1 | [xmanrui/dsh-feishu](https://github.com/xmanrui/dsh-feishu) | Connect multiple Feishu bots to DeepSeek Harness with QR-code setup and streaming chat. / 多飞书机器人接入 DSH，QR 码配置，流式聊天。 |
| ⭐ 1 | [congchuanling-dot/DSH-Telegram-Relay](https://github.com/congchuanling-dot/DSH-Telegram-Relay) | Turn Telegram into a remote conversation and notification channel for DeepSeek Harness. / Telegram 远程对话与通知通道。 |
| ⭐ 1 | [YYTbit/dsh-plugin-cost-tracker](https://github.com/YYTbit/dsh-plugin-cost-tracker) | Token cost tracker for DeepSeek Harness. / Token 用量追踪器。 |
| ⭐ 1 | [yyh-001/dsh-expression](https://github.com/yyh-001/dsh-expression) | Emoji plugin: semantic image search, sends real files via companion QQ channel. / DSH 表情包插件：语义搜图，走 companion QQ 通道。 |
| ⭐ 3 | [loudMore/dsh-drop-to-path](https://github.com/loudMore/dsh-drop-to-path) | DSH plugin that delivers images AND files to text-only models: images keep native attachment UI, other files show as chips and path on send — pairs with vision toolkits. / DSH 插件：图片和文件直达纯文本模型，图片保留原生附件，其他文件显示为方块并转为路径。 |
| ⭐ 2 | [wz-heng/dsh-feishu-bridge](https://github.com/wz-heng/dsh-feishu-bridge) | Feishu (Lark) channel bridge for DeepSeek Harness: message a Feishu bot, it runs a dsh agent turn, the reply comes back. / 飞书通道桥接：向飞书机器人发消息驱动 DSH Agent，回复返回。 |
| ⭐ 2 | [hi-wenw/dsh-telegram-channel](https://github.com/hi-wenw/dsh-telegram-channel) | DeepSeek Harness Telegram mobile remote: bind live Web sessions (Codex-style). Install: dsh plugin add github:hi-wenw/dsh-telegram-channel. / DSH Telegram 移动远程：绑定实时 Web 会话（Codex 风格）。 |
| ⭐ 6 | [flymysql/dsh-remote](https://github.com/flymysql/dsh-remote) | Remote-work assistant for DeepSeek Harness: connect via SSH (key or password), pick workspace, and run agent sessions remotely. / DSH 远程工作助手：SSH 连接（密钥或密码）、选择工作区、远程运行 Agent 会话。 |
| ⭐ 4 | [UynajGI/dsh-ssh](https://github.com/UynajGI/dsh-ssh) | SSH remote-execution plugin for DeepSeek Harness: ProxyJump chain, SFTP filesystem, subprocess over remote SSH. / DSH SSH 远程执行插件：ProxyJump 链、SFTP 文件系统、远程 SSH 子进程。 |
| ⭐ 2 | [Yan-Zero/dsh-remote-ssh](https://github.com/Yan-Zero/dsh-remote-ssh) | Use SSH hosts as transparent workspaces in DeepSeek Harness — no local setup needed. / 将 SSH 主机作为 DSH 透明工作区使用，无需本地配置。 |
| ⭐ 1 | [liguobao/deepseek-harness-remote](https://github.com/liguobao/deepseek-harness-remote) | Secure remote control for DSH: Harness and codebase stay on the host, paired clients view sessions via a restricted protocol. / DSH 安全远程控制方案：Harness 和代码仓库留在 Host，配对客户端通过受限协议查看会话。 |
| ⭐ 2 | [610la/dsh-notification-center](https://github.com/610la/dsh-notification-center) | DSH notification center plugin: browser notifications + 21 sound effects triggered by conversation/task/error/approval events. / DSH 通知中心插件：对话/任务完成/报错/等待批准事件触发浏览器通知 + 21 种匹配音效。 |
| ⭐ 2 | [dbydd/dsh-onlyne](https://github.com/dbydd/dsh-onlyne) | IM gateway for DeepSeek Harness agents — send and receive QQ, WeChat, Feishu and Telegram messages from dsh sessions. / DSH 即时通讯网关：从会话收发 QQ/微信/飞书/Telegram 消息。 |
| ⭐ 6 | [Hongtwenfive1226/DSH-Mobile-for-Android](https://github.com/Hongtwenfive1226/DSH-Mobile-for-Android) | Android mobile client for DeepSeek Harness via Tailscale — secure remote access to your DSH agent from phone. / 基于 Tailscale 的 DSH Android 移动端：安全远程访问本地 DSH Agent。 |
| ⭐ 1 | [hongshuxifan321/dsh-mobile-app](https://github.com/hongshuxifan321/dsh-mobile-app) | DSH Remote — Android companion app for DeepSeek Harness, send commands and receive agent responses on mobile. / DSH Remote：Android 伴侣应用，手机端发送指令、接收 Agent 回复。 |


| ⭐ 10 | [PlutoKeating/dsh-lark-bot](https://github.com/PlutoKeating/dsh-lark-bot) | Feishu/Lark bot bridge for DSH: drive your local coding agent from Lark with full project workspace management. / DSH 飞书/Lark Bot 桥接：从飞书控制本地编码 Agent，含完整项目工作区管理。 |
| ⭐ 6 | [yeruizhi/dsh-lark-meeting-notifier](https://github.com/yeruizhi/dsh-lark-meeting-notifier) | Feishu meeting reminder plugin for DSH: alerts when your AI session overlaps with real-world calendar meetings. / DSH 飞书会议提醒插件：AI 会话与真实会议冲突时主动推送提醒。 |
| ⭐ 5 | [amlyczz/dsh-lark-link](https://github.com/amlyczz/dsh-lark-link) | High-reliability Feishu/Lark bridge for DSH: QR one-click auth, multi-device sessions, persistent connections. / DSH 高可靠飞书/Lark 桥接：扫码一键登录、多设备持久会话。 |
| ⭐ 2 | [cmfok/dsh-feishucard](https://github.com/cmfok/dsh-feishucard) | DSH ↔ Feishu streaming reply card bridge: real-time message cards with interactive buttons and live updates. / DSH 飞书流式回复卡片桥接：实时消息卡片带交互按钮与实时更新。 |
| ⭐ 0 | [sosojust/dsh-messge-channels](https://github.com/sosojust/dsh-messge-channels) | Connect Feishu, DingTalk, and WeCom to DeepSeek Harness — chat-driven agent control across multiple IM platforms. / DSH 多 IM 桥接：连接飞书/钉钉/企微，多平台聊天驱动 Agent。 |
| ⭐ 0 | [zxz9988/dsh-wechat-bridge](https://github.com/zxz9988/dsh-wechat-bridge) | DSH WeChat bridge plugin: connect mobile WeChat (iLink/ClawBot protocol) to your agent for cross-platform messaging. / DSH 微信桥接插件：连接手机微信（iLink/ClawBot 协议）至 Agent。 |
| ⭐ 2 | [wly8691-jpg/knowlp-rag](https://github.com/wly8691-jpg/knowlp-rag) | KnowLP-RAG: dual knowledge-graph RAG for Markdown notes — MCP + native Cordis plugin for DeepSeek Harness (dsh) & Claude Code. / KnowLP-RAG：双知识图谱 RAG，用于 Markdown 笔记——DSH 与 Claude Code 的双平台 MCP + 原生插件。 |
| ⭐ 9 | [zhuiyueya/dsh-im-gateway](https://github.com/zhuiyueya/dsh-im-gateway) | Aggregate IM gateway: connect DSH agents to WeChat, Feishu, Telegram, Discord & 20+ chat platforms from one plugin. / DSH 聚合 IM 网关：一个插件接入微信/飞书/Telegram/Discord 等 20+ 聊天平台。 |
---

## 🧠 Memory & Persistence / 记忆与持久化

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 5 | [vlln/dsh-paste-input](https://github.com/vlln/dsh-paste-input) | Ctrl+V paste + drag-and-drop file input enhancement for DSH. / Ctrl+V 粘贴 + 拖拽文件输入增强。 |
| ⭐ 16 | [omdsh-dev/dsh-mnemon](https://github.com/omdsh-dev/dsh-mnemon) | Complete local memory system: runtime memory, searchable archives, supervised memory. / 完备本地记忆系统：运行时记忆/可检索档案/受监督记忆体。 |
| ⭐ 2 | [nowledge-co/nowledge-mem-deepseek-harness](https://github.com/nowledge-co/nowledge-mem-deepseek-harness) | Nowledge Mem community plugin bundle for DeepSeek Harness. / Nowledge Mem 社区插件 bundle。 |
| ⭐ 1 | [RealAlexandreAI/dsh-nocturne-memory](https://github.com/RealAlexandreAI/dsh-nocturne-memory) | Nocturne Memory client for DeepSeek Harness. / Nocturne Memory 客户端。 |
| ⭐ 1 | [PerryLink/dsh-memento](https://github.com/PerryLink/dsh-memento) | Bounded, layered, approval-gated, auditable cross-session memory: ctx.memory + SQLite provider. / 有界分层审批审计跨会话记忆：ctx.memory + SQLite provider。 |
| ⭐ 1 | [cking000bigdemon/dsh-toolbelt](https://github.com/cking000bigdemon/dsh-toolbelt) | 8-in-1 toolkit including cross-agent memory. / 8 合 1 工具带含跨 Agent 记忆。 |
| ⭐ 1 | [alooshxl/dsh-session-pins](https://github.com/alooshxl/dsh-session-pins) | Persistent pinned-session menu for DeepSeek Harness. / 持久化固定会话菜单。 |
| ⭐ 3 | [3TXX/dsh-persistence](https://github.com/3TXX/dsh-persistence) | Persistence tool. / 持久化工具。 |
| ⭐ 1 | [U-Illll/dsh-memory](https://github.com/U-Illll/dsh-memory) | Memory retrieval plugin for DeepSeek Harness: wiki double-link memory graph with 9 tools. / DSH 记忆检索插件：wiki 双链记忆图谱 + 9 个工具。 |
| ⭐ 1 | [chancelu/dsh-llmwiki](https://github.com/chancelu/dsh-llmwiki) | Local Markdown wiki as long-term memory for DeepSeek Harness — RRF-fused retrieval. / 本地 Markdown Wiki 作为长期记忆：RRF 融合检索。 |
| ⭐ 1 | [Jelee0145/dsh-mem](https://github.com/Jelee0145/dsh-mem) | Cross-session long-term memory for DeepSeek Harness: durable JSON-file memory store. / 跨会话长期记忆：JSON 文件持久化存储。 |
| ⭐ 1 | [quan2005/dsh-plugin-jinji](https://github.com/quan2005/dsh-plugin-jinji) | Minimal text memory system for DeepSeek Harness: dual-track memory (log + entity profile). / 极简文本记忆系统：双轨记忆（流水日志 + 实体画像）。 |
| ⭐ 1 | [Spirtxiaoqi7/mindspace-dsh-session-memory](https://github.com/Spirtxiaoqi7/mindspace-dsh-session-memory) | Editable, session-isolated personalization memory for DeepSeek Harness. / 可编辑、会话隔离的个性化记忆。 |
| ⭐ 1 | [IAMLieutenant/dsh-tool-user-memory](https://github.com/IAMLieutenant/dsh-tool-user-memory) | DeepSeek Harness user memory plugin. / DSH 用户记忆插件。 |
| ⭐ 1 | [A-Dawn/A_memorix-deepseek-harness](https://github.com/A-Dawn/A_memorix-deepseek-harness) | A_memorix memory integration bundle for DeepSeek Harness. / A_memorix 记忆集成 bundle。 |
| ⭐ 1 | [mchenziyi/dsh-Mnemosyne](https://github.com/mchenziyi/dsh-Mnemosyne) | Long-term memory and progressive disclosure plugin for DeepSeek Harness. / 长期记忆与渐进式披露插件。 |
| ⭐ 1 | [ICCuse/dsh-file-memory](https://github.com/ICCuse/dsh-file-memory) | File-backed working memory tools for DeepSeek Harness: memorize/recall key premises verbatim. / 文件备份工作记忆工具：原样记忆/回忆关键前提。 |
| ⭐ 1 | [mbj733/dsh-hermes-memory](https://github.com/mbj733/dsh-hermes-memory) | DSH agent preset + plugin: Hermes-style cross-session memory & autonomous skill learning. / Hermes 风格跨会话记忆与自主技能学习。 |
| ⭐ 1 | [reshuibuduo/dsh-tmcra-memory](https://github.com/reshuibuduo/dsh-tmcra-memory) | TMCRA Agent 长期记忆系统的 DeepSeek Harness 接入插件：跨对话延续项目记忆，自动沉淀项目知识。 / TMCRA Agent 长期记忆接入插件。 |
| ⭐ 1 | [clouwer/dsh-memsearch](https://github.com/clouwer/dsh-memsearch) | Automatic semantic memory plugin for DeepSeek Harness via memsearch. / 基于 memsearch 的自动语义记忆插件。 |
| ⭐ 1 | [mario03690/dsh-netcafe](https://github.com/mario03690/dsh-netcafe) | DeepSeek Harness bundle: adds AI NetCafé hosted outcome tools (statement extraction with reconciliation). / AI NetCafé 托管结果工具包。 |
| ⭐ 1 | [LeslieWylie/dsh-evidence-memory](https://github.com/LeslieWylie/dsh-evidence-memory) | Git-backed project memory with line-addressable evidence, freshness tracking, and audit trail. / Git 驱动的项目记忆：行级可寻址证据、新鲜度追踪与审计追踪。 |
| ⭐ 1 | [2303572348/deepseek-harness-memory](https://github.com/2303572348/deepseek-harness-memory) | DeepSeek Harness memory plugin. / DSH 记忆插件。 |
| ⭐ 1 | [Haoran2099/focal-dsh](https://github.com/Haoran2099/focal-dsh) | Task-isolated, privacy-first memory for DeepSeek Harness. / 任务隔离、隐私优先的记忆系统。 |
| ⭐ 1 | [Danilky666/dsh-vision](https://github.com/Danilky666/dsh-vision) | DeepSeek Harness vision plugin: visual working memory for text-only agents (numbered element inventory). / DSH 视觉插件：纯文本 Agent 的视觉工作记忆。 |
| ⭐ 7 | [knqiufan/powercontext-dsh](https://github.com/knqiufan/powercontext-dsh) | DeepSeek Harness plugin connecting to a PowerContext Server over HTTP for recall, memory, handoff, experience, and skills. / DSH 插件：通过 HTTP 连接 PowerContext 服务器，支持回忆、记忆、交接、经验和技能。 |
| ⭐ 2 | [384961890-ui/pawin-brain-deepseek-harness](https://github.com/384961890-ui/pawin-brain-deepseek-harness) | Brain-inspired runtime for DSH agents — remember, self-correct, learn. v0.1 ships memory (injection, notes, recall), 100% covered. / 类脑运行时：记忆注入、笔记与回忆，全自动测试覆盖。 |
| ⭐ 1 | [Culeot/dsh-agent-memory](https://github.com/Culeot/dsh-agent-memory) | Cross-session long-term memory plugin for DeepSeek Harness — durable memory store that persists across agent sessions. / DSH 跨会话长期记忆插件：持久化记忆存储，跨 Agent 会话延续。 |

---

## 🤖 Multi-Agent & Workflows / 多 Agent 与工作流

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 258 | [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) | AgentTeams plugin for multi-agent collaboration in DeepSeek Harness. / AgentTeams 插件：多 Agent 协作。 |
| ⭐ 111 | [hewzhew/dsh-agent-rp](https://github.com/hewzhew/dsh-agent-rp) | SillyTavern migration and next-generation Agent RP for DSH. / SillyTavern 迁移与下一代 DSH Agent RP。 |
| ⭐ 5 | [R3alloc/dsh-session-deeplink](https://github.com/R3alloc/dsh-session-deeplink) | DeepSeek Harness plugin for shareable session deep links — generate and share persistent session URLs. / DSH 会话深链接插件：生成并分享持久化会话 URL。 |
| ⭐ 25 | [zenx0x/allinluna](https://github.com/zenx0x/allinluna) | Resource-aware multi-agent orchestration for Codex and DeepSeek Harness (All in Flash DSH plugin). / 资源感知多 Agent 编排，支持 Codex 与 DSH（All in Flash DSH 插件）。 |
| ⭐ 31 | [titanwings/dsh-automation](https://github.com/titanwings/dsh-automation) | Scheduled tasks: run coding tasks in fresh Agent sessions on schedule, managed from DSH Web or an Agent. / 定时任务：按计划在全新 Agent Session 中运行编码任务，由 DSH Web 或 Agent 管理。 |
| ⭐ 9 | [omdsh-dev/dsh-deep-research](https://github.com/omdsh-dev/dsh-deep-research) | Adaptive deep-research orchestrator with cybernetics/information-theory design. / 自适应深度研究编排器，cybernetics/信息论设计。 |
| ⭐ 14 | [omdsh-dev/dsh-data-agent](https://github.com/omdsh-dev/dsh-data-agent) | Let AI connect to databases and write SQL queries. / 让 AI 连数据库、写 SQL 的 DSH 插件。 |
| ⭐ 4 | [HuanLinOTO/dsh-plugin-yet-another-subagent](https://github.com/HuanLinOTO/dsh-plugin-yet-another-subagent) | Configurable subagent profile system with Web UI settings / real-time progress / subagent tree. / 可配置子代理 profile 系统 + Web UI 设置/实时进度/子代理树。 |
| ⭐ 3 | [shaokeyibb/dsh-plugin-product-subagents](https://github.com/shaokeyibb/dsh-plugin-product-subagents) | Role-based Codex/Claude Code/ACP subagent providers with durable session recovery. / Role-based Codex/Claude Code/ACP subagent providers，可恢复会话。 |
| ⭐ 3 | [Buyi-wsgzg/dsh-sidechain](https://github.com/Buyi-wsgzg/dsh-sidechain) | Side-chain plugin: /side persistent side-session + /btw one-shot side question. / 侧会话插件：/side 持续性侧会话 + /btw 一次性侧问。 |
| ⭐ 3 | [jiesou/dsh-stream-rules](https://github.com/jiesou/dsh-stream-rules) | Inject rules when needed, without wasting context. / 流规则注入，按需生效不浪费上下文。 |
| ⭐ 5 | [fakechris/dsh-track](https://github.com/fakechris/dsh-track) | Embedded task management engine: decision-point protocol, thought capture wall, Linear-style issues. / 嵌入式任务管理引擎：决策点协议、念头捕获墙、Linear 形 issue。 |
| ⭐ 2 | [BlockRunAI/dsh-clawrouter](https://github.com/BlockRunAI/dsh-clawrouter) | A second brain for your DSH agent — strong-model review before risky tool calls, plus 70 models from one wallet. / DSH Agent 第二大脑：高风险工具调用前强模型审核，单钱包接入 70 个模型。 |
| ⭐ 2 | [openma-ai/deepseek-harness-acp](https://github.com/openma-ai/deepseek-harness-acp) | ACP server implementation for DeepSeek Harness. / ACP server 实现。 |
| ⭐ 2 | [Karbo123/DSH-EvoResearch](https://github.com/Karbo123/DSH-EvoResearch) | Self-evolving research workflow for DeepSeek Harness — autonomous literature search, hypothesis generation, and experiment tracking. / DSH 自进化科研工作流：自主文献检索、假设生成与实验追踪。 |
| ⭐ 4 | [ZK-Andy/dsh-continual-evolve](https://github.com/ZK-Andy/dsh-continual-evolve) | Continual self-evolution plugin for DeepSeek Harness: versioned, auditable, rollback-safe harness state refined from session trajectories, with benchmark-driven validation loop. / DSH 持续自进化插件：版本化可审计的 harness 状态，从会话轨迹中优化，带基准驱动的验证循环。 |
| ⭐ 1 | [yoke233/dsh-prime-agent](https://github.com/yoke233/dsh-prime-agent) | Prime Agent-inspired persistent RLM control plane for DSH Code Mode. / Prime Agent 风格持久化 RLM 控制面。 |
| ⭐ 1 | [Tieboyh/dsh-session-search](https://github.com/Tieboyh/dsh-session-search) | Index-free cross-agent session search for DeepSeek Harness. / 免索引跨 Agent 会话搜索。 |
| ⭐ 1 | [dongsheng123132/task-passport](https://github.com/dongsheng123132/task-passport) | Open task handoff protocol: verified state, not chat logs. / 开放任务交接协议（Verified State，非聊天日志）。 |
| ⭐ 1 | [wulun811/LiuHe](https://github.com/wulun811/LiuHe) | LLM-native code toolkit: tree-sitter + 44 MCP tools for atomic editing, impact analysis, reference tracing. / LLM-native 代码工具包：tree-sitter + 44 MCP 原子编辑工具。 |
| ⭐ 1 | [LoserFox/distill](https://github.com/LoserFox/distill) | Auto conversation distillation: background subagent reflection + skill create/update. / 自动对话蒸馏：后台 subagent 反省 + 技能 create/update。 |
| ⭐ 1 | [ConradLu2740/pa-dsh](https://github.com/ConradLu2740/pa-dsh) | ProactiveAgent × DeepSeek Harness plugin set: proactive memory + proactive suggestions. / 主动记忆 + 主动建议插件组。 |
| ⭐ 1 | [dongsheng123132/dshx](https://github.com/dongsheng123132/dshx) | Machine-friendly DeepSeek Harness adapter with cwd, stdin, timeout, stable JSON. / 机器友好的 DSH 适配器。 |
| ⭐ 1 | [TideSparrow/computer-use-dsh](https://github.com/TideSparrow/computer-use-dsh) | Codex-style computer use plugin for DeepSeek Harness: screenshot, click, type, scroll. / Codex 风格电脑操控插件。 |
| ⭐ 6 | [humblebanana/dsh-record-replay](https://github.com/humblebanana/dsh-record-replay) | Record macOS desktop workflows by demonstration and turn them into agent skills (open-record-replay skill + orr_* tools). / 通过演示录制 macOS 桌面工作流，转化为 agent 技能。 |
| ⭐ 5 | [KirschBluteX/engineer-software](https://github.com/KirschBluteX/engineer-software) | Runtime-neutral, evidence-driven software engineering workflow for Codex and DeepSeek Harness. / 运行时中立的证据驱动软件工程工作流，支持 Codex 与 DSH。 |
| ⭐ 1 | [fangweixuan26-hash/dsh-a2a-agent](https://github.com/fangweixuan26-hash/dsh-a2a-agent) | Expose a DeepSeek Harness agent over the Agent2Agent (A2A) protocol: agent card, JSON-RPC, LLM replies. / 将 DSH Agent 暴露为 A2A 协议服务：agent card、JSON-RPC、LLM 回复。 |
| ⭐ 8 | [cosyncing/cosyncing](https://github.com/cosyncing/cosyncing) | Synchronize and orchestrate agents from CLI to GUI, across desktop to phone. / 跨桌面到手机同步编排 Agent：CLI 到 GUI 的 Agent 协同。 |
| ⭐ 0 | [CriscolTheCoder/dsh-workflow-groups](https://github.com/CriscolTheCoder/dsh-workflow-groups) | Workflow groups kanban: each grouped workflow gets an independent tab showing status/stage/subagent/logs in real time. / 分组工作流看板：每个分组 workflow 独立标签页实时展示状态/阶段/子 agent/日志。 |
| ⭐ 0 | [lisycotana/dsh-workflow-worktree](https://github.com/lisycotana/dsh-workflow-worktree) | Git worktree isolation backend for DSH workflows — implements registerIsolationAdapter() seam. / DSH 工作流 Git worktree 隔离后端。 |
| ⭐ 2 | [MiloMMIN/dsh-agent-board](https://github.com/MiloMMIN/dsh-agent-board) | Cross-Agent workspace: watches Claude Code / Codex / Kimi Code / Pi / Hermes and continues their work with one click. / 跨 Agent 工作台：监控其他 Agent 并在 DSH 中一键接续工作。 |
| ⭐ 1 | [forrestsweet/dsh-agent-replay](https://github.com/forrestsweet/dsh-agent-replay) | Session replay and redacted-share plugin: export real agent trajectories as standalone interactive HTML for docs, demos, and feedback. / DSH 会话回放与脱敏分享：导出 Agent 轨迹为独立交互 HTML。 |

---

## 🎨 Skins & Desktop Pets / 皮肤与桌宠

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 552 | [Small-tailqwq/dsh-deep-whale](https://github.com/Small-tailqwq/dsh-deep-whale) | Whale girl skin series (Deep Sea Maid Atelier), CC BY-NC-SA 4.0. / 鲸鱼娘皮肤系列（深海女仆工坊），CC BY-NC-SA 4.0。 |
| ⭐ 120 | [vlln/whale-girl](https://github.com/vlln/whale-girl) | Desktop pet (QQ pet style): draggable/feeding/playing, accumulation-type companion. / 桌面宠物插件（QQ 宠物形态）：拖拽/投喂/玩耍，积累型伙伴。 |
| ⭐ 17 | [lhh010/dsh-ui-whale](https://github.com/lhh010/dsh-ui-whale) | Hand-drawn pixel whale companion: blinking, tail-waving, water-spouting, heart-bubbles, sleeping. / 全手绘像素鲸鱼伙伴：眨眼/摆尾/喷水/冒爱心/睡觉。 |
| ⭐ 86 | [Nagi-ovo/dsh-visualize](https://github.com/Nagi-ovo/dsh-visualize) | In-chat generative UI: interactive HTML cards streamed into conversation, whale-blue theme. / 对话内生成式 UI：交互式 HTML 卡片流式渲染，鲸鱼蓝主题跟随。 |
| ⭐ 353 | [Nagi-ovo/dsh-ads](https://github.com/Nagi-ovo/dsh-ads) | 2005-style Chinese web sidebar ads / in-chat info stream / corner popups (fictional assets). / 2005 年中文站点风格侧栏广告 / 角落弹窗（虚构素材）。 |
| ⭐ 7 | [HuanLinOTO/dsh-plugin-pet-rs](https://github.com/HuanLinOTO/dsh-plugin-pet-rs) | DSH desktop pet (Rust): 5-state whale + dual SSE real-time push + transparent always-on-top + tray. / DSH 桌宠 Rust 版：5 态鲸鱼 + SSE 推送 + 透明置顶窗 + 系统托盘。 |
| ⭐ 21 | [alingalingling/ui-status-label](https://github.com/alingalingling/ui-status-label) | Customize the "deep diving…" status text to anything you want. / 自定义 deep diving 状态文字。 |
| ⭐ 4 | [01Virex/dsh-status-rotator](https://github.com/01Virex/dsh-status-rotator) | Rainbow gradient typewriter-animated status phrases, configurable from JSON. / 彩虹渐变打字机动画状态文字，JSON 配置。 |
| ⭐ 4 | [lhh010/dsh-ui-progress](https://github.com/lhh010/dsh-ui-progress) | Session progress bar: todos real progress / token rate / interrupt orange state. / 会话进度条：todos 真实进度 / token 速率 / 中断橘红态。 |
| ⭐ 4 | [vlln/dsh-navbar](https://github.com/vlln/dsh-navbar) | Conversation node navbar: quick-jump to user messages from right edge. / 对话节点导航条：右缘节点串快速跳转 user 消息。 |
| ⭐ 4 | [vlln/dsh-task-status](https://github.com/vlln/dsh-task-status) | Background task status bar: task progress + real-time output tail. / 后台任务状态条：任务进度 + 实时输出 tail。 |
| ⭐ 3 | [LaplaceYoung/dsh-qq2006](https://github.com/LaplaceYoung/dsh-qq2006) | QQ2006 skin plugin: register qq2006 theme, mirror body[data-ds-skin], global skin table. / QQ2006 皮肤插件：注册主题、镜像 body、全局皮肤表。 |
| ⭐ 3 | [147228/dsh-xiaoyao-skins](https://github.com/147228/dsh-xiaoyao-skins) | XiXiaoYao × DSH Web skin collection + installer + community creation toolkit. / 夕小瑶 × DSH Web 皮肤合集 + 安装器。 |
| ⭐ 3 | [Small-tailqwq/dsh-deepcel](https://github.com/Small-tailqwq/dsh-deepcel) | Excel-inspired DSH skin. / 模仿 Excel 的 DSH 皮肤。 |
| ⭐ 2 | [Vim0x3c/dsh-skin-appearance](https://github.com/Vim0x3c/dsh-skin-appearance) | DSH appearance customization: 8 built-in themes + custom wallpaper (transparency/blur), host settings persistence. / DSH 外观定制插件：八套内置主题 + 自定义壁纸（透明度/模糊），Host 设置持久化。 |
| ⭐ 1 | [lssyd20070106/dsh-ui-preset-enhance](https://github.com/lssyd20070106/dsh-ui-preset-enhance) | Third-party DSH WebUI enhancement: custom backgrounds, theme colors, prompt presets, token/context visibility, and manual compaction. / 第三方 DSH WebUI 增强插件：自定义背景、主题色、提示词预设、token/上下文可见性与手动压缩。 |
| ⭐ 2 | [LilycleHeart/liuli-theme](https://github.com/LilycleHeart/liuli-theme) | Liuli (琉璃) theme for DeepSeek Harness — translucent glass-morphism style with harmony color palette. / 琉璃主题：DSH 半透明玻璃态风格，配色和谐。 |
| ⭐ 3 | [gameswu/dsh-plugin-background](https://github.com/gameswu/dsh-plugin-background) | DSH wallpaper plugin. / DSH 壁纸插件。 |
| ⭐ 1 | [stushansusu/dsh-miku-skin](https://github.com/stushansusu/dsh-miku-skin) | Hatsune Miku theme: blue-purple magenta gradient, frosted glass panels, dual light/dark themes. / 初音未来主题皮肤：蓝紫洋红渐变、毛玻璃面板、亮暗双主题。 |
| ⭐ 1 | [yuxino/dsh-blue-whale-maid](https://github.com/yuxino/dsh-blue-whale-maid) | Blue whale maid: task-completion reminder for DSH web. / 蓝鲸女仆：任务完成提醒器。 |
| ⭐ 2 | [f0909172434/dsh-deepseek-girl-pet](https://github.com/f0909172434/dsh-deepseek-girl-pet) | Animated deepseek girl desktop pet plugin for DeepSeek Harness. / 动画深Seek女孩桌宠插件。 |
| ⭐ 2 | [YLifeOnlyOnce/dsh-dynamic-island](https://github.com/YLifeOnlyOnce/dsh-dynamic-island) | Tiny liquid-glass companion for DSH — breathes while agent thinks, pulses while working, politely asks before touching anything. / DSH 的小玻璃伙伴：思考时呼吸，工作时脉动，行动前礼貌询问。 |
| ⭐ 1 | [xiaoshihou514/dsh-desktop-pet](https://github.com/xiaoshihou514/dsh-desktop-pet) | DeepSeek Harness: whale girl desktop pet! / 鲸鱼娘桌宠！ |
| ⭐ 1 | [minybear/DeepSeek-Harness-Pet](https://github.com/minybear/DeepSeek-Harness-Pet) | Codex-style desktop pet plugin for DeepSeek Harness. / Codex 风格桌宠插件。 |
| ⭐ 1 | [pineapple880066/dsh-webUI-pets](https://github.com/pineapple880066/dsh-webUI-pets) | Codex-style desktop pets for the DeepSeek Harness Web UI. / Codex 风格 Web UI 桌宠。 |
| ⭐ 1 | [zealot00/dsh-pet](https://github.com/zealot00/dsh-pet) | Desktop pet for DeepSeek Harness Web UI: sprite animation, agent state linkage, drag, alarm & pomodo. / DSH Web UI 桌宠：精灵动画、状态联动、拖拽、闹钟和番茄钟。 |
| ⭐ 1 | [zealot00/dsh-pet-zhuangfangyi](https://github.com/zealot00/dsh-pet-zhuangfangyi) | DeepSeek Harness WebUI desktop pet plugin (chibi pet with idle animation & click speech). / WebUI 桌宠插件（Q版宠物，待机动画 + 点击说话）。 |
| ⭐ 1 | [brittanistrehlowll-oss/dsh-pet-shura](https://github.com/brittanistrehlowll-oss/dsh-pet-shura) | 修罗小脑斧 — animated desktop pet for the DeepSeek Harness web surface: v2 spritesheet animation. / 修罗小脑斧——DSH Web 动画桌宠，v2 精灵表动画。 |
| ⭐ 14 | [dancingmemory/dskin](https://github.com/dancingmemory/dskin) | DSKIN · DSH cartoon pixel skin plugin — walking, blinking pixel pets; original UI untouched. / DSH 卡通像素皮肤插件：散步眨眼像素宠物，不改动原始界面。 |
| ⭐ 4 | [LAN-TINA-WS/dsh-gui-customization](https://github.com/LAN-TINA-WS/dsh-gui-customization) | DSH fashion workshop: Nous blue palette, ambient glow, background image presets (CN+EN). / DSH 时装工坊：Nous 蓝配色/氛围光/背景图预设。 |
| ⭐ 3 | [leavestring/awesome-dsh-background-plugin](https://github.com/leavestring/awesome-dsh-background-plugin) | DSH Web background personalization: upload custom images (auto-compressed to 1600px) or one-click switch aurora/ember/rice-paper presets with live preview. / DSH Web 背景个性化插件：上传自定义图片（浏览器端自动压缩至1600px以内）或一键切换极光/余烬/宣纸三种预设，实时预览。 |
| ⭐ 2 | [xuhurdern-beep/dsh-live-reload](https://github.com/xuhurdern-beep/dsh-live-reload) | One-click hot reload of running DSH plugin composition — restart-free plugin refresh. / 一键热重载运行中的 DSH 插件组合，无需重启。 |

---

## 🔔 Notifications & Status / 通知与状态

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 2 | [Haytham818/dsh-notify](https://github.com/haytham818/dsh-notify) | DSH system notification: task done, errors, questions, approval wait. / DSH 系统通知插件：任务完成/错误/提问/等待审批。 |
| ⭐ 1 | [ShanFeng2046/deepseek-harness-notification](https://github.com/ShanFeng2046/deepseek-harness-notification) | Auto bell + macOS banner notification on reply completion. / 回答完成自动响铃 + macOS 横幅通知。 |
| ⭐ 1 | [Luaphes/dsh-web-attention-badge](https://github.com/Luaphes/dsh-web-attention-badge) | Attention reminders for DeepSeek Harness Web UI: frame badge, (N) tab title, whale favicon. / DSH Web UI 注意力提醒：帧徽章、(N) 标签页标题、鲸鱼 favicon。 |
| ⭐ 1 | [rizkirmdhnnn/dsh-tool-notify](https://github.com/rizkirmdhnnn/dsh-tool-notify) | DSH plugin: model-facing notify tool — send notifications to ntfy or generic webhooks. / DSH 通知工具：向 ntfy 或通用 Webhook 发送通知。 |
| ⭐ 1 | [yeshimei/dsh-sound](https://github.com/yeshimei/dsh-sound) | Distinct alert sounds for DeepSeek Harness: network error, approval request, question asked. / DSH 区分警报声音：网络错误、审批请求、提问。 |
| ⭐ 1 | [kiim-wong/dsh-push](https://github.com/kiim-wong/dsh-push) | Push DeepSeek Harness agent lifecycle notifications to configurable channels. / 将 DSH Agent 生命周期通知推送到可配置渠道。 |
| ⭐ 1 | [1514100951/dsh-notify-plugins](https://github.com/1514100951/dsh-notify-plugins) | DeepSeek Harness desktop notification plugins: browser + native Windows toasts on task finish/error. / DSH 桌面通知插件：浏览器 + Windows 原生 toast。 |
| ⭐ 1 | [Caxson/dsh-plugin-browser-notify](https://github.com/Caxson/dsh-plugin-browser-notify) | DeepSeek Harness web notify plugin. / DSH Web 通知插件。 |
| ⭐ 0 | [c-ling/dsh-plugin-notify](https://github.com/c-ling/dsh-plugin-notify) | DSH message reminder plugin: sends notifications to browser/system/Feishu/DingTalk/WeChat Work/generic webhook on turn end or approval wait. / DSH 消息提醒：回合结束或等待确认时推送至浏览器/系统/飞书/钉钉/企微/Webhook。 |
| ⭐ 1 | [ly6170/dsh-messager](https://github.com/ly6170/dsh-messager) | DeepSeek Harness message reminder messenger: supports third-party channels (currently Feishu webhook). / DSH 消息提醒信使，支持飞书 webhook 等第三方通道。 |
| ⭐ 4 | [pitetow/dsh-notify-on-complete](https://github.com/pitetow/dsh-notify-on-complete) | Desktop notification plugin for DeepSeek Harness — alerts when a run ends. / DSH 桌面通知插件：任务结束时发出提醒。 |
| ⭐ 0 | [THEWOLFWALKER/dsh-notifier](https://github.com/THEWOLFWALKER/dsh-notifier) | Unified notification push for DSH: one notify() API, 8 channel adapters (Telegram/DingTalk/Feishu/wxpusher/PushPlus/ServerChan/Bark/Webhook), dual trigger (session events + agent tools). / DSH 统一通知推送：一个 notify() API 对接 8 个渠道（Telegram/钉钉/飞书/wxpusher/PushPlus/ServerChan/Bark/Webhook），双触发（会话事件 + Agent 工具）。 |
| ⭐ 2 | [halosb/dsh-workmate](https://github.com/halosb/dsh-workmate) | DSH work companion: task-completion notifications (Toast/Webhook) + private knowledge base search. / DSH 工作搭档：长任务完成通知（Toast/Webhook）+ 私有知识库检索。 |
| ⭐ 2 | [Moximxxx/dsh-find-skill](https://github.com/Moximxxx/dsh-find-skill) | DSH plugin bridging the vercel-labs/skills ecosystem: LLM-driven skill search, install, and lifecycle for temp/project/glob scopes. / DSH 技能发现插件：桥接 vercel-labs/skills 生态，LLM 驱动的 skill 搜索/安装/生命周期管理。 |
| ⭐ 3 | [xxxxxxxyu/dsh-notify-sound](https://github.com/xxxxxxxyu/dsh-notify-sound) | Plays a sound when the agent finishes replying — sound, volume and on/off configurable in Settings. / Agent 回复结束时播放提示音，可在设置中调节音量与开关。 |
| ⭐ 2 | [yangyongzhen/dsh-notify](https://github.com/yangyongzhen/dsh-notify) | Task-completion notifications via ServerChan / DingTalk / Feishu / generic webhooks. / 任务完成通知：支持 ServerChan/钉钉/飞书/通用 Webhook。 |

---

## 📊 Data & Finance / 数据与金融

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 6 | [AnacondaKC/dsh-stock-market](https://github.com/AnacondaKC/dsh-stock-market) | Stock market analysis plugin. / 股票市场分析插件。 |
| ⭐ 8 | [HuanLinOTO/dsh-plugin-mineru](https://github.com/HuanLinOTO/dsh-plugin-mineru) | MinerU document parsing: PDF/images/DOCX/PPTX/XLSX → structured Markdown/JSON. / MinerU 文档解析：PDF/图片/DOCX/PPTX/XLSX → Markdown/JSON。 |
| ⭐ 4 | [Han-1413141/dsh-cost-meter](https://github.com/Han-1413141/dsh-cost-meter) | Session cost stats: current session, daily, history synced with official pricing. / 会话费用统计：本会话费用、当日费用、历史记录与官方价格同步。 |
| ⭐ 3 | [Degurechaff57/dsh-openapi](https://github.com/Degurechaff57/dsh-openapi) | Safe OpenAPI 3.x discovery and API calling tools for DeepSeek Harness. / OpenAPI 3.x 发现与 API 调用安全工具。 |
| ⭐ 3 | [Fisfzy/zotero-harvest](https://github.com/Fisfzy/zotero-harvest) | Zotero literature harvesting: multi-source search + OA download + local import. / Zotero 文献采集：多源检索 + OA 下载 + 本地入库。 |
| ⭐ 2 | [lordqyxz/dsh-ark-quota](https://github.com/lordqyxz/dsh-ark-quota) | Volcano Ark subscription remaining quota sidebar widget. / 火山方舟订阅套餐剩余额度 DSH 侧边栏组件。 |
| ⭐ 2 | [renat3u/tonghuashun-webui](https://github.com/renat3u/tonghuashun-webui) | Tonghuashun-style WebUI plugin. / 仿同花顺的 WebUI 插件。 |
| ⭐ 1 | [AdamPlatin123/dsh-tonghuashun](https://github.com/AdamPlatin123/dsh-tonghuashun) | Tonghuashun terminal-style skin + code-volume K-line market panel. / 同花顺行情终端风格皮肤 + 代码量 K 线行情面板。 |
| ⭐ 1 | [Blaczz/dsh-sci](https://github.com/Blaczz/dsh-sci) | Zero-dependency scientific computing tools for DeepSeek Harness: physical-unit conversion, CODATA constants, Runge-Kutta ODE simulation. No core changes. / 零依赖科学计算工具：物理单位换算、CODATA 常量、Runge-Kutta ODE 仿真，无需修改核心。 |
| ⭐ 1 | [Alyosha28/deep_option](https://github.com/Alyosha28/deep_option) | Hong Kong/US stock options research and risk agent. / 港美股期权研究与风险 Agent。 |
| ⭐ 1 | [lin-cheng-lab/dsh-deepseek-balance](https://github.com/lin-cheng-lab/dsh-deepseek-balance) | DeepSeek API balance monitor: floating badge + 7-day/30-day usage charts. / DeepSeek API 余额监视器：右下角悬浮徽章 + 7天/30天费用图表。 |
| ⭐ 1 | [hashdiana/dsh-token-usage](https://github.com/hashdiana/dsh-token-usage) | Token usage tracking. / Token 用量追踪。 |
| ⭐ 1 | [Ghost011118/dsh-balance-meter](https://github.com/Ghost011118/dsh-balance-meter) | DeepSeek account balance and session cost readout. / DeepSeek 账户余额和会话费用读取。 |
| ⭐ 1 | [jelly-000/dsh-balance-monitor](https://github.com/jelly-000/dsh-balance-monitor) | DeepSeek balance, remaining-ratio bar and today's spend in the sidebar footer. / DeepSeek 账户余额、剩余比例条与今日花费侧边栏。 |
| ⭐ 1 | [TwotwoPiggy/dsh-balance](https://github.com/TwotwoPiggy/dsh-balance) | Real-time token tracking + accurate session cost estimation with peak/off-peak pricing. / 实时 token 追踪 + 精确会话费用估算（支持峰谷定价）。 |
| ⭐ 4 | [TheTianzz/dsh-billing](https://github.com/TheTianzz/dsh-billing) | Account balance + session cost: /balance /cost commands, deepseek_billing tool, Web UI dual capsule, official pricing sync every 12h. / 账户余额 + 会话费用：/balance /cost 命令、deepseek_billing 工具、Web UI 双胶囊，官方价格每 12 小时自动同步。 |
| ⭐ 2 | [x2802490130-prog/dsh-balance-float](https://github.com/x2802490130-prog/dsh-balance-float) | Floating balance widget for DSH Web — persistent bottom-right display of account balance with one-click logout. / DSH 悬浮余额插件：右下角常驻显示余额 + 一键退出。 |
| ⭐ 1 | [Liu-ty/dsh-balance-display](https://github.com/Liu-ty/dsh-balance-display) | DeepSeek API balance overlay for DeepSeek Harness. / DeepSeek API 余额叠加层。 |
| ⭐ 2 | [juhe291/dsh-token-panel](https://github.com/juhe291/dsh-token-panel) | Real-time token consumption HUD: live usage monitor, context pressure, cost estimation, trend curves, daily/monthly stats. / 实时 Token 消耗监控插件：用量统计、成本估算、趋势曲线、按日按月报表。 |
| ⭐ 3 | [Smalldy/godot-bridge](https://github.com/Smalldy/godot-bridge) | DSH plugin that launches and drives a running Godot 4.x game through it — agent-controlled game automation. / DSH 与 Godot 4.x 游戏桥接：通过 DSH Agent 启动并控制运行中的 Godot 游戏。 |
| ⭐ 2 | [LemCAE/dsh-balance](https://github.com/LemCAE/dsh-balance) | Account balance + session cost estimation for DeepSeek Harness. / DSH 账户余额与会话费用估算插件。 |
| ⭐ 1 | [ArcanePivot/dsh-api-balance](https://github.com/ArcanePivot/dsh-api-balance) | DeepSeek API balance widget for DSH Web UI — view balance from the host side. / DSH Web UI API 余额组件：从主机侧查看 DeepSeek API 余额。 |
| ⭐ 3 | [liustack/pptfast](https://github.com/liustack/pptfast) | Stable, editable PPTX generation for AI agents — semantic IR in, native DrawingML out. / 稳定的 AI Agent PPTX 生成：语义 IR 输入，原生 DrawingML 输出。 |

---

## 🎮 Entertainment / 娱乐与趣味

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 8 | [hellodigua/dsh-emoji](https://github.com/hellodigua/dsh-emoji) | Auto-add emoji to AI replies. / AI 回复自动添加表情。 |
| ⭐ 7 | [lhh010/dsh-minigames](https://github.com/lhh010/dsh-minigames) | 18 offline mini-games: Dino jump, Tetris, Tank, Minesweeper, 2048, Sudoku, Pac-Man. / 18 款离线小游戏：恐龙跳一跳/俄罗斯方块/坦克大战/扫雷/2048/数独/吃豆人。 |
| ⭐ 7 | [omdsh-dev/dsh-gomoku](https://github.com/omdsh-dev/dsh-gomoku) | Play Gomoku with AI, or let two AIs battle each other. / 与 AI 下五子棋，也可让 AI 对局。 |
| ⭐ 4 | [SenmuuuuW/dsh-whale-report](https://github.com/SenmuuuuW/dsh-whale-report) | 🐋 Whale notebook — your Agent's annual report: daily/weekly/monthly/yearly summaries from session event logs, any time range, read-only. / 鲸鱼记事本：从会话事件日志生成日报/周报/月报/年报，任意区间、只读不改写。 |
| ⭐ 14 | [SenmuuuuW/dsh-group-photo](https://github.com/SenmuuuuW/dsh-group-photo) | DSH beta closing group photo wall: GitHub OAuth polaroid photo station. / DSH 内测收官合影墙：GitHub OAuth 拍立得合影站。 |
| ⭐ 24 | [c3ll256/dsh-toy](https://github.com/c3ll256/dsh-toy) | Toy Control Protocol for DSH — toy-based event hooks and playful agent interaction patterns. / DSH 玩具控制协议：玩具式事件钩子和趣味 Agent 交互模式。 |
| ⭐ 3 | [hellosky983/dsh-mc-launcher](https://github.com/hellosky983/dsh-mc-launcher) | Minecraft launcher built on DeepSeek Harness: full-screen UI, version download, Microsoft device-code login, game launch from DSH host process. / 基于 DSH 的 Minecraft 启动器：全屏 UI、版本下载、微软设备码登录。 |
| ⭐ 1 | [JasonJin2006/dsh-sound-effects-plugin](https://github.com/JasonJin2006/dsh-sound-effects-plugin) | Reasonix-style sound effects: generative pentatonic ambient music + success/attention chimes. / Reasonix 风格音效：生成五声音阶环境音乐 + 成功/注意力提示音。 |
| ⭐ 4 | [HuanLinOTO/dsh-plugin-d399](https://github.com/HuanLinOTO/dsh-plugin-d399) | Mini-game menu popup while model generates (Wordle/Match-3/192 parametric games). / 模型生成时右下角弹出小游戏菜单（Wordle/消消乐/192 款参数化小游戏）。 |
| ⭐ 1 | [HuanLinOTO/dsh-plugin-auto-blame](https://github.com/HuanLinOTO/dsh-plugin-auto-blame) | LLM generates 3 critical follow-up suggestions after each turn, click-to-send chips. / 回合结束后 LLM 生成 3 条批判性跟进建议，点击即发送。 |
| ⭐ 1 | [HuanLinOTO/dsh-plugin-anti-ads](https://github.com/HuanLinOTO/dsh-plugin-anti-ads) | DSH Web ad blocker with four independent defense layers targeting dsh-ads plugin. / DSH Web 广告拦截器：四层独立防御拦截 dsh-ads 插件的所有广告位。 |
| ⭐ 1 | [HuanLinOTO/dsh-plugin-aigc-canvas](https://github.com/HuanLinOTO/dsh-plugin-aigc-canvas) | Provider-agnostic AIGC HTTP bridge + infinite canvas + ffmpeg post-processing, 13 tools. / Provider-agnostic AIGC HTTP 桥 + 无限画布 + ffmpeg 后处理，13 个工具。 |
| ⭐ 1 | [HuanLinOTO/dsh-plugin-spur](https://github.com/HuanLinOTO/dsh-plugin-spur) | Hanging whip in chat stream; flick tip (>2.0 px/ms) to send agent a "go work!" message. / 聊天流中悬挂皮鞭：甩动鞭梢（>2.0 px/ms）向 agent 发送 go work 消息。 |
| ⭐ 1 | [yoke233/dsh-pixel-whale](https://github.com/yoke233/dsh-pixel-whale) | Lively pixel-whale running-state companion for DSH Web. / 活体像素鲸鱼运行状态伙伴。 |
| ⭐ 1 | [fff1122/dsh-agent-arcade](https://github.com/fff1122/dsh-agent-arcade) | Deterministic Agent-played Snake game for DeepSeek Harness. / DSH 确定性 Agent 蛇棋游戏。 |
| ⭐ 1 | [skeleton9/deepseek-harness-mario](https://github.com/skeleton9/deepseek-harness-mario) | HTML Mario Game by DeepSeek Harness. / DSH HTML 马里奥游戏。 |
| ⭐ 1 | [xuhaiL/game-ceanter](https://github.com/xuhaiL/game-ceanter) | Mini-games made with DeepSeek Harness. / 使用 DSH 制作的小游戏。 |
| ⭐ 3 | [JuneLearn/dsh-image2-draw](https://github.com/JuneLearn/dsh-image2-draw) | DeepSeek Harness Image2 image generation plugin — call gpt-image-2 via OpenAI-compatible interface with custom baseURL and API Key. / DSH Image2 生图插件：通过第三方 OpenAI Images 兼容接口调用 gpt-image-2，配置 baseURL 和 API Key 即可。 |
| ⭐ 1 | [ylwl1997/dshbase](https://github.com/ylwl1997/dshbase) | DSH base: guides and plugin ecosystem index for DeepSeek Harness. / DSH 基础指南与插件生态索引。 |


---

## 📚 Tutorials & Guides / 教程与手册

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 170 | [Electricitysheep/dsh-handbook](https://github.com/Electricitysheep/dsh-handbook) | DSH from 0 to 1 deep handbook: install/plugin dev/performance tuning/case studies (CN+EN PDF). / DSH 从 0 到 1 深度手册：安装/插件开发/性能调优/实测案例（中英 PDF）。 |
| ⭐ 18 | [yanhua1010/dsh-harness-tutorial](https://github.com/yanhua1010/dsh-harness-tutorial) | Agent principles tutorial: VitePress site + 8 demos + mini-harness teaching project. / Agent 原理实现教程：VitePress 站点 + 8 个 Demo + mini-harness 教学项目。 |
| ⭐ 40 | [pingfanfan/hello-dsh](https://github.com/pingfanfan/hello-dsh) | Zero-to-plugin tutorial with 22 Chinese skill examples. / 零基础插件开发教程（含 22 个中文技能实例）。 |
| ⭐ 4 | [omdsh-dev/dsh-plugin-dev](https://github.com/omdsh-dev/dsh-plugin-dev) | Plugin development pitfall archive: cordis dual-copy, tsconfig trio, Windows junction. / 插件开发踩坑档案：cordis 双副本、tsconfig 三件套、Windows junction。 |
| ⭐ 65 | [hikariming/dshfind](https://github.com/hikariming/dshfind) | DSH principles, plugin marketplace & best practices. / DSH 原理学习、插件市场与最佳实践。 |
| ⭐ 16 | [whyihaveyou/dsh-suite](https://github.com/whyihaveyou/dsh-suite) | Bilingual curated plugin directory with daily compatibility CI. / 双语精选插件目录，每日兼容 CI。 |
| ⭐ 3 | [lwmxiaobei/dsh-plugins](https://github.com/lwmxiaobei/dsh-plugins) | DSH plugin navigation and introduction directory. / DSH 插件导航与介绍目录。 |
| ⭐ 3 | [Siberia-yuan/deepseek-harness-human-guide](https://github.com/Siberia-yuan/deepseek-harness-human-guide) | Plain-language bilingual DSH & Cordis guide: write your first plugin in 30 minutes. / 大白话双语 DSH & Cordis 指南：30 分钟从零写第一个插件。 |
| ⭐ 2 | [hoco-scy/deepseek-harness-deep-dive](https://github.com/hoco-scy/deepseek-harness-deep-dive) | Source-pinned, bilingual systems dissection of DeepSeek Harness — 36 chapters, 1,094 evidence records. / DeepSeek Harness 源码级双语系统解析——36 章，1,094 条证据记录。 |
| ⭐ 1 | [flysheep-ai/learn_deepseek_harness](https://github.com/flysheep-ai/learn_deepseek_harness) | Runnable, progressive course on deepseek harness internals — 18 chapters from a 60-line agent loop. / 可运行的渐进式 DSH 内部教程：18 章，从 60 行 agent loop 开始。 |

---

## 🔌 Infrastructure / 基础设施

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 1 | [CloudyMountain/dsh-path-guard](https://github.com/CloudyMountain/dsh-path-guard) | Path guard plugin for DSH: deny agent tool access to configured sensitive paths, layered filesystem protection. / DSH 路径守护插件：阻止 agent 工具访问配置的敏感路径，分层文件系统保护。 |
| ⭐ 2 | [cdxiaodong/dsh-guardian](https://github.com/cdxiaodong/dsh-guardian) | DSH guardian plugin: automated safety monitoring and intervention for agent operations — intercept risky tool calls. / DSH 守护者插件：自动化安全监控与 agent 操作干预，拦截高风险工具调用。 |
| ⭐ 1 | [LeslieWylie/dsh-fleet-audit](https://github.com/LeslieWylie/dsh-fleet-audit) | Agent fleet hygiene audit for DSH: credential-file permissions, embedded git-token leak detection, security posture checks. / DSH Agent 舰队卫生审计：凭证文件权限检查、嵌入 git token 泄漏检测、安全态势评估。 |
| ⭐ 0 | [runseal-labs/dsh-tool-runseal](https://github.com/runseal-labs/dsh-tool-runseal) | RunSeal sandbox plugin for DSH: OS-native policy execution boundary for untrusted code (Windows/macOS/Linux). / DSH RunSeal 沙盒插件：为 dsh 提供 OS 原生策略执行边界（Windows/macOS/Linux）。 |
| ⭐ 1 | [LouisHaoL/dsh-homerail-dag](https://github.com/LouisHaoL/dsh-homerail-dag) | HomeRail-style DAG orchestration plugin for DSH: YAML-defined workflows with detection triggers and state machines. / DSH HomeRail 风格 DAG 编排插件：YAML 定义工作流+检测触发+状态机。 |
| ⭐ 1 | [LeemanCheung/dsh-task-dag](https://github.com/LeemanCheung/dsh-task-dag) | Persistent live DAG visualization for DeepSeek Harness subagents and workflows — real-time task dependency graph. / DSH 持久化实时 DAG 可视化：子 agent 与工作流依赖关系实时流转图。 |
| ⭐ 1 | [libaie/onboard-dsh-projects](https://github.com/libaie/onboard-dsh-projects) | Multi-repo workflow isolation skill for DSH — one isolated entry agent per repository with independent context. / DSH 多仓库工作流隔离技能：每个仓库一个独立隔离入口 agent，上下文互不干扰。 |
| ⭐ 3.9k | [Devin-AXIS/iPolloWork](https://github.com/Devin-AXIS/iPolloWork) | Full-featured AI workspace integrating DeepSeek Harness for subagent delegation, dual-ecosystem. / 全功能 AI 工作台 + DSH subagent 委托，双生态整合。 |
| ⭐ 679 | [hellowind777/helloagents](https://github.com/hellowind777/helloagents) | Self-evolving autonomous agent partner that analyzes problems and keeps working until implementation and verification are complete. / 自主高级智能伙伴：不仅分析问题，更持续工作直至完成实现与验证。 |
| ⭐ 561 | [nutshellai-tech/mobius](https://github.com/nutshellai-tech/mobius) | First self-evolving open-source Agent OS — connects your team, AI agents, devices, and compute into one unified system. / 首个自进化开源 Agent OS：连接团队、AI Agent、设备与算力。 |
| ⭐ 275 | [cofy-x/axern](https://github.com/cofy-x/axern) | Open-source sandboxes for AI agents, untrusted code execution, and durable services. / 开源沙箱：AI Agent 不可信代码执行 + 持久化服务。 |
| ⭐ 163 | [hust-open-atom-club/oh-dsh](https://github.com/hust-open-atom-club/oh-dsh) | One-stop community distro: TUI + desktop + Web UI three-form unified experience. / 一站式社区发行版：TUI + 桌面 + Web UI 三种形态统一。 |
| ⭐ 51 | [OBdangshang07/DSH_Creative_Workshop](https://github.com/OBdangshang07/DSH_Creative_Workshop) | Steam Workshop-inspired plugin discovery, trust graph, collections, and transactional installation planning for DeepSeek Harness plugins. / Steam Workshop 风格插件发现/信任图谱/集合/事务性安装规划。 |
| ⭐ 37 | [HenryZ838978/deepseek-harness](https://github.com/HenryZ838978/deepseek-harness) | Python lib + dsh CLI + MCP server + SKILL.md for DeepSeek V4-Pro/V4-Flash; 16 protocol quirks documented, 270+ trials. / DeepSeek V4-Pro/V4-Flash Python 库 + dsh CLI + MCP Server + SKILL.md，含 16 个协议细节与 270+ 次测试。 |
| ⭐ 29 | [bradeGithub/DSH-Plugins-Marketplace](https://github.com/bradeGithub/DSH-Plugins-Marketplace) | One-click browse/install/update all GitHub dsh-plugin topic plugins in DSH Web GUI. / Web GUI 中一键浏览/安装/更新所有 GitHub dsh-plugin 主题插件。 |
| ⭐ 4 | [xiaohai-78/Top](https://github.com/xiaohai-78/Top) | Daily plugin leaderboard: tracks every repo, ranks by stars, archives daily snapshots. / 每日插件排行榜：追踪每个 repo，stars 排名，首页展示。 |
| ⭐ 3 | [runzhliu/deepseek-harness-docker](https://github.com/runzhliu/deepseek-harness-docker) | Docker/K8s packaging: hardened image + Compose stack + Helm chart + Web UI. / Docker/K8s 打包：强化镜像 + Compose + Helm Chart。 |
| ⭐ 2 | [openma-ai/deepseek-harness-typescript-sdk](https://github.com/openma-ai/deepseek-harness-typescript-sdk) | TypeScript SDK mirroring the official Python SDK for DeepSeek Harness. / TypeScript SDK，镜像官方 Python SDK。 |
| ⭐ 2 | [vibeinging/dsh-trace](https://github.com/vibeinginan/dsh-trace) | Telemetry backend: exports turns, model steps, and tool calls to yiTrace over HTTP. / Telemetry 后端：导出 turns/model steps/tool calls 到 yiTrace。 |
| ⭐ 1 | [rsagacom/dsh-ajw](https://github.com/rsagacom/dsh-ajw) | DS Armor Net: daily aggregation of DeepSeek Harness plugin ecosystem open-source projects. / DS安甲网：每日聚合 DSH 插件生态开源项目。 |
| ⭐ 1 | [techysy/deepseek-harness-fnos](https://github.com/techysy/deepseek-harness-fnos) | fnOS app: local resident service, official unified gateway access. / fnOS 应用：本地常驻服务，官方统一网关接入。 |
| ⭐ 1 | [Securstack/securstack-dsh-plugin](https://github.com/Securstack/securstack-dsh-plugin) | SecurStack adapter: repository security scans, policy gates, doctor diagnostics. / SecurStack 适配器：仓库安全扫描/策略门控/医生诊断。 |
| ⭐ 1 | [Sunrisepeak/dsh-index](https://github.com/Sunrisepeak/dsh-index) | DSH Plugin Package Index — install dsh-plugin with just one command. / DSH Plugin Package Index：一条命令安装所有插件。 |
| ⭐ 1 | [bobleer/deepseek-harness-plugin-mcp](https://github.com/bobleer/deepseek-harness-plugin-mcp) | MCP server that lets any agent discover, install, and run DSH plugins. / MCP Server：让任何 Agent 发现/安装/运行 DSH 插件。 |
| ⭐ 1 | [CSY656/dsh-skill-remote](https://github.com/CSY656/dsh-skill-remote) | Remote skills.sh/GitHub skill provider: install any skill with one prompt. / 远程技能提供者：一条 prompt 安装任意 skill。 |
| ⭐ 2 | [omdsh-dev/dsh-llm-fallbacks](https://github.com/omdsh-dev/dsh-llm-fallbacks) | Role-based LLM retry & fallback strategy plugin — routes failures to backup models per role. / 基于角色的模型重试备用策略插件：按角色路由失败到备份模型。 |
| ⭐ 1 | [Nexus-Aethra/DSH-plugin-switch](https://github.com/Nexus-Aethra/DSH-plugin-switch) | DSH Plugin Switch marketplace: browse, search, and install plugins and skills for DeepSeek Harness. / DSH 插件市场：浏览/搜索/安装 DSH 插件与技能。 |
| ⭐ 1 | [yunhuantian/dsh-plugin-hub](https://github.com/yunhuantian/dsh-plugin-hub) | Graphical app-store inside the Harness Web UI — browse, search, and install community plugins. / DSH Web UI 内嵌图形化插件应用商店：浏览/搜索/安装社区插件。 |
| ⭐ 1 | [wink-run/dsh-plugin-store](https://github.com/wink-run/dsh-plugin-store) | DeepSeek Harness plugin store for browsing and installing dsh-plugin ecosystem plugins. / DSH 插件商店：浏览和安装 dsh-plugin 生态插件。 |
| ⭐ 3 | [kairoz9/dsh-mcp-admin](https://github.com/kairoz9/dsh-mcp-admin) | View MCP server status (/mcp) and manage MCP servers per profile from the Settings page. / 查看 MCP 服务器状态 (/mcp)，从设置页按 profile 管理 MCP 服务器。 |
| ⭐ 2 | [zebbkira/dsh-skills-mcp-manager](https://github.com/zebbkira/dsh-skills-mcp-manager) | DSH Web GUI plugin: adds a "Skills & MCP" card to Settings -> Web UI Plugins for browser-based skill and MCP server management. / DSH Web GUI 正式插件包：在设置页「Web UI 插件」分组新增「技能与 MCP」卡片。 |
| ⭐ 2 | [GuoMonth/dsh-multi-tenant](https://github.com/GuoMonth/dsh-multi-tenant) | Multi-tenant SaaS extension for DeepSeek Harness: tenant identity, session isolation, authorization. / DSH 多租户 SaaS 扩展：租户身份、会话隔离、授权。 |
| ⭐ 2 | [chushixixin/dsh-harness-mcp-server](https://github.com/chushixixin/dsh-harness-mcp-server) | Expose DeepSeek Harness agent capabilities as an MCP server (brain=Hermes, arms=Harness). / 将 DSH Agent 能力暴露为 MCP 服务器（brain=Hermes，arms=Harness）。 |
| ⭐ 5 | [weinibuliu/deepseek-harness-vsc-extension](https://github.com/weinibuliu/deepseek-harness-vsc-extension) | DeepSeek Harness VS Code extension — seamless integration of DSH agent into your IDE workflow. / DeepSeek Harness VS Code 扩展，Agent 与 IDE 无缝集成。 |
| ⭐ 2 | [NEXTINDIE/DeepSeek-Harness-for-VS-Code](https://github.com/NEXTINDIE/DeepSeek-Harness-for-VS-Code) | Use DeepSeek Harness in VS Code like ChatGPT/Copilot: @dsh in native chat, standalone views, cross-project sessions, shared via DSH API. Auto-starts server. / 在 VS Code 中使用 DSH：原生对话 @dsh、独立视图、跨项目会话，DSH API 共享，自动启动服务。 |
| ⭐ 2 | [Edge-Echo/dsh-mcp-bridge](https://github.com/Edge-Echo/dsh-mcp-bridge) | Curated MCP server bundle for DeepSeek Harness: one install brings demo, mcp-list, and verification tools. / DSH 精选 MCP 服务器 bundle：一键安装即可使用演示、列表和验证工具。 |
| ⭐ 4 | [labmimors/dsh-mcp-lens](https://github.com/labmimors/dsh-mcp-lens) | Shrink MCP schema overhead: 1,000 remote tools behind 2 exact-schema interfaces, plus local calculator and CI budget Action. / 减少 MCP schema 开销：千级远程工具收敛为 2 个精确 schema，附本地计算器与 CI 预算 Action。 |
| ⭐ 2 | [KYinCode/dsh-project-mcp-bridge](https://github.com/KYinCode/dsh-project-mcp-bridge) | Per-project MCP loading: drop a .dsh/mcp.json into a project and its sessions get MCP tools automatically with live config reload. / 按项目加载 MCP：在项目目录放置 .dsh/mcp.json 即可自动注入 MCP 工具并实时重载配置。 |

---

## 🎙️ Voice & Audio / 语音与音频

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 2 | [Richard-Yang0130/dsh-web-speech-input](https://github.com/Richard-Yang0130/dsh-web-speech-input) | Voice input plugin for DeepSeek Harness using the browser Web Speech API. / 浏览器 Web Speech API 语音输入插件。 |
| ⭐ 1 | [pinch-eng/dsh-audio-dub](https://github.com/pinch-eng/dsh-audio-dub) | Dub video and audio into 10 languages with voice cloning, from a DeepSeek Harness agent. / DSH Agent 语音克隆多语言配音。 |
| ⭐ 1 | [meomeo-dev/dsh-voice](https://github.com/meomeo-dev/dsh-voice) | Conversation-tone switcher bundle for DeepSeek Harness — ships the 令 (Ling) tone and create-voice. / DSH 对话语调切换 bundle。 |
| ⭐ 1 | [leaveimagination/dsh-qwen-voice](https://github.com/leaveimagination/dsh-qwen-voice) | Voice control and multi-session task dispatch for DeepSeek Harness, powered by Qwen Audio Agent. / Qwen Audio Agent 驱动的语音控制与多会话任务分发。 |
| ⭐ 1 | [zhuiyueya/dsh-voice](https://github.com/zhuiyueya/dsh-voice) | Voice for DeepSeek Harness — speech-to-text input + read-aloud TTS for text-only DeepSeek, zero deps. / DSH 语音插件：语音输入 + 朗读输出。 |
| ⭐ 1 | [YS-Chu/dsh-tts-voice](https://github.com/YS-Chu/dsh-tts-voice) | Let your DeepSeek Harness speak. / 让你的 DSH 开口说话。 |
| ⭐ 1 | [CharlesLiuZC/deepseek-harness-voice-context](https://github.com/CharlesLiuZC/deepseek-harness-voice-context) | DeepSeek Harness with Voice Context speech-to-text integration. / DSH 语音上下文集成。 |
| ⭐ 2 | [STARDUSTLC666/dsh-rss](https://github.com/STARDUSTLC666/dsh-rss) | RSS subscription plugin for DeepSeek Harness: rss_list/add/remove/fetch/check 5 tools, RSS 0.9x/1.0/2.0 + Atom normalization. / DSH RSS 订阅插件：rss_list/add/remove/fetch/check 五工具，RSS 0.9x/1.0/2.0 与 Atom 归一化解。 |
| ⭐ 2 | [STARDUSTLC666/dsh-calendar](https://github.com/STARDUSTLC666/dsh-calendar) | Calendar plugin for DeepSeek Harness: calendar_list/create/update/delete/search 5 tools, CalDAV protocol support (Google/iCloud/Nextcloud). / DSH 日历插件：calendar_list/create/update/delete/search 五工具，CalDAV 协议支持 Google/iCloud/Nextcloud。 |
| ⭐ 0 | [STARDUSTLC666/dsh-voice](https://github.com/STARDUSTLC666/dsh-voice) | Dual voice plugin for DeepSeek Harness: voice_tts (Edge-TTS free Microsoft neural TTS) + voice_stt (OpenAI-compatible STT). / DSH 语音双件套：voice_tts（edge-tts 免费微软神经语音合成）+ voice_stt（OpenAI 兼容语音识别）。 |
| ⭐ 3 | [Zachary7456/dsh-voice-mic](https://github.com/Zachary7456/dsh-voice-mic) | Voice input plugin: mic button / shortcut recording, real-time transcription backfill into input box. Three engines: Web Speech, local SenseVoice/Paraformer offline, OpenAI-compatible cloud ASR. / DSH 语音输入插件：麦克风按钮/快捷键录音，实时转写回填输入框，支持三种识别引擎。 |
| ⭐ 3 | [Da-Mie/dsh-beacons](https://github.com/Da-Mie/dsh-beacons) | Right-edge prompt navigator (Codex-style scrub rail with scroll-spy) plus Windows toast notifications for DSH. / DSH 右侧边缘提示词导航（滚动追踪）+ Windows toast 通知。 |

---
## ⚡ Skills & Methodologies / 技能与方法论

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 4 | [dhicoc/dsh-reverse-skill](https://github.com/dhicoc/dsh-reverse-skill) | Complete reverse-skill (85 SKILL.md) as a DSH Cordis plugin — offline/air-gapped skill pack for any DSH environment. / DSH Cordis 插件版逆向技能：85 个 SKILL.md，离线可用，适配任意 DSH 环境。 |
| ⭐ 3 | [Relistencode/dsh-extension-hub](https://github.com/Relistencode/dsh-extension-hub) | CLI + settings-page UI for managing DSH skills and MCP servers with zh/en i18n and Claude/Codex import compatibility. / DSH 技能与 MCP 服务器管理面板：CLI + 设置页 UI，中英双语，支持 Claude/Codex 导入。 |
| ⭐ 1 | [KiWi233333/dsh-creator](https://github.com/KiWi233333/dsh-creator) | Build verified extensions for DeepSeek Harness with an installable agent skill — craft plugins via natural language. / 用可安装 Agent 技能构建验证通过的 DSH 扩展：通过自然语言创建插件。 |
| ⭐ 1 | [Suida/dsh-skills](https://github.com/Suida/dsh-skills) | Curated DSH agent skills collection with categorized templates for common development and automation workflows. / 精选 DSH Agent 技能集：按工作流分类的模板集合，覆盖常用开发场景。 |
| ⭐ 0 | [dhicoc/dsh-wuyun-liuqi](https://github.com/dhicoc/dsh-wuyun-liuqi) | Traditional Chinese medicine AI skill bundle: 31 SKILL.md for 五运六气 (Wu Yun Liu Qi) analysis, wrapped as DSH Cordis plugin. / 中医 AI 技能包：31 个 SKILL.md 封装五运六气（运气学）分析，DSH Cordis 插件。 |
| ⭐ 2 | [zhn1100/dsh-forge](https://github.com/zhn1100/dsh-forge) | Reproducible DSH plugin development environment with deterministic builds. / 可复现的 DSH 插件开发环境。 |
| ⭐ 1 | [qomob/DSHwiki](https://github.com/qomob/DSHwiki) | Community wiki and daily-aggregated plugin directory for DSH — original Chinese tutorials + auto-updating ecosystem with AI-translated descriptions. / DSH 社区 Wiki 与每日聚合插件目录：原创中文教程 + 自动更新生态（AI 翻译描述）。 |
| ⭐ 315 | [linhay/harmony-next.skills](https://github.com/linhay/harmony-next.skills) | Expert guidance for HarmonyOS NEXT (API 12+) development: IDE ops, perf tuning, architecture (HAP/HAR/HSP). / HarmonyOS NEXT (API 12+) 专家指南：IDE 操作、性能调优、架构。 |
| ⭐ 73 | [Nagi-ovo/dsh-find-plugins](https://github.com/Nagi-ovo/dsh-find-plugins) | Find, install, and verify DSH plugins directly from within the agent — GitHub dsh-plugin topic search built in. / 在 Agent 内搜索、安装并验证 DSH 插件，内置 GitHub dsh-plugin 话题搜索。 |
| ⭐ 25 | [Fishquito7/dsh-skill-viewer](https://github.com/Fishquito7/dsh-skill-viewer) | DSH Web UI plugin: Skills settings section with hot enable/disable, delete and add. / DSH Web UI 插件：技能设置页，支持热启停、删除与添加。 |
| ⭐ 11 | [tianji-qingtian/dsh-composer-polish](https://github.com/tianji-qingtian/dsh-composer-polish) | One-click ✨ polish for composer drafts — flash rewrite, auto fill-back. / 输入框草稿一键 ✨ 润色：flash 改写、自动回填。 |
| ⭐ 2 | [rainforest888/dsh-plugins-raincode](https://github.com/rainforest888/dsh-plugins-raincode) | Model layer = raincode (model pool/cache/retry) + /skills browser. / 模型层 = raincode(模型池/缓存/重试) + /skills 浏览。 |
| ⭐ 1 | [rxa3c/chat2skill](https://github.com/rxa3c/chat2skill) | Extract and iterate skills from daily conversations with AI. / 从日常 AI 对话中提取和迭代技能。 |
| ⭐ 1 | [Bandersnatch0x/design-playbook](https://github.com/Bandersnatch0x/design-playbook) | UI generation constraints + contracts — composable with ui-ux-pro-max + frontend-design. / UI 生成约束/可审查/可循环的声明+契约插件。 |
| ⭐ 1 | [litestartup-com/litestartup-skills](https://github.com/litestartup-com/litestartup-skills) | Publish blog, docs, website, changelog, send campaign email directly from your AI agent. / 发布博客/文档/网站/changelog，一键发送营销邮件。 |
| ⭐ 1 | [omdsh-dev/dsh-book2skill](https://github.com/omdsh-dev/dsh-book2skill) | 5-stage long task (fetch→parse→understand→generate→install) with 3 human gates. / 5 阶段长任务（fetch→parse→understand→generate→install）。 |
| ⭐ 1 | [PerryLink/dsh-claude-move](https://github.com/PerryLink/dsh-claude-move) | Migrate Claude Code sessions, memory, skills and CLAUDE.md into DSH with seamless resume. / 迁移 Claude Code 会话/记忆/技能到 DSH。 |
| ⭐ 1 | [D-Robotics/dsh-plugin-rdk](https://github.com/D-Robotics/dsh-plugin-rdk) | D-Robotics RDK (地瓜机器人) integration for DeepSeek Harness — native RDK skill catalog and device detection. / 地瓜机器人 RDK 集成：技能目录与设备检测。 |
| ⭐ 0 | [H1a3x/dsh-prompt-inject](https://github.com/H1a3x/dsh-prompt-inject) | System-prompt template injection for DeepSeek Harness — named templates with global default and per-workspace overrides. / DSH 系统提示词模板注入，支持全局默认和按工作区覆盖。 |
| ⭐ 1 | [randerous/dsh-turn-meta](https://github.com/randerous/dsh-turn-meta) | Opt-in per-step turn metadata for DeepSeek Harness — a minimal first-plugin template (dsh-plugin). / DSH 每步元数据记录，最小化插件模板。 |
| ⭐ 0 | [ttxl314/dsh-skill-lord-serf](https://github.com/ttxl314/dsh-skill-lord-serf) | Lord/Serf protocol 0.5 skills for DSH — file-based multi-agent orchestration (Lord delegates, Serf works). / Lord/Serf 协议 0.5 技能，文件式多 Agent 编排。 |
| ⭐ 0 | [a903067276-rgb/dsh-hud](https://github.com/a903067276-rgb/dsh-hud) | HUD status panel plugin for DSH web: git status, MCP servers, skills, model & token usage in a floating panel. / DSH Web HUD 悬浮面板：Git/MCP/技能/token 状态。 |
| ⭐ 0 | [xiaoxiaosrm/dsh-mattpocock-skills](https://github.com/xiaoxiaosrm/dsh-mattpocock-skills) | Unofficial DSH port of mattpocock/skills — Engineering (18) + Productivity (7) skills. / DSH 版 mattpocock skills：工程(18) + 生产力(7)。 |
| ⭐ 0 | [leechen298/Code2Skill](https://github.com/leechen298/Code2Skill) | Generate Function, MCP, Agent Skill, and offline test packages from existing code; installable as a DSH plugin. / 从现有代码生成函数/MCP/Agent Skill 及离线测试包。 |
| ⭐ 0 | [YTxue/dsh-skill-manager](https://github.com/YTxue/dsh-skill-manager) | Skill manager in Settings sidebar: list/enable/disable, folder batch import with conflict prompts, DSH-spec check & auto-fix, system/project scope labels. / 设置侧边栏技能管理器：列出/启停/批量导入，冲突提示，一键修复。 |
| ⭐ 0 | [dmsobtl/dsh-skill-evolve](https://github.com/dmsobtl/dsh-skill-evolve) | Agent self-evolution engine: auto-distills reusable skills from successful sessions, gets smarter over time. / Agent 自我进化引擎：从成功会话中自动提炼可复用 skill，越用越聪明。 |
| ⭐ 0 | [Thomas-key/dsh-skill-manager](https://github.com/Thomas-key/dsh-skill-manager) | Manage DeepSeek Harness skills: list and toggle filesystem skills instantly. / DSH 技能管理器：列出并即时切换文件系统技能。 |
| ⭐ 5 | [DDDFXYqiming/Agent_Extensions](https://github.com/DDDFXYqiming/Agent_Extensions) | Agent Skills & DeepSeek Harness extension library: general agent skills (General_skills) + DSH standard plugins, out-of-the-box capability enhancement bundle. / Agent 技能与 DSH 扩展库：通用智能体技能 + DSH 标准插件，开箱即用的能力增强集合。 |
| ⭐ 2 | [xiaoxianyu-office/dsh-skills-manager](https://github.com/xiaoxianyu-office/dsh-skills-manager) | DSH Skills manager: system/user skill categorization in Settings, enable/disable/edit/delete new skills. / DSH 技能管理器：设置页系统/用户技能分类，支持启停/编辑/删除/新建。 |
| ⭐ 2 | [Lanxing6480/dsh-skill-manager](https://github.com/Lanxing6480/dsh-skill-manager) | Skill management plugin for DeepSeek Harness: list, toggle, and organize agent skills. / DSH 技能管理插件：列出、切换和组织 Agent 技能。 |
| ⭐ 2 | [hellosky983/dsh-skillradar](https://github.com/hellosky983/dsh-skillradar) | Scans session-visible skills and ranks them by relevance to the recent conversation. / 扫描会话可见技能并按与最近对话的相关性排序。 |
| ⭐ 2 | [sandbaseai/sandbase-skills](https://github.com/sandbaseai/sandbase-skills) | Native DSH skills for research and growth workflows, with an npm CLI that installs complete skill bundles. / DSH 原生研究与增长工作流技能，带 npm CLI 安装完整技能包。 |
| ⭐ 1 | [muretai/muretai-dsh-skill](https://github.com/muretai/muretai-dsh-skill) | Join the Muretai agent network from DSH — one-step install, MCP wiring, inbound-message routing. / 从 DSH 加入 Muretai Agent 网络：一键安装、MCP 接线、入站消息路由。 |
| ⭐ 1 | [caoqinnan-web/dsh-project-organizer](https://github.com/caoqinnan-web/dsh-project-organizer) | Project Context Engineering for AI agents — a DSH Skill and installable plugin. / AI 代理项目上下文工程：DSH 技能与可安装插件。 |
| ⭐ 1 | [hexbee/dsh-skill-panel](https://github.com/hexbee/dsh-skill-panel) | DSH plugin: manage agent skills in Settings sidebar. / DSH 插件：设置侧边栏管理 Agent 技能。 |
| ⭐ 1 | [OneZero-Y/dsh-plugin-kit](https://github.com/OneZero-Y/dsh-plugin-kit) | Agent skills and a working template for building standalone DeepSeek Harness (DSH) plugins. / 构建独立 DSH 插件的 Agent 技能与可工作模板。 |
| ⭐ 1 | [JoukoPuro/dsh-prompt-polish](https://github.com/JoukoPuro/dsh-prompt-polish) | Icon-only composer button that rewrites prompts via connected LLM with balanced/concise/detailed/code styles. / 仅图标 composer 按钮，通过连接的 LLM 以均衡/简洁/详细/代码风格改写提示词。 |
| ⭐ 1 | [Jesse-njx/dsh-skillport](https://github.com/Jesse-njx/dsh-skillport) | Every skill you already have — Claude Code, Codex, Cursor, Gemini CLI — works in DSH: Agent Skills Sync. / 你已有的所有技能（Claude Code/Codex/Cursor/Gemini CLI）在 DSH 中运行：Agent 技能同步。 |
| ⭐ 2 | [sulfide2085/dsh-skill-manager](https://github.com/sulfide2085/dsh-skill-manager) | Unified skill manager for DSH/Codex/Claude: hot toggle, GitHub skill-market one-click install, local ZIP import, conflict detection. / 跨工具统一技能管理器：DSH/Codex/Claude 技能热启停、GitHub 市场一键安装、本地 ZIP 导入。 |
| ⭐ 1 | [cheshireez/dsh-skill-hub](https://github.com/cheshireez/dsh-skill-hub) | DeepSeek Harness Web GUI skill hub: browse/search full local skill directory, enable/disable, view source, diagnose, create new skills. / DSH Web GUI 技能中枢：浏览/搜索完整本地技能目录、启用/禁用、查看正文、排查诊断、新建技能。 |
| ⭐ 1 | [lywusichen/dsh-skill-panel](https://github.com/lywusichen/dsh-skill-panel) | DeepSeek Harness skill floating panel plugin: sidebar skill button, one-click view loaded skills and open local directory. / DSH 技能悬浮窗插件：侧边栏技能按钮，一键查看已加载技能并打开本地目录。 |
| ⭐ 1 | [winterhuan/dsh-skills-viewer](https://github.com/winterhuan/dsh-skills-viewer) | Read-only Skills settings page plugin for DeepSeek Harness Web. / DSH Web 只读技能设置页插件。 |
| ⭐ 3 | [YOYOGEMOW/DeepSeek_Prism](https://github.com/YOYOGEMOW/DeepSeek_Prism) | On-demand vision Codex Skill for text-only DeepSeek models: VEP/1 vision evidence pack + multi-provider fallback. / 纯文本 DeepSeek 模型按需识图 Codex Skill（VEP/1 视觉证据包 + 多 Provider 降级）。 |
| ⭐ 3 | [sanshanya/better-model-provider](https://github.com/sanshanya/better-model-provider) | Per-model capability declaration for DeepSeek Harness: reasoning-effort levels (wire spellings) + real-time context pressure indicator. / DSH 每模型能力声明：推理强度挡位（wire spellings）+ 实时上下文压力指示器。 |
| ⭐ 2 | [Yihong89/dsh-teacher](https://github.com/Yihong89/dsh-teacher) | DSH teacher plugin: Socratic tutor that leads you to answers from a markdown question set, tracks knowledge gaps in-session. / DSH 教师插件：苏格拉底式引导，基于 Markdown 题库逐层启发，会话内追踪知识盲点。 |

| ⭐ 1 | [Fishsb/dsh-prompt-enhancer](https://github.com/Fishsb/dsh-prompt-enhancer) | One-click prompt enhancement for DeepSeek Harness — polish drafts with LLM-powered rewriting before sending. / 一键优化草稿：DSH 提示词增强插件，发送前 LLM 润色。 |
| ⭐ 3 | [Aik358/dsh-auto-memory](https://github.com/Aik358/dsh-auto-memory) | Three-layer auto-memory for DSH: user-level/project notes/daily logs with automatic injection, retrieval, daily reflection, visual panel. / DSH 三层自动记忆：用户级/项目笔记/每日日志自动注入与检索、每日反思、可视化面板。 |

---

## 🔬 Advanced & Experimental / 高级与实验性

| Stars | Repo | Description / 描述 |
|-------|------|---------------------|
| ⭐ 574 | [sandbaseai/sandbase-harness](https://github.com/sandbaseai/sandbase-harness) | Open-source CMA-compatible agent runtime for any model — MCP tools, sandboxed sessions, audit/replay, local console. DSH bundle included. / 开源 CMA 兼容 agent 运行时，含 MCP 工具/沙箱会话/审计回放，内置 DSH bundle。 |
| ⭐ 1 | [jorinyang/dsh-clawshell](https://github.com/jorinyang/dsh-clawshell) | ClawShell vision as DSH plugins: self-perception, closed-loop self-adaptation, trust/niche swarm, insight mining, knowledge genome. / ClawShell 视觉作为 DSH 插件：自我感知、闭环自适应、信任/利基蜂群、洞察挖掘、知识基因组。 |
| ⭐ 2 | [ottotheagent/otto-dsh](https://github.com/ottotheagent/otto-dsh) | Book real flights, hotels & cars with Otto from DeepSeek Harness — the otto-travel MCP connector as a dsh plugin. / 通过 DSH 使用 Otto 预订航班/酒店/租车。 |
| ⭐ 2 | [yuhui-sama/dsh-agentsoul](https://github.com/yuhui-sama/dsh-agentsoul) | Local personality, memory and distillation layer for DSH — SOUL/IDENTITY/USER/STATE persona files, cross-session memory, auto-loaded on startup. / DSH 本地人格与记忆蒸馏层：SOUL/IDENTITY/USER/STATE 人格文件，跨会话记忆，启动时自动加载。 |
| ⭐ 72 | [omdsh-dev/dsh-genui](https://github.com/omdsh-dev/dsh-genui) | GenUI: render layouts/charts/forms/mermaid/3D scenes inline via dsh-ui fence. / GenUI：dsh-ui fence 内渲染布局/图表/表单/mermaid/3D 场景。 |
| ⭐ 2 | [LeslieWylie/dsh-ops-kit](https://github.com/LeslieWylie/dsh-ops-kit) | Reusable DSH bundle for evidence-driven memory, orchestration, benchmark operations, and plugin release workflows. / 可复用 DSH bundle：证据驱动记忆、编排、基准测试与插件发布工作流。 |
| ⭐ 37 | [omdsh-dev/dsh-annotation](https://github.com/omdsh-dev/dsh-annotation) | Web selection annotation: select text → annotate → enter to send; bubble-hidden annotation blocks. / Web 选中批注：选文字→批注→回车发送，气泡隐藏块。 |
| ⭐ 8 | [omdsh-dev/fabric](https://github.com/omdsh-dev/fabric) | MC Fabric-style hook processor for DeepSeek Harness. / MC Fabric 风格的 hook 处理器。 |
| ⭐ 4 | [ayuanwong/deepseek-harness-ux](https://github.com/ayuanwong/deepseek-harness-ux) | Long tasks without transcript clutter: focused progress, auto-folded history, details on demand. / 长任务进度折叠：关键进度清晰，完成后自动收起。 |
| ⭐ 3 | [fuhefei/dsh-sentinel](https://github.com/fuhefei/dsh-sentinel) | Condition-driven wakeup: durable file/command/http/process/webhook watches that wake the agent. / 条件驱动唤醒：durable file/command/http/watch 触发 Agent。 |
| ⭐ 3 | [william-jin-cmu/dsh-evolve](https://github.com/william-jin-cmu/dsh-evolve) | Self-evolving plugin: agent grows/cuts capabilities mid-session — evolve_add hot-mount persist, evolve_remove reversible. / 自进化插件：agent 在 session 内热挂载/卸载 cordis 插件。 |
| ⭐ 3 | [yanglongyun/dsh-ramify](https://github.com/yanglongyun/dsh-ramify) | Creative branch canvas: tree-shaped workspace generation, comparison, and iteration of multiple方案的. / 创意分支画布：树状工作区生成/对比/迭代多方案。 |
| ⭐ 3 | [RangeKing/vibemeter](https://github.com/RangeKing/vibemeter) | See what your agents are doing. Understand how you work together. / 查看 agent 在做什么，理解协作方式。 |
| ⭐ 3 | [renat3u/dsh-web-archive](https://github.com/renat3u/dsh-web-archive) | Collapse "useless messages" (Think, Bash, etc.) in conversations. / 折叠"无用消息"（Think/Bash 等）。 |
| ⭐ 3 | [icodesign/orbis](https://github.com/icodesign/orbis) | Mobile client for DeepSeek Harness remote control. / DeepSeek Harness 远程控制移动客户端。 |
| ⭐ 3 | [btspoony/dsh-advisor](https://github.com/btspoony/dsh-advisor) | Pair a second model that passively reviews each turn and injects notes. / 第二模型配对：每轮被动注入见解与审查。 |
| ⭐ 3 | [SnowCrescenter-tech/dsh-milestone](https://github.com/SnowCrescenter-tech/dsh-milestone) | Git-style milestone timeline: hover for metadata, click to jump to any message. / Git 风格里程碑时间线：悬停看元数据，点击跳转。 |
| ⭐ 3 | [HuanLinOTO/dsh-plugin-sleep](https://github.com/HuanLinOTO/dsh-plugin-sleep) | sleep tool: pause for specified ms then return, with cancellation/clamping support. / sleep 工具：指定毫秒暂停后返回，支持取消。 |
| ⭐ 3 | [HuanLinOTO/dsh-plugin-interpreters](https://github.com/HuanLinOTO/dsh-plugin-interpreters) | run_python/run_node tools that execute code via stdin, with interpreter-path config. / run_python/run_node 工具，stdin 执行代码。 |
| ⭐ 3 | [HuanLinOTO/dsh-plugin-better-sidebar-plugin-office](https://github.com/HuanLinOTO/dsh-plugin-better-sidebar-plugin-office) | Office suite preview (.docx/.xlsx/.pptx) for better-sidebar as a separate bundle. / better-sidebar 的 Office 三件套预览扩展。 |
| ⭐ 3 | [HuanLinOTO/dsh-plugin-ya-workspace-sidebar](https://github.com/HuanLinOTO/dsh-plugin-ya-workspace-sidebar) | Workspace sidebar replacement: top global recent sessions + Workspace→Session menu. / 工作区侧栏替代：全局最近会话 + Workspace→Session 菜单。 |
| ⭐ 3 | [Mongfayi/dsh-recall](https://github.com/Mongfayi/dsh-recall) | Message recall: undo a turn and everything after it, without reverting code changes. / 消息撤回：撤销 turn 及之后所有内容，不还原代码。 |
| ⭐ 3 | [forrestchang/dsh-multica-runtime](https://github.com/forrestchang/dsh-multica-runtime) | Support dsh runtime on Multica platform. / Multica 上的 dsh runtime 支持。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-calculator](https://github.com/omdsh-dev/dsh-tool-calculator) | Zero-dependency mathematical expression evaluator. / 零依赖数学表达式求值器。 |
| ⭐ 2 | [omdsh-dev/dsh-tool-csv](https://github.com/omdsh-dev/dsh-tool-csv) | RFC 4180 CSV parsing/querying/stats/conversion. / RFC 4180 CSV 解析/查询/统计/转换。 |
| ⭐ 2 | [PerryLink/dsh-auto-review](https://github.com/PerryLink/dsh-auto-review) | Second-model AI auto-review: read-only reviewer subagent returns structured allow/deny verdicts. / 第二模型 AI 自动审核：read-only reviewer subagent 返回 allow/deny 裁决。 |
| ⭐ 2 | [Yihong89/dsh-plugins](https://github.com/Yihong89/dsh-plugins) | dsh-usage-report: per-session token usage & estimated cost (/usage + usage_report). / dsh-usage-report：按会话 token 用量 & 估算费用。 |
| ⭐ 1 | [baixinghao/intent-gate](https://github.com/baixinghao/intent-gate) | Enforce intent alignment BEFORE coding: PRD → intent-confidence gate → Mermaid contracts → lint. / 编码前强制意图对齐：PRD → intent-confidence gate → Mermaid 契约。 |
| ⭐ 1 | [ang-XWBWZ/Pwiki](https://github.com/ang-XWBWZ/Pwiki) | Local-first knowledge retrieval engine: BM25, semantic search, reranking, MCP integration. / 本地优先知识检索引擎：BM25 + 语义搜索 + reranking。 |
| ⭐ 1 | [qingzhuo-cn/agent-fix](https://github.com/qingzhuo-cn/agent-fix) | Universal repair skill & CLI for AI coding agents (Claude Code, Codex, OpenCode, Hermes). / AI 编码 Agent 通用修复 skill & CLI。 |
| ⭐ 1 | [lujoai/Lujo-MCP](https://github.com/lujoai/Lujo-MCP) | MCP protocol AI debugging/tracing platform: session mgmt, link tracing, error analysis, Dashboard. / MCP 协议 AI 调试追踪平台：会话管理/链路追踪/错误分析/Dashboard。 |
| ⭐ 1 | [lhmd/dsh-director-toolkit](https://github.com/lhmd/dsh-director-toolkit) | Direction pack for 3D artists: Blender, Three.js, Houdini, C4D — paste idea, get compact direction. / 3D 艺术家/技术设计师方向包：Blender/Three.js/Houdini/C4D。 |
| ⭐ 1 | [lhmd/dsh-promotion-toolkit](https://github.com/lhmd/dsh-promotion-toolkit) | Turn any idea into platform-native publicity content. / 任何想法变成各平台原生宣发内容。 |
| ⭐ 1 | [sjscy05/matlab-modelsim-vivado-plugin](https://github.com/sjscy05/matlab-modelsim-vivado-plugin) | MATLAB + ModelSim + Vivado full-flow IC design tools for digital communication tasks. / MATLAB + ModelSim + Vivado 全流程 IC 设计工具。 |
| ⭐ 1 | [TecFancy/dsh-deeptutor](https://github.com/TecFancy/dsh-deeptutor) | DeepTutor bridge bundle: learning capabilities, knowledge bases & note archiving. / DeepTutor 桥接：学习能力、知识库、笔记归档。 |
| ⭐ 1 | [Ilharp/dsh-tool-approval](https://github.com/Ilharp/dsh-tool-approval) | Manual approval mode ("Manual Mode"/"Ask Mode") for DeepSeek Harness. / 手动审批模式（Manual Mode / Ask Mode）。 |
| ⭐ 1 | [jumpserver-east/jumpserver-dsh](https://github.com/jumpserver-east/jumpserver-dsh) | JumpServer asset management plugin, operate assets through KoKo. / JumpServer 资产管理插件，通过 KoKo 操作。 |
| ⭐ 1 | [joyfoxai/dsh-eco-router](https://github.com/joyfoxai/dsh-eco-router) | Token-efficient model-routing flywheel for DeepSeek Harness. / Token 高效模型路由飞轮。 |
| ⭐ 1 | [erduotong/dsh-plugin-graph](https://github.com/erduotong/dsh-plugin-graph) | Plugin relationship graph visualization for DSH. / 插件关系图谱可视化。 |
| ⭐ 1 | [sikitse/dsh-dev-actions](https://github.com/sikitse/dsh-dev-actions) | Turn repeated dev commands, prompts, and habits into one-click DSH actions. / AI 将重复开发命令/提示/习惯变为一键 action。 |
| ⭐ 1 | [havingautism/dsh-ultra-ui](https://github.com/havingautism/dsh-ultra-ui) | Ultra UI for DSH. / DSH Ultra UI。 |
| ⭐ 1 | [omdsh-dev/dsh-voice-funasr](https://github.com/omdsh-dev/dsh-voice-funasr) | Voice recognition plugin for DSH (FunASR). / DSH 语音识别插件（FunASR）。 |
| ⭐ 1 | [maskshell/solidforge-dsh](https://github.com/maskshell/solidforge-dsh) | Two-axis convergence discipline (spec-gaming orthogonal axis) native implementation for DSH. / 双轴收敛纪律（spec-gaming 正交轴）的 DSH 原生实现。 |
| ⭐ 1 | [AOWAYHONG/dsh-hide-reasoning](https://github.com/AOWAYHONG/dsh-hide-reasoning) | Fold reasoning steps into summary cards with model badge, token/phase/tool time stats. / 推理步骤折叠为摘要卡片（模型徽章 + token/阶段/工具耗时统计）。 |
| ⭐ 1 | [maque2333/dsh-ui-topbar-compact](https://github.com/maque2333/dsh-ui-topbar-compact) | Compact the native DSH WebUI topbar. / 缩窄原生 DSH WebUI 顶栏。 |
| ⭐ 1 | [yangYzc/dsh-plugin-quote-reply](https://github.com/yangYzc/dsh-plugin-quote-reply) | Select text in conversation and quote it into the composer or reply in a new window. / 引用选中文字并回复到新窗口。 |
| ⭐ 1 | [LoftyTao/dsh-ui-workbench](https://github.com/LoftyTao/dsh-ui-workbench) | Right sidebar file manager and change reviewer for DSH WebUI. / DSH WebUI 右侧边文件管理以及变更审查界面。 |
| ⭐ 1 | [JulieSapir/dsh-vscode](https://github.com/JulieSapir/dsh-vscode) | [WIP] DeepSeek Harness WebUI for VS Code, based on iframe. / DSH WebUI 的 VS Code 扩展（iframe 嵌入）。 |
| ⭐ 1 | [Toukaiteio/dsh-effort-tweak](https://github.com/Toukaiteio/dsh-effort-tweak) | Change the reasoning effort of custom models in DeepSeek Harness WebUI. / 修改 DSH WebUI 自定义模型的思考强度。 |
| ⭐ 1 | [Yuuz12/dsh-webui-auth](https://github.com/Yuuz12/dsh-webui-auth) | Persistent auth plugin for DeepSeek Harness WebUI: enforce login at the HTTP/transport layer. / DSH WebUI 持久化认证插件：HTTP/传输层强制登录。 |
| ⭐ 1 | [BrambleXu/dsh-annotate](https://github.com/BrambleXu/dsh-annotate) | Visual browser element annotation for DeepSeek Harness: DOM, styles, accessibility data capture. / DSH 可视化浏览器元素批注：DOM/样式/无障碍数据捕获。 |
| ⭐ 1 | [Toukaiteio/dsh-plugin-installer](https://github.com/Toukaiteio/dsh-plugin-installer) | Marketplace plugin to integrate your DeepSeek Harness into the GitHub plugin ecosystem. / 插件市场安装器：一键集成 DSH 到 GitHub 插件生态。 |
| ⭐ 1 | [DietCokewithSugar/dsh-user-experience](https://github.com/DietCokewithSugar/dsh-user-experience) | Persona-driven UX walkthrough plugin for DeepSeek Harness — scans React + TypeScript source code. / 人格驱动的 UX 引导插件：扫描 React + TypeScript 源码。 |
| ⭐ 1 | [akira399/dsh-godot-skill](https://github.com/akira399/dsh-godot-skill) | Godot Engine 4.x full-stack game dev skill plugin for DeepSeek Harness. / Godot Engine 4.x 全栈游戏开发技能插件。 |
| ⭐ 1 | [Yauntyour/DSH-for-VSC](https://github.com/yauntyour/DSH-for-VSC) | Bring DeepSeek Harness WebUI into VS Code: embedded panel + sidebar console. / 把 DSH WebUI 搬进 VS Code：编辑器内嵌面板 + 侧边栏控制台。 |
| ⭐ 1 | [Alvis-HaoH/gkd](https://github.com/Alvis-HaoH/gkd) | Claude Code delegation plugin: dispatch tasks to sub-agents (or --codex to local Codex). / Claude Code 委派插件：将任务派给子 Agent 或本机 Codex。 |
| ⭐ 17 | [LayneChai/superpowers-dsh](https://github.com/LayneChai/superpowers-dsh) | Superpowers skills for DeepSeek Harness: TDD, debugging, planning, collaboration adapted. / Superpowers 方法论技能适配 DSH。 |
| ⭐ 1 | [drowned-fish1/deepseek-harness-skillx](https://github.com/drowned-fish1/deepseek-harness-skillx) | Safely discover, audit, and adopt external Agent Skills for DeepSeek Harness. / 安全发现、审计和采用外部 Agent Skills。 |
| ⭐ 1 | [duan-1128/My-Agent-System](https://github.com/duan-1128/My-Agent-System) | Custom Agent Harness on Claude Code + DeepSeek: 17 skills, role-based dispatcher, hooks, cross-session. / 基于 Claude Code + DeepSeek 的自定义 Agent Harness。 |
| ⭐ 4 | [wei-jia-fu14/pi2dsh](https://github.com/weijiafu14/pi2dsh) | Bridge Pi and DeepSeek Harness ecosystems: one Pi Host ABI runs unmodified Pi extensions. / 桥接 Pi 与 DSH 生态：原生运行 Pi 扩展。 |
| ⭐ 1 | [cyzlmh/dsh-pi-adapter](https://github.com/cyzlmh/dsh-pi-adapter) | Run pi coding-agent extensions (ExtensionAPI) inside DeepSeek Harness via cordis plugin bridge. / 通过 cordis 桥在 DSH 中运行 pi 编码扩展。 |
| ⭐ 1 | [lehhair/dsh-home-ui](https://github.com/lehhair/dsh-home-ui) | PiUI-inspired home feed visual refinement plugin for DeepSeek Harness web client. / PiUI 风格首页信息流视觉优化插件。 |
| ⭐ 1 | [jotarozaku-jpg/DeepSeek-Harness-VSCode-Extension](https://github.com/jotarozaku-jpg/DeepSeek-Harness-VSCode-Extension) | Unofficial source-only Visual Studio Code client for DeepSeek Harness over ACP. / DSH 的 VS Code 非官方扩展（ACP 协议）。 |
| ⭐ 1 | [egnmosk/dsh-browser-bridge](https://github.com/egnmosk/dsh-browser-bridge) | DeepSeek Harness plugin + browser extension bridge: browser_* agent tools. / DSH 插件 + 浏览器扩展桥接。 |
| ⭐ 1 | [kit-zeason/dsh-simple-CLI](https://github.com/kit-zeason/dsh-simple-CLI) | Minimal DeepSeek Harness extension tailored for contemporary CLI mobilization. / 最小化 DSH CLI 扩展。 |
| ⭐ 1 | [cnyac/dsh-polling](https://github.com/cnyac/dsh-polling) | Cron scheduled tasks plugin for DeepSeek Harness: natural-language scheduled sessions. / 定时任务插件：自然语言调度会话。 |
| ⭐ 1 | [momo-gen/dsh-browser-pilot](https://github.com/momo-gen/dsh-browser-pilot) | Self-contained Cordis agent-preset for browser automation with DSH. / 自包含浏览器自动化 Agent 预设。 |
| ⭐ 1 | [get-aop/aop-plugin](https://github.com/get-aop/aop-plugin) | AOP Software Delivery Workflow Plugin for DeepSeek Harness (Plan → Implement → Review → Browse). / AOP 软件交付工作流插件。 |
| ⭐ 1 | [joygqz/vscode-dsh](https://github.com/joygqz/vscode-dsh) | Launch the DeepSeek Harness web GUI from VS Code: one click starts the server. / 从 VS Code 一键启动 DSH Web GUI。 |
| ⭐ 1 | [dawsondx/dsh-web-open](https://github.com/dawsondx/dsh-web-open) | When dsh web is ready, print the full GUI URL and open in browser. / dsh web 就绪后自动打开浏览器。 |
| ⭐ 1 | [yyyyukari/dsh-plugin-workshop](https://github.com/yyyyukari/dsh-plugin-workshop) | Steam Workshop-style plugin browser for DSH Web UI — zero-server, GitHub-powered. / Steam Workshop 风格零服务端插件浏览器。 |
| ⭐ 9 | [HsiangNianian/dsh-auto-continue](https://github.com/HsiangNianian/dsh-auto-continue) | DSH Web UI plugin: automatically sends "继续" (continue) when a request is interrupted by network errors or other non-human causes. / DSH 自动续连：网络错误等非人工中断时自动发送"继续"。 |
| ⭐ 7 | [Tyan66666/billion-context-dsh](https://github.com/Tyan66666/billion-context-dsh) | Model-driven context management (Active Context Pruning / ACP) for DeepSeek Harness — model decides what to compress. / DSH 模型驱动上下文管理（Active Context Pruning）：模型自主决定压缩策略。 |
| ⭐ 0 | [Blaczz/dsh-deck-builder](https://github.com/Blaczz/dsh-deck-builder) | DSH tool plugin: convert Markdown into self-contained HTML presentations (slides) with themes and keyboard navigation. / DSH Markdown → HTML 幻灯片生成器，支持主题与键盘导航。 |
| ⭐ 2 | [zcx369658780/governed-workflow-for-dsh](https://github.com/zcx369658780/governed-workflow-for-dsh) | Policy-enforced, evidence-first governed workflows for DeepSeek Harness agents. / 策略强制执行、证据优先的 DSH Agent 治理工作流。 |
| ⭐ 1 | [dshworks/dsh-hydrophone](https://github.com/dshworks/dsh-hydrophone) | Background stream listeners that wake the DSH agent — harness analog of Claude Code's Monitor tool, built on the jobs subsystem. / 后台流监听器：唤醒 DSH Agent，类比 Claude Code Monitor 工具，基于 jobs 子系统构建。 |
| ⭐ 7 | [Areium/dsh-fail-logger](https://github.com/Areium/dsh-fail-logger) | Tool failure reason logger for DeepSeek Harness: auto-logs failures across native tools/PTC run_code/inline tool calls, deduplicates, counts, and writes to skill memory. / DSH 工具失败原因记录器：自动记录所有执行模式的工具失败，去重计数后沉淀进 skill 记忆。 |
| ⭐ 3 | [Chhlafiu4312/promptwall](https://github.com/Chhlafiu4312/promptwall) | Local prompt-injection and secret-exfiltration firewall for DeepSeek Harness. / DSH 本地提示词注入与密钥外泄防火墙。 |
| ⭐ 10 | [omdsh-dev/dsh-security-audit](https://github.com/omdsh-dev/dsh-security-audit) | Local security audit plugin for DeepSeek Harness: config/plugin-source/session/network exposure risk report (read-only, sanitized). / DSH 本机安全审计插件：配置/插件来源/会话/网络暴露面只读脱敏风险报告。 |
| ⭐ 2 | [Slywalker2006/dsh-passwords](https://github.com/Slywalker2006/dsh-passwords) | DeepSeek Harness login gateway: first-run setup, at-rest encryption, brute-force protection for Web GUI. / DSH 登录网关：首次运行设置、静态加密、Web GUI 防暴力破解。 |
| ⭐ 2 | [Cavan-Ou/hermes-dsh-collab](https://github.com/Cavan-Ou/hermes-dsh-collab) | Battle-tested multi-agent collaboration playbook for DeepSeek Harness: model-tier routing, spec discussion, handoff validation. / DSH 经过实战检验的多 Agent 协作剧本：模型分级路由、spec 讨论、交接验证。 |
| ⭐ 2 | [LeslieWylie/dsh-agent-orchestration](https://github.com/LeslieWylie/dsh-agent-orchestration) | Evidence-first multi-agent workflow planning, handoff validation, and Loop Guard skills for DeepSeek Harness. / 证据优先的多 Agent 工作流规划、交接验证与 Loop Guard 技能。 |
| ⭐ 2 | [ZSeven-W/dsh-noema](https://github.com/ZSeven-W/dsh-noema) | Noema long-term memory plugin for DSH: durable, inspectable agent memory with recall tools and a set of memory primitives. / DSH Noema 长期记忆插件：持久化、可检查的 Agent 记忆，带回忆工具和一套记忆原语。 |
| ⭐ 1 | [jiezeng2004-design/dsh-requirements-alignment](https://github.com/jiezeng2004-design/dsh-requirements-alignment) | Lightweight requirement alignment for DeepSeek Harness — align important decisions before execution. / DSH 轻量需求对齐：在执行前对齐关键决策。 |
| ⭐ 2 | [Qinling-Melon-Farmers/dsh-memoir](https://github.com/Qinling-Melon-Farmers/dsh-memoir) | DSH project persistent memory plugin (TypeScript): session distillation + experience precipitation, writes to PROJECT_MEMORY.md with global index. / DSH 项目持久化记忆插件（TypeScript）：会话归纳 + 经验教训沉淀，写入 PROJECT_MEMORY.md 与全局索引。 |
| ⭐ 2 | [huguangyu666/dsh-plugin-notify](https://github.com/huguangyu666/dsh-plugin-notify) | DeepSeek Harness plugin: notification outlets — desktop notifications / Chinese voice broadcast / beep sounds proactively contact users (long task complete, errors, call user back). Windows local zero-dependency. / DSH 插件：通知出口——agent 通过桌面通知/中文语音播报/提示音主动联系用户（长任务完成、出错、呼叫用户回来）。Windows 本机零依赖。 |
| ⭐ 0 | [wxxb789/dsh-legion](https://github.com/wxxb789/dsh-legion) | Configurable multi-model subagent profiles for DeepSeek Harness. / DSH 可配置多模型子代理 profile。 |
| ⭐ 1 | [yha9806/dsh-subagent-admission](https://github.com/yha9806/dsh-subagent-admission) | Shared lifecycle admission protocol and reference policy kernel for DeepSeek Harness subagents. / DSH subagent 共享生命周期准入协议与参考策略内核。 |
| ⭐ 2 | [skylar-fei/dsh-wechat-maid](https://github.com/skylar-fei/dsh-wechat-maid) | DSH plugin providing WeChat remote control, proactive dialogue, future tasks, desktop pet features; check future task status in real-time from desktop pet panel. / DSH 插件：微信远程控制、主动对话、未来任务、桌宠功能。(https://github.com/dshworks/dsh-hydrophone) | Background stream listeners that wake the DSH agent — harness analog of Claude Code's Monitor tool, built on the jobs subsystem. / 后台流监听器：唤醒 DSH Agent，类比 Claude Code Monitor 工具，基于 jobs 子系统构建。 |
| ⭐ 104 | [Sikao-Engine/KimiX](https://github.com/Sikao-Engine/KimiX) | Next-gen lightweight coding agent CLI — with DSH plugin support. / 下一代轻量级编码 Agent CLI，支持 DSH 插件。 |
| ⭐ 12 | [dingkaihu63/dsh-robotic-harness](https://github.com/dingkaihu63/dsh-robotic-harness) | Robotic Harness for DeepSeek Harness: embodied-intelligence research tools, MuJoCo pick-place simulation with fault injection, evidence-based diagnostics. / DSH 机器人学研究工具：MuJoCo 抓取模拟、故障注入、基于证据的诊断。 |
| ⭐ 9 | [modusensus/dsh-mneme](https://github.com/modusensus/dsh-mneme) | Mneme memory plugin for DSH: SQLite + human-editable Markdown dual-write, autoDream consolidation, 140 tests. / DSH Mneme 记忆插件：SQLite + 可人工编辑的 Markdown 双写，autoDream 梦境巩固，140 个测试护航。 |
| ⭐ 1 | [jeremy9682/dsh-cursor-codex](https://github.com/jeremy9682/dsh-cursor-codex) | Connect DSH to Cursor and Codex: ACP agent bundle, MCP server, skills, and config templates. / 将 DSH 接入 Cursor 和 Codex：ACP Agent 套件、MCP 服务器、技能和配置模板。 |
| ⭐ 1 | [Aloneswork/deepseek-harness-codex-bridge](https://github.com/Aloneswork/deepseek-harness-codex-bridge) | Bidirectional Codex ↔ DSH MCP bridge: Codex leads, DSH assists, local collaborative workflow. / Codex 主导、DeepSeek Harness 辅助的本地双向 MCP 协作桥。 |
| ⭐ 2 | [Tkingxiao/dsh-any-background](https://github.com/Tkingxiao/dsh-any-background) | Custom theme plugin for DSH: background images (size/position), main and settings UI transparency, full-color wheel. / DSH 自定义主题插件：背景图（大小和位置）、主界面和设置界面透明度、色轮全色主题色。 |
| ⭐ 2 | [TQSY114514/dsh-ui-appearance](https://github.com/TQSY114514/dsh-ui-appearance) | Appearance customization for DSH: theme color palette, background image, opacity/blur, glass effect. / DSH 外观定制插件：主题调色板、背景图、透明度/模糊、玻璃效果。 |
| ⭐ 1 | [zby1211/cordis-transfer-plugin](https://github.com/zby1211/cordis-transfer-plugin) | Persistent DSH plugin for importing and exporting dynamic Cordis Plugins. / DSH 持久化插件：导入导出动态 Cordis 插件。 |
| ⭐ 0 | [DoloresCaritasAngelus/DSH-AUX](https://github.com/DoloresCaritasAngelus/DSH-AUX) | Auxiliary model system for DSH: unified aux-LLM routing (per-task model, timeout, concurrency, failure cooldown, main-model fallback) + vision/web/compression tools. / DSH 辅助模型系统：统一 aux-LLM 路由（按任务模型/超时/并发/失败冷却/主模型备用）+ 视觉/网页/压缩工具。 |
| ⭐ 2 | [halosb/dsh-bg-beautify](https://github.com/halosb/dsh-bg-beautify) | DSH Web UI beautification plugin: background images + translucent panels with live settings page. / DSH Web UI 美化插件：背景图 + 面板半透明，设置页实时调节。 |


| ⭐ 0 | [Xrainsmile/DSH-Plugin-Doctor](https://github.com/Xrainsmile/DSH-Plugin-Doctor) | Compatibility, security, isolated install, and rollback doctor for DeepSeek Harness plugins — diagnose and fix broken bundles. / DSH 插件医生：兼容性检查、安全扫描、隔离安装与回滚修复。 |
---

## 🤝 Contributing / 贡献

We welcome contributions of all kinds — new plugins, bug fixes, documentation, or scan source adapters.

### Add a Plugin / 添加插件

```sh
# 1. Configure your tokens
cp .env.example .env
chmod 600 .env
# Edit .env: add GITHUB_TOKEN (optional), GITLAB_TOKEN if needed

# 2. Dry-run to preview changes (no write)
python3 scripts/dsh_discovery.py --repo "$(pwd)" --dry-run

# 3. Run the full discovery
python3 scripts/dsh_discovery.py --repo "$(pwd)"

# 4. Commit and push
git add README.md var/dsh-discovery-state.json var/dsh-discovery-report.json
git commit -m "chore: scan cycle — +N new plugins"
git push
```

### Run as a LaunchAgent (auto hourly) / 定时自动运行

```sh
./scripts/install-hourly-discovery.sh install   # install
./scripts/install-hourly-discovery.sh check     # verify config
./scripts/install-hourly-discovery.sh uninstall # remove
```

### Add a New Source Adapter / 新增数据源

Subclass `SourceAdapter` in `scripts/dsh_discovery/sources.py` and register it in `dsh_discovery.py`. Each adapter implements:

```python
def discover(self) -> DiscoveryResult:
    """Return hits with Candidate objects."""
```

---

## 📥 Installation / 安装

### For DSH Users / DSH 用户

```sh
# Run from npm
npx @deepseek-ai/dsh web

# Install a plugin via dsh CLI
dsh plugin --profile web add github:owner/repo#ref&path:/<plugin-path>

# Python SDK
pip install deepseek-harness-sdk
```

### For Oh-My-DSH Maintainers / 维护者

See [Contributing](#-contributing--贡献) above. The hourly discovery pipeline runs automatically via LaunchAgent on macOS.

---

## Hourly Discovery Operations

The stdlib-only discovery job writes local state and a structured report below `var/`. Preview a bounded fixture run or a no-write run with:

```sh
python3 scripts/dsh_discovery.py --repo "$(pwd)" --fixtures
python3 scripts/dsh_discovery.py --repo "$(pwd)" --dry-run
```

Both modes acquire the overlap lock but never write README/state/report and never commit or push. A normal run uses the guarded Git wrapper: it requires a clean `main` checkout at the fetched `origin/main` tip, stages only approved catalog files, never force-pushes, and skips a push without material README/data changes.

Copy `.env.example` to `.env`, set only needed tokens, and make it private: `chmod 600 .env`. Check, install, or uninstall the macOS LaunchAgent with `scripts/install-hourly-discovery.sh check|install|uninstall`; installation is explicit, uses a 3600-second interval, and never changes shell profiles.

Discovery is intentionally bounded to the configured source adapters and their request budgets. The catalog is curated rather than exhaustive; source outages, private repositories, changed APIs, and evidence rules can leave valid projects uncovered.

---

## 📊 Ecosystem Stats / 生态统计

| Metric / 指标 | Value / 数值 |
|---|---|
| Total dsh-plugin repos / 总仓库数 | **2,300+** |
| **Curated收录** | **~519+** |
| Highest-starred plugin / 最高 Star 插件 | [dsh-web-ui](https://github.com/zhu1090093659/dsh-web-ui) ⭐ 1.9k |
| Primary languages / 主要语言 | TypeScript / JavaScript / Python |
| Most active maintainers / 核心维护者 | [omdsh-dev](https://github.com/omdsh-dev), [vlln](https://github.com/vlln), [Anionex](https://github.com/Anionex), [Nagi-ovo](https://github.com/Nagi-ovo) |

---

*Last updated: 2026-08-15 · +22 new resources added across 9 categories, 16 star counts refreshed · Source: GitHub Search API + gh CLI verified · dsh-plugin topic contains 2,700+ repos, curated ~647+*
*最后更新：2026-08-15 · 本轮新增 22 个资源，覆盖 9 个类别 · 16 项 Star 计数更新 · 数据来源：GitHub Search API + gh CLI 验证 · dsh-plugin topic 共 2,700+ 仓库，精选收录约 647+ 个*

---

⭐ If this helped you navigate the DSH ecosystem, **give us a star** — it motivates continued development and helps others find this resource.
⭐ 如果这个项目帮助了你探索 DSH 生态，**点个 Star** 支持我们 — 它激励持续维护并帮助更多人发现这里。
