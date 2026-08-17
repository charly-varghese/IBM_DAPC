"""
=========================================================
CV_10 – My Practice

Business Examples using Matrix Operations
=========================================================
"""

import numpy as np

sales_q1 = np.array([[1200, 1500], [1800, 2000]])

sales_q2 = np.array([[1300, 1600], [1900, 2100]])

print("=" * 60)
print("BUSINESS MATRIX OPERATIONS")
print("=" * 60)

print("\nQ1 Sales")
print(sales_q1)

print("\nQ2 Sales")
print(sales_q2)

print("\nCombined Sales")
print(sales_q1 + sales_q2)

print("\nSales Difference")
print(sales_q2 - sales_q1)

price = np.array([[50, 60], [70, 80]])

print("\nRevenue Matrix")
print(sales_q1 * price)

print("\nMatrix Multiplication")
print(np.matmul(sales_q1, price))

print("\nTranspose")
print(sales_q1.T)

print("\nPractice Completed Successfully.")
