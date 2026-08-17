"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 04
iloc() Function

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 04 - iloc()")
print("=" * 70)

# ==========================================================
# Create DataFrame
# ==========================================================

employee = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Rose", "John", "James", "Mary", "David"],
    "Department": ["Finance", "IT", "HR", "Marketing", "Sales"],
    "Salary": [50000, 65000, 45000, 55000, 70000],
    "Experience": [2, 5, 1, 3, 6],
}

df = pd.DataFrame(employee)

print("\nFULL DATAFRAME\n")
print(df)

# ==========================================================
# Example 1 : First Row
# ==========================================================

print("\n" + "=" * 70)
print("Example 1 : First Row")
print("=" * 70)

print(df.iloc[0])

# ==========================================================
# Example 2 : One Value
# ==========================================================

print("\n" + "=" * 70)
print("Example 2 : One Value")
print("=" * 70)

print(df.iloc[1, 3])

# ==========================================================
# Example 3 : First Column
# ==========================================================

print("\n" + "=" * 70)
print("Example 3 : First Column")
print("=" * 70)

print(df.iloc[:, 0])

# ==========================================================
# Example 4 : Multiple Columns
# ==========================================================

print("\n" + "=" * 70)
print("Example 4 : Multiple Columns")
print("=" * 70)

print(df.iloc[:, [1, 3]])

# ==========================================================
# Example 5 : Multiple Rows
# ==========================================================

print("\n" + "=" * 70)
print("Example 5 : Multiple Rows")
print("=" * 70)

print(df.iloc[1:4])

# ==========================================================
# Example 6 : Rows and Columns
# ==========================================================

print("\n" + "=" * 70)
print("Example 6 : Rows and Columns")
print("=" * 70)

print(df.iloc[1:4, 1:4])

# ==========================================================
# Example 7 : First 3 Rows
# ==========================================================

print("\n" + "=" * 70)
print("Example 7 : First 3 Rows")
print("=" * 70)

print(df.iloc[:3])

# ==========================================================
# Example 8 : Last 2 Rows
# ==========================================================

print("\n" + "=" * 70)
print("Example 8 : Last 2 Rows")
print("=" * 70)

print(df.iloc[-2:])

# ==========================================================
# Example 9 : Specific Rows
# ==========================================================

print("\n" + "=" * 70)
print("Example 9 : Specific Rows")
print("=" * 70)

print(df.iloc[[0, 2, 4]])

# ==========================================================
# Example 10 : Specific Rows and Columns
# ==========================================================

print("\n" + "=" * 70)
print("Example 10 : Specific Rows and Columns")
print("=" * 70)

print(df.iloc[[0, 2, 4], [1, 3]])

print("\n" + "=" * 70)
print("iloc() PRACTICE COMPLETED")
print("=" * 70)
