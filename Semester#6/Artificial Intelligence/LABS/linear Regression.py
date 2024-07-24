# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:00:00 2024
@author: Laiba Binta Tahir
"""
#linear Regression

import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 1.3, 3.75, 2.25])
n = len(x)

# Calculate means
X_mean = np.mean(x)
Y_mean = np.mean(y)

print("X_mean:", X_mean)
print("Y_mean:", Y_mean)

# Calculate covariance
cov = np.sum((x - X_mean) * (y - Y_mean)) / (n - 1)
print("Covariance:", cov)

# Calculate variance
var = np.sum((x - X_mean) ** 2) / (n - 1)
print("Variance:", var)

# Calculate slope (b) and intercept (a)
b = cov / var
a = Y_mean - b * X_mean

print("b (slope) =", b)
print("a (intercept) =", a)



