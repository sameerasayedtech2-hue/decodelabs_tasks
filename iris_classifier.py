"""
Project 2: Data Classification Using AI — Iris dataset with KNN
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix, classification_report, f1_score, accuracy_score
)
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Load the dataset ---
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

df = pd.DataFrame(X, columns=feature_names)
df["species"] = pd.Categorical.from_codes(y, target_names)
print("Dataset shape:", X.shape)
print(df.head())
print(df["species"].value_counts())

# --- Step 2: Train-test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"\nTrain samples: {len(X_train)}, Test samples: {len(X_test)}")

# --- Step 3: Feature scaling ---
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --- Step 4: Find the best K ---
error_rates = []
k_range = range(1, 21)
for k in k_range:
    knn_k = KNeighborsClassifier(n_neighbors=k)
    knn_k.fit(X_train_scaled, y_train)
    preds_k = knn_k.predict(X_test_scaled)
    error_rates.append(np.mean(preds_k != y_test))

best_k = k_range[np.argmin(error_rates)]
print(f"\nBest K: {best_k} (error rate = {min(error_rates):.4f})")

plt.figure(figsize=(8, 5))
plt.plot(k_range, error_rates, marker="o", linestyle="--")
plt.axvline(best_k, color="orange", linestyle=":", label=f"Best K = {best_k}")
plt.title("Error Rate vs K Value")
plt.xlabel("K Value")
plt.ylabel("Error Rate")
plt.legend()
plt.tight_layout()
plt.savefig("k_selection_elbow.png", dpi=150)
plt.close()

# --- Step 5: Train final model ---
model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train_scaled, y_train)
predictions = model.predict(X_test_scaled)

# --- Step 6: Evaluate ---
acc = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average="macro")
cm = confusion_matrix(y_test, predictions)

print(f"\nAccuracy: {acc:.4f}")
print(f"F1 score (macro): {f1:.4f}")
print("\nConfusion matrix:\n", cm)
print("\nClassification report:\n",
      classification_report(y_test, predictions, target_names=target_names))

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=target_names, yticklabels=target_names)
plt.title("Confusion Matrix — Iris KNN Classifier")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.savefig("confusion_matrix.png", dpi=150)
plt.close()

print("\nSaved: k_selection_elbow.png, confusion_matrix.png")