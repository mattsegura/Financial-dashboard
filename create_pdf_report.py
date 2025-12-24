#!/usr/bin/env python3
"""
Create comprehensive PDF report for NoirFlow database visualization
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib import colors
from datetime import datetime
import json

# Create PDF
pdf_filename = "NoirFlow_Database_Visualization_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter,
                       rightMargin=0.5*inch, leftMargin=0.5*inch,
                       topMargin=0.5*inch, bottomMargin=0.5*inch)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#000000'),
    spaceAfter=12,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=18,
    textColor=colors.HexColor('#000000'),
    spaceAfter=10,
    spaceBefore=15,
    fontName='Helvetica-Bold'
)

subheading_style = ParagraphStyle(
    'CustomSubHeading',
    parent=styles['Heading3'],
    fontSize=14,
    textColor=colors.HexColor('#333333'),
    spaceAfter=8,
    spaceBefore=10,
    fontName='Helvetica-Bold'
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=11,
    textColor=colors.HexColor('#000000'),
    spaceAfter=8,
    alignment=TA_LEFT,
    fontName='Helvetica'
)

# Title Page
elements.append(Spacer(1, 1.5*inch))
title = Paragraph("NoirFlow Expense Tracker", title_style)
elements.append(title)
elements.append(Spacer(1, 0.2*inch))

subtitle = Paragraph("Database Visualization Report", heading_style)
elements.append(subtitle)
elements.append(Spacer(1, 0.3*inch))

date_text = Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}", body_style)
elements.append(date_text)
elements.append(Spacer(1, 0.5*inch))

# Executive Summary
elements.append(Paragraph("Executive Summary", heading_style))
summary_text = """
This report provides a comprehensive visualization of the NoirFlow Expense Tracker database structure 
and data analysis. The application currently uses in-memory mock data stored in the Dashboard component 
(components/Dashboard.tsx). The database consists of 5 primary data models with a total of 23 records 
across transactions, subscriptions, monthly data, category data, and dashboard statistics.
"""
elements.append(Paragraph(summary_text, body_style))
elements.append(Spacer(1, 0.3*inch))

# Key Metrics Table
elements.append(Paragraph("Key Metrics", subheading_style))
metrics_data = [
    ['Metric', 'Value'],
    ['Storage Type', 'In-Memory (Mock Data)'],
    ['Location', 'components/Dashboard.tsx'],
    ['Total Records', '23'],
    ['Data Models', '5'],
    ['Transactions', '5'],
    ['Subscriptions', '3'],
    ['Monthly Data Points', '6'],
    ['Category Data Points', '4'],
]

metrics_table = Table(metrics_data, colWidths=[3*inch, 3*inch])
metrics_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#000000')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 12),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f5f5')),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 10),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
]))
elements.append(metrics_table)
elements.append(PageBreak())

# Database Schema Section
elements.append(Paragraph("Database Schema & Structure", heading_style))
schema_text = """
The NoirFlow application uses a TypeScript-based data structure with the following models:
"""
elements.append(Paragraph(schema_text, body_style))
elements.append(Spacer(1, 0.2*inch))

# Data Models Description
models_data = [
    ['Model', 'Fields', 'Description'],
    ['Transaction', '6 fields', 'Stores expense transactions with amount, category, subcategory, date, and payment mode'],
    ['Subscription', '5 fields', 'Manages recurring subscriptions with name, renewal date, amount, and icon'],
    ['ChartDataPoint', '4 fields', 'Generic data structure for chart visualizations (monthly & category data)'],
    ['DashboardStats', '5 fields', 'Aggregated financial statistics including balance, expenses, investments, and goals'],
    ['Enums', '2 types', 'PaymentMode (UPI/Card/Bank/Cash) and TimeRange (Weekly/Monthly/Yearly)'],
]

models_table = Table(models_data, colWidths=[1.5*inch, 1.2*inch, 3.8*inch])
models_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#000000')),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 11),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f5f5')),
    ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
    ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
    ('FONTSIZE', (0, 1), (-1, -1), 9),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')]),
]))
elements.append(models_table)
elements.append(Spacer(1, 0.3*inch))

# Add main visualization image
elements.append(Paragraph("Complete Database Visualization", heading_style))
elements.append(Spacer(1, 0.2*inch))

try:
    img1 = Image('database_visualization.png', width=7*inch, height=8.4*inch)
    elements.append(img1)
except:
    elements.append(Paragraph("Error: Could not load database_visualization.png", body_style))

elements.append(PageBreak())

# Detailed Analysis Section
elements.append(Paragraph("Detailed Data Analysis", heading_style))
analysis_text = """
The following visualizations provide in-depth analysis of the transaction patterns, 
spending distribution, payment preferences, and financial metrics tracked by the application.
"""
elements.append(Paragraph(analysis_text, body_style))
elements.append(Spacer(1, 0.2*inch))

try:
    img2 = Image('database_analysis.png', width=7*inch, height=5.25*inch)
    elements.append(img2)
except:
    elements.append(Paragraph("Error: Could not load database_analysis.png", body_style))

elements.append(Spacer(1, 0.3*inch))

# Data Insights
elements.append(Paragraph("Key Insights", heading_style))

# Load and parse the JSON data
try:
    with open('database_structure.json', 'r') as f:
        data = json.load(f)
    
    transactions = data['transactions']
    subscriptions = data['subscriptions']
    stats = data['dashboard_stats']
    monthly_data = data['monthly_data']
    category_data = data['category_data']
    
    # Calculate insights
    total_transactions = len(transactions)
    avg_transaction = sum(t['amount'] for t in transactions) / total_transactions
    max_transaction = max(t['amount'] for t in transactions)
    
    # Payment mode distribution
    modes = [t['mode'] for t in transactions]
    mode_counts = {}
    for mode in modes:
        mode_counts[mode] = mode_counts.get(mode, 0) + 1
    most_used_mode = max(mode_counts, key=mode_counts.get)
    
    total_sub_cost = sum(s['amount'] for s in subscriptions)
    max_monthly = max(m['value'] for m in monthly_data)
    avg_monthly = sum(m['value'] for m in monthly_data) / len(monthly_data)
    goal_progress = (stats['goal'] / stats['goalTarget']) * 100
    
    insights_list = [
        f"• Total number of transactions recorded: {total_transactions}",
        f"• Average transaction amount: ${avg_transaction:,.2f}",
        f"• Highest single transaction: ${max_transaction:,.2f}",
        f"• Most frequently used payment method: {most_used_mode} ({mode_counts[most_used_mode]} transactions)",
        f"• Active subscriptions: {len(subscriptions)} services",
        f"• Total monthly subscription cost: ${total_sub_cost:.2f}",
        f"• Highest monthly expense recorded: ${max_monthly:,}",
        f"• Average monthly expenses: ${avg_monthly:,.0f}",
        f"• Goal completion progress: {goal_progress:.1f}%",
        f"• Top spending category: {category_data[0]['name']} (${category_data[0]['value']:,.2f})",
        f"• Current account balance: ${stats['balance']:,.2f}",
        f"• Total investments: ${stats['investment']:,.2f}",
    ]
    
    for insight in insights_list:
        elements.append(Paragraph(insight, body_style))
        elements.append(Spacer(1, 0.05*inch))
    
except Exception as e:
    elements.append(Paragraph(f"Error loading insights: {str(e)}", body_style))

elements.append(PageBreak())

# Technical Details
elements.append(Paragraph("Technical Implementation Details", heading_style))

tech_text = """
<b>Storage Architecture:</b><br/>
The application currently uses in-memory data storage with mock data defined directly in the 
Dashboard component. This approach is suitable for prototyping and demonstration purposes.
<br/><br/>
<b>Data Location:</b><br/>
• Primary data source: components/Dashboard.tsx<br/>
• Type definitions: types.ts<br/>
• Service layer: services/geminiService.ts (AI insights)<br/>
<br/>
<b>Technology Stack:</b><br/>
• Frontend: React 19.2.1 with TypeScript<br/>
• Build Tool: Vite 6.2.0<br/>
• Charts: Recharts 3.5.1<br/>
• AI Integration: Google Gemini AI (@google/genai 1.32.0)<br/>
• Icons: Lucide React 0.556.0<br/>
<br/>
<b>Data Models (TypeScript Interfaces):</b><br/>
• Transaction: Expense tracking with categorization<br/>
• Subscription: Recurring payment management<br/>
• ChartDataPoint: Visualization data structure<br/>
• DashboardStats: Aggregated financial metrics<br/>
• TimeRange: Enum for time-based filtering<br/>
<br/>
<b>Future Considerations:</b><br/>
For production deployment, consider implementing:<br/>
• Persistent storage (LocalStorage, IndexedDB, or backend database)<br/>
• API integration for real-time data synchronization<br/>
• User authentication and multi-user support<br/>
• Data backup and export functionality<br/>
• Enhanced data validation and error handling<br/>
"""

elements.append(Paragraph(tech_text, body_style))
elements.append(Spacer(1, 0.3*inch))

# Recommendations
elements.append(Paragraph("Recommendations", heading_style))

recommendations_text = """
<b>1. Database Migration:</b> Consider migrating from in-memory storage to a persistent solution 
like Firebase, Supabase, or a traditional SQL/NoSQL database for production use.
<br/><br/>
<b>2. Data Validation:</b> Implement comprehensive input validation and sanitization to ensure 
data integrity across all models.
<br/><br/>
<b>3. API Layer:</b> Create a dedicated API service layer to abstract data operations and enable 
easier migration to different storage solutions.
<br/><br/>
<b>4. State Management:</b> Consider implementing Redux, Zustand, or React Context for more 
sophisticated state management as the application scales.
<br/><br/>
<b>5. Data Export:</b> Add functionality to export financial data in standard formats (CSV, JSON, PDF) 
for user records and tax purposes.
<br/><br/>
<b>6. Real-time Sync:</b> Implement real-time data synchronization for multi-device access and 
automatic backup functionality.
"""

elements.append(Paragraph(recommendations_text, body_style))

# Footer
elements.append(Spacer(1, 0.5*inch))
footer_text = Paragraph(
    f"<i>Report generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')}</i><br/>"
    "<i>NoirFlow Expense Tracker - Database Visualization Report</i>",
    ParagraphStyle('Footer', parent=body_style, fontSize=9, textColor=colors.HexColor('#666666'), alignment=TA_CENTER)
)
elements.append(footer_text)

# Build PDF
doc.build(elements)
print(f"✓ PDF report generated: {pdf_filename}")
print(f"\nReport includes:")
print(f"  • Executive summary and key metrics")
print(f"  • Complete database schema visualization")
print(f"  • Detailed data analysis charts")
print(f"  • Key insights and statistics")
print(f"  • Technical implementation details")
print(f"  • Recommendations for production deployment")
