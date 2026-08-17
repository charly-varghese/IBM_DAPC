"""
=========================================================
CV_06 – My Practice

Business Examples using NumPy Array Operations
=========================================================
"""

import numpy as np

product_a = np.array([1200, 1500, 1800, 1700])
product_b = np.array([800, 1000, 900, 1100])

print("=" * 60)
print("PRODUCT SALES COMPARISON")
print("=" * 60)

print("\nProduct A Sales")
print(product_a)

print("\nProduct B Sales")
print(product_b)

print("\nCombined Sales")
print(product_a + product_b)

print("\nSales Difference")
print(product_a - product_b)

print("\nTotal Revenue (Price × Quantity)")
price = np.array([50, 40, 30, 60])

print(product_a * price)

print("\nGST (18%)")
gst = product_a * 0.18
print(gst)

print("\nSales After 10% Growth")
growth = product_a * 1.10
print(growth)

print("\nDiscounted Sales (5%)")
discount = product_a * 0.95
print(discount)

print("\nPractice Completed Successfully.")
