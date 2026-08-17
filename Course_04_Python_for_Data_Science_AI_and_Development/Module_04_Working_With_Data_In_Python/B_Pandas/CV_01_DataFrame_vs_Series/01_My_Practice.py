"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 01
DataFrame vs Series

Author : Varghese
=============================================================
"""

# ============================================================
# Import Pandas
# ============================================================

import pandas as pd

print("=" * 60)
print("PANDAS DATAFRAME vs SERIES")
print("=" * 60)

# ============================================================
# STEP 1
# Create a Python Dictionary
# ============================================================

student = {

    "Name": ["Rose", "John", "James"],

    "Age": [25, 30, 38],

    "Department": [
        "Finance",
        "IT",
        "HR"
    ],

    "Salary": [
        50000,
        60000,
        70000
    ]

}

print("\nSTEP 1 : Python Dictionary")
print(student)

# ============================================================
# STEP 2
# Convert Dictionary into DataFrame
# ============================================================

df = pd.DataFrame(student)

print("\n" + "=" * 60)
print("STEP 2 : DATAFRAME")
print("=" * 60)

print(df)

# ============================================================
# STEP 3
# Check Data Type
# ============================================================

print("\nSTEP 3 : Type of df")

print(type(df))

# ============================================================
# STEP 4
# Display One Column
# ============================================================

print("\n" + "=" * 60)
print("STEP 4 : SINGLE COLUMN")
print("=" * 60)

print(df["Name"])

# ============================================================
# STEP 5
# Type of Single Column
# ============================================================

print("\nSTEP 5 : Type")

print(type(df["Name"]))

# ============================================================
# STEP 6
# Display One Column as DataFrame
# ============================================================

print("\n" + "=" * 60)
print("STEP 6 : DOUBLE BRACKET")
print("=" * 60)

print(df[["Name"]])

print(type(df[["Name"]]))

# ============================================================
# STEP 7
# Multiple Columns
# ============================================================

print("\n" + "=" * 60)
print("STEP 7 : MULTIPLE COLUMNS")
print("=" * 60)

print(df[["Name", "Salary"]])

# ============================================================
# STEP 8
# Shape
# ============================================================

print("\nSTEP 8 : Shape")

print(df.shape)

# ============================================================
# STEP 9
# Columns
# ============================================================

print("\nSTEP 9 : Columns")

print(df.columns)

# ============================================================
# STEP 10
# Summary
# ============================================================

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("DataFrame      : Table")
print("Series         : Single Column")
print("[]             : Series")
print("[[]]           : DataFrame")
print("shape          : Rows & Columns")
print("columns        : Column Names")

print("\nPRACTICE COMPLETED")