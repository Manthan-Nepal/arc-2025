# Logistic Regression

This repository documents a hands-on journey through the foundational stages of data science, focusing on  logistic regression using Python. The content is structured as a series of Jupyter Notebooks, inspired by the [arc-2025](https://github.com/Tech-Manthan-Nepal/arc-2025) curriculum and related resources.

---

## Overview

This project implements logistic regression for spam detection, featuring both custom implementation and sklearn comparison. Key components include:
- **Custom Logistic Regression Implementation**
- **Data Preprocessing and EDA**
- **Class Imbalance Handling**
- **Model Evaluation and Comparison**
- **Performance Metrics Analysis**

---

## Topics Covered

1. **Logistic Regression Implementation**
   - Custom implementation with L2 regularization
   - Gradient descent optimization
   - Binary cross-entropy loss
   - Sigmoid activation function

2. **Data Analysis & Preprocessing**
   - Data cleaning and exploration
   - Feature scaling using StandardScaler
   - Train-test splitting
   - Class imbalance analysis

3. **Model Evaluation**
   - Classification reports
   - Confusion matrices
   - ROC curves and AUC scores
   - Precision-Recall analysis

4. **Class Imbalance Handling**
   - SMOTE implementation
   - Balanced vs Imbalanced performance comparison
   - Effect on model metrics

---

## Implementation Details

1. **Custom Logistic Regression Features:**
   - Configurable learning rate and iterations
   - L2 regularization for preventing overfitting
   - Binary cross-entropy loss computation
   - Gradient descent optimization

2. **Model Comparison:**
   - Custom implementation vs sklearn
   - Performance metrics comparison
   - ROC curve analysis
   - Impact of class balancing

3. **Evaluation Metrics:**
   - Accuracy, Precision, Recall, F1-score
   - Confusion matrices
   - ROC curves and AUC scores
   - Performance on balanced and imbalanced data

---

## Dataset Features

The spam detection dataset includes:
- **num_links**: Number of links in the email
- **num_words**: Total word count
- **has_offer**: Binary indicator for special offers
- **sender_score**: Sender reputation score
- **all_caps**: Presence of all capital letters
- **is_spam**: Target variable (binary classification)

---

## Tasks Completed

1. **Implementation**
   - Custom logistic regression from scratch
   - L2 regularization implementation
   - Sklearn model comparison
   - SMOTE for handling class imbalance

2. **Analysis**
   - Comprehensive EDA
   - Model performance evaluation
   - Class imbalance impact study
   - Metric selection justification

3. **Evaluation**
   - Performance metrics comparison
   - ROC curve analysis
   - Impact of balanced data
   - Precision-Recall trade-offs

---

## How to Use

1. Navigate to the `Source Code` folder to explore Jupyter Notebooks containing step-by-step code and explanations.
2. Refer to the provided resources for a deeper understanding of concepts.
3. Run and modify the scripts to reinforce learning through practice.
