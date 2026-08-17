"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 05
Slicing in Pandas

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 05 - SLICING")
print("=" * 70)

# ==========================================================
# Create DataFrame
# ==========================================================

employee = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Rose", "John", "James", "Mary", "David", "Linda"],
    "Department": ["Finance", "IT", "HR", "Marketing", "Sales", "IT"],
    "Salary": [50000, 65000, 45000, 55000, 70000, 62000],
    "Experience": [2, 5, 1, 3, 6, 4],
}

df = pd.DataFrame(employee)

print("\nFULL DATAFRAME\n")
print(df)

# ==========================================================
# Example 1
# iloc Row Slicing
# ==========================================================

print("\n" + "=" * 70)
print("Example 1 : iloc Row Slicing")
print("=" * 70)

print(df.iloc[1:4])

# ==========================================================
# Example 2
# iloc Column Slicing
# ==========================================================

print("\n" + "=" * 70)
print("Example 2 : iloc Column Slicing")
print("=" * 70)

print(df.iloc[:, 1:4])

# ==========================================================
# Example 3
# iloc Row & Column Slicing
# ==========================================================

print("\n" + "=" * 70)
print("Example 3 : iloc Row & Column Slicing")
print("=" * 70)

print(df.iloc[1:5, 1:4])

# ==========================================================
# Example 4
# loc Row Slicing
# ==========================================================

print("\n" + "=" * 70)
print("Example 4 : loc Row Slicing")
print("=" * 70)

print(df.loc[1:4])

# ==========================================================
# Example 5
# loc Column Slicing
# ==========================================================

print("\n" + "=" * 70)
print("Example 5 : loc Column Slicing")
print("=" * 70)

print(df.loc[:, "Name":"Salary"])

# ==========================================================
# Example 6
# loc Row & Column Slicing
# ==========================================================

print("\n" + "=" * 70)
print("Example 6 : loc Row & Column Slicing")
print("=" * 70)

print(df.loc[1:4, "Name":"Salary"])

# ==========================================================
# Example 7
# Head
# ==========================================================

print("\n" + "=" * 70)
print("Example 7 : First Three Rows")
print("=" * 70)

print(df.head(3))

# ==========================================================
# Example 8
# Tail
# ==========================================================

print("\n" + "=" * 70)
print("Example 8 : Last Three Rows")
print("=" * 70)

print(df.tail(3))

# ==========================================================
# Example 9
# Every Second Row
# ==========================================================

print("\n" + "=" * 70)
print("Example 9 : Every Second Row")
print("=" * 70)

print(df.iloc[::2])

# ==========================================================
# Example 10
# Reverse DataFrame
# ==========================================================

print("\n" + "=" * 70)
print("Example 10 : Reverse Order")
print("=" * 70)

print(df.iloc[::-1])

print("\n" + "=" * 70)
print("SLICING PRACTICE COMPLETED")
print("=" * 70)
