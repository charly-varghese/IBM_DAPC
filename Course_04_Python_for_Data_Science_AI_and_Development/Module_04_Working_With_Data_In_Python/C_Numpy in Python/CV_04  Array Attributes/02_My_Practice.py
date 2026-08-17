"""
=========================================================
CV_04 – My Practice

Understanding NumPy Array Attributes
=========================================================
"""

import numpy as np

sales = np.array([
    [25000,30000,28000],
    [35000,42000,39000],
    [45000,47000,50000]
])

print("=" * 60)
print("BUSINESS SALES DATA")
print("=" * 60)

print("\nSales Data")
print(sales)

print("\nShape :", sales.shape)
print("Dimensions :", sales.ndim)
print("Size :", sales.size)
print("Data Type :", sales.dtype)
print("Item Size :", sales.itemsize)
print("Memory :", sales.nbytes)

print("\nConvert to Float")

sales_float = sales.astype(float)

print(sales_float)
print(sales_float.dtype)
