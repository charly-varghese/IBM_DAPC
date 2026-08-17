"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_07 – Mathematical Functions

File : 01_IBM_Lab.py

Objective:
Learn common mathematical functions in NumPy.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY MATHEMATICAL FUNCTIONS")
print("=" * 60)

numbers = np.array([4, 9, 16, 25, 36])

print("\nNumbers")
print(numbers)

print("\nSquare Root")
print(np.sqrt(numbers))

print("\nPower (Square)")
print(np.power(numbers, 2))

print("\nExponential")
print(np.exp([1, 2, 3]))

print("\nNatural Logarithm")
print(np.log(numbers))

values = np.array([-10, -5, 8, -25, 30])

print("\nAbsolute Values")
print(np.abs(values))

decimal_values = np.array([12.35, 15.89, 20.45, 18.50])

print("\nRound")
print(np.round(decimal_values))

print("\nCeiling")
print(np.ceil(decimal_values))

print("\nFloor")
print(np.floor(decimal_values))

print("\nLab Completed Successfully.")
