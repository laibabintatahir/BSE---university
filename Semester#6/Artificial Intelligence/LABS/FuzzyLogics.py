# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:56:55 2024

@author: Laiba Binta Tahir
"""

# Define the detection levels for both sensors
import numpy as np
detection_levels_sensor_1 = [0, 0.2, 0.35, 0.65, 0.85, 1]
detection_levels_sensor_2 = [0, 0.35, 0.25, 0.8, 0.95, 1]

# gain values 
gains = [0, 10, 20, 30, 40, 50]

#compute the union 
def fuzzy_union(set1, set2):
    return np.maximum(set1,set2)

# Function to compute the intersection of two fuzzy sets
def fuzzy_intersection(set1, set2):
    return np.minimum(set1, set2)

# Function to compute the difference 
def fuzzy_difference(set1, set2):
     return [min(a, 1 - b) for a, b in zip(set1, set2)]

# Function to compute the complement of a fuzzy set
def fuzzy_complement(set1):
    return [1 - a for a in set1]

# Function to format the results to 2 decimal places
def format_result(result):
    return [f"{value:.2f}" for value in result]

# Function to print the results
def print_result(result, X, operation_name):
    result_str = " ".join(f"{val}/{X[i]}" for i, val in enumerate(result))
    print(f"{operation_name}: {result_str}")

# Compute the union
union = fuzzy_union(detection_levels_sensor_1, detection_levels_sensor_2)
formatted_union = format_result(union)

# Compute the intersection
intersection = fuzzy_intersection(detection_levels_sensor_1, detection_levels_sensor_2)
formatted_intersection = format_result(intersection)

# Compute the difference (Sensor 1 - Sensor 2)
difference_sensor_1_minus_sensor_2 = fuzzy_difference(detection_levels_sensor_1, detection_levels_sensor_2)
formatted_difference_sensor_1_minus_sensor_2 = format_result(difference_sensor_1_minus_sensor_2)

# Compute the difference (Sensor 2 - Sensor 1)
difference_sensor_2_minus_sensor_1 = fuzzy_difference(detection_levels_sensor_2, detection_levels_sensor_1)
formatted_difference_sensor_2_minus_sensor_1 = format_result(difference_sensor_2_minus_sensor_1)

# Compute the complement for Sensor 1
complement_sensor_1 = fuzzy_complement(detection_levels_sensor_1)
formatted_complement_sensor_1 = format_result(complement_sensor_1)

# Compute the complement for Sensor 2
complement_sensor_2 = fuzzy_complement(detection_levels_sensor_2)
formatted_complement_sensor_2 = format_result(complement_sensor_2)

# Print the Universe of Discourse and detection levels
print("Membership X: ", gains)
print("D1: ", format_result(detection_levels_sensor_1))
print("D2: ", format_result(detection_levels_sensor_2))

# Print the results of the operations
print_result(formatted_union, gains, "\nUnion")
print_result(formatted_intersection, gains, "\nIntersection")
print_result(formatted_difference_sensor_1_minus_sensor_2, gains, "\nDifference (S1 - S2)")
print_result(formatted_difference_sensor_2_minus_sensor_1, gains, "\nDifference (S2 - S1)")
print_result(formatted_complement_sensor_1, gains, "\nComplement of Sensor 1")
print_result(formatted_complement_sensor_2, gains, "\nComplement of Sensor 2")
