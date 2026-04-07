"""
Generate a Jagged Profile scatter plot from the baseline data.

This script reads the JSONL file containing evaluation results and produces
`jagged_profile_plot.png`, where each point represents a transaction. The x-axis
shows the model's confidence and the y-axis indicates correctness (1=correct,
0=incorrect). Points are colored by model.
"""
import json
import matplotlib.pyplot as plt

DATA_PATH = 'data/appendix_full_evaluation_data_v1.jsonl'

# Load data
records = []
with open(DATA_PATH, 'r') as f:
    for line in f:
        records.append(json.loads(line))

# Color mapping for models
colors = {
    'GPT-4o': 'red',
    'Llama 3.1': 'blue',
    'Mistral Large': 'green'
}

# Plot scatter points
for record in records:
    plt.scatter(record['confidence'], record['correct'],
                color=colors.get(record['model'], 'gray'),
                alpha=0.6)

# Create custom legend
handles = []
labels = []
for model, color in colors.items():
    handles.append(plt.Line2D([0], [0], marker='o', color='w', label=model,
                              markerfacecolor=color, markersize=6))
    labels.append(model)

plt.legend(handles, labels)
plt.xlabel('Model Confidence')
plt.ylabel('Correctness (1=correct, 0=incorrect)')
plt.title('Jagged Profile Scatter Plot')
plt.grid(True, linestyle='--', alpha=0.5)

# Save figure
plt.tight_layout()
plt.savefig('jagged_profile_plot.png')
print('Plot saved to jagged_profile_plot.png')
