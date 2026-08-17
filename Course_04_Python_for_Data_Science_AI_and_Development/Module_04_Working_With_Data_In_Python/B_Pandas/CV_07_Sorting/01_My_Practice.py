"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 07
Sorting Data

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 07 - SORTING")
print("=" * 70)

# ==========================================================
# Create DataFrame
# ==========================================================

employee = {

    "Employee_ID":[101,102,103,104,105,106],

    "Name":[
        "Rose",
        "John",
        "James",
        "Mary",
        "David",
        "Linda"
    ],

    "Department":[
        "Finance",
        "IT",
        "HR",
        "Marketing",
        "Sales",
        "IT"
    ],

    "Salary":[
        50000,
        65000,
        45000,
        55000,
        70000,
        62000
    ],

    "Experience":[
        2,
        5,
        1,
        3,
        6,
        4
    ]
}

df = pd.DataFrame(employee)

print("\nFULL DATAFRAME\n")
print(df)

# ==========================================================
# Example 1 : Sort Salary Ascending
# ==========================================================

print("\n" + "=" * 70)
print("Example 1 : Salary Ascending")
print("=" * 70)

print(df.sort_values(by="Salary"))

# ==========================================================
# Example 2 : Sort Salary Descending
# ==========================================================

print("\n" + "=" * 70)
print("Example 2 : Salary Descending")
print("=" * 70)

print(df.sort_values(by="Salary", ascending=False))

# ==========================================================
# Example 3 : Sort by Name
# ==========================================================

print("\n" + "=" * 70)
print("Example 3 : Name Ascending")
print("=" * 70)

print(df.sort_values(by="Name"))

# ==========================================================
# Example 4 : Sort by Experience
# ==========================================================

print("\n" + "=" * 70)
print("Example 4 : Experience Descending")
print("=" * 70)

print(df.sort_values(by="Experience", ascending=False))

# ==========================================================
# Example 5 : Sort by Department then Salary
# ==========================================================

print("\n" + "=" * 70)
print("Example 5 : Department then Salary")
print("=" * 70)

print(df.sort_values(by=["Department","Salary"]))

# ==========================================================
# Example 6 : Different Order
# ==========================================================

print("\n" + "=" * 70)
print("Example 6 : Department ASC Salary DESC")
print("=" * 70)

print(df.sort_values(
    by=["Department","Salary"],
    ascending=[True,False]
))

# ==========================================================
# Example 7 : Sort Index Ascending
# ==========================================================

print("\n" + "=" * 70)
print("Example 7 : Index Ascending")
print("=" * 70)

print(df.sort_index())

# ==========================================================
# Example 8 : Sort Index Descending
# ==========================================================

print("\n" + "=" * 70)
print("Example 8 : Index Descending")
print("=" * 70)

print(df.sort_index(ascending=False))

# ==========================================================
# Example 9 : Top 3 Highest Salaries
# ==========================================================

print("\n" + "=" * 70)
print("Example 9 : Top 3 Salaries")
print("=" * 70)

top_salary = df.sort_values(
    by="Salary",
    ascending=False
)

print(top_salary.head(3))

# ==========================================================
# Example 10 : Lowest 2 Salaries
# ==========================================================

print("\n" + "=" * 70)
print("Example 10 : Lowest 2 Salaries")
print("=" * 70)

low_salary = df.sort_values(by="Salary")

print(low_salary.head(2))

print("\n" + "=" * 70)
print("SORTING PRACTICE COMPLETED")
print("=" * 70)