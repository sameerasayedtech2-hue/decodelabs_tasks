# Project 2: Data Classification Using AI

**DecodeLabs — Industrial Training Kit | Batch 2026**

---

## Overview

This project implements a **supervised machine learning pipeline** that classifies iris flowers into one of **three species** (*setosa*, *versicolor*, *virginica*) based on four physical measurements. It follows the **Input → Process → Output (IPO)** framework taught in the training kit.

## Goal

Build a basic classification model using a small dataset (Iris) — proving the ability to **train, test, and validate** an AI model through supervised learning.

## Dataset

The built-in **Iris dataset** from scikit-learn:

- **150 samples**, perfectly balanced across 3 classes (50 each)
- **4 features**: sepal length, sepal width, petal length, petal width (all in cm)
- **Target**: species (setosa / versicolor / virginica)

## Pipeline

| Stage | What happens |
|---|---|
| **Input** | Load Iris dataset → inspect shape/class balance → scale features with `StandardScaler` |
| **Process** | **80/20 stratified train-test split** → select best K via elbow method → train `KNeighborsClassifier` |
| **Output** | Confusion matrix, classification report, **accuracy**, and **F1 score** |

## Requirements

```bash
pip install scikit-learn pandas matplotlib seaborn
```

## How to Run

```bash
python iris_classifier.py
```

## Files

| File | Description |
|---|---|
| `iris_classifier.py` | Main script — full pipeline from data loading to evaluation |
| `k_selection_elbow.png` | Error rate vs. K plot, used to pick the optimal number of neighbors |
| `confusion_matrix.png` | Heatmap of predicted vs. actual species on the test set |

## Key Skills Demonstrated

- Data loading and exploratory inspection
- Train/test splitting with stratification
- **Feature scaling** (fit on train, transform on test — avoiding data leakage)
- Hyperparameter selection (choosing K via error-rate elbow)
- Model training and prediction with scikit-learn's `fit` / `predict` workflow
- Model evaluation **beyond raw accuracy**: confusion matrix, precision, recall, F1 score

## Results

| Metric | Score |
|---|---|
| **Best K** | **1** |
| **Accuracy** | **96.67%** |
| **F1 Score (macro)** | **0.9666** |

> **Important:** The only misclassification was **one *virginica* sample predicted as *versicolor*** — these two species have known overlap in petal measurements, so this is an expected edge case, not a model flaw. *Setosa* was classified with **perfect accuracy**, as it's linearly separable from the other two species.

## Notes

- `random_state=42` is used throughout for **reproducibility**.
- Scaling is fit **only on the training set** and applied to the test set — this prevents test-data leakage into the model.
- **Accuracy alone can be misleading** on imbalanced datasets (the "Accuracy Mirage"). Since Iris classes are balanced here, accuracy is a fair metric — but F1 score and the confusion matrix are included regardless, as best practice.