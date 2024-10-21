import seaborn as sns
import matplotlib.pyplot as plt

def plot_custom_confusion_matrix(cm: np.ndarray, cats_col: list[str]):
    """
    Plot the 5x5 custom confusion matrix using seaborn's heatmap.
    
    Args:
    - cm: The 5x5 confusion matrix as a NumPy array.
    - cats_col: List of category names for labeling the axes.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=cats_col, yticklabels=cats_col)
    plt.xlabel('Predicted Category')
    plt.ylabel('True Category')
    plt.title('Custom Confusion Matrix')
    plt.show()

# Example usage:

# Generate the custom confusion matrix from the previous step
custom_cm = custom_confusion_matrix(label_df, pred_df, cats_col)

# Plot the confusion matrix
plot_custom_confusion_matrix(custom_cm, cats_col)
