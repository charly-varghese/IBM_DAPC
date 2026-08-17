"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_05 – Statistical Functions

File : 01_IBM_Lab.py

Objective:
Learn NumPy statistical functions.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY STATISTICAL FUNCTIONS")
print("=" * 60)

sales = np.array([1200, 1350, 980, 1500, 1750, 1625, 1800])

print("\nSales Data")
print(sales)

print("\nSum")
print(np.sum(sales))

print("\nMean")
print(np.mean(sales))

print("\nMedian")
print(np.median(sales))

print("\nMinimum")
print(np.min(sales))

print("\nMaximum")
print(np.max(sales))

print("\nStandard Deviation")
print(np.std(sales))

print("\nVariance")
print(np.var(sales))

print("\n25th Percentile")
print(np.percentile(sales, 25))

print("\n50th Percentile")
print(np.percentile(sales, 50))

print("\n75th Percentile")
print(np.percentile(sales, 75))

print("\nLab Completed Successfully.")
