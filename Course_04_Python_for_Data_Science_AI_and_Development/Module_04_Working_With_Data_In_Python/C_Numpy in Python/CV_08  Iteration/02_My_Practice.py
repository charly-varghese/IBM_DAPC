"""
=========================================================
CV_08 – My Practice

Business Examples using Array Iteration
=========================================================
"""

import numpy as np

employees = np.array(
    [["John", "Sales"], ["Mary", "Finance"], ["David", "HR"], ["Sara", "IT"]]
)

print("=" * 60)
print("EMPLOYEE DETAILS")
print("=" * 60)

print("\nRows")

for row in employees:
    print(row)

print("\nIndividual Values")

for row in employees:
    for value in row:
        print(value)

sales = np.array([[25000, 30000], [32000, 35000], [41000, 45000]])

print("\nSales Data using np.nditer()")

for value in np.nditer(sales):
    print(value)

print("\nPractice Completed Successfully.")
