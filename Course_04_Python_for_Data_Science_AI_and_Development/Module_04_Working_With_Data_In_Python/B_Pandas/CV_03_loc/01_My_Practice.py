"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 03
loc() Function

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 03 - loc()")
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
# Example 1
# One Row
# ==========================================================

print("\n" + "=" * 70)
print("Example 1 : One Row")
print("=" * 70)

print(df.loc[0])

# ==========================================================
# Example 2
# One Value
# ==========================================================

print("\n" + "=" * 70)
print("Example 2 : One Value")
print("=" * 70)

print(df.loc[1, "Salary"])

# ==========================================================
# Example 3
# Multiple Columns
# ==========================================================

print("\n" + "=" * 70)
print("Example 3 : Multiple Columns")
print("=" * 70)

print(df.loc[:, ["Name", "Salary"]])

# ==========================================================
# Example 4
# Multiple Rows
# ==========================================================

print("\n" + "=" * 70)
print("Example 4 : Multiple Rows")
print("=" * 70)

print(df.loc[1:3])

# ==========================================================
# Example 5
# Rows and Columns
# ==========================================================

print("\n" + "=" * 70)
print("Example 5 : Rows and Columns")
print("=" * 70)

print(df.loc[1:3, ["Name", "Department"]])

# ==========================================================
# Example 6
# Label Slicing
# ==========================================================

print("\n" + "=" * 70)
print("Example 6 : Label Slicing")
print("=" * 70)

print(df.loc[0:2, "Employee_ID":"Salary"])

# ==========================================================
# Example 7
# Set Index
# ==========================================================

print("\n" + "=" * 70)
print("Example 7 : Set Index")
print("=" * 70)

df2 = df.set_index("Name")

print(df2)

# ==========================================================
# Example 8
# Access Using Label
# ==========================================================

print("\n" + "=" * 70)
print("Example 8 : Access Using Label")
print("=" * 70)

print(df2.loc["Mary"])

# ==========================================================
# Example 9
# One Value
# ==========================================================

print("\n" + "=" * 70)
print("Example 9 : One Value")
print("=" * 70)

print(df2.loc["John", "Salary"])

# ==========================================================
# Example 10
# Multiple Labels
# ==========================================================

print("\n" + "=" * 70)
print("Example 10 : Multiple Labels")
print("=" * 70)

print(df2.loc[["Rose", "David"], ["Department", "Salary"]])

print("\n" + "=" * 70)
print("loc() PRACTICE COMPLETED")
print("=" * 70)
