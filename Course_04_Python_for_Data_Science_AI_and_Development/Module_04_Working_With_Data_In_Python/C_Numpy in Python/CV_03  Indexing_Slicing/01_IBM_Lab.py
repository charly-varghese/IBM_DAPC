"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_03 – Indexing and Slicing

File : 01_IBM_Lab.py

Objective:
Learn how to access, modify, and slice NumPy arrays.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY INDEXING & SLICING")
print("=" * 60)

sales = np.array([1200, 1350, 980, 1500, 1750, 1625, 1800])

print("\nOriginal Array")
print(sales)

# Positive Indexing
print("\nFirst Element")
print(sales[0])

print("\nFourth Element")
print(sales[3])

# Negative Indexing
print("\nLast Element")
print(sales[-1])

print("\nSecond Last Element")
print(sales[-2])

# Basic Slicing
print("\nFirst Three Elements")
print(sales[0:3])

print("\nMiddle Elements")
print(sales[2:5])

print("\nLast Three Elements")
print(sales[-3:])

# Step Slicing
print("\nEvery Second Element")
print(sales[::2])

# Reverse Array
print("\nReverse Order")
print(sales[::-1])

# Modify Values
sales[2] = 1100

print("\nUpdated Array")
print(sales)

print("\nLab Completed Successfully.")
