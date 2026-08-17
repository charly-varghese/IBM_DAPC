"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_12 – NumPy Mini Project

Project:
Retail Sales Performance Analysis

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY MINI PROJECT")
print("=" * 60)

sales = np.array(
    [1200, 1500, 1800, 900, 2200, 1750, 2400, 2600, 1950, 2100, 1850, 3000]
)

print("\nMonthly Sales")
print(sales)

print("\nTotal Sales")
print(np.sum(sales))

print("\nAverage Sales")
print(np.mean(sales))

print("\nHighest Sales")
print(np.max(sales))

print("\nLowest Sales")
print(np.min(sales))

print("\nStandard Deviation")
print(np.std(sales))

print("\nQuarter-1")
print(sales[:3])

print("\nHigh Sales (>2000)")
print(sales[sales > 2000])

print("\nSorted Sales")
print(np.sort(sales))

print("\nUnique Values")
print(np.unique(sales))

print("\nSales Growth (10%)")
print(sales * 1.10)

print("\nMini Project Completed Successfully.")
