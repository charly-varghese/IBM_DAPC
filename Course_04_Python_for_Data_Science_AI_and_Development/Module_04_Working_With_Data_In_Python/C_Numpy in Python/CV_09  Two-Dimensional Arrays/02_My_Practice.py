"""
=========================================================
CV_09 – My Practice

Business Examples using 2D Arrays
=========================================================
"""

import numpy as np

employees = np.array(
    [[101, 45000, 5], [102, 52000, 7], [103, 61000, 4], [104, 70000, 10]]
)

print("=" * 60)
print("EMPLOYEE DATA")
print("=" * 60)

print("\nEmployee Dataset")
print(employees)

print("\nEmployee IDs")
print(employees[:, 0])

print("\nSalaries")
print(employees[:, 1])

print("\nExperience")
print(employees[:, 2])

print("\nFirst Employee")
print(employees[0])

print("\nLast Employee")
print(employees[-1])

print("\nSecond Employee Salary")
print(employees[1, 1])

print("\nPractice Completed Successfully.")
