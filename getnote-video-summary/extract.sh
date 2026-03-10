#!/bin/bash
# Get笔记视频提取 - API 版本
# 自动创建链接笔记、轮询进度、获取 AI 摘要

set -e

# Get笔记 API 配置
API_KEY="${GETNOTE_API_KEY:-gk_live_d379ba1d7687b353.68eb584376d81a18f1a06c8886f2cf932003d0782a6ca082}"
CLIENT_ID="${GETNOTE_CLIENT_ID:-cli_3802f9db08b811f197679c63c078bacc}"
BASE_URL="https://openapi.biji.com"

# 参数检查
VIDEO_URL="$1"
if [ -z "$VIDEO_URL" ]; then
    echo "❌ 错误: 请提供视频链接" >&2
    echo "用法: $0 <视频链接>" >&2
    exit 1
fi

# 检查是否是视频链接
if ! echo "$VIDEO_URL" | grep -qE "(bilibili|b23\.tv|xiaohongshu|xhsm|douyin|youtube)"; then
    echo "⚠️ 警告: 链接可能不是受支持的视频平台" >&2
fi

echo "📝 正在创建链接笔记..."
echo "🔗 URL: $VIDEO_URL"

# 1. 创建链接笔记
response=$(curl -s -X POST "${BASE_URL}/open/api/v1/resource/note/save" \
  -H "Authorization: ${API_KEY}" \
  -H "X-Client-ID: ${CLIENT_ID}" \
  -H "Content-Type: application/json" \
  -d "{\"title\":\"视频笔记\",\"note_type\":\"link\",\"link_url\":\"${VIDEO_URL}\",\"tags\":[\"视频总结\",\"AI笔记\"]}")

# 检查响应
if ! echo "$response" | grep -q '"success":true'; then
    echo "❌ 创建笔记失败: $response" >&2
    exit 1
fi

# 检查是否是重复链接
duplicate_count=$(echo "$response" | grep -o '"duplicate_count":[0-9]*' | cut -d':' -f2 | head -1)

if [ "$duplicate_count" = "1" ]; then
    echo "ℹ️ 该链接已存在笔记，正在查询..."
    
    # 查询最近的笔记列表找到这个链接
    list_response=$(curl -s -X GET "${BASE_URL}/open/api/v1/resource/note/list?since_id=0" \
      -H "Authorization: ${API_KEY}" \
      -H "X-Client-ID: ${CLIENT_ID}")
    
    # 从列表中找到包含该链接的笔记
    note_id=$(echo "$list_response" | grep -o '"id":[0-9]*' | head -1 | cut -d':' -f2)
    
    if [ -z "$note_id" ]; then
        echo "❌ 无法找到已存在的笔记" >&2
        exit 1
    fi
    
    echo "✅ 找到已有笔记，ID: $note_id"
    
    # 直接获取笔记详情
    echo "📄 正在获取摘要内容..."
    
    details=$(curl -s -X GET "${BASE_URL}/open/api/v1/resource/note/detail?id=${note_id}" \
      -H "Authorization: ${API_KEY}" \
      -H "X-Client-ID: ${CLIENT_ID}")
    
    if ! echo "$details" | grep -q '"success":true'; then
        echo "❌ 获取笔记详情失败" >&2
        exit 1
    fi
    
    # 提取并输出内容
    echo ""
    echo "═══════════════════════════════════════"
    echo "           📺 视频 AI 总结"
    echo "═══════════════════════════════════════"
    echo ""
    
    title=$(echo "$details" | grep -o '"title":"[^"]*"' | cut -d'"' -f4 | head -1)
    echo "🎬 $title"
    echo ""
    
    content=$(echo "$details" | grep -o '"content":"[^"]*"' | cut -d'"' -f4 | head -1)
    
    if [ -n "$content" ]; then
        echo -e "$content"
    else
        echo "⚠️ 暂无摘要内容"
    fi
    
    echo ""
    echo "═══════════════════════════════════════"
    echo "💾 已保存至 Get笔记 (已有笔记)"
    echo "🆔 笔记 ID: $note_id"
    exit 0
fi

# 提取 task_id
task_id=$(echo "$response" | grep -o '"task_id":"[^"]*"' | cut -d'"' -f4 | head -1)

if [ -z "$task_id" ]; then
    echo "❌ 无法获取任务 ID" >&2
    exit 1
fi

echo "✅ 笔记任务已创建"
echo "🆔 Task ID: $task_id"
echo "⏳ 等待 AI 处理中..."

# 2. 轮询任务进度
max_attempts=20
attempt=0

while [ $attempt -lt $max_attempts ]; do
    attempt=$((attempt + 1))
    
    sleep 5
    
    progress=$(curl -s -X POST "${BASE_URL}/open/api/v1/resource/note/task/progress" \
      -H "Authorization: ${API_KEY}" \
      -H "X-Client-ID: ${CLIENT_ID}" \
      -H "Content-Type: application/json" \
      -d "{\"task_id\":\"${task_id}\"}")
    
    status=$(echo "$progress" | grep -o '"status":"[^"]*"' | cut -d'"' -f4 | head -1)
    
    case "$status" in
        "success")
            note_id=$(echo "$progress" | grep -o '"note_id":[0-9]*' | cut -d':' -f2 | head -1)
            echo "✅ 处理完成！笔记 ID: $note_id"
            break
            ;;
        "failed")
            echo "❌ 处理失败" >&2
            exit 1
            ;;
        "pending"|"processing")
            echo "  处理中... ($attempt/$max_attempts)"
            ;;
        *)
            echo "  未知状态: $status"
            ;;
    esac
done

if [ -z "$note_id" ]; then
    echo "⚠️ 处理时间较长，笔记仍在后台处理中" >&2
    echo "Task ID: $task_id" >&2
    exit 1
fi

# 3. 获取笔记详情
echo "📄 正在获取摘要内容..."

details=$(curl -s -X GET "${BASE_URL}/open/api/v1/resource/note/detail?id=${note_id}" \
  -H "Authorization: ${API_KEY}" \
  -H "X-Client-ID: ${CLIENT_ID}")

if ! echo "$details" | grep -q '"success":true'; then
    echo "❌ 获取笔记详情失败" >&2
    exit 1
fi

# 提取并输出内容
echo ""
echo "═══════════════════════════════════════"
echo "           📺 视频 AI 总结"
echo "═══════════════════════════════════════"
echo ""

# 提取标题
title=$(echo "$details" | grep -o '"title":"[^"]*"' | cut -d'"' -f4 | head -1)
echo "🎬 $title"
echo ""

# 提取 AI 摘要内容
content=$(echo "$details" | grep -o '"content":"[^"]*"' | cut -d'"' -f4 | head -1)

# 输出内容（处理换行）
if [ -n "$content" ]; then
    # 将 \n 替换为实际换行
    echo -e "$content"
else
    echo "⚠️ 暂无摘要内容，可能还在处理中"
fi

echo ""
echo "═══════════════════════════════════════"

# 可选：输出原文内容
if [ "$2" = "--full" ]; then
    echo ""
    echo "📝 完整转写内容："
    echo ""
    # 从 web_page.content 中提取
    full_content=$(echo "$details" | sed 's/.*"web_page":{[^}]*"content":"//;s/"[^}]*}$//' | sed 's/\\n/\n/g' | head -c 2000)
    echo "$full_content"
    echo ""
    echo "... (内容已截断，完整内容请访问 Get笔记)"
fi

echo ""
echo "💾 已保存至 Get笔记"
echo "🆔 笔记 ID: $note_id"
