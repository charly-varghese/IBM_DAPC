"""
==========================================================
IBM Data Analyst Professional Certificate

Course 04
Module 04

Practice Lab
Selecting Data in a DataFrame

Author : Varghese
==========================================================
"""

import pandas as pd

print("=" * 60)
print("CREATE DATAFRAME")
print("=" * 60)

# --------------------------------------------------
# Dictionary
# --------------------------------------------------

x = {
    "Name": ["Rose", "John", "Jane", "Mary"],
    "ID": [1, 2, 3, 4],
    "Department": [
        "Architect Group",
        "Software Group",
        "Design Team",
        "Infrastructure",
    ],
    "Salary": [100000, 80000, 50000, 60000],
}

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

df = pd.DataFrame(x)

print(df)

print("\n")

# ==================================================
# COLUMN SELECTION
# ==================================================

print("=" * 60)
print("COLUMN SELECTION")
print("=" * 60)

x = df[["ID"]]

print(x)

print(type(x))

print("\n")

# ==================================================
# MULTIPLE COLUMNS
# ==================================================

print("=" * 60)
print("MULTIPLE COLUMNS")
print("=" * 60)

z = df[["Department", "Salary", "ID"]]

print(z)

print("\n")

# ==================================================
# SERIES
# ==================================================

print("=" * 60)
print("SERIES")
print("=" * 60)

student = df["Name"]

print(student)

print(type(student))

print("\n")

# ==================================================
# EXERCISE 1
# ==================================================

print("=" * 60)
print("EXERCISE 1")
print("=" * 60)

data = {
    "Student": ["David", "Samuel", "Terry", "Evan"],
    "Age": [27, 24, 22, 32],
    "Country": ["UK", "Canada", "China", "USA"],
    "Course": ["Python", "Data Structures", "Machine Learning", "Web Development"],
    "Marks": [85, 72, 89, 76],
}

df1 = pd.DataFrame(data)

print(df1)

print("\n")

# ==================================================
# EXERCISE 2
# ==================================================

print("=" * 60)
print("MARKS COLUMN")
print("=" * 60)

b = df1[["Marks"]]

print(b)

print("\n")

# ==================================================
# EXERCISE 3
# ==================================================

print("=" * 60)
print("COUNTRY AND COURSE")
print("=" * 60)

c = df1[["Country", "Course"]]

print(c)

print("\n")

# ==================================================
# SERIES
# ==================================================

student_series = df1["Student"]

print(student_series)

print(type(student_series))

print("\n")

# ==================================================
# ILOC
# ==================================================

print("=" * 60)
print("ILOC")
print("=" * 60)

print(df.iloc[0, 0])

print(df.iloc[0, 2])

print("\n")

# ==================================================
# LOC
# ==================================================

print("=" * 60)
print("LOC")
print("=" * 60)

print(df.loc[0, "Salary"])

print("\n")

# ==================================================
# SET INDEX
# ==================================================

print("=" * 60)
print("SET INDEX")
print("=" * 60)

df2 = df.set_index("Name")

print(df2)

print("\n")

print(df2.loc["Jane", "Salary"])

print(df2.loc["Jane", "Department"])

print(df2.iloc[3, 2])

print("\n")

# ==================================================
# SLICING
# ==================================================

print("=" * 60)
print("SLICING")
print("=" * 60)

print(df.iloc[0:2, 0:3])

print("\n")

print(df.loc[0:2, "ID":"Department"])

print("\n")

print(df2.loc["Rose":"Jane", "ID":"Department"])

print("\n")

print("=" * 60)
print("IBM LAB COMPLETED")
print("=" * 60)

import pandas as pd

print("=" * 60)
print("CREATE DATAFRAME")
print("=" * 60)

# --------------------------------------------------
# Dictionary
# --------------------------------------------------

x = {
    "Name": ["Rose", "John", "Jane", "Mary"],
    "ID": [1, 2, 3, 4],
    "Department": [
        "Architect Group",
        "Software Group",
        "Design Team",
        "Infrastructure",
    ],
    "Salary": [100000, 80000, 50000, 60000],
}

# --------------------------------------------------
# Create DataFrame
# --------------------------------------------------

df = pd.DataFrame(x)

print(df)

print("\n")

# ==================================================
# COLUMN SELECTION
# ==================================================

print("=" * 60)
print("COLUMN SELECTION")
print("=" * 60)

x = df[["ID"]]

print(x)

print(type(x))

print("\n")

# ==================================================
# MULTIPLE COLUMNS
# ==================================================

print("=" * 60)
print("MULTIPLE COLUMNS")
print("=" * 60)

z = df[["Department", "Salary", "ID"]]

print(z)

print("\n")

# ==================================================
# SERIES
# ==================================================

print("=" * 60)
print("SERIES")
print("=" * 60)

student = df["Name"]

print(student)

print(type(student))

print("\n")

# ==================================================
# EXERCISE 1
# ==================================================

print("=" * 60)
print("EXERCISE 1")
print("=" * 60)

data = {
    "Student": ["David", "Samuel", "Terry", "Evan"],
    "Age": [27, 24, 22, 32],
    "Country": ["UK", "Canada", "China", "USA"],
    "Course": ["Python", "Data Structures", "Machine Learning", "Web Development"],
    "Marks": [85, 72, 89, 76],
}

df1 = pd.DataFrame(data)

print(df1)

print("\n")

# ==================================================
# EXERCISE 2
# ==================================================

print("=" * 60)
print("MARKS COLUMN")
print("=" * 60)

b = df1[["Marks"]]

print(b)

print("\n")

# ==================================================
# EXERCISE 3
# ==================================================

print("=" * 60)
print("COUNTRY AND COURSE")
print("=" * 60)

c = df1[["Country", "Course"]]

print(c)

print("\n")

# ==================================================
# SERIES
# ==================================================

student_series = df1["Student"]

print(student_series)

print(type(student_series))

print("\n")

# ==================================================
# ILOC
# ==================================================

print("=" * 60)
print("ILOC")
print("=" * 60)

print(df.iloc[0, 0])

print(df.iloc[0, 2])

print("\n")

# ==================================================
# LOC
# ==================================================

print("=" * 60)
print("LOC")
print("=" * 60)

print(df.loc[0, "Salary"])

print("\n")

# ==================================================
# SET INDEX
# ==================================================

print("=" * 60)
print("SET INDEX")
print("=" * 60)

df2 = df.set_index("Name")

print(df2)

print("\n")

print(df2.loc["Jane", "Salary"])

print(df2.loc["Jane", "Department"])

print(df2.iloc[3, 2])

print("\n")

# ==================================================
# SLICING
# ==================================================

print("=" * 60)
print("SLICING")
print("=" * 60)

print(df.iloc[0:2, 0:3])

print("\n")

print(df.loc[0:2, "ID":"Department"])

print("\n")

print(df2.loc["Rose":"Jane", "ID":"Department"])

print("\n")

print("=" * 60)
print("IBM LAB COMPLETED")
print("=" * 60)
