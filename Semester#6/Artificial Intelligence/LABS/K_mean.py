# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 08:11:27 2024

@author: Laiba Binta Tahir
"""
# K Medoid 

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data points
data = np.array([
    [2, 6],
    [3, 4],
    [3, 8],
    [4, 7],
    [6, 2],
    [6, 4],
    [7, 3],
    [7, 4],
    [8, 5],
    [7, 6]
])

# Medoids
medoid1 = np.array([3, 4])
medoid2 = np.array([7, 4])

# Manhattan distance function
def manhattan_distance(a, b):
    return np.abs(a - b).sum(axis=1)

# Distances to each medoid
dist_to_m1 = manhattan_distance(data, medoid1)
dist_to_m2 = manhattan_distance(data, medoid2)

# Assign clusters based on nearest medoid
clusters = np.where(dist_to_m1 < dist_to_m2, 'C1', 'C2')

# Calculate cost
cost = np.sum(np.minimum(dist_to_m1, dist_to_m2))

# Create a DataFrame for easier visualization
df = pd.DataFrame(data, columns=['x', 'y'])
df['Cluster'] = clusters

print(df)
print(f"Total cost: {cost}")

# Plot clusters
plt.figure(figsize=(8, 6))

# Plot data points
for cluster, color in zip(['C1', 'C2'], ['blue', 'green']):
    clustered_data = df[df['Cluster'] == cluster]
    plt.scatter(clustered_data['x'], clustered_data['y'], label=f'Cluster {cluster}', c=color)

# Plot medoids
plt.scatter(medoid1[0], medoid1[1], c='red', marker='X', s=200, label='Medoid C1 (3, 4)')
plt.scatter(medoid2[0], medoid2[1], c='orange', marker='X', s=200, label='Medoid C2 (7, 4)')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('K-Medoids Clustering')
plt.legend()
plt.grid(True)
plt.show()
