"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 10
Handling Missing Data

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 10 - HANDLING MISSING DATA")
print("=" * 70)

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv("../datasets/employees_missing.csv")

print("\nFULL DATASET\n")
print(df)

# ==========================================================
# Example 1 : Check Missing Values
# ==========================================================

print("\n" + "=" * 70)
print("Example 1 : isnull()")
print("=" * 70)

print(df.isnull())

# ==========================================================
# Example 2 : Count Missing Values
# ==========================================================

print("\n" + "=" * 70)
print("Example 2 : Missing Value Count")
print("=" * 70)

print(df.isnull().sum())

# ==========================================================
# Example 3 : Check Non-Missing Values
# ==========================================================

print("\n" + "=" * 70)
print("Example 3 : notnull()")
print("=" * 70)

print(df.notnull())

# ==========================================================
# Example 4 : Drop Rows with Missing Values
# ==========================================================

print("\n" + "=" * 70)
print("Example 4 : dropna()")
print("=" * 70)

print(df.dropna())

# ==========================================================
# Example 5 : Fill Missing Salary
# ==========================================================

print("\n" + "=" * 70)
print("Example 5 : Fill Salary with Mean")
print("=" * 70)

df_salary = df.copy()

mean_salary = df_salary["Salary"].mean()

df_salary["Salary"] = df_salary["Salary"].fillna(mean_salary)

print(df_salary)

# ==========================================================
# Example 6 : Fill Missing Experience
# ==========================================================

print("\n" + "=" * 70)
print("Example 6 : Fill Experience with Median")
print("=" * 70)

df_exp = df.copy()

median_exp = df_exp["Experience"].median()

df_exp["Experience"] = df_exp["Experience"].fillna(median_exp)

print(df_exp)

# ==========================================================
# Example 7 : Fill Department
# ==========================================================

print("\n" + "=" * 70)
print("Example 7 : Fill Department")
print("=" * 70)

df_dept = df.copy()

df_dept["Department"] = df_dept["Department"].fillna("Unknown")

print(df_dept)

# ==========================================================
# Example 8 : Fill City
# ==========================================================

print("\n" + "=" * 70)
print("Example 8 : Fill City")
print("=" * 70)

df_city = df.copy()

df_city["City"] = df_city["City"].fillna("Not Available")

print(df_city)

# ==========================================================
# Example 9 : Forward Fill
# ==========================================================

print("\n" + "=" * 70)
print("Example 9 : Forward Fill")
print("=" * 70)

print(df.fillna(method="ffill"))

# ==========================================================
# Example 10 : Backward Fill
# ==========================================================

print("\n" + "=" * 70)
print("Example 10 : Backward Fill")
print("=" * 70)

print(df.fillna(method="bfill"))

print("\n" + "=" * 70)
print("HANDLING MISSING DATA COMPLETED")
print("=" * 70)
