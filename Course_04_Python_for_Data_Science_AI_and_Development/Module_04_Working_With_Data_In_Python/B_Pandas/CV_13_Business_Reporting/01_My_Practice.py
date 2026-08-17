"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 13
Business Reporting

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 13 - BUSINESS REPORTING")
print("=" * 70)

# ==========================================================
# STEP 1 : Load Dataset
# ==========================================================

df = pd.read_csv("../datasets/processed/employee_database.csv")

print("\nEmployee Database Loaded Successfully")

# ==========================================================
# STEP 2 : Company KPIs
# ==========================================================

print("\n" + "=" * 70)
print("COMPANY KPI SUMMARY")
print("=" * 70)

print(f"Total Employees      : {len(df)}")
print(f"Departments          : {df['Department'].nunique()}")
print(f"Cities               : {df['City'].nunique()}")
print(f"Projects             : {df['Project'].nunique()}")

print(f"\nTotal Salary         : ₹ {df['Salary'].sum():,.2f}")
print(f"Average Salary       : ₹ {df['Salary'].mean():,.2f}")
print(f"Highest Salary       : ₹ {df['Salary'].max():,.2f}")
print(f"Lowest Salary        : ₹ {df['Salary'].min():,.2f}")

# ==========================================================
# STEP 3 : Department Summary
# ==========================================================

print("\n" + "=" * 70)
print("DEPARTMENT REPORT")
print("=" * 70)

department_report = (
    df.groupby("Department")
      .agg(
          Employees=("Employee_ID", "count"),
          Total_Salary=("Salary", "sum"),
          Average_Salary=("Salary", "mean"),
          Highest_Salary=("Salary", "max"),
          Lowest_Salary=("Salary", "min")
      )
      .round(2)
)

print(department_report)

# ==========================================================
# STEP 4 : City Report
# ==========================================================

print("\n" + "=" * 70)
print("CITY REPORT")
print("=" * 70)

city_report = (
    df.groupby("City")
      .agg(
          Employees=("Employee_ID", "count"),
          Average_Salary=("Salary", "mean")
      )
      .round(2)
)

print(city_report)

# ==========================================================
# STEP 5 : Project Report
# ==========================================================

print("\n" + "=" * 70)
print("PROJECT REPORT")
print("=" * 70)

project_report = (
    df.groupby("Project")
      .agg(
          Employees=("Employee_ID", "count")
      )
)

print(project_report)

# ==========================================================
# STEP 6 : Top 5 Highest Paid Employees
# ==========================================================

print("\n" + "=" * 70)
print("TOP 5 HIGHEST PAID EMPLOYEES")
print("=" * 70)

top_salary = (
    df.sort_values(
        by="Salary",
        ascending=False
    )
    [["Name", "Department", "Salary"]]
    .head(5)
)

print(top_salary)

# ==========================================================
# STEP 7 : Save Reports
# ==========================================================

department_report.to_csv(
    "../output/csv/department_summary.csv"
)

city_report.to_csv(
    "../output/csv/city_summary.csv"
)

project_report.to_csv(
    "../output/csv/project_summary.csv"
)

top_salary.to_csv(
    "../output/csv/top_salary_report.csv",
    index=False
)

print("\nCSV Reports Saved Successfully")

# ==========================================================
# STEP 8 : Executive Summary
# ==========================================================

print("\n" + "=" * 70)
print("EXECUTIVE SUMMARY")
print("=" * 70)

print("""
✓ Company KPI Report Generated

✓ Department Report Generated

✓ City Report Generated

✓ Project Report Generated

✓ Top Salary Report Generated

✓ Reports Exported Successfully

Business Reporting Completed.
""")

print("=" * 70)