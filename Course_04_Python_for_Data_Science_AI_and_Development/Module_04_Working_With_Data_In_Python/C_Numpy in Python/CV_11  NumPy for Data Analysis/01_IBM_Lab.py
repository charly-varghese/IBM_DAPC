"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_11 – NumPy for Data Analysis

File : 01_IBM_Lab.py

Objective:
Learn data analysis techniques using NumPy.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY FOR DATA ANALYSIS")
print("=" * 60)

sales = np.array([1200, 1500, 1800, 900, 2200, 1750, 800, 2600])

print("\nSales Data")
print(sales)

print("\nSales Greater than 1500")
print(sales[sales > 1500])

print("\nSales Less than 1000")
print(sales[sales < 1000])

print("\nSorted Sales")
print(np.sort(sales))

print("\nUnique Values")

duplicate_sales = np.array([1200, 1500, 1200, 1800, 2200, 1800])

print(np.unique(duplicate_sales))

print("\nMaximum Sales")
print(np.max(sales))

print("\nMinimum Sales")
print(np.min(sales))

print("\nAverage Sales")
print(np.mean(sales))

print("\nLab Completed Successfully.")
