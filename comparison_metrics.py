import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# Results from Decision Tree and KNN
# ==========================================

decision_tree = {
    'Accuracy': 90.61,
    'Precision': 90.54,
    'Recall': 90.61,
    'F1-Score': 90.42
}

knn = {
    'Accuracy': 70.35,
    'Precision': 71.49,
    'Recall': 70.35,
    'F1-Score': 70.28
}

# ==========================================
# Colours
# ==========================================

decision_tree_color = '#AD1457'   # Dark Rose
knn_color = '#00838F'            # Dark Teal

models = ['Decision Tree', 'KNN']

# ==========================================
# Figure 8.1 Accuracy
# ==========================================

plt.figure(figsize=(6,4))
plt.bar(
    models,
    [decision_tree['Accuracy'], knn['Accuracy']],
    color=[decision_tree_color, knn_color]
)

plt.title('Accuracy Comparison')
plt.ylabel('Accuracy (%)')
plt.tight_layout()

plt.savefig('accuracy_comparison.png')
plt.show()

# ==========================================
# Figure 8.2 Precision
# ==========================================

plt.figure(figsize=(6,4))
plt.bar(
    models,
    [decision_tree['Precision'], knn['Precision']],
    color=[decision_tree_color, knn_color]
)

plt.title('Precision Comparison')
plt.ylabel('Precision (%)')
plt.tight_layout()

plt.savefig('precision_comparison.png')
plt.show()

# ==========================================
# Figure 8.3 Recall
# ==========================================

plt.figure(figsize=(6,4))
plt.bar(
    models,
    [decision_tree['Recall'], knn['Recall']],
    color=[decision_tree_color, knn_color]
)

plt.title('Recall Comparison')
plt.ylabel('Recall (%)')
plt.tight_layout()

plt.savefig('recall_comparison.png')
plt.show()

# ==========================================
# Figure 8.4 F1 Score
# ==========================================

plt.figure(figsize=(6,4))
plt.bar(
    models,
    [decision_tree['F1-Score'], knn['F1-Score']],
    color=[decision_tree_color, knn_color]
)

plt.title('F1 Score Comparison')
plt.ylabel('F1 Score (%)')
plt.tight_layout()

plt.savefig('f1_comparison.png')
plt.show()

# ==========================================
# Figure 8.5 Overall Comparison
# ==========================================

metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']

dt_scores = [90.61, 90.54, 90.61, 90.42]
knn_scores = [70.35, 71.49, 70.35, 70.28]

x = np.arange(len(metrics))
width = 0.35

plt.figure(figsize=(8,5))

plt.bar(
    x - width/2,
    dt_scores,
    width,
    label='Decision Tree',
    color=decision_tree_color
)

plt.bar(
    x + width/2,
    knn_scores,
    width,
    label='KNN',
    color=knn_color
)

plt.xticks(x, metrics)

plt.ylabel('Score (%)')
plt.xlabel('Evaluation Metrics')
plt.title('Overall Performance Comparison')

plt.legend()

plt.tight_layout()

plt.savefig('overall_metrics_comparison.png')
plt.show()

print("All graphs generated successfully.")
