#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os

# Register Chinese font
try:
    pdfmetrics.registerFont(TTFont('PingFang', '/System/Library/Fonts/PingFang.ttc'))
    font_name = 'PingFang'
except:
    font_name = 'Helvetica'

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
    fontName=font_name,
    fontSize=24,
    textColor=colors.HexColor('#1a1a1a'),
    spaceAfter=30,
    alignment=TA_CENTER
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontName=font_name,
    fontSize=16,
    textColor=colors.HexColor('#2c3e50'),
    spaceAfter=12,
    spaceBefore=20
)

subheading_style = ParagraphStyle(
    'CustomSubHeading',
    parent=styles['Heading3'],
    fontName=font_name,
    fontSize=13,
    textColor=colors.HexColor('#34495e'),
    spaceAfter=8,
    spaceBefore=12
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontName=font_name,
    fontSize=10,
    textColor=colors.HexColor('#333333'),
    spaceAfter=8,
    alignment=TA_JUSTIFY,
    leading=16
)

caption_style = ParagraphStyle(
    'Caption',
    parent=styles['Normal'],
    fontName=font_name,
    fontSize=8,
    textColor=colors.grey,
    spaceAfter=4
)

# Build the document
story = []

# Title
story.append(Paragraph("OpenClaw Use Cases Report", title_style))
story.append(Spacer(1, 20))
story.append(Paragraph("Xiaohongshu 50+ Real User Cases Summary", body_style))
story.append(Spacer(1, 10))
story.append(Paragraph(f"Report Date: {datetime.now().strftime('%Y-%m-%d')}", caption_style))
story.append(Spacer(1, 30))

# Overview section
story.append(Paragraph("Data Overview", heading_style))
overview_data = [
    ['Data Source', 'Xiaohongshu Platform'],
    ['Keywords', 'OpenClaw / Clawdbot / 龙虾'],
    ['Analysis Time', 'March 2026'],
    ['Max Likes', '4000+'],
    ['Content Type', 'Tutorials, Reviews, Tips, Use Cases']
]
overview_table = Table(overview_data, colWidths=[2*inch, 4*inch])
overview_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f8f9fa')),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#2c3e50')),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, -1), font_name),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
]))
story.append(overview_table)
story.append(Spacer(1, 20))

# Main use cases
story.append(Paragraph("Main Use Cases", heading_style))

# Category 1
story.append(Paragraph("1. Programming (AI Coding)", subheading_style))
programming_cases = [
    "Use with Cursor, Claude Code, Cline for AI programming",
    "Kimi-K2.5, DeepSeek for code generation",
    "Automated code review and optimization",
    "Volcano Ark Coding Plan (9.9 CNY/month Lite)",
    "Note: Some users report compatibility issues with Kilo Code"
]
for case in programming_cases:
    story.append(Paragraph(f"- {case}", body_style))
story.append(Spacer(1, 10))

# Category 2
story.append(Paragraph("2. Office Automation", subheading_style))
office_cases = [
    "Email classification, filtering and replies",
    "Calendar management and meeting scheduling",
    "Document organization and formatting",
    "Workflow automation",
    "Data processing"
]
for case in office_cases:
    story.append(Paragraph(f"- {case}", body_style))
story.append(Spacer(1, 10))

# Category 3
story.append(Paragraph("3. File Management", subheading_style))
file_cases = [
    "Folder organization and classification",
    "Batch file deletion",
    "File content analysis and summary",
    "WARNING: Users reported accidentally deleting D drive",
    "Recommendation: Test on cloud first"
]
for case in file_cases:
    story.append(Paragraph(f"- {case}", body_style))
story.append(Spacer(1, 10))

# Category 4
story.append(Paragraph("4. Messaging", subheading_style))
social_cases = [
    "WeChat / Telegram / Feishu integration",
    "Control AI assistant via messages",
    "Auto-reply and customer service",
    "Group management"
]
for case in social_cases:
    story.append(Paragraph(f"- {case}", body_style))
story.append(Spacer(1, 10))

# Category 5
story.append(Paragraph("5. Life Assistant", subheading_style))
life_cases = [
    "Online shopping price comparison",
    "Food delivery recommendations",
    "Travel route planning",
    "News aggregation",
    "Video summarization (Bilibili, Douyin, Xiaohongshu)"
]
for case in life_cases:
    story.append(Paragraph(f"- {case}", body_style))
story.append(Spacer(1, 10))

# Skills
story.append(Paragraph("6. Popular Skills", subheading_style))
skills_data = [
    ['Skill', 'Function', 'Rating'],
    ['Weather', 'Real-time weather', '5 stars'],
    ['Video Summary', 'AI video summarization', '5 stars'],
    ['Stock', 'Stock quotes', '4 stars'],
    ['Email', 'Gmail automation', '4 stars'],
    ['Calendar', 'Google Calendar sync', '4 stars'],
    ['Notion', 'Note management', '3 stars'],
]
skills_table = Table(skills_data, colWidths=[1.5*inch, 3*inch, 0.8*inch])
skills_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), font_name),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
]))
story.append(skills_table)
story.append(Spacer(1, 20))

story.append(PageBreak())

# Popular posts
story.append(Paragraph("Popular Posts Analysis", heading_style))
popular_posts = [
    ['Title', 'Likes', 'Content'],
    ['OpenClaw Full Tutorial (4.6K)', '4,673', 'Installation guide'],
    ['Amazing OpenClaw Uses (4.2K)', '4,254', 'Creative use cases'],
    ['Clawdbot Deployment (2.8K)', '2,885', 'Cloud deployment'],
    ['Must-have Skills (2.2K)', '2,267', 'Recommended skills'],
    ['Non-tech User Guide (3.1K)', '3,116', 'Beginner friendly'],
]
posts_table = Table(popular_posts, colWidths=[2.8*inch, 0.8*inch, 2.4*inch])
posts_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#e74c3c')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (1, 0), 'CENTER'),
    ('ALIGN', (2, 0), (2, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), font_name),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')])
]))
story.append(posts_table)
story.append(Spacer(1, 20))

# User feedback
story.append(Paragraph("User Feedback Summary", heading_style))

story.append(Paragraph("Positive", subheading_style))
positive_feedback = [
    "- Truly 'from talk to action' - AI actually does the work",
    "- Low barrier: runs on 2GB RAM, one-line install",
    "- No vendor lock-in: OpenAI, Anthropic, domestic models",
    "- Cross-platform: Mac, Windows, Linux",
    "- Affordable: Volcano Ark 9.9 CNY/month",
    "- Rich skills ecosystem"
]
for fb in positive_feedback:
    story.append(Paragraph(fb, body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Negative", subheading_style))
negative_feedback = [
    "- Security risk: may delete important files",
    "- Not suitable for 90% of ordinary users",
    "- Compatibility issues with some tools",
    "- Token consumption is fast",
    "- Chinese ecosystem needs improvement"
]
for fb in negative_feedback:
    story.append(Paragraph(fb, body_style))
story.append(Spacer(1, 10))

story.append(Paragraph("Recommendations", subheading_style))
advice_feedback = [
    "- Test on cloud server first",
    "- Set proper file access permissions",
    "- Choose cost-effective models",
    "- Install skills from trusted sources"
]
for fb in advice_feedback:
    story.append(Paragraph(fb, body_style))
story.append(Spacer(1, 20))

# Best practices
story.append(Paragraph("Best Practices", heading_style))
tips = [
    ("Beginners", "Start with cloud deployment before local"),
    ("Model Choice", "Volcano Ark Coding Plan (9.9 CNY/month)"),
    ("Security", "Set file access permissions properly"),
    ("Skills", "Install from official/trusted sources"),
    ("Cost Control", "Monitor token usage")
]
for title, content in tips:
    story.append(Paragraph(f"<b>{title}</b>: {content}", body_style))
    story.append(Spacer(1, 6))

story.append(Spacer(1, 20))

# Conclusion
story.append(Paragraph("Conclusion", heading_style))
conclusion = """OpenClaw, as an open-source AI assistant, is changing human-AI collaboration. From programming to daily life, from personal efficiency to workflow automation, it demonstrates AI's powerful ability to "actually do the work."

However, like any powerful tool, OpenClaw has learning curves and security risks. Users should:
- Start with simple tasks
- Understand permission settings
- Test in sandbox environment before production
- Follow community for latest updates

The future of AI belongs to those who leverage tools to improve efficiency."""
story.append(Paragraph(conclusion, body_style))
story.append(Spacer(1, 30))

# Footer
story.append(Paragraph("=" * 50, caption_style))
story.append(Paragraph("Data Source: Xiaohongshu Public Content", caption_style))
story.append(Paragraph("Analysis Tool: OpenClaw AI Assistant", caption_style))
story.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", caption_style))

# Build PDF
doc.build(story)
print(f"PDF generated: {output_path}")
