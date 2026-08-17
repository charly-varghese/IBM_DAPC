"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 14
Time Series Analysis

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 14 - TIME SERIES ANALYSIS")
print("=" * 70)

# ==========================================================
# STEP 1 : Load Dataset
# ==========================================================

df = pd.read_csv("../datasets/processed/employee_database.csv")

print("\nEmployee Database Loaded Successfully")

# ==========================================================
# STEP 2 : Convert Join_Date
# ==========================================================

df["Join_Date"] = pd.to_datetime(df["Join_Date"])

print("\nJoin_Date converted to datetime.")

# ==========================================================
# STEP 3 : Extract Date Components
# ==========================================================

df["Year"] = df["Join_Date"].dt.year
df["Month"] = df["Join_Date"].dt.month
df["Month_Name"] = df["Join_Date"].dt.month_name()
df["Day"] = df["Join_Date"].dt.day

print("\nDate Components Added")

print(df.head())

# ==========================================================
# STEP 4 : Monthly Joining Report
# ==========================================================

print("\n" + "=" * 70)
print("MONTHLY JOINING REPORT")
print("=" * 70)

monthly = df.groupby("Month_Name").agg(Employees=("Employee_ID", "count"))

print(monthly)

# ==========================================================
# STEP 5 : Yearly Joining Report
# ==========================================================

print("\n" + "=" * 70)
print("YEARLY JOINING REPORT")
print("=" * 70)

yearly = df.groupby("Year").agg(Employees=("Employee_ID", "count"))

print(yearly)

# ==========================================================
# STEP 6 : Employees Joined in 2024
# ==========================================================

print("\n" + "=" * 70)
print("EMPLOYEES JOINED IN 2024")
print("=" * 70)

joined_2024 = df[df["Year"] == 2024]

print(joined_2024)

# ==========================================================
# STEP 7 : Employees Joined After 2023
# ==========================================================

print("\n" + "=" * 70)
print("JOINED AFTER 2023")
print("=" * 70)

recent = df[df["Join_Date"] >= "2024-01-01"]

print(recent)

# ==========================================================
# STEP 8 : Save Reports
# ==========================================================

monthly.to_csv("../output/csv/monthly_joining_report.csv")

yearly.to_csv("../output/csv/yearly_joining_report.csv")

print("\nReports Saved Successfully")

# ==========================================================
# STEP 9 : Executive Summary
# ==========================================================

print("\n" + "=" * 70)
print("TIME SERIES SUMMARY")
print("=" * 70)

print(f"Total Employees : {len(df)}")
print(f"Years Covered   : {df['Year'].nunique()}")
print(f"First Join Date : {df['Join_Date'].min().date()}")
print(f"Latest Join Date: {df['Join_Date'].max().date()}")

print("\nTime Series Analysis Completed Successfully")

print("=" * 70)
