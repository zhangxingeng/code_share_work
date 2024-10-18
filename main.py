import pandas as pd
import numpy as np
from sklearn.metrics import multilabel_confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def literal_to_num(label_col: pd.Series) -> pd.Series:
    """Convert 'yes', 'no', and '?' to numeric values for each category."""
    return label_col.replace({'yes': 1, 'no': 0, '?': 0.5}).astype(int)

def compute_multilabel_confusion_matrix(label_df: pd.DataFrame, pred_df: pd.DataFrame, categories: list[str]):
    """Compute multilabel confusion matrix for all categories."""
    true_labels = label_df[categories].apply(literal_to_num)
    pred_labels = pred_df[categories].apply(literal_to_num)
    
    # Compute the multilabel confusion matrix for all categories
    mcm = multilabel_confusion_matrix(true_labels, pred_labels)
    
    return mcm

def plot_confusion_matrices(mcm: np.ndarray, categories: list[str]):
    """Plot confusion matrices for each category."""
    for idx, category in enumerate(categories):
        cm = mcm[idx]
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Pred 0', 'Pred 1'], yticklabels=['True 0', 'True 1'])
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.title(f'Confusion Matrix for {category}')
        plt.show()

def evaluate_multilabel_classification(label_df: pd.DataFrame, pred_df: pd.DataFrame, categories: list[str]):
    """Evaluate multilabel confusion matrix for all categories and plot them."""
    # Compute the multilabel confusion matrix for each category
    mcm = compute_multilabel_confusion_matrix(label_df, pred_df, categories)
    
    # Plot the confusion matrix for each category
    plot_confusion_matrices(mcm, categories)

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

# Run evaluation and plot the confusion matrices
evaluate_multilabel_classification(label_df, pred_df, categories)
