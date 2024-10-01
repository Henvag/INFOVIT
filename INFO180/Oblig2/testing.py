

from sklearn.metrics import confusion_matrix

# Example true labels and predicted labels
y_true = [0, 1, 0, 1, 0, 1, 1, 0]
y_pred = [0, 0, 0, 1, 0, 1, 1, 1]

# Generate the confusion matrix
cm = confusion_matrix(y_true, y_pred)

print(cm)