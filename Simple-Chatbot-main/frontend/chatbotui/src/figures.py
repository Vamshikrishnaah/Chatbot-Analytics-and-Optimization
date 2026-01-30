"""
figures.py
Chatbot Analytics & Optimization – Visualization Structure (No Data Dependency)

NOTE:
This script generates placeholder analytics figures to demonstrate
visualization structure and interpretation for academic purposes.
"""

# =====================================================
# CLI ARGUMENTS
# =====================================================
import argparse
parser = argparse.ArgumentParser(description="Chatbot Analytics Figures (No Data)")
parser.add_argument("--headless", action="store_true", help="Save figures only (no popups)")
args = parser.parse_args()
HEADLESS = args.headless

# =====================================================
# VISUALIZATION IMPORTS
# =====================================================
import matplotlib
matplotlib.use("TkAgg" if not HEADLESS else "Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import numpy as np
import pandas as pd
import os

sns.set_style("whitegrid")

# =====================================================
# OUTPUT FOLDER
# =====================================================
OUT = "outputs/visualizations"
os.makedirs(OUT, exist_ok=True)

# =====================================================
# PLACEHOLDER ANALYTICS DATA
# =====================================================
intents = ["greet", "query_knowledge_base", "bot_challenge", "goodbye"]
intent_counts = [860, 610, 460, 70]

hours = np.arange(24)
response_time = np.random.normal(400, 40, size=24)

csat_scores = [50, 110, 230, 410, 200]

sentiment = {"positive": 780, "neutral": 820, "negative": 400}

completed = [1520, 480]
converted = [620, 1380]

confusion_matrix = np.array([
    [720, 80, 40, 20],
    [90, 620, 60, 30],
    [40, 70, 510, 40],
    [10, 20, 30, 110]
])

heatmap_data = np.random.randint(0, 80, size=(7, 24))

words = "hello hi help bot human course fees admission deadline contact thank you".split()

# =====================================================
# FIGURE 1: COMPREHENSIVE DASHBOARD
# =====================================================
fig = plt.figure(figsize=(20, 12))
gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.3)

ax1 = fig.add_subplot(gs[0, 0])
ax1.bar(intents, intent_counts)
ax1.set_title("Intent Distribution")

ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(hours, response_time, marker="o")
ax2.set_title("Response Time by Hour")

ax3 = fig.add_subplot(gs[0, 2])
ax3.bar([1,2,3,4,5], csat_scores)
ax3.set_title("CSAT Distribution")

ax4 = fig.add_subplot(gs[1, 0])
ax4.bar(sentiment.keys(), sentiment.values())
ax4.set_title("Sentiment Distribution")

ax5 = fig.add_subplot(gs[1, 1])
pd.DataFrame({
    "Completed": completed,
    "Converted": converted
}, index=["Yes", "No"]).plot(kind="bar", ax=ax5)
ax5.set_title("Completion & Conversion")

ax6 = fig.add_subplot(gs[1, 2])
ax6.axis("off")
ax6.text(
    0.05, 0.5,
    """KEY METRICS

Intent Accuracy: 85.2%
Conversion Rate: 30.9%
Avg CSAT: 3.74 / 5
Fallback Rate: 11.8%
Completion Rate: 76.4%
Avg Response Time: 402 ms
""",
    fontsize=11,
    family="monospace",
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.4)
)

plt.suptitle("Chatbot Analytics Dashboard (Demonstration)", fontsize=18, fontweight="bold")
plt.savefig(f"{OUT}/01_comprehensive_dashboard.png", dpi=300, bbox_inches="tight")

# =====================================================
# FIGURE 2: CONFUSION MATRIX
# =====================================================
plt.figure(figsize=(8, 6))
sns.heatmap(
    confusion_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=intents,
    yticklabels=intents
)
plt.title("Confusion Matrix – Intent Recognition")
plt.xlabel("Predicted Intent")
plt.ylabel("True Intent")
plt.tight_layout()
plt.savefig(f"{OUT}/02_confusion_matrix.png", dpi=300)

# =====================================================
# FIGURE 3: INTENT DISTRIBUTION
# =====================================================
plt.figure(figsize=(8, 6))
plt.bar(intents, intent_counts)
plt.title("User Query Distribution by Intent")
plt.xlabel("Intent")
plt.ylabel("Number of Queries")
plt.tight_layout()
plt.savefig(f"{OUT}/03_intent_distribution.png", dpi=300)

# =====================================================
# FIGURE 4: SESSION HEATMAP
# =====================================================
plt.figure(figsize=(16, 8))
sns.heatmap(heatmap_data, cmap="YlOrRd")
plt.title("Session Heatmap – User Activity Patterns")
plt.xlabel("Hour of Day")
plt.ylabel("Day of Week")
plt.tight_layout()
plt.savefig(f"{OUT}/04_session_heatmap.png", dpi=300)

# =====================================================
# FIGURE 5: FALLBACK VS NON-FALLBACK
# =====================================================
plt.figure(figsize=(6, 6))
plt.pie(
    [88.2, 11.8],
    labels=["Non-Fallback", "Fallback"],
    autopct="%1.1f%%",
    startangle=140
)
plt.title("Fallback vs Non-Fallback Queries")
plt.tight_layout()
plt.savefig(f"{OUT}/05_fallback_rate.png", dpi=300)

# =====================================================
# FIGURE 6: WORD CLOUD
# =====================================================
plt.figure(figsize=(14, 8))
wc = WordCloud(width=1200, height=600, background_color="white").generate(" ".join(words))
plt.imshow(wc)
plt.axis("off")
plt.title("Most Common Keywords in User Messages")
plt.tight_layout()
plt.savefig(f"{OUT}/06_wordcloud.png", dpi=300)

# =====================================================
# DISPLAY OR CLOSE
# =====================================================
if not HEADLESS:
    plt.show()
else:
    plt.close("all")
    print("All 6 demonstration figures generated successfully.")
