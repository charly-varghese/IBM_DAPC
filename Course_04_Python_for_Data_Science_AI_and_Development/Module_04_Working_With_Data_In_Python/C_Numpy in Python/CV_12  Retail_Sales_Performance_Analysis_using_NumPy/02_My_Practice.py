"""
=========================================================
CV_12 – My Practice

Business Dashboard using NumPy
=========================================================
"""

import numpy as np

products = np.array([[101, 1200], [102, 2500], [103, 1800], [104, 3100], [105, 2700]])

print("=" * 60)
print("PRODUCT SALES DASHBOARD")
print("=" * 60)

print("\nDataset")
print(products)

print("\nProduct IDs")
print(products[:, 0])

print("\nSales")
print(products[:, 1])

print("\nAverage Sales")
print(np.mean(products[:, 1]))

print("\nHighest Sales")
print(np.max(products[:, 1]))

print("\nLowest Sales")
print(np.min(products[:, 1]))

print("\nProducts Above 2000")
print(products[products[:, 1] > 2000])

print("\nSorted Sales")
print(np.sort(products[:, 1]))

print("\nProjected Sales (15% Growth)")
print(products[:, 1] * 1.15)

print("\nPractice Completed Successfully.")
