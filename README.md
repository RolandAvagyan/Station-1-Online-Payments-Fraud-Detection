# Fraud Detection Model

## Data set link

-https://www.kaggle.com/datasets/ealaxi/paysim1/data

## Model Features

- Features: step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, oldbalanceDest, newbalanceDest
- Target: isFraud (binary: 1 for fraud transaction, 0 otherwise)

## Model Evaluation

- Accuracy: 0.95

## Model Description

- Used Decision Tree Classifier model from scikit-learn library.
- Chose this model due to its simplicity and ability to handle non-linear relationships in data.
- Achieved a high accuracy of 95%, indicating good performance on the test data.
