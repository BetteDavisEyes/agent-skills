# 多区域 MCP Endpoint 配置

Octoparse MCP Server 支持两套环境：

| 区域 | Endpoint | 说明 |
|------|----------|------|
| **international** | https://mcp.octoparse.com | 海外环境 |
| **china** | https://mcp.bazhuayu.com | 国内环境 |

## 业界标准参考

根据 [MCP Registry - Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers)，多区域配置采用 **URL Template Variables** 方式：

- 使用 `{variable}` 占位符
- `variables.choices` 定义可选值
- `variables.default` 指定默认值

## 配置方式

### 1. 环境变量（程序化调用）

```bash
# 使用国内环境
export OCTOPARSE_MCP_REGION=china

# 使用海外环境（默认）
export OCTOPARSE_MCP_REGION=international

# 或直接指定 URL 覆盖
export OCTOPARSE_MCP_URL=https://mcp.bazhuayu.com
```

### 2. Cursor MCP 配置

在 Cursor 中添加 MCP 服务器时，根据所在区域选择 URL：

- 海外：`https://mcp.octoparse.com`
- 国内：`https://mcp.bazhuayu.com`

### 3. MCP server.json（标准格式）

项目提供 `mcp/server.json`，符合 MCP Registry 规范，支持 `host` 变量选择：

```json
{
  "remotes": [{
    "url": "https://{host}",
    "variables": {
      "host": {
        "choices": ["mcp.octoparse.com", "mcp.bazhuayu.com"],
        "default": "mcp.octoparse.com"
      }
    }
  }]
}
```

### 4. SDK 运行时解析

使用 `sdk.load_skill()` 加载 skill 时，会自动根据 `OCTOPARSE_MCP_REGION` 解析 endpoint：

```python
from sdk import load_skill, get_invoke_endpoint

skill = load_skill("octoparse_get_task_scraped_data")
# skill["invoke"]["endpoint"] 已根据环境变量解析
endpoint = get_invoke_endpoint(skill)
```

## 生成 Skills 时指定区域

```bash
# 生成时使用国内 endpoint 作为默认
OCTOPARSE_MCP_REGION=china python3 generator/mcps_to_skills.py --merge

# 生成时使用海外 endpoint（默认）
python3 generator/mcps_to_skills.py --merge
```
