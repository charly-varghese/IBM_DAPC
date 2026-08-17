"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 12
Data Integration (Merge & Join)

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 12 - DATA INTEGRATION")
print("=" * 70)

# ==========================================================
# STEP 1 : Load Datasets
# ==========================================================

employees = pd.read_csv("../datasets/employees_cleaned.csv")
departments = pd.read_csv("../datasets/departments.csv")
cities = pd.read_csv("../datasets/cities.csv")
projects = pd.read_csv("../datasets/projects.csv")

print("\nEmployees Dataset")
print(employees.head())

print("\nDepartments Dataset")
print(departments.head())

print("\nCities Dataset")
print(cities.head())

print("\nProjects Dataset")
print(projects.head())

# ==========================================================
# STEP 2 : Merge Employees + Departments
# ==========================================================

print("\n" + "=" * 70)
print("Merge : Employees + Departments")
print("=" * 70)

emp_dept = pd.merge(employees, departments, on="Department", how="left")

print(emp_dept)

# ==========================================================
# STEP 3 : Merge with Cities
# ==========================================================

print("\n" + "=" * 70)
print("Merge : Employees + Cities")
print("=" * 70)

emp_city = pd.merge(employees, cities, on="City", how="left")

print(emp_city)

# ==========================================================
# STEP 4 : Merge with Projects
# ==========================================================

print("\n" + "=" * 70)
print("Merge : Employees + Projects")
print("=" * 70)

emp_project = pd.merge(employees, projects, on="Employee_ID", how="left")

print(emp_project)

# ==========================================================
# STEP 5 : Complete Employee Database
# ==========================================================

print("\n" + "=" * 70)
print("Complete Employee Database")
print("=" * 70)

employee_database = pd.merge(employees, departments, on="Department", how="left")

employee_database = pd.merge(employee_database, cities, on="City", how="left")

employee_database = pd.merge(employee_database, projects, on="Employee_ID", how="left")

print(employee_database)

# ==========================================================
# STEP 6 : Save Integrated Dataset
# ==========================================================

output_file = "../output/employee_database.csv"

employee_database.to_csv(output_file, index=False)

print("\nIntegrated dataset saved successfully.")
print(output_file)

# ==========================================================
# STEP 7 : Report
# ==========================================================

print("\n" + "=" * 70)
print("DATA INTEGRATION REPORT")
print("=" * 70)

print(f"Employee Records : {len(employee_database)}")
print(f"Columns          : {len(employee_database.columns)}")
print(f"Departments      : {employee_database['Department'].nunique()}")
print(f"Cities           : {employee_database['City'].nunique()}")
print(f"Projects         : {employee_database['Project'].nunique()}")

print("\nPipeline Completed Successfully")

print("=" * 70)
