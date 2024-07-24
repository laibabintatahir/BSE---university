# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:56:55 2024

@author: Laiba Binta Tahir
"""

#fuzzy logic task 5 - 6 

import numpy as np

# Define the matrices R and S
R = np.array([[0.6, 0.3],
              [0.2, 0.9]])

S = np.array([[1, 0.5, 0.3],
              [0.8, 0.4, 0.7]])

# Min-Max Composition
min_max_composition = np.zeros((R.shape[0], S.shape[1]))

for i in range(R.shape[0]):
    for j in range(S.shape[1]):
        min_max_composition[i, j] = np.max([np.min([R[i, k], S[k, j]]) for k in range(R.shape[1])])

# Max-Product Composition
max_product_composition = np.zeros((R.shape[0], S.shape[1]))

for i in range(R.shape[0]):
    for j in range(S.shape[1]):
        max_product_composition[i, j] = np.max([R[i, k] * S[k, j] for k in range(R.shape[1])])

print("Min-Max Composition:")
print(min_max_composition)

print("\nMax-Product Composition:")
print(max_product_composition)