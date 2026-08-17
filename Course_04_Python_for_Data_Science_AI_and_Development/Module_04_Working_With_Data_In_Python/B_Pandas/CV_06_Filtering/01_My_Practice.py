"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 06
Filtering Data

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 06 - FILTERING")
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
# Example 1 : Salary > 55000
# ==========================================================

print("\n" + "=" * 70)
print("Example 1 : Salary > 55000")
print("=" * 70)

print(df[df["Salary"] > 55000])

# ==========================================================
# Example 2 : Salary < 60000
# ==========================================================

print("\n" + "=" * 70)
print("Example 2 : Salary < 60000")
print("=" * 70)

print(df[df["Salary"] < 60000])

# ==========================================================
# Example 3 : Department == IT
# ==========================================================

print("\n" + "=" * 70)
print("Example 3 : Department = IT")
print("=" * 70)

print(df[df["Department"] == "IT"])

# ==========================================================
# Example 4 : Experience >= 4
# ==========================================================

print("\n" + "=" * 70)
print("Example 4 : Experience >= 4")
print("=" * 70)

print(df[df["Experience"] >= 4])

# ==========================================================
# Example 5 : Multiple Conditions (&)
# ==========================================================

print("\n" + "=" * 70)
print("Example 5 : IT Employees with Salary > 60000")
print("=" * 70)

print(df[(df["Department"] == "IT") & (df["Salary"] > 60000)])

# ==========================================================
# Example 6 : OR Condition (|)
# ==========================================================

print("\n" + "=" * 70)
print("Example 6 : HR OR Finance")
print("=" * 70)

print(df[(df["Department"] == "HR") | (df["Department"] == "Finance")])

# ==========================================================
# Example 7 : isin()
# ==========================================================

print("\n" + "=" * 70)
print("Example 7 : isin()")
print("=" * 70)

print(df[df["Department"].isin(["IT", "Sales"])])

# ==========================================================
# Example 8 : between()
# ==========================================================

print("\n" + "=" * 70)
print("Example 8 : Salary between 50000 and 65000")
print("=" * 70)

print(df[df["Salary"].between(50000, 65000)])

# ==========================================================
# Example 9 : String Filtering
# ==========================================================

print("\n" + "=" * 70)
print("Example 9 : Name Starts With J")
print("=" * 70)

print(df[df["Name"].str.startswith("J")])

# ==========================================================
# Example 10 : NOT EQUAL (!=)
# ==========================================================

print("\n" + "=" * 70)
print("Example 10 : Department != IT")
print("=" * 70)

print(df[df["Department"] != "IT"])

print("\n" + "=" * 70)
print("FILTERING PRACTICE COMPLETED")
print("=" * 70)
