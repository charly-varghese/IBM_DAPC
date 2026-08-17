"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 11
Data Cleaning Pipeline

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 11 - DATA CLEANING PIPELINE")
print("=" * 70)

# ==========================================================
# STEP 1 : Load Dataset
# ==========================================================

print("\nSTEP 1 : Load Dataset")

df = pd.read_csv("../datasets/employees_missing.csv")

print(df)

# ==========================================================
# STEP 2 : Explore Dataset
# ==========================================================

print("\nSTEP 2 : Dataset Information")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nInformation:")
df.info()

print("\nSummary Statistics:")
print(df.describe())

# ==========================================================
# STEP 3 : Missing Value Analysis
# ==========================================================

print("\nSTEP 3 : Missing Values")

missing_before = df.isnull().sum()

print(missing_before)

print("\nTotal Missing Values:", missing_before.sum())

# ==========================================================
# STEP 4 : Data Cleaning
# ==========================================================

print("\nSTEP 4 : Cleaning Dataset")

# Fill Salary with Mean
salary_mean = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(salary_mean)

# Fill Experience with Median
experience_median = df["Experience"].median()
df["Experience"] = df["Experience"].fillna(experience_median)

# Fill Department
df["Department"] = df["Department"].fillna("Unknown")

# Fill City
df["City"] = df["City"].fillna("Not Available")

print("Cleaning Completed.")

# ==========================================================
# STEP 5 : Validation
# ==========================================================

print("\nSTEP 5 : Validation")

missing_after = df.isnull().sum()

print(missing_after)

print("\nTotal Missing Values:", missing_after.sum())

# ==========================================================
# STEP 6 : Save Clean Dataset
# ==========================================================

output_file = "../output/employees_cleaned.csv"

df.to_csv(output_file, index=False)

print(f"\nClean dataset saved to: {output_file}")

# ==========================================================
# STEP 7 : Reload Clean Dataset
# ==========================================================

print("\nSTEP 7 : Reload Clean Dataset")

clean_df = pd.read_csv(output_file)

print(clean_df)

# ==========================================================
# STEP 8 : Cleaning Report
# ==========================================================

print("\n" + "=" * 70)
print("DATA CLEANING REPORT")
print("=" * 70)

print(f"Rows                : {df.shape[0]}")
print(f"Columns             : {df.shape[1]}")
print(f"Missing Before      : {missing_before.sum()}")
print(f"Missing After       : {missing_after.sum()}")
print(f"Output File         : {output_file}")

print("\nPIPELINE COMPLETED SUCCESSFULLY")
print("=" * 70)
