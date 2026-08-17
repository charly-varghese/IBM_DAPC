"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_09 – Two-Dimensional Arrays

File : 01_IBM_Lab.py

Objective:
Learn how to create and work with 2D NumPy arrays.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY TWO-DIMENSIONAL ARRAYS")
print("=" * 60)

sales = np.array([[1200, 1350, 1400], [1500, 1600, 1700], [1800, 1900, 2000]])

print("\nSales Data")
print(sales)

print("\nShape")
print(sales.shape)

print("\nDimensions")
print(sales.ndim)

print("\nRows")
print(sales.shape[0])

print("\nColumns")
print(sales.shape[1])

print("\nFirst Row")
print(sales[0])

print("\nSecond Column")
print(sales[:, 1])

print("\nElement (Row 2, Column 3)")
print(sales[1, 2])

print("\nLast Row")
print(sales[-1])

print("\nLab Completed Successfully.")
