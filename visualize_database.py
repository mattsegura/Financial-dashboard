#!/usr/bin/env python3
"""
Database Visualization Script for NoirFlow Expense Tracker
Analyzes the app's data structure and generates comprehensive visualizations
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import seaborn as sns
from datetime import datetime
import numpy as np

# Set style
sns.set_style('whitegrid')
plt.rcParams['figure.facecolor'] = '#0a0a0a'
plt.rcParams['axes.facecolor'] = '#1a1a1a'
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['grid.color'] = '#333333'
plt.rcParams['font.family'] = 'sans-serif'

# Mock data from the app
transactions = [
    {'id': '1', 'amount': 2100.00, 'category': 'Shopping', 'subCategory': 'Amazon', 'date': '31 May 2025', 'mode': 'UPI'},
    {'id': '2', 'amount': 299.00, 'category': 'Movie', 'subCategory': 'IMAX', 'date': '28 May 2025', 'mode': 'UPI'},
    {'id': '3', 'amount': 5000.00, 'category': 'Investment', 'subCategory': 'Groww', 'date': '24 May 2025', 'mode': 'Bank'},
    {'id': '4', 'amount': 2460.00, 'category': 'Travel', 'subCategory': 'Uber', 'date': '20 May 2025', 'mode': 'Card'},
    {'id': '5', 'amount': 678.00, 'category': 'Food', 'subCategory': 'Swiggy', 'date': '15 May 2025', 'mode': 'UPI'},
]

subscriptions = [
    {'id': '1', 'name': 'Netflix', 'date': '15 June 2025', 'amount': 149.00, 'icon': 'https://picsum.photos/40/40?random=1'},
    {'id': '2', 'name': 'Spotify', 'date': '24 Aug 2025', 'amount': 49.00, 'icon': 'https://picsum.photos/40/40?random=2'},
    {'id': '3', 'name': 'Figma', 'date': '01 Jan 2026', 'amount': 3999.00, 'icon': 'https://picsum.photos/40/40?random=3'},
]

monthly_data = [
    {'name': 'Dec', 'value': 16000},
    {'name': 'Jan', 'value': 27000},
    {'name': 'Feb', 'value': 9000},
    {'name': 'Mar', 'value': 15000},
    {'name': 'Apr', 'value': 26000},
    {'name': 'May', 'value': 24000},
]

category_data = [
    {'name': 'Food', 'value': 6156, 'color': '#ffffff'},
    {'name': 'Invest', 'value': 5000, 'color': '#a3a3a3'},
    {'name': 'Shop', 'value': 4356, 'color': '#525252'},
    {'name': 'Travel', 'value': 3670, 'color': '#262626'},
]

stats = {
    'balance': 898450.00,
    'monthlyExpenses': 24093.00,
    'investment': 145555.00,
    'goal': 75000,
    'goalTarget': 145000
}

# Save data structure to JSON
database_structure = {
    'transactions': transactions,
    'subscriptions': subscriptions,
    'monthly_data': monthly_data,
    'category_data': category_data,
    'dashboard_stats': stats
}

with open('database_structure.json', 'w') as f:
    json.dump(database_structure, f, indent=2)

print("✓ Database structure saved to database_structure.json")

# Create visualizations
fig = plt.figure(figsize=(20, 24))
fig.suptitle('NoirFlow Expense Tracker - Database Visualization', 
             fontsize=24, fontweight='bold', color='white', y=0.995)

# 1. Database Schema Diagram
ax1 = plt.subplot(4, 2, 1)
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
ax1.axis('off')
ax1.set_title('Database Schema & Relationships', fontsize=16, fontweight='bold', pad=20, color='white')

# Transaction Table
trans_box = FancyBboxPatch((0.5, 6.5), 4, 2.8, boxstyle="round,pad=0.1", 
                           edgecolor='#ffffff', facecolor='#262626', linewidth=2)
ax1.add_patch(trans_box)
ax1.text(2.5, 9, 'Transaction', ha='center', fontsize=12, fontweight='bold', color='white')
ax1.text(1, 8.5, '• id: string (PK)', fontsize=9, color='#a3a3a3')
ax1.text(1, 8.1, '• amount: number', fontsize=9, color='#a3a3a3')
ax1.text(1, 7.7, '• category: string', fontsize=9, color='#a3a3a3')
ax1.text(1, 7.3, '• subCategory: string', fontsize=9, color='#a3a3a3')
ax1.text(1, 6.9, '• date: string', fontsize=9, color='#a3a3a3')
ax1.text(1, 6.6, '• mode: enum', fontsize=9, color='#a3a3a3')

# Subscription Table
sub_box = FancyBboxPatch((5.5, 6.5), 4, 2.3, boxstyle="round,pad=0.1", 
                         edgecolor='#ffffff', facecolor='#262626', linewidth=2)
ax1.add_patch(sub_box)
ax1.text(7.5, 9, 'Subscription', ha='center', fontsize=12, fontweight='bold', color='white')
ax1.text(6, 8.5, '• id: string (PK)', fontsize=9, color='#a3a3a3')
ax1.text(6, 8.1, '• name: string', fontsize=9, color='#a3a3a3')
ax1.text(6, 7.7, '• date: string', fontsize=9, color='#a3a3a3')
ax1.text(6, 7.3, '• amount: number', fontsize=9, color='#a3a3a3')
ax1.text(6, 6.9, '• icon: string (URL)', fontsize=9, color='#a3a3a3')

# DashboardStats Table
stats_box = FancyBboxPatch((0.5, 3.5), 4, 2.3, boxstyle="round,pad=0.1", 
                           edgecolor='#ffffff', facecolor='#262626', linewidth=2)
ax1.add_patch(stats_box)
ax1.text(2.5, 6, 'DashboardStats', ha='center', fontsize=12, fontweight='bold', color='white')
ax1.text(1, 5.5, '• balance: number', fontsize=9, color='#a3a3a3')
ax1.text(1, 5.1, '• monthlyExpenses: number', fontsize=9, color='#a3a3a3')
ax1.text(1, 4.7, '• investment: number', fontsize=9, color='#a3a3a3')
ax1.text(1, 4.3, '• goal: number', fontsize=9, color='#a3a3a3')
ax1.text(1, 3.9, '• goalTarget: number', fontsize=9, color='#a3a3a3')

# ChartData Tables
chart_box = FancyBboxPatch((5.5, 3.5), 4, 2.3, boxstyle="round,pad=0.1", 
                           edgecolor='#ffffff', facecolor='#262626', linewidth=2)
ax1.add_patch(chart_box)
ax1.text(7.5, 6, 'ChartDataPoint', ha='center', fontsize=12, fontweight='bold', color='white')
ax1.text(6, 5.5, '• name: string', fontsize=9, color='#a3a3a3')
ax1.text(6, 5.1, '• value: number', fontsize=9, color='#a3a3a3')
ax1.text(6, 4.7, '• color?: string', fontsize=9, color='#a3a3a3')
ax1.text(6, 4.3, '• amt?: number', fontsize=9, color='#a3a3a3')
ax1.text(6.5, 3.9, 'Used for: Monthly & Category', fontsize=8, color='#666666', style='italic')

# Enums
enum_box = FancyBboxPatch((2, 0.5), 6, 2.3, boxstyle="round,pad=0.1", 
                          edgecolor='#a3a3a3', facecolor='#1a1a1a', linewidth=1, linestyle='--')
ax1.add_patch(enum_box)
ax1.text(5, 2.5, 'Enums & Types', ha='center', fontsize=12, fontweight='bold', color='white')
ax1.text(2.5, 2.1, '• PaymentMode:', fontsize=9, color='#a3a3a3')
ax1.text(3.5, 2.1, 'UPI | Card | Bank | Cash', fontsize=9, color='#666666')
ax1.text(2.5, 1.7, '• TimeRange:', fontsize=9, color='#a3a3a3')
ax1.text(3.5, 1.7, 'Weekly | Monthly | Yearly', fontsize=9, color='#666666')
ax1.text(2.5, 1.3, '• Storage:', fontsize=9, color='#a3a3a3')
ax1.text(3.5, 1.3, 'In-Memory (Mock Data)', fontsize=9, color='#666666')
ax1.text(2.5, 0.9, '• Location:', fontsize=9, color='#a3a3a3')
ax1.text(3.5, 0.9, 'components/Dashboard.tsx', fontsize=9, color='#666666')

# 2. Transaction Distribution by Category
ax2 = plt.subplot(4, 2, 2)
categories = [t['category'] for t in transactions]
category_counts = {}
for cat in categories:
    category_counts[cat] = category_counts.get(cat, 0) + 1

colors = ['#ffffff', '#a3a3a3', '#737373', '#525252', '#404040']
bars = ax2.bar(category_counts.keys(), category_counts.values(), color=colors[:len(category_counts)], 
               edgecolor='white', linewidth=1.5)
ax2.set_title('Transaction Count by Category', fontsize=14, fontweight='bold', pad=15, color='white')
ax2.set_xlabel('Category', fontsize=11, color='white')
ax2.set_ylabel('Count', fontsize=11, color='white')
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.set_facecolor('#1a1a1a')
for spine in ax2.spines.values():
    spine.set_color('#333333')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontsize=10, color='white', fontweight='bold')

# 3. Transaction Amounts Distribution
ax3 = plt.subplot(4, 2, 3)
amounts = [t['amount'] for t in transactions]
categories_for_amounts = [t['category'] for t in transactions]

bars = ax3.barh(categories_for_amounts, amounts, color=['#ffffff', '#d4d4d4', '#a3a3a3', '#737373', '#525252'], 
                edgecolor='white', linewidth=1.5)
ax3.set_title('Transaction Amounts by Category', fontsize=14, fontweight='bold', pad=15, color='white')
ax3.set_xlabel('Amount ($)', fontsize=11, color='white')
ax3.set_ylabel('Category', fontsize=11, color='white')
ax3.grid(axis='x', alpha=0.3, linestyle='--')
ax3.set_facecolor('#1a1a1a')
for spine in ax3.spines.values():
    spine.set_color('#333333')

# Add value labels
for i, (bar, amount) in enumerate(zip(bars, amounts)):
    ax3.text(amount + 100, bar.get_y() + bar.get_height()/2,
             f'${amount:,.2f}',
             ha='left', va='center', fontsize=9, color='white', fontweight='bold')

# 4. Payment Mode Distribution
ax4 = plt.subplot(4, 2, 4)
modes = [t['mode'] for t in transactions]
mode_counts = {}
for mode in modes:
    mode_counts[mode] = mode_counts.get(mode, 0) + 1

colors_pie = ['#ffffff', '#a3a3a3', '#737373', '#525252']
wedges, texts, autotexts = ax4.pie(mode_counts.values(), labels=mode_counts.keys(), autopct='%1.1f%%',
                                     colors=colors_pie[:len(mode_counts)], startangle=90,
                                     textprops={'color': 'white', 'fontsize': 11, 'fontweight': 'bold'},
                                     wedgeprops={'edgecolor': 'black', 'linewidth': 2})
ax4.set_title('Payment Mode Distribution', fontsize=14, fontweight='bold', pad=15, color='white')

# 5. Monthly Expenses Trend
ax5 = plt.subplot(4, 2, 5)
months = [m['name'] for m in monthly_data]
values = [m['value'] for m in monthly_data]

bars = ax5.bar(months, values, color=['#333333' if v < 25000 else '#ffffff' for v in values],
               edgecolor='white', linewidth=1.5)
ax5.plot(months, values, color='#ffffff', linewidth=2, marker='o', markersize=8, 
         markerfacecolor='#ffffff', markeredgecolor='black', markeredgewidth=2)
ax5.set_title('Monthly Expenses Trend', fontsize=14, fontweight='bold', pad=15, color='white')
ax5.set_xlabel('Month', fontsize=11, color='white')
ax5.set_ylabel('Expenses ($)', fontsize=11, color='white')
ax5.grid(axis='y', alpha=0.3, linestyle='--')
ax5.set_facecolor('#1a1a1a')
for spine in ax5.spines.values():
    spine.set_color('#333333')

# Add value labels
for i, (month, value) in enumerate(zip(months, values)):
    ax5.text(i, value + 500, f'${value:,}', ha='center', va='bottom', 
             fontsize=9, color='white', fontweight='bold')

# 6. Category Spending Distribution
ax6 = plt.subplot(4, 2, 6)
cat_names = [c['name'] for c in category_data]
cat_values = [c['value'] for c in category_data]
cat_colors = [c['color'] for c in category_data]

wedges, texts, autotexts = ax6.pie(cat_values, labels=cat_names, autopct='%1.1f%%',
                                     colors=cat_colors, startangle=90,
                                     textprops={'color': 'black', 'fontsize': 11, 'fontweight': 'bold'},
                                     wedgeprops={'edgecolor': 'black', 'linewidth': 2})
# Make text white for darker slices
for i, autotext in enumerate(autotexts):
    if cat_colors[i] in ['#525252', '#262626']:
        autotext.set_color('white')
for i, text in enumerate(texts):
    if cat_colors[i] in ['#525252', '#262626']:
        text.set_color('white')
        
ax6.set_title('Top Category Spending Distribution', fontsize=14, fontweight='bold', pad=15, color='white')

# 7. Dashboard Stats Overview
ax7 = plt.subplot(4, 2, 7)
ax7.axis('off')
ax7.set_title('Dashboard Statistics Overview', fontsize=14, fontweight='bold', pad=15, color='white')

stat_names = ['Account Balance', 'Monthly Expenses', 'Total Investment', 'Goal Progress', 'Goal Target']
stat_values = [stats['balance'], stats['monthlyExpenses'], stats['investment'], stats['goal'], stats['goalTarget']]
stat_colors = ['#ffffff', '#ff6b6b', '#4ecdc4', '#95e1d3', '#a3a3a3']

y_pos = 0.85
for name, value, color in zip(stat_names, stat_values, stat_colors):
    # Background box
    box = FancyBboxPatch((0.1, y_pos - 0.08), 0.8, 0.12, boxstyle="round,pad=0.01", 
                         edgecolor=color, facecolor='#262626', linewidth=2)
    ax7.add_patch(box)
    
    ax7.text(0.15, y_pos, name, fontsize=11, color='#a3a3a3', va='center')
    ax7.text(0.85, y_pos, f'${value:,.2f}', fontsize=12, fontweight='bold', 
             color=color, va='center', ha='right')
    y_pos -= 0.18

# Goal progress bar
goal_progress = (stats['goal'] / stats['goalTarget']) * 100
ax7.text(0.15, 0.1, f'Goal Progress: {goal_progress:.1f}%', fontsize=11, color='white', fontweight='bold')
progress_bar = Rectangle((0.15, 0.02), 0.7, 0.04, facecolor='#333333', edgecolor='white', linewidth=1)
ax7.add_patch(progress_bar)
progress_fill = Rectangle((0.15, 0.02), 0.7 * (goal_progress / 100), 0.04, 
                          facecolor='#ffffff', edgecolor='none')
ax7.add_patch(progress_fill)

# 8. Subscription Details
ax8 = plt.subplot(4, 2, 8)
ax8.axis('off')
ax8.set_title('Active Subscriptions', fontsize=14, fontweight='bold', pad=15, color='white')

y_pos = 0.85
total_sub_cost = sum(s['amount'] for s in subscriptions)

for i, sub in enumerate(subscriptions):
    # Background box
    box = FancyBboxPatch((0.1, y_pos - 0.12), 0.8, 0.18, boxstyle="round,pad=0.01", 
                         edgecolor='#ffffff', facecolor='#262626', linewidth=2)
    ax8.add_patch(box)
    
    # Icon placeholder
    icon_circle = plt.Circle((0.18, y_pos - 0.03), 0.04, color='#ffffff', ec='black', linewidth=2)
    ax8.add_patch(icon_circle)
    ax8.text(0.18, y_pos - 0.03, sub['name'][:2], ha='center', va='center', 
             fontsize=9, fontweight='bold', color='black')
    
    ax8.text(0.28, y_pos, sub['name'], fontsize=12, fontweight='bold', color='white', va='top')
    ax8.text(0.28, y_pos - 0.08, f"Next: {sub['date']}", fontsize=9, color='#a3a3a3', va='top')
    ax8.text(0.85, y_pos - 0.03, f"${sub['amount']:.2f}", fontsize=12, fontweight='bold', 
             color='#ffffff', va='center', ha='right')
    
    y_pos -= 0.25

# Total subscription cost
ax8.text(0.5, 0.1, f'Total Monthly Subscriptions: ${total_sub_cost:.2f}', 
         fontsize=12, fontweight='bold', color='#ffffff', ha='center',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#262626', edgecolor='#ffffff', linewidth=2))

plt.tight_layout()
plt.savefig('database_visualization.png', dpi=300, facecolor='#0a0a0a', edgecolor='none', bbox_inches='tight')
print("✓ Database visualization saved to database_visualization.png")

# Create detailed data analysis report
fig2, axes = plt.subplots(2, 2, figsize=(16, 12), facecolor='#0a0a0a')
fig2.suptitle('NoirFlow - Detailed Data Analysis', fontsize=20, fontweight='bold', color='white', y=0.98)

# Transaction timeline
ax_timeline = axes[0, 0]
dates = [t['date'] for t in transactions]
amounts = [t['amount'] for t in transactions]
categories = [t['category'] for t in transactions]

x_pos = range(len(transactions))
colors_timeline = ['#ffffff', '#d4d4d4', '#a3a3a3', '#737373', '#525252']
bars = ax_timeline.bar(x_pos, amounts, color=colors_timeline, edgecolor='white', linewidth=1.5)
ax_timeline.set_xticks(x_pos)
ax_timeline.set_xticklabels([f"T{i+1}" for i in x_pos], fontsize=10)
ax_timeline.set_title('Transaction Timeline & Amounts', fontsize=13, fontweight='bold', pad=10, color='white')
ax_timeline.set_xlabel('Transaction ID', fontsize=10, color='white')
ax_timeline.set_ylabel('Amount ($)', fontsize=10, color='white')
ax_timeline.grid(axis='y', alpha=0.3, linestyle='--')
ax_timeline.set_facecolor('#1a1a1a')
for spine in ax_timeline.spines.values():
    spine.set_color('#333333')

# Add category labels
for i, (bar, cat) in enumerate(zip(bars, categories)):
    ax_timeline.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 100,
                     cat[:4], ha='center', va='bottom', fontsize=8, color='white', rotation=0)

# Data type distribution
ax_types = axes[0, 1]
ax_types.axis('off')
ax_types.set_title('Data Structure Summary', fontsize=13, fontweight='bold', pad=10, color='white')

data_summary = [
    ('Transactions', len(transactions), '#ffffff'),
    ('Subscriptions', len(subscriptions), '#a3a3a3'),
    ('Monthly Data Points', len(monthly_data), '#737373'),
    ('Category Data Points', len(category_data), '#525252'),
    ('Dashboard Stats', len(stats), '#404040'),
]

y_pos = 0.9
for name, count, color in data_summary:
    box = FancyBboxPatch((0.1, y_pos - 0.08), 0.8, 0.12, boxstyle="round,pad=0.01", 
                         edgecolor=color, facecolor='#262626', linewidth=2)
    ax_types.add_patch(box)
    ax_types.text(0.15, y_pos, name, fontsize=11, color='#a3a3a3', va='center')
    ax_types.text(0.85, y_pos, f'{count} records', fontsize=11, fontweight='bold', 
                 color=color, va='center', ha='right')
    y_pos -= 0.18

# Financial summary
ax_financial = axes[1, 0]
financial_metrics = ['Balance', 'Expenses', 'Investment', 'Goal', 'Target']
financial_values = [stats['balance'], stats['monthlyExpenses'], stats['investment'], 
                   stats['goal'], stats['goalTarget']]

bars = ax_financial.barh(financial_metrics, financial_values, 
                        color=['#ffffff', '#ff6b6b', '#4ecdc4', '#95e1d3', '#a3a3a3'],
                        edgecolor='white', linewidth=1.5)
ax_financial.set_title('Financial Metrics Comparison', fontsize=13, fontweight='bold', pad=10, color='white')
ax_financial.set_xlabel('Amount ($)', fontsize=10, color='white')
ax_financial.grid(axis='x', alpha=0.3, linestyle='--')
ax_financial.set_facecolor('#1a1a1a')
for spine in ax_financial.spines.values():
    spine.set_color('#333333')

for bar, value in zip(bars, financial_values):
    ax_financial.text(value + 5000, bar.get_y() + bar.get_height()/2,
                     f'${value:,.0f}', ha='left', va='center', 
                     fontsize=9, color='white', fontweight='bold')

# Data relationships
ax_relations = axes[1, 1]
ax_relations.axis('off')
ax_relations.set_title('Data Relationships & Insights', fontsize=13, fontweight='bold', pad=10, color='white')

insights = [
    f"• Total Transactions: {len(transactions)}",
    f"• Average Transaction: ${sum(amounts)/len(amounts):,.2f}",
    f"• Highest Transaction: ${max(amounts):,.2f}",
    f"• Most Used Payment: {max(mode_counts, key=mode_counts.get)}",
    f"• Active Subscriptions: {len(subscriptions)}",
    f"• Monthly Sub Cost: ${total_sub_cost:.2f}",
    f"• Highest Monthly Expense: ${max(values):,}",
    f"• Average Monthly Expense: ${sum(values)/len(values):,.0f}",
    f"• Goal Completion: {goal_progress:.1f}%",
    f"• Top Spending Category: {category_data[0]['name']}",
]

y_pos = 0.95
for insight in insights:
    ax_relations.text(0.1, y_pos, insight, fontsize=11, color='white', va='top',
                     family='monospace')
    y_pos -= 0.09

plt.tight_layout()
plt.savefig('database_analysis.png', dpi=300, facecolor='#0a0a0a', edgecolor='none', bbox_inches='tight')
print("✓ Detailed analysis saved to database_analysis.png")

print("\n" + "="*60)
print("DATABASE VISUALIZATION COMPLETE")
print("="*60)
print(f"\nGenerated Files:")
print(f"  1. database_structure.json - Complete data structure")
print(f"  2. database_visualization.png - Schema & visualizations")
print(f"  3. database_analysis.png - Detailed data analysis")
print(f"\nDatabase Summary:")
print(f"  • Storage Type: In-Memory (Mock Data)")
print(f"  • Location: components/Dashboard.tsx")
print(f"  • Total Records: {len(transactions) + len(subscriptions) + len(monthly_data) + len(category_data) + len(stats)}")
print(f"  • Data Models: 5 (Transaction, Subscription, ChartDataPoint, DashboardStats, Enums)")
print("="*60)
