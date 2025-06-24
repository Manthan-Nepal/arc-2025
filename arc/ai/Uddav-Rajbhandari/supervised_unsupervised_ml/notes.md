# how to spot overfitting

| Metric                | Overfitting Sign                    |
| --------------------- | ----------------------------------- |
| Train Accuracy/Recall | **Much higher** than Test score     |
| Test Accuracy/Recall  | **Lower** than expected             |
| Precision/Recall      | **Drops** on Test compared to Train |
| ROC-AUC               | **Lower** on Test vs Train          |
| Confusion Matrix      | **Many false positives/negatives**  |


# Explanation of Each Metric
- 1️⃣ Precision (Positive Predictive Value)

Definition: The fraction of correct positive predictions.

Interpretation: Out of all predicted positive samples, how many were actually positive?

Example:
For class 1 (spam/malware), a precision of 0.64 means: “Out of all predicted spam emails, 64% were truly spam.”

- 2️⃣  Recall (Sensitivity or True Positive Rate)

​

Definition: The fraction of actual positives correctly identified.

Interpretation: Out of all actual positive samples, how many were correctly predicted?

Example:
Recall of 0.62 for class 1 means: “Out of all actual spam emails, 62% were correctly identified.”
# What is ROC-AUC?
 ROC-AUC (Receiver Operating Characteristic - Area Under Curve) is a threshold-independent metric. It measures how well your model distinguishes between the two classes: