
import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Data
data = {
    'Sepal Length': [5.3, 5.1, 7.2, 5.4, 5.1, 5.4, 7.4, 6.1, 7.3, 6.0, 5.8, 6.3, 5.1, 6.3, 5.5],
    'Sepal Width': [3.7, 3.8, 3.0, 3.4, 3.3, 3.9, 2.8, 2.8, 2.9, 2.7, 2.8, 2.3, 2.5, 2.5, 2.4],
    'Species': ['Setosa', 'Setosa', 'Virginica', 'Setosa', 'Setosa', 'Setosa', 'Virginica', 'Versicolor', 'Virginica', 'Versicolor', 'Virginica', 'Versicolor', 'Versicolor', 'Versicolor', 'Versicolor']
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode the target variable
le = LabelEncoder()
df['Species'] = le.fit_transform(df['Species'])

# Features and target
X = df[['Sepal Length', 'Sepal Width']]
y = df['Species']

# Train KNN classifier
knn = KNeighborsClassifier().fit(X, y)

# New data point for prediction
new_data = pd.DataFrame({ 'Sepal Length': [5.2], 'Sepal Width': [3.1] })

# Predict the species
predicted = knn.predict(new_data)

# Decode the predicted species
predicted_species = le.inverse_transform(predicted)

print(predicted_species)
