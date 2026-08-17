"""
=========================================================
CV_07 – My Practice

Business Examples using Mathematical Functions
=========================================================
"""

import numpy as np

profits = np.array([45000.55, 52000.75, 61000.25, 72000.90])

print("=" * 60)
print("BUSINESS MATHEMATICAL ANALYSIS")
print("=" * 60)

print("\nOriginal Profit")
print(profits)

print("\nRounded Profit")
print(np.round(profits))

print("\nCeiling")
print(np.ceil(profits))

print("\nFloor")
print(np.floor(profits))

expenses = np.array([-12000, -8000, 5000, -15000])

print("\nAbsolute Expenses")
print(np.abs(expenses))

investment = np.array([100, 225, 400, 625])

print("\nSquare Root")
print(np.sqrt(investment))

growth = np.array([2, 3, 4])

print("\nPower of 3")
print(np.power(growth, 3))

print("\nPractice Completed Successfully.")
