import pandas as pd
import numpy as np
from pandas import read_csv, get_dummies
from sklearn.preprocessing import OrdinalEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score

# Read the data from the csv file (setting header to infer sets the first row as column names)
# Data has 1000 (instances) rows and 7 columns (attributes), we see this by printing the data shape
data = read_csv('party_data.csv', header="infer")
print(f"Data Shape: {data.shape}")

"""
Here is a general explanation of the code


Preprocessing the data for k-NN and Decision Tree:

First the data is one-hot encoded, then the data is encoded using OrdinalEncoder.
The data is then shuffled and split into training and test sets, 80% training and 20% test.

We then train and evaluate the k-NN classifier with different values of k (3, 5, 11, 17).


Accuracy means, how often the classifier is correct. So in the confusion matrix you use addition on the TP and TN values and divide by the total number of instances.
Precision means, when it predicts how often is it correct. So in the confusion matrix you use divide the TP by the total"predicted positive" values

Example:
[[ 71   8]
 [  7 114]]
 
 If this is the confusion matrix, the accuracy is (71+114)/(71+8+7+114) = 0.92 = 92%
 And if the same confusion matrix is used ,the precision for the "ok" class is 114/(8+114) = 0.93 = 93%
"""

# Preprocessing the data for k-NN and Decision Tree
encoder = OrdinalEncoder()
data_dummies = get_dummies(data)
data_encoded = encoder.fit_transform(data_dummies)
data_encoded = np.random.permutation(data_encoded)
X = data_encoded[:, :-1]
y = data_encoded[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Get all unique labels
all_labels = np.unique(y)

# Function to train and evaluate k-NN
def train_and_evaluate_knn(k):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_train = knn.predict(X_train)
    y_pred_test = knn.predict(X_test)
    precision = precision_score(y_test, y_pred_test, pos_label=encoder.categories_[-1][1], zero_division=0)
    print(f'k-NN (k={k}) - Train Accuracy: {accuracy_score(y_train, y_pred_train):.2f}, Test Accuracy: {accuracy_score(y_test, y_pred_test):.2f}')
    print(f'Confusion Matrix:\n{confusion_matrix(y_test, y_pred_test, labels=all_labels)}')
    print(f'Precision for "ok" class: {precision:.2f}')
    return precision

# Evaluate k-NN with different values of k
knn_precisions = [train_and_evaluate_knn(k) for k in [3, 5, 11, 17]]

# Preprocess the data for Logistic Regression
data_dummies_lr = get_dummies(data, drop_first=True)
data_encoded_lr = encoder.fit_transform(data_dummies_lr)
data_encoded_lr = np.random.permutation(data_encoded_lr)
X_lr = data_encoded_lr[:, :-1]
y_lr = data_encoded_lr[:, -1]
X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)

# Function to train and evaluate Logistic Regression
def train_and_evaluate_lr(penalty):
    lr = LogisticRegression(penalty=penalty, solver='liblinear' if penalty else 'newton-cg')
    lr.fit(X_train_lr, y_train_lr)
    y_pred_train_lr = lr.predict(X_train_lr)
    y_pred_test_lr = lr.predict(X_test_lr)
    precision = precision_score(y_test_lr, y_pred_test_lr, pos_label=encoder.categories_[-1][1], zero_division=0)
    print(f'Logistic Regression (penalty={penalty}) - Train Accuracy: {accuracy_score(y_train_lr, y_pred_train_lr):.2f}, Test Accuracy: {accuracy_score(y_test_lr, y_pred_test_lr):.2f}')
    print(f'Confusion Matrix:\n{confusion_matrix(y_test_lr, y_pred_test_lr, labels=all_labels)}')
    print(f'Precision for "ok" class: {precision:.2f}')
    return precision

# Evaluate Logistic Regression with and without regularization
lr_precisions = [train_and_evaluate_lr('l2'), train_and_evaluate_lr(None)]

# Function to train and evaluate Decision Tree
def train_and_evaluate_dt(criterion):
    dt = DecisionTreeClassifier(criterion=criterion, random_state=42)
    dt.fit(X_train, y_train)
    y_pred_train_dt = dt.predict(X_train)
    y_pred_test_dt = dt.predict(X_test)
    precision = precision_score(y_test, y_pred_test_dt, pos_label=encoder.categories_[-1][1], zero_division=0)
    print(f'Decision Tree (criterion={criterion}) - Train Accuracy: {accuracy_score(y_train, y_pred_train_dt):.2f}, Test Accuracy: {accuracy_score(y_test, y_pred_test_dt):.2f}')
    print(f'Confusion Matrix:\n{confusion_matrix(y_test, y_pred_test_dt, labels=all_labels)}')
    print(f'Precision for "ok" class: {precision:.2f}')
    return precision

# Evaluate Decision Tree with different criteria
dt_precisions = [train_and_evaluate_dt('gini'), train_and_evaluate_dt('entropy')]

# Find the best model based on precision for "ok" class
all_precisions = knn_precisions + lr_precisions + dt_precisions
best_precision = max(all_precisions)
best_model_index = all_precisions.index(best_precision)

model_names = ['k-NN (k=3)', 'k-NN (k=5)', 'k-NN (k=11)', 'k-NN (k=17)', 'Logistic Regression (l2)', 'Logistic Regression (None)', 'Decision Tree (gini)', 'Decision Tree (entropy)']
best_model = model_names[best_model_index]

print(f'The best model for minimizing party killers is: {best_model} with a precision of {best_precision:.2f}')



