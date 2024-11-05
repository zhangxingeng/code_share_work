import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Sample DataFrame for demonstration (replace with your actual DataFrame)
data = {
    'rule_list': [['C1c'], ['G5', 'J1'], ['F', 'G5', 'J1'], ['C1c'], ['C1d']],
    'sim': [['M2'], ['G5'], ['G5'], ['G5'], ['G5']],
    # Add more rows as needed
}
df = pd.DataFrame(data)

# Function to calculate precision, recall, and F1 for each row
def calculate_metrics(row):
    # Convert rule_list and sim to sets for easier comparison
    true_labels = set(row['rule_list'])
    predicted_labels = set(row['sim'])
    
    # Calculate precision, recall, and F1-score
    tp = len(true_labels & predicted_labels)  # True Positives
    fp = len(predicted_labels - true_labels)  # False Positives
    fn = len(true_labels - predicted_labels)  # False Negatives
    
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    return pd.Series([precision, recall, f1])

# Apply the function to each row and calculate metrics
df[['precision', 'recall', 'f1_score']] = df.apply(calculate_metrics, axis=1)

# Calculate average precision, recall, and F1-score across all rows
average_precision = df['precision'].mean()
average_recall = df['recall'].mean()
average_f1 = df['f1_score'].mean()

# Display the individual row metrics and the overall averages
print("Individual Metrics for Each Row:")
print(df[['rule_list', 'sim', 'precision', 'recall', 'f1_score']])

print("\nOverall Averages:")
print(f"Average Precision: {average_precision:.2f}")
print(f"Average Recall: {average_recall:.2f}")
print(f"Average F1-score: {average_f1:.2f}")
