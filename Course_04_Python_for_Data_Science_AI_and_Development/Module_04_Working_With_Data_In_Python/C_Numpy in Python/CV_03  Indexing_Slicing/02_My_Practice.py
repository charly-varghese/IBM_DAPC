"""
=========================================================
CV_03 – My Practice

Business Examples using Indexing & Slicing
=========================================================
"""

import numpy as np

employees = np.array(["John", "Mary", "David", "Sara", "Alex", "James", "Linda"])

print("=" * 60)
print("EMPLOYEE DATA")
print("=" * 60)

print("\nEmployee List")
print(employees)

print("\nFirst Employee")
print(employees[0])

print("\nLast Employee")
print(employees[-1])

print("\nFirst Three Employees")
print(employees[:3])

print("\nLast Three Employees")
print(employees[-3:])

print("\nAlternate Employees")
print(employees[::2])

employees[1] = "Sophia"

print("\nUpdated Employee List")
print(employees)

# Sales Example

sales = np.array([25000, 30000, 27000, 35000, 42000])

print("\nMonthly Sales")
print(sales)

print("\nHighest Recent Sales")
print(sales[-2:])

print("\nQuarter-1 Sales")
print(sales[:3])
