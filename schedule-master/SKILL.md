---
name: schedule-master
description: "日程管理中枢：整合 Google Calendar、Notion Todo、Notion Projects，提供完整的日程概览。"
---

# 日程管理指南

## 主人（51哥）的日程放在哪里？

| 类型 | 位置 | 用途 | 查询方式 |
|------|------|------|----------|
| 🗓️ **固定时间日程** | Google Calendar | 有明确时间的约会、截止日 | `gws calendar` |
| 📋 **待办任务** | Notion「最终 Todo」 | 无固定时间的任务、待办 | Notion API |
| 📁 **项目** | Notion「项目」 | 长期项目、视频系列 | Notion API |

## 数据库详情

从 `~/.config/notion/databases.json` 读取：

**Notion「最终 Todo」**
- Data Source ID: 见 `databases.json` → `todo.data_source_id`
- 字段：任务、状态、领域、截止日期、Projects（关联）
- 状态：Todo / In Progress / Done

**Notion「项目」**
- Data Source ID: 见 `databases.json` → `projects.data_source_id`
- 字段：项目、类别、状态、开始/截止日期、关联 Todo

## 整合查询（完整日程）

当用户说以下任意一种时，执行完整日程查询：
- "完整日程"
- "今日日程"
- "看看日程"
- "schedule"
- "今天有什么安排"

**执行步骤：**

```bash
# 1. Google Calendar 今日事件
gws calendar events list --params '{
  "calendarId": "p2o51willam@gmail.com",
  "timeMin": "今天00:00:00+09:00",
  "timeMax": "今天23:59:59+09:00",
  "singleEvents": true,
  "orderBy": "startTime"
}'

# 2. Notion Todo（未完成）
TODO_ID=$(jq -r '.todo.data_source_id' ~/.config/notion/databases.json)
curl -X POST "https://api.notion.com/v1/data_sources/$TODO_ID/query" \
  -H "Authorization: Bearer $(cat ~/.config/notion/api_key)" \
  -H "Notion-Version: 2025-09-03" \
  -d '{"page_size": 20}'
# 筛选：状态 ≠ Done

# 3. Notion Projects
PROJECT_ID=$(jq -r '.projects.data_source_id' ~/.config/notion/databases.json)
curl -X POST "https://api.notion.com/v1/data_sources/$PROJECT_ID/query" \
  -H "Authorization: Bearer $(cat ~/.config/notion/api_key)" \
  -H "Notion-Version: 2025-09-03" \
  -d '{"page_size": 10}'
```

**输出格式：**
```
📅 完整日程 - 3月XX日

🗓️ 固定日程（Google Calendar）
- XX:XX 事件名

📝 待办任务（Notion Todo）
- [状态] 任务名 （领域）截止:日期

📁 活跃项目（Notion Projects）
- 项目名 （类别）

💡 今日重点：...
```

## 单独查询

| 需求 | 使用的 Skill | 命令 |
|------|-------------|------|
| 只看日历 | gws-calendar | `gws calendar events list` |
| 只看待办 | notion-todo-projects | Notion API query |
| 只看项目 | notion-todo-projects | Notion API query |
| 发邮件 | gws-gmail-send | `gws gmail users messages send` |

## 关联关系

- Todo 里的「Projects」字段 → 关联到项目数据库
- 项目里的「关联 Todo」字段 → 关联到 Todo 数据库
- Calendar 固定日程可以对应到某个 Todo 或项目

## 早报配置

- **早报A（8:00）**：天气 + Gmail
- **早报B（8:30）**：Calendar + Todo + Projects
