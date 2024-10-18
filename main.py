https://citi.zoom.us/j/6721254229?pwd=hPCYbzrXBeW86o7dg03QCvEPZINadW.1
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def literal_to_num(label_col: pd.Series) -> pd.Series:
    """Convert 'yes', 'no', and '?' to numeric values for each category."""
    return label_col.replace({'yes': 1, 'no': 0, '?': 0.5}).astype(int)

def aggregate_predictions(true_df: pd.DataFrame, pred_df: pd.DataFrame, categories: list[str]):
    """Convert multi-label classifications into single multi-class predictions."""
    # Convert all categories to numeric values (1 for 'yes', 0 for 'no')
    true_labels = true_df[categories].apply(literal_to_num)
    pred_labels = pred_df[categories].apply(literal_to_num)
    
    # Aggregate the true and predicted values by treating the set of categories as one label
    true_aggregated = true_labels.apply(lambda row: tuple(row), axis=1)
    pred_aggregated = pred_labels.apply(lambda row: tuple(row), axis=1)
    
    return true_aggregated, pred_aggregated

def build_5x5_confusion_matrix(true_aggregated, pred_aggregated, categories: list[str]):
    """Build a 5x5 confusion matrix from multi-class predictions."""
    unique_combinations = list(set(true_aggregated) | set(pred_aggregated))
    label_map = {comb: idx for idx, comb in enumerate(unique_combinations)}
    
    # Map true and predicted values to their respective indices in the label map
    true_mapped = true_aggregated.map(label_map)
    pred_mapped = pred_aggregated.map(label_map)
    
    # Build a confusion matrix
    cm = confusion_matrix(true_mapped, pred_mapped, labels=list(label_map.values()))
    
    return cm, label_map

def plot_5x5_confusion_matrix(cm: np.ndarray, label_map: dict, categories: list[str]):
    """Plot the 5x5 confusion matrix."""
    labels = [str(k) for k in label_map.keys()]  # Create a string representation of the category combinations
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('5x5 Confusion Matrix for All Categories')
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.show()

def evaluate_5x5_confusion_matrix(label_df: pd.DataFrame, pred_df: pd.DataFrame, categories: list[str]):
    """Evaluate and plot the 5x5 confusion matrix."""
    # Aggregate true and predicted multi-label values into single multi-class predictions
    true_aggregated, pred_aggregated = aggregate_predictions(label_df, pred_df, categories)
    
    # Build the confusion matrix
    cm, label_map = build_5x5_confusion_matrix(true_aggregated, pred_aggregated, categories)
    
    # Plot the confusion matrix
    plot_5x5_confusion_matrix(cm, label_map, categories)

# Example DataFrames
label_df = pd.DataFrame({
    'issue_id': [1, 2, 3, 4, 5],
    'cat_1': ['yes', 'no', '?', 'yes', 'no'],
    'cat_2': ['no', 'yes', 'no', 'no', 'no'],
    'cat_3': ['yes', 'no', 'no', 'no', 'no'],
    'cat_4': ['no', 'yes', 'no', 'no', 'yes'],
    'cat_5': ['yes', 'no', 'yes', 'yes', 'no']
})

pred_df = pd.DataFrame({
    'issue_id': [1, 2, 3, 4, 5],
    'cat_1': ['yes', 'no', 'yes', 'no', 'no'],
    'cat_2': ['no', 'yes', 'no', 'yes', 'no'],
    'cat_3': ['yes', 'no', 'no', 'no', 'yes'],
    'cat_4': ['no', 'yes', 'no', 'yes', 'no'],
    'cat_5': ['no', 'yes', 'yes', 'yes', 'no']
})

# Define the categories (multi-labels)
categories = ['cat_1', 'cat_2', 'cat_3', 'cat_4', 'cat_5']

# Run evaluation and plot the 5x5 confusion matrix
evaluate_5x5_confusion_matrix(label_df, pred_df, categories)



'''  '''
