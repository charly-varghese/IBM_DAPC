"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_10 – Matrix Operations

File : 01_IBM_Lab.py

Objective:
Learn basic matrix operations using NumPy.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY MATRIX OPERATIONS")
print("=" * 60)

A = np.array([[1, 2], [3, 4]])

B = np.array([[5, 6], [7, 8]])

print("\nMatrix A")
print(A)

print("\nMatrix B")
print(B)

print("\nMatrix Addition")
print(A + B)

print("\nMatrix Subtraction")
print(A - B)

print("\nElement-wise Multiplication")
print(A * B)

print("\nMatrix Multiplication")
print(np.matmul(A, B))

print("\nDot Product")
print(np.dot(A, B))

print("\nTranspose of Matrix A")
print(A.T)

print("\nIdentity Matrix (3x3)")
print(np.eye(3))

print("\nLab Completed Successfully.")
