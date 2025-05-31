##  Why is accuracy not suitable evaluation metrics for all the cases?
    Key Reason: Accuracy is misleading in imbalanced datasets
    Accuracy measures the proportion of correct predictions out of all predictions. However, it does not account for class imbalance. In spam dataset, if the number of non-spam (0) emails is much higher than spam (1), the model can achieve high accuracy simply by predicting most emails as non-spam.

## Model's Imbalance Evidence:
Accuracy is high (94.2%), but

Recall (52.4%) is low — meaning the model is missing many actual spam emails (false negatives).

Precision (80.6%) is okay, but again, recall is low.

This shows that the model is biased toward the majority class (non-spam) and performs poorly in detecting the minority class (spam).

## When is accuracy not suitable?
When class imbalance exists (e.g., spam detection, fraud detection, rare disease prediction).

When false positives or false negatives have different costs (e.g., spam detection: missing a spam email is more harmful than wrongly flagging a non-spam email).

## What metrics should you consider instead?
Precision: Focuses on the correctness of positive predictions (spam detection in this case).

Recall (Sensitivity): Focuses on how many actual positives are detected (important in spam detection).

F1-Score: Harmonic mean of precision and recall — good for imbalanced datasets.



## Precision vs. Recall: When to Choose Which?
Choose Precision when...
- False positives are costly (predicting something as positive when it’s actually negative is bad).

- You want to avoid false alarms.

## Example Scenarios:

- Spam detection: Don’t want to mark important emails as spam.

- Email marketing: Avoid sending offers to uninterested customers.

 - Cancer diagnosis (for rare cases): Avoid alarming patients who are not sick.

##  Choose Recall when...
- False negatives are costly (missing a positive case is very bad).

- You want to catch as many positive cases as possible.

### Example Scenarios:

- Fraud detection: Better to flag a few extra transactions than miss a fraud.

- Medical diagnosis (common diseases): Catch as many cases as possible.

- Search engines: Retrieve as many relevant results as possible.

## when to chose metrices
| Metric        | Use When...                                                      | Example                                   |
| ------------- | ---------------------------------------------------------------- | ----------------------------------------- |
| **Precision** | **False positives are costly.** You want correct positives.      | Spam detection (minimize false alarms).   |
| **Recall**    | **False negatives are costly.** You want to catch all positives. | Cancer detection (minimize missed cases). |
| **F1 Score**  | Balance precision and recall.                                    | General classification with trade-offs.   |


## Summary Table
Metric	    When to Choose               Example Scenarios
Precision	Minimize false positives	 Spam detection, Email marketing
Recall	    Minimize false negatives	 Fraud detection, Medical diagnosis