"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 02
Column Selection

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 02 - COLUMN SELECTION")
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

# ==========================================================
# Display DataFrame
# ==========================================================

print("\nFULL DATAFRAME\n")
print(df)

# ==========================================================
# Single Column
# ==========================================================

print("\n" + "=" * 70)
print("SINGLE COLUMN")
print("=" * 70)

print(df["Name"])

print(type(df["Name"]))

# ==========================================================
# Single Column as DataFrame
# ==========================================================

print("\n" + "=" * 70)
print("SINGLE COLUMN AS DATAFRAME")
print("=" * 70)

print(df[["Name"]])

print(type(df[["Name"]]))

# ==========================================================
# Multiple Columns
# ==========================================================

print("\n" + "=" * 70)
print("MULTIPLE COLUMNS")
print("=" * 70)

print(df[["Name", "Salary"]])

# ==========================================================
# Column Names
# ==========================================================

print("\n" + "=" * 70)
print("COLUMN NAMES")
print("=" * 70)

print(df.columns)

# ==========================================================
# Shape
# ==========================================================

print("\n" + "=" * 70)
print("DATAFRAME SHAPE")
print("=" * 70)

print(df.shape)

# ==========================================================
# Head
# ==========================================================

print("\n" + "=" * 70)
print("FIRST 3 ROWS")
print("=" * 70)

print(df.head(3))

# ==========================================================
# Tail
# ==========================================================

print("\n" + "=" * 70)
print("LAST 2 ROWS")
print("=" * 70)

print(df.tail(2))

# ==========================================================
# Info
# ==========================================================

print("\n" + "=" * 70)
print("DATAFRAME INFORMATION")
print("=" * 70)

df.info()

# ==========================================================
# Data Types
# ==========================================================

print("\n" + "=" * 70)
print("DATA TYPES")
print("=" * 70)

print(df.dtypes)

# ==========================================================
# Summary
# ==========================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
✔ []             → Series

✔ [[]]           → DataFrame

✔ columns        → Displays column names

✔ shape          → Returns (rows, columns)

✔ head()         → First rows

✔ tail()         → Last rows

✔ info()         → DataFrame information

✔ dtypes         → Data type of every column
""")

print("=" * 70)
print("PRACTICE COMPLETED")
print("=" * 70)
