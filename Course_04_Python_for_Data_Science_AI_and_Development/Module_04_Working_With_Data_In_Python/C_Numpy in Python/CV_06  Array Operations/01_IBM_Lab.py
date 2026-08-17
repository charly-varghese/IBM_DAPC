"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_06 – Array Operations

File : 01_IBM_Lab.py

Objective:
Learn arithmetic operations using NumPy arrays.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY ARRAY OPERATIONS")
print("=" * 60)

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("\nArray 1")
print(arr1)

print("\nArray 2")
print(arr2)

print("\nAddition")
print(arr1 + arr2)

print("\nSubtraction")
print(arr1 - arr2)

print("\nMultiplication")
print(arr1 * arr2)

print("\nDivision")
print(arr1 / arr2)

print("\nExponent")
print(arr2**2)

print("\nScalar Addition")
print(arr1 + 100)

print("\nScalar Multiplication")
print(arr1 * 10)

print("\nLab Completed Successfully.")
