"""
=============================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

Pandas Mastery Series

Chapter 08
GroupBy

Author : Varghese
=============================================================
"""

import pandas as pd

print("=" * 70)
print("PANDAS MASTERY SERIES")
print("CHAPTER 08 - GROUPBY")
print("=" * 70)

# ==========================================================
# Create DataFrame
# ==========================================================

employee = {

    "Employee_ID":[101,102,103,104,105,106,107,108],

    "Name":[
        "Rose",
        "John",
        "James",
        "Mary",
        "David",
        "Linda",
        "Kevin",
        "Sophia"
    ],

    "Department":[
        "Finance",
        "IT",
        "HR",
        "Marketing",
        "Sales",
        "IT",
        "Finance",
        "HR"
    ],

    "Salary":[
        50000,
        65000,
        45000,
        55000,
        70000,
        62000,
        58000,
        48000
    ],

    "Experience":[
        2,
        5,
        1,
        3,
        6,
        4,
        7,
        2
    ]
}

df = pd.DataFrame(employee)

print("\nFULL DATAFRAME\n")
print(df)

# ==========================================================
# Example 1 : Create Groups
# ==========================================================

print("\n" + "=" * 70)
print("Example 1 : Group by Department")
print("=" * 70)

group = df.groupby("Department")

print(group)

# ==========================================================
# Example 2 : Display Finance Group
# ==========================================================

print("\n" + "=" * 70)
print("Example 2 : Finance Department")
print("=" * 70)

print(group.get_group("Finance"))

# ==========================================================
# Example 3 : Employee Count
# ==========================================================

print("\n" + "=" * 70)
print("Example 3 : Employee Count")
print("=" * 70)

print(group["Name"].count())

# ==========================================================
# Example 4 : Average Salary
# ==========================================================

print("\n" + "=" * 70)
print("Example 4 : Average Salary")
print("=" * 70)

print(group["Salary"].mean())

# ==========================================================
# Example 5 : Total Salary
# ==========================================================

print("\n" + "=" * 70)
print("Example 5 : Total Salary")
print("=" * 70)

print(group["Salary"].sum())

# ==========================================================
# Example 6 : Maximum Salary
# ==========================================================

print("\n" + "=" * 70)
print("Example 6 : Maximum Salary")
print("=" * 70)

print(group["Salary"].max())

# ==========================================================
# Example 7 : Minimum Salary
# ==========================================================

print("\n" + "=" * 70)
print("Example 7 : Minimum Salary")
print("=" * 70)

print(group["Salary"].min())

# ==========================================================
# Example 8 : Average Experience
# ==========================================================

print("\n" + "=" * 70)
print("Example 8 : Average Experience")
print("=" * 70)

print(group["Experience"].mean())

# ==========================================================
# Example 9 : Multiple Aggregations
# ==========================================================

print("\n" + "=" * 70)
print("Example 9 : Multiple Statistics")
print("=" * 70)

print(
    group["Salary"].agg(
        ["count","sum","mean","min","max"]
    )
)

# ==========================================================
# Example 10 : Group by Department and Display All
# ==========================================================

print("\n" + "=" * 70)
print("Example 10 : All Groups")
print("=" * 70)

for department, data in group:

    print(f"\nDepartment : {department}")
    print(data)

print("\n" + "=" * 70)
print("GROUPBY PRACTICE COMPLETED")
print("=" * 70)