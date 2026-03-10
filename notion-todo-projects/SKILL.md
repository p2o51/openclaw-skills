---
name: notion-todo-projects
description: "Query Notion databases: Todo list and Projects."
metadata:
  openclaw:
    category: "productivity"
    requires:
      bins: ["curl", "jq"]
---

# Notion - Todo & Projects

Query two databases:
- 📋 **最终 Todo** - Tasks and todos
- 📁 **项目** - Project management

## Config

- API Key: `~/.config/notion/api_key`
- Databases: `~/.config/notion/databases.json`

## Query Todo

```bash
TODO_ID=$(jq -r '.todo.data_source_id' ~/.config/notion/databases.json)
curl -X POST "https://api.notion.com/v1/data_sources/$TODO_ID/query" \
  -H "Authorization: Bearer $(cat ~/.config/notion/api_key)" \
  -H "Notion-Version: 2025-09-03" \
  -d '{"page_size": 10}'
```

Fields: 任务, 状态, 领域, 截止日期, Projects

## Query Projects

```bash
PROJECT_ID=$(jq -r '.projects.data_source_id' ~/.config/notion/databases.json)
curl -X POST "https://api.notion.com/v1/data_sources/$PROJECT_ID/query" \
  -H "Authorization: Bearer $(cat ~/.config/notion/api_key)" \
  -H "Notion-Version: 2025-09-03" \
  -d '{"page_size": 10}'
```

Fields: 项目, 类别, 状态, 开始/截止日期, 关联 Todo

## Create Todo

```bash
# Database ID for creating pages (from databases.json parent)
DB_ID="108d68ca7f324588a8b3ce3f822bbe59"
curl -X POST "https://api.notion.com/v1/pages" \
  -H "Authorization: Bearer $(cat ~/.config/notion/api_key)" \
  -H "Notion-Version: 2025-09-03" \
  -d "{
    \"parent\": {\"database_id\": \"$DB_ID\"},
    \"properties\": {
      \"任务\": {\"title\": [{\"text\": {\"content\": \"新任务\"}}]},
      \"状态\": {\"status\": {\"name\": \"Todo\"}}
    }
  }"
```
