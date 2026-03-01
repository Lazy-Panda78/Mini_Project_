"""
preprocess.py — Download, clean, augment, and split dataset.
Run: python preprocess.py
"""
# import os, shutil
# from sklearn.model_selection import train_test_split
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

RAW_DIR = "../data/raw"
PROCESSED_DIR = "../data/processed"
SPLIT = (0.70, 0.15, 0.15)  # train / val / test

def run():
    """Resize images, apply augmentation config, save splits."""
    # TODO: implement
    print("TODO: implement preprocessing pipeline")

if __name__ == "__main__":
    run()
