"""
evaluate.py — Generate evaluation metrics and confusion matrix.
Run: python evaluate.py
"""
# from sklearn.metrics import classification_report, confusion_matrix
# import seaborn as sns, matplotlib.pyplot as plt

CLASSES = ["Spoiled", "Moderately Fresh", "Fresh"]

def evaluate(model_path: str, test_data_dir: str):
    """Load model and compute accuracy, F1, confusion matrix."""
    # TODO: implement
    pass

if __name__ == "__main__":
    evaluate("../models/freshness_model.h5", "../data/processed/test")
