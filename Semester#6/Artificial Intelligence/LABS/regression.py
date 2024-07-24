# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:29:29 2024

@author: Laiba Binta Tahir
"""

# logistic Regression

import numpy as np

# Example 1: Entrance Marks and Selection
def logistic(beta_0, beta_1, x):
    z = beta_0 + beta_1 * x
    prob = 1 / (1 + np.exp(-z))
    return prob

# Given parameters for example 1
beta_0 = 1
beta_1 = 8
x_1 = 60

# Compute probability
prob_1 = logistic(beta_0, beta_1, x_1)
print(f"Probability of selection for x = {x_1} is {prob_1}")

# Determine selection based on threshold
threshold = 0.5
selection = "selected" if prob_1 >= threshold else "not selected"
print(f"The student with marks {x_1} is {selection}.\n")

# Example 2: Hours Studied and Passing
def logistic_regression_odds(hours):
    log_odds = -64 + 2 * hours
    prob = 1 / (1 +  np.exp(-log_odds) )
    return prob

# Given parameters for example 2
hours_2 = 33

# Compute probability
prob_2 = logistic_regression_odds(hours_2)
print(f"Probability of passing for hours studied = {hours_2} is {prob_2}")

# Given probability
p = 0.95

neg_z = np.log((1 - p) / p)

z = -neg_z

