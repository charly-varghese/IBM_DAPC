"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_08 – Iterating Arrays

File : 01_IBM_Lab.py

Objective:
Learn different methods to iterate through NumPy arrays.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY ARRAY ITERATION")
print("=" * 60)

# 1D Array
numbers = np.array([10, 20, 30, 40, 50])

print("\n1D Array Iteration")

for value in numbers:
    print(value)

# 2D Array
sales = np.array([[1200, 1350, 1500], [1600, 1750, 1800]])

print("\n2D Array")

for row in sales:
    print(row)

print("\nIndividual Elements using Nested Loop")

for row in sales:
    for value in row:
        print(value)

print("\nUsing np.nditer()")

for item in np.nditer(sales):
    print(item)

print("\nLab Completed Successfully.")
