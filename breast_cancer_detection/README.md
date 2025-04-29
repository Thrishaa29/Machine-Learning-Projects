# Breast Cancer Prediction using Logistic Regression

This project builds a predictive model using logistic regression to classify breast cancer tumors as **malignant** or **benign**. The model is trained and evaluated using a publicly available dataset.

## 📁 Dataset

The dataset contains various features computed from digitized images of breast mass biopsies, including:

- Radius, texture, perimeter, area, smoothness, etc.
- Mean, worst, and standard error values for each attribute
- Diagnosis: Malignant (M) or Benign (B)

> Data Source: [Breast Cancer Wisconsin (Diagnostic) Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))

---

## 📌 Objective

- Train a logistic regression classifier
- Preprocess data: handle missing values, standardize features
- Evaluate model performance using:
  - Confusion Matrix
  - Precision & Recall
  - ROC-AUC Score
- Tune the classification threshold
- Explain the role of the sigmoid function

---

## 📊 Process Overview

### 1. Data Preprocessing

- Dropped irrelevant columns like `id` and unnamed columns.
- Encoded the target column `diagnosis`:
  - **M (Malignant)** → `1`
  - **B (Benign)** → `0`
- Filled missing values using **mean imputation**.
- Scaled all features using **StandardScaler** to normalize the input values.

### 2. Train/Test Split

Used an 80/20 stratified split:
```python
train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
✅ Requirements
Python 3.x

scikit-learn

pandas

numpy

matplotlib
