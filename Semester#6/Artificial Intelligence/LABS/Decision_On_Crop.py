
"""
Created on Mon Jul  1 10:42:02 2024

@author: Laiba Binta Tahir
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('D:/Semester 6/Artificial Intelligence/LABS/crop.csv')

# Explore the dataset
print(data.head())

#print(data.isnull().sum())

X = data.drop('label', axis=1)
y = data['label']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


dt_model = DecisionTreeClassifier().fit(X_train, y_train)

# Plot the decision tree
plt.figure(figsize=(30,30))
plot_tree(dt_model, feature_names=X.columns, class_names=dt_model.classes_.astype(str), filled=True, rounded=True)
plt.title('Decision Tree')
plt.show()

# Make predictions and evaluate the model
y_pred = dt_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


# Plot feature importance
feature_importances = dt_model.feature_importances_
plt.figure(figsize=(10,6))
plt.barh(X.columns, feature_importances, color='skyblue')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.title('Feature Importance')
plt.show()
