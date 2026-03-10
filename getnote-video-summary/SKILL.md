---
name: getnote-video-summary
description: |
  使用 Get 笔记 API 自动提取视频内容并生成 AI 总结。
  支持 B站、小红书、抖音、YouTube 等平台。
  
  **当用户说「总结这个视频」「提取视频内容」「帮我分析这个视频」且提供视频链接时使用此技能。**
---

# Get 笔记视频总结 (API 版)

通过 Get 笔记 API 自动处理视频链接，获取 AI 生成的结构化摘要和完整转写内容。

## 支持平台

- B站 (bilibili.com / b23.tv)
- 小红书 (xiaohongshu.com / xhsm.com)
- 抖音 (douyin.com)
- YouTube (youtube.com)

## 使用方法

### 方式一：直接调用脚本（推荐）

```bash
# 基础用法 - 获取 AI 摘要
~/.openclaw/workspace/skills/getnote-video-summary/extract.sh "<视频链接>"

# 完整模式 - 同时输出转写原文
~/.openclaw/workspace/skills/getnote-video-summary/extract.sh "<视频链接>" --full
```

### 方式二：手动 API 调用

如需自定义处理流程，可直接调用 Get 笔记 API：

#### 1. 创建链接笔记
```bash
curl -X POST 'https://openapi.biji.com/open/api/v1/resource/note/save' \
  -H 'Authorization: gk_live_<API_KEY>' \
  -H 'X-Client-ID: <CLIENT_ID>' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "视频笔记",
    "note_type": "link",
    "link_url": "https://b23.tv/xxxx",
    "tags": ["视频总结"]
  }'
```

**响应示例**：
```json
{
  "success": true,
  "data": {
    "tasks": [{"task_id": "xxx", "url": "..."}]
  }
}
```

#### 2. 轮询任务进度
```bash
curl -X POST 'https://openapi.biji.com/open/api/v1/resource/note/task/progress' \
  -H 'Authorization: gk_live_<API_KEY>' \
  -H 'X-Client-ID: <CLIENT_ID>' \
  -H 'Content-Type: application/json' \
  -d '{"task_id": "xxx"}'
```

**状态说明**：
- `pending` - 等待处理
- `processing` - AI 处理中（通常 20-40 秒）
- `success` - 处理完成
- `failed` - 处理失败

#### 3. 获取笔记详情
```bash
curl -X GET 'https://openapi.biji.com/open/api/v1/resource/note/detail?id=<NOTE_ID>' \
  -H 'Authorization: gk_live_<API_KEY>' \
  -H 'X-Client-ID: <CLIENT_ID>'
```

**关键字段**：
- `data.note.content` - AI 生成的结构化摘要（Markdown 格式）
- `data.note.web_page.content` - 视频转写原文
- `data.note.title` - 自动生成的标题
- `data.note.tags` - AI 自动生成的标签

## 输出示例

```
📝 正在创建链接笔记...
✅ 笔记任务已创建
🆔 Task ID: 69ad759105edc2672866b3f7
⏳ 等待 AI 处理中...
  处理中... (1/20)
  处理中... (2/20)
  ...
✅ 处理完成！笔记 ID: 1903717953719931464
📄 正在获取摘要内容...

═══════════════════════════════════════
           📺 视频 AI 总结
═══════════════════════════════════════

🎬 免费无限制OpenCore配置指南：基于NVIDIA API与千问大模型的搭建方案

### 🔑 核心方案概述
- **免费无限制**：使用完全免费的NVIDIA API token...
...

💾 已保存至 Get笔记
🆔 笔记 ID: 1903717953719931464
```

## 处理时间

- 10 分钟以内的视频：约 20-40 秒
- 10-30 分钟视频：约 40-90 秒
- 30 分钟以上：可能需要 2-5 分钟

## API 配置

脚本已内置默认 API Key，如需使用自己的账号，设置环境变量：

```bash
export GETNOTE_API_KEY=gk_live_your_key
export GETNOTE_CLIENT_ID=cli_your_client_id
```

获取 API Key：https://www.biji.com/openapi

## 与 Get 笔记 skill 的关系

| Skill | 用途 | 方式 |
|-------|------|------|
| `getnote-video-summary` | 视频内容提取总结 | 自动 API 调用 |
| `Get笔记` | 通用笔记管理（创建/查询/删除） | API 调用 |

**建议组合使用**：
1. 用 `getnote-video-summary` 自动处理视频链接
2. 用 `Get笔记` skill 进行后续的笔记管理（添加标签、移入知识库等）

## 故障排查

### 问题：API 返回鉴权错误
**解决**：检查 API Key 和 Client ID 是否正确，或是否已过期

### 问题：处理状态一直为 pending/processing
**解决**：正常现象，视频较长时需要更多时间，建议耐心等待或增加轮询次数

### 问题：返回的摘要为空
**解决**：可能视频还在处理中，稍后再查询笔记详情；或该视频无法提取字幕

### 问题：某些平台视频无法处理
**解决**：部分视频因版权或平台限制无法提取，可尝试其他平台链接
