# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:16:40 2024

@author: Laiba Binta Tahir
"""

import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Data
data = {
    'Day': ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14'],
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize LabelEncoders for each feature
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
le_decision = LabelEncoder()

# Encode features and target
df['Outlook'] = le_outlook.fit_transform(df['Outlook'])
df['Temp'] = le_temp.fit_transform(df['Temp'])
df['Humidity'] = le_humidity.fit_transform(df['Humidity'])
df['Wind'] = le_wind.fit_transform(df['Wind'])
df['Decision'] = le_decision.fit_transform(df['Decision'])

# Features and target
X = df[['Outlook', 'Temp', 'Humidity', 'Wind']]
y = df['Decision']

# Train Naive Bayes classifier
nb = CategoricalNB()
nb.fit(X, y)

# New data point for prediction
new_data = pd.DataFrame({
    'Outlook': [le_outlook.transform(['Sunny'])[0]], 
    'Temp': [le_temp.transform(['Cool'])[0]], 
    'Humidity': [le_humidity.transform(['High'])[0]], 
    'Wind': [le_wind.transform(['Strong'])[0]]
})

# Predict decision
prediction = nb.predict(new_data)
predicted_decision = le_decision.inverse_transform(prediction)

print(f'Outlook: Sunny, Temp: Cool, Humidity: High, Wind: Strong -> Decision: {predicted_decision[0]}')
