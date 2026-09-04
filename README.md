# 0Land

> 大厂 AI Agent 开发实习备战计划 · 2026.09 → 2027.04

## 🎯 目标

- **2027 年春季（2-4 月）拿到大厂 AI Agent 开发实习 offer**
- 目标公司：字节 / 阿里 / 腾讯（同步投 AI 创业公司练手与保底）
- 岗位定位：**大模型应用开发 / Agent 工程岗**（工程向，非算法岗）
- 主语言：Python

## 📋 个人定位

- 研二在读，非计算机专业
- 现状：Python / Java 语法基础 ✓ ｜ 数据结构 ✗ ｜ 项目经验 ✗
- 差异化打法：两个可演示的开源项目 + 扎实刷题 + 持续技术输出

## 🧵 三条并行主线

| 主线 | 内容 | 每日投入 | 时间跨度 |
| :--- | :--- | :--- | :--- |
| ① 算法刷题 | 数据结构打底 → 代码随想录 → Hot 100 二刷 | 1.5-2h | 9 月 → 面试 |
| ② LLM/Agent 项目 | Python 工程 → LLM 基础 → 两个开源项目 | 2-3h | 9 月 → 1 月 |
| ③ 八股 | 网络 → OS → MySQL/Redis → Python 语言面 | 1h | 10 月 → 1 月 |

## 🗓️ 分月计划

### 2026.09 ｜ Python 工程能力（项目线地基）

| 周 | 内容 | 交付物 |
| :--- | :--- | :--- |
| 第 1 周 | 装饰器、生成器、上下文管理器、异常处理、类型标注 | 带重试和计时的 HTTP 请求装饰器 |
| 第 2 周 | asyncio 入门 | 并发请求 20 个 URL，对比同步性能 |
| 第 3 周 | FastAPI 官方教程 | TODO 应用：CRUD + SQLite |
| 第 4 周 | JWT 鉴权、Pydantic 校验、错误处理 | TODO 加登录鉴权 + 第一篇技术博客 |

✅ **验收标准**：不看教程，独立写出带数据库和鉴权的 FastAPI REST API

### 2026.10 ｜ LLM 应用基础

| 周 | 内容 | 交付物 |
| :--- | :--- | :--- |
| 第 1 周 | Prompt 工程 + 对话补全 API | 调通第一条消息 |
| 第 2 周 | 流式输出、token 计费、多轮对话管理 | CLI 对话助手（多轮记忆 + 流式） |
| 第 3 周 | **Tool Calling 吃透**（agent 的地基） | 查天气/查快递助手 |
| 第 4 周 | 结构化输出、错误重试 | LLM 文本转结构化数据存入 SQLite + 博客 |

✅ **验收标准**：不看教程，独立写出带 tool calling 的 agent 循环

### 2026.11 ｜ Agent 核心 + 项目 1

- 必读经典：Anthropic《Building Effective Agents》《Writing Tools for Agents》、OpenAI《A Practical Guide to Building Agents》
- 手写 agent loop（先不用框架）→ ReAct、上下文管理、记忆、重试
- LangGraph 官方教程（graph / state / checkpoint / human-in-the-loop）
- MCP：原理 + 手写一个 MCP server
- **项目 1：个人知识库问答 Agent**（11 月中启动，约 5 周）
  - 文档解析 → 分块 → embedding → 向量库（Chroma）→ 检索 → 重排 → 带引用生成
  - Agent 化：query 改写、检索质量自检、多路召回
  - 加分：Langfuse tracing + eval 评测集
  - 要求：全程自己写代码、开源、README、技术博客

✅ **验收标准**：项目 1 开源，三篇经典文章读完，刷题 150+

### 2026.12 ｜ 进阶 + 项目 2

- 多智能体编排（planner / executor / reviewer）、agent 评测、成本与延迟优化、流式 + 前端
- **项目 2：多智能体内容生产流水线**（选题 → 调研 → 写作 → 审校，LangGraph 编排）
- 部署到公网，简历放链接，面试官可当场试用
- 可选加分：给 LangChain / LangGraph / Dify 提 PR、hackathon / Coze 比赛

✅ **验收标准**：项目 2 上线公网，简历 v1

### 2027.01 ｜ 打磨与冲刺

- 两个项目：补测试、补 eval、录 demo 视频
- 简历 STAR 写法 + 量化指标（准确率、延迟、成本）
- 八股四科过完一轮，牛客面经自测

### 2027.02-04 ｜ 投递与面试

- 1 月中起投日常实习，2 月底起投暑期实习春招正式批（内推优先）
- 每次面试 24h 内复盘，高频问题沉淀笔记

## ⏰ 每日节奏（有课日）

```
早上 1.5h   算法（固定，雷打不动）
课间 30min  八股碎片化阅读
晚上 2.5h   项目开发
周末        算法周赛 + 项目大块时间 + 写博客
```

## 🏁 里程碑检查清单

- [ ] 09 月第 2 周：仓库建立、WSL2 + 开发环境就绪、数据结构打底开始
- [ ] 10 月第 4 周：刷题 80+、CLI 对话助手 + tool calling demo 完成
- [ ] 11 月第 4 周：刷题 150+、项目 1 开源、三篇经典 agent 文章读完
- [ ] 12 月第 4 周：项目 2 上线公网、简历 v1
- [ ] 01 月第 4 周：简历 v2 投出第一批、八股四科过完一轮
- [ ] 02-04 月：面试 10+ 场、复盘文档持续更新

## 📁 仓库目录规划

```
.
├── README.md     # 学习计划与进展（本文件）
├── notes/        # 学习笔记与面试复盘
├── practice/     # Python 工程练习
└── projects/     # 项目 1 / 项目 2
```

## 📚 学习资源

| 方向 | 资源 |
| :--- | :--- |
| 算法 | [代码随想录](https://programmercarl.com)、LeetCode、王道数据结构（B 站） |
| Python | 廖雪峰 Python、realpython asyncio、[FastAPI 官方文档](https://fastapi.tiangolo.com) |
| LLM | 李宏毅《生成式 AI 导论》（B 站）、OpenAI Cookbook、Anthropic 文档 |
| Agent | [Building Effective Agents](https://anthropic.com/engineering/building-effective-agents)、[LangGraph 文档](https://langchain-ai.github.io/langgraph/)、[MCP](https://modelcontextprotocol.io) |
| 八股 | [小林 coding](https://xiaolincoding.com)、JavaGuide、牛客面经 |

---

> 每周更新进展，每学一个知识点必落到代码，每两周一篇技术博客。
