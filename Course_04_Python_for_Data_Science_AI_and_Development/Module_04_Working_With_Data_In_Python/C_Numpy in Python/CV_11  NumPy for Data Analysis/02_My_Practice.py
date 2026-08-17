"""
=========================================================
CV_11 – My Practice

Business Data Analysis using NumPy
=========================================================
"""

import numpy as np

employees = np.array([35000, 45000, 50000, 65000, 50000, 70000, 85000, 35000])

print("=" * 60)
print("EMPLOYEE SALARY ANALYSIS")
print("=" * 60)

print("\nSalary Data")
print(employees)

print("\nHigh Salary (>50000)")
print(employees[employees > 50000])

print("\nLow Salary (<40000)")
print(employees[employees < 40000])

print("\nSorted Salary")
print(np.sort(employees))

print("\nUnique Salary")
print(np.unique(employees))

print("\nHighest Salary")
print(np.max(employees))

print("\nLowest Salary")
print(np.min(employees))

print("\nAverage Salary")
print(np.mean(employees))

print("\nPractice Completed Successfully.")
