# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:12:02 2024

@author: Laiba Binta Tahir
"""

import numpy as np
from sklearn.linear_model import LinearRegression

# Data
X = np.array([[3, 8], [4, 5], [5, 7], [6, 3], [2, 1]])
Y = np.array([-3.7, 3.5, 2.5, 11.5, 5.7])

# Fit linear regression model
model = LinearRegression().fit(X, Y)

# Coefficients
b = model.coef_
a = model.intercept_

print(f"Coefficients (b): {b}")
print(f"Intercept (a): {a}")

# Predicting the value of Y when X1 = 3 and X2 = 2
X_pred = np.array([[3, 2]])
Y_pred = model.predict(X_pred)

print(f"Predicted Y value: {Y_pred[0]}")
