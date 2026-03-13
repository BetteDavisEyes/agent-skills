# Agent Skills 规范对比

本文档对比当前项目与业界标准 [Agent Skills Specification (agentskills.io)](https://agentskills.io/specification) 及 Apify agent-skills 的差异。

## 业界标准概览

**Agent Skills** 是由 Anthropic 主导的开放格式，被 Claude、Cursor、Apify 等采用，规范见 [agentskills.io/specification](https://agentskills.io/specification)。

### 标准要求的目录结构

```
skill-name/
├── SKILL.md          # 必需：YAML frontmatter + Markdown 指令
├── scripts/          # 可选：可执行代码
├── references/       # 可选：补充文档
├── assets/           # 可选：模板、资源
└── ...
```

### SKILL.md 必需字段

| 字段 | 约束 |
|------|------|
| `name` | 1-64 字符，仅小写字母、数字、连字符，与目录名一致 |
| `description` | 1-1024 字符，描述做什么及何时使用 |

### 可选字段

- `license` - 许可证
- `compatibility` - 环境要求（产品、依赖、网络）
- `metadata` - 任意键值对
- `allowed-tools` - 预批准工具列表（实验性）

---

## 当前项目 vs 标准

| 维度 | 业界标准 | 当前项目 | 状态 |
|------|----------|----------|------|
| **核心文件** | SKILL.md | SKILL.md + skill.json + README.md | ✅ |
| **name 格式** | lowercase + hyphens | lowercase + underscores（可用 --spec-compliant） | ⚠️ 可选 |
| **frontmatter** | name, description, license, metadata... | 已包含 | ✅ |
| **指令内容** | SKILL.md body | SKILL.md body | ✅ |
| **Tool Schema** | 非标准要求 | skill.json ✓ | ✓ 扩展能力 |
| **示例** | 可选 | example.json ✓ | ✓ |
| **scripts/** | 可选 | 无 | - |
| **references/** | 可选 | 无 | - |
| **渐进式披露** | metadata 常驻、body 按需 | SKILL.md 含 metadata | ✅ |

---

## 双重定位说明

当前项目同时服务两种用途：

1. **Tool Schema（程序化）**：skill.json 提供 JSON Schema，供 OpenAI/Anthropic function calling、LangChain 等框架使用
2. **Agent Instructions（语义）**：SKILL.md 提供人类可读指令，供 Claude、Cursor 等 agent 理解何时用、怎么用

业界标准以 **SKILL.md** 为核心；skill.json 是项目扩展，用于 MCP 工具的程序化调用。

---

## 已实施的优化

- [x] 为每个 skill 生成 SKILL.md（符合 agentskills.io）
- [x] 添加 license、metadata、compatibility 等 frontmatter
- [x] 支持 `--spec-compliant` 生成符合规范的 hyphen 命名
- [x] 添加 skill 验证脚本
- [x] 保留 skill.json 作为 tool schema
