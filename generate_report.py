#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

# Create the PDF document
output_path = os.path.expanduser("~/Desktop/OpenClaw小红书使用实例报告.pdf")
doc = SimpleDocTemplate(output_path, pagesize=A4,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)

# Styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=30,
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=12,
    spaceBefore=20
)

subheading_style = ParagraphStyle(
    'CustomSubHeading',
    parent=styles['Heading3'],
    fontSize=13,
    textColor=colors.HexColor('#34495e'),
    spaceAfter=8,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=10,
    textColor=colors.HexColor('#333333'),
    spaceAfter=8,
    alignment=TA_JUSTIFY,
    leading=16
)

caption_style = ParagraphStyle(
    'Caption',
    parent=styles['Normal'],
    fontSize=8,
    textColor=colors.grey,
    spaceAfter=4
)

# Build the document
story = []

# Title
story.append(Paragraph("🦞 OpenClaw 使用实例分析报告", title_style))
story.append(Spacer(1, 20))
story.append(Paragraph("小红书 50+ 真实用户案例汇总", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph(f"报告生成日期: {datetime.now().strftime('%Y年%m月%d日')}", caption_style))
story.append(Spacer(1, 30))

# Overview section
story.append(Paragraph("📊 数据概览", heading_style))
overview_data = [
    ['数据来源', '小红书平台'],
    ['搜索关键词', 'OpenClaw / 龙虾 / Clawdbot'],
    ['分析时间', '2026年3月'],
    ['热度范围', '最高 4000+ 点赞'],
    ['内容类型', '教程、评测、避坑指南、使用案例']
]
overview_table = Table(overview_data, colWidths=[2*inch, 4*inch])
overview_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8f9fa')),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#2c3e50')),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
]))
story.append(overview_table)
story.append(Spacer(1, 20))

# Main use cases
story.append(Paragraph("🔍 主要使用场景分类", heading_style))

# Category 1: 编程开发
story.append(Paragraph("1. 编程开发 (AI Coding)", subheading_style))
programming_cases = [
    "✅ 配合 Cursor、Claude Code、Cline 等 IDE 实现 AI 编程",
    "✅ 使用 Kimi-Double 2.5、DeepSeek 等国产模型进行代码生成",
    "✅ 自动化代码审查和优化",
    "✅ 接通火山方舟 Coding Plan 实现低成本编程 (9.9元/月 Lite)",
    "⚠️ 部分用户反馈 Kilo Code 等工具存在兼容性问题"
]
for case in programming_cases:
    story.append(Paragraph(f"• {case}", body_style))
story.append(Spacer(1, 10))

# Category 2: 自动化办公
story.append(Paragraph("2. 自动化办公", subheading_style))
office_cases = [
    "📧 邮件自动分类、筛选和回复",
    "📅 日程管理和会议安排",
    "📝 文档整理与格式化",
    "🔄 重复性工作流程自动化",
    "📊 数据处理与表格整理"
]
for case in office_cases:
    story.append(Paragraph(f"• {case}", body_style))
story.append(Spacer(1, 10))

# Category 3: 文件管理
story.append(Paragraph("3. 文件管理", subheading_style))
file_cases = [
    "📂 文件夹整理与分类",
    "🗑️ 批量删除不需要的文件",
    "📋 文件内容分析与摘要",
    "⚠️ 警告：有用户反馈意外删除了D盘，建议先在测试环境使用",
    "💡 建议：使用云服务器先行测试后再用于生产环境"
]
for case in file_cases:
    story.append(Paragraph(f"• {case}", body_style))
story.append(Spacer(1, 10))

# Category 4: 社交通讯
story.append(Paragraph("4. 社交通讯", subheading_style))
social_cases = [
    "💬 接入微信/Telegram/飞书等通讯平台",
    "📱 通过消息发送指令控制 AI 助手",
    "🔔 自动回复和客服功能",
    "📢 群组管理和消息处理"
]
for case in social_cases:
    story.append(Paragraph(f"• {case}", body_style))
story.append(Spacer(1, 10))

# Category 5: 生活助手
story.append(Paragraph("5. 生活助手", subheading_style))
life_cases = [
    "🛒 网购比价和商品推荐",
    "🍽️ 餐饮外卖推荐和下单",
    "🚗 出行路线规划和预约",
    "📰 新闻资讯汇总和解读",
    "🎬 视频内容总结（支持 B站、小红书、抖音等）"
]
for case in life_cases:
    story.append(Paragraph(f"• {case}", body_style))
story.append(Spacer(1, 10))

# Category 6: 技能扩展
story.append(Paragraph("6. 技能扩展 (Skills)", subheading_style))
skills_intro = """用户可以通过安装不同的 Skills 来扩展 OpenClaw 的功能。根据小红书热门帖子推荐，以下是热门技能："""
story.append(Paragraph(skills_intro, body_style))

skills_data = [
    ['技能名称', '功能描述', '热度'],
    ['天气查询', '获取实时天气和预报', '⭐⭐⭐⭐⭐'],
    ['视频总结', 'B站/抖音/小红书视频AI总结', '⭐⭐⭐⭐⭐'],
    ['股票行情', '实时股价和交易分析', '⭐⭐⭐⭐'],
    ['邮件管理', 'Gmail 邮件自动处理', '⭐⭐⭐⭐'],
    ['日历同步', 'Google Calendar 集成', '⭐⭐⭐⭐'],
    ['Notion集成', '笔记和数据库管理', '⭐⭐⭐'],
    ['GitHub集成', '代码仓库操作', '⭐⭐⭐'],
    ['浏览器控制', '自动化网页操作', '⭐⭐⭐'],
]
skills_table = Table(skills_data, colWidths=[1.5*inch, 3*inch, 0.8*inch])
skills_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
]))
story.append(skills_table)
story.append(Spacer(1, 20))

# Page break
story.append(PageBreak())

# Popular posts section
story.append(Paragraph("🔥 热门帖子案例分析", heading_style))

posts_intro = """以下是小红书上最受欢迎的 OpenClaw 相关帖子，反映了用户最关心的内容："""
story.append(Paragraph(posts_intro, body_style))
story.append(Spacer(1, 10))

popular_posts = [
    ['标题', '点赞数', '主要内容'],
    ['火爆全网的OpenClaw，如何使用？【保姆级】', '4,673', '详细安装教程和入门指南'],
    ['龙虾的惊人用法：现在还有啥是AI不能干的', '4,254', 'OpenClaw 各种脑洞大开的用法'],
    ['Clawdbot 保姆级 部署教程', '2,885', '云端部署完整攻略'],
    ['OpenClaw值得安装的skills❗', '2,267', '推荐必装的实用技能'],
    ['开工第四天，一个文科生跑通了OpenClaw', '3,116', '非技术用户入门分享'],
    ['废物人类的OpenClaw机器人公司', '1,908', '用AI运营自动化公司'],
    ['为什么还没人对龙虾之父发骚？', '1,038', '对创始人的调侃'],
    ['openclaw真牛，把我D盘删了个干净', '426', '安全警告：文件删除风险'],
    ['openclaw 不适合90%的普通人', '479', '理性分析适用人群'],
    ['根本不会用openclaw', '347', '新手入门困难吐槽'],
]
posts_table = Table(popular_posts, colWidths=[2.8*inch, 0.8*inch, 2.4*inch])
posts_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (1, 0), 'CENTER'),
    ('ALIGN', (2, 0), (2, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
]))
story.append(posts_table)
story.append(Spacer(1, 20))

# User feedback
story.append(Paragraph("💬 用户反馈总结", heading_style))

story.append(Paragraph("正面评价 (👍)", subheading_style))
positive_feedback = [
    "• 真正的「从动嘴到动手」，AI不只是给建议，而是真的干活",
    "• 门槛低，2GB内存就能跑，一行命令安装",
    "• 不绑定供应商，OpenAI、Anthropic、国产模型随便用",
    "• 支持多平台：Mac、Windows、Linux",
    "• 火山方舟 Coding Plan 价格实惠 (9.9元/月起)",
    "• 技能系统丰富，可扩展性强"
]
for fb in positive_feedback:
    story.append(Paragraph(fb, body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("负面评价 (👎)", subheading_style))
negative_feedback = [
    "• 有安全隐患：可能误删重要文件（已有D盘被删案例）",
    "• 不适合90%的普通人，需要一定技术基础",
    "• 部分工具存在兼容性问题（如Kilo Code）",
    "• 遇到文件冲突会死循环，还扣额度",
    "• Token消耗快，需要持续付费",
    "• 中文生态支持有待完善"
]
for fb in negative_feedback:
    story.append(Paragraph(fb, body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("建议反馈 (💡)", subheading_style))
advice_feedback = [
    "• 建议先在云服务器上测试，熟悉后再用于生产环境",
    "• 注意文件操作权限，设置合理的访问限制",
    "• 选择性价比高的模型（如火山方舟、豆包等）",
    "• 关注Skills的安全性，避免安装来路不明的技能"
]
for fb in advice_feedback:
    story.append(Paragraph(fb, body_style))
story.append(Spacer(1, 20))

# Usage tips
story.append(Paragraph("⚙️ 最佳实践建议", heading_style))

tips = [
    ("1. 新手入门", "建议先使用云服务器部署，熟悉操作后再考虑本地部署"),
    ("2. 模型选择", "国内用户推荐火山方舟 Coding Plan（9.9元/月 Lite），性价比高"),
    ("3. 安全优先", "设置文件访问权限，避免授予全部文件访问权限"),
    ("4. 技能安装", "从官方或可信来源安装Skills，注意权限要求"),
    ("5. 成本控制", "使用Pro模式时注意Token消耗，可设置预算提醒"),
    ("6. 渠道选择", "飞书/微信/Telegram等消息平台使用最方便")
]
for title, content in tips:
    story.append(Paragraph(f"<b>{title}</b>: {content}", body_style))
    story.append(Spacer(1, 6))

story.append(Spacer(1, 20))

# Conclusion
story.append(Paragraph("📝 结论", heading_style))
conclusion = """OpenClaw 作为一款开源 AI 助手，正在改变人机协作的方式。从编程开发到日常生活，从个人效率提升到自动化工作流，它展现了 AI "从动嘴到动手"的强大能力。

然而，如同任何强大工具一样，OpenClaw 也存在一定的学习门槛和安全风险。建议用户：
- 从简单任务开始尝试
- 充分了解权限设置
- 在测试环境验证后再用于生产
- 关注社区最新动态和安全更新

AI 的未来，属于那些善于利用工具提升效率的人。希望这份报告能帮助你更好地了解 OpenClaw 的实际应用场景。"""
story.append(Paragraph(conclusion, body_style))
story.append(Spacer(1, 30))

# Footer
story.append(Paragraph("=" * 50, caption_style))
story.append(Paragraph("📊 数据来源：小红书平台公开内容", caption_style))
story.append(Paragraph("🤖 分析工具：OpenClaw AI 助手", caption_style))
story.append(Paragraph(f"🔗 报告生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", caption_style))

# Build PDF
doc.build(story)
print(f"✅ PDF报告已生成: {output_path}")
