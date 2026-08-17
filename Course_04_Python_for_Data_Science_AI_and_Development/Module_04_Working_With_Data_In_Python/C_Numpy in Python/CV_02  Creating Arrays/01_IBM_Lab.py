"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_02 – Creating Arrays

File : 01_IBM_Lab.py

Objective:
Learn different methods to create NumPy arrays.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("CREATING NUMPY ARRAYS")
print("=" * 60)

# Create array from a Python list
arr1 = np.array([10, 20, 30, 40, 50])
print("\nArray from List:")
print(arr1)

# Create array from a tuple
arr2 = np.array((100, 200, 300))
print("\nArray from Tuple:")
print(arr2)

# Create a zero array
zeros = np.zeros(5)
print("\nZeros Array:")
print(zeros)

# Create a ones array
ones = np.ones(5)
print("\nOnes Array:")
print(ones)

# Create an array using arange()
sequence = np.arange(1, 11)
print("\nArray using arange():")
print(sequence)

# Create random integers
np.random.seed(10)
sales = np.random.randint(1000, 5000, 10)

print("\nRandom Sales Data:")
print(sales)

print("\nLab Completed Successfully.")
