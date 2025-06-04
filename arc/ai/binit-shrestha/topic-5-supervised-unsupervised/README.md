## Supervised and Unsupervised Learning Algorithms

### Task was to determine whether annual income of person is > $50k

- Dataset was loaded, both data and testing parts

- All sorts of visualization was done, null values removed - they were negligible in number

- Checked the target feature (> $50k & <= $50k) and converted to labels (1, 0)

- Imbalanced observed (1 << 0), SMOTE was used to balance the classes

- Also dropped some features due to redundancy (Education & Final Weight)

- Numerical columns scaled, Categorical encoded

- Data was finalized and training began, calculating metrics for various models

- KNN, SVM, Decision Tree, Random Forest, Gradient Boosting, Naive Bayes

- All models perfomed similarly with some having better performance in some metrics

    - Random Forest - Slightly higher Accuracy
    - Gradient Boosting - Slightly better Precision etc
- In Confusion Matrices, we aimed to reduce False Negatives, so we don't misclassify high income (> $50k) as wrong

    - FN was minimal in all models, except Naive Bayes