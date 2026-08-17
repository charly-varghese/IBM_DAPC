"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 09
Aggregation Functions

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 09 - AGGREGATION")
print("=" * 70)

# ==========================================================
# Load Dataset
# ==========================================================

df = pd.read_csv("datasets/employees.csv")

print("\nFULL DATASET\n")
print(df)

# ==========================================================
# SUM
# ==========================================================

print("\n" + "=" * 70)
print("SUM OF SALARY")
print("=" * 70)

print(df["Salary"].sum())

# ==========================================================
# MEAN
# ==========================================================

print("\n" + "=" * 70)
print("AVERAGE SALARY")
print("=" * 70)

print(df["Salary"].mean())

# ==========================================================
# MEDIAN
# ==========================================================

print("\n" + "=" * 70)
print("MEDIAN SALARY")
print("=" * 70)

print(df["Salary"].median())

# ==========================================================
# MINIMUM
# ==========================================================

print("\n" + "=" * 70)
print("MINIMUM SALARY")
print("=" * 70)

print(df["Salary"].min())

# ==========================================================
# MAXIMUM
# ==========================================================

print("\n" + "=" * 70)
print("MAXIMUM SALARY")
print("=" * 70)

print(df["Salary"].max())

# ==========================================================
# COUNT
# ==========================================================

print("\n" + "=" * 70)
print("TOTAL EMPLOYEES")
print("=" * 70)

print(df["Employee_ID"].count())

# ==========================================================
# STANDARD DEVIATION
# ==========================================================

print("\n" + "=" * 70)
print("STANDARD DEVIATION")
print("=" * 70)

print(df["Salary"].std())

# ==========================================================
# VARIANCE
# ==========================================================

print("\n" + "=" * 70)
print("VARIANCE")
print("=" * 70)

print(df["Salary"].var())

# ==========================================================
# DESCRIBE
# ==========================================================

print("\n" + "=" * 70)
print("DESCRIBE")
print("=" * 70)

print(df.describe())

# ==========================================================
# AGGREGATION USING agg()
# ==========================================================

print("\n" + "=" * 70)
print("MULTIPLE AGGREGATIONS")
print("=" * 70)

print(df["Salary"].agg(["count", "sum", "mean", "median", "min", "max", "std", "var"]))

print("\n" + "=" * 70)
print("AGGREGATION PRACTICE COMPLETED")
print("=" * 70)
