"""
===============================================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

Module 05 – APIs and Data Collection

Lab 01 – Introduction to APIs

File : 01_IBM_Lab.py

Objective:
    • Understand the concept of an API.
    • Learn how Pandas acts as an API.
    • Create and use DataFrames.
    • Perform basic DataFrame operations.
    • Prepare for working with REST APIs.

Author : Charly Varghese
===============================================================================
"""

# =============================================================================
# Import Required Libraries
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt

print("=" * 70)
print("IBM DAPC - MODULE 05")
print("LAB 01 - INTRODUCTION TO APIs")
print("=" * 70)

# =============================================================================
# SECTION 1
# Pandas as an API
# =============================================================================

print("\nSECTION 1 : Pandas as an API")
print("-" * 70)

# Creating a Python Dictionary

student_data = {"Math": [11, 21, 31], "Science": [12, 22, 32]}

print("\nPython Dictionary")
print(student_data)

# =============================================================================
# Creating a Pandas DataFrame
# =============================================================================

df = pd.DataFrame(student_data)

print("\nDataFrame Created Successfully")
print(df)

print("\nData Type")
print(type(df))

# =============================================================================
# Display First Rows
# =============================================================================

print("\nFirst Five Rows")

print(df.head())

# =============================================================================
# Calculate Mean
# =============================================================================

print("\nColumn Mean")

print(df.mean())

# =============================================================================
# Explanation
# =============================================================================

print("""
Observation:

The DataFrame object communicates with the Pandas library.

Instead of manually calculating values,
we simply call methods like:

    df.head()

or

    df.mean()

Pandas performs all the calculations internally
and returns the result.

This is one example of using an API.
""")

# =============================================================================
# SECTION 2
# Introduction to REST APIs
# =============================================================================

print("=" * 70)
print("SECTION 2 : REST APIs")
print("=" * 70)

print("""
REST API (Representational State Transfer API)

A REST API allows Python programs to communicate
with software running on another computer
through HTTP requests.

Request  --->  Internet --->  Server

Response <---  Internet <---  Server

Most REST APIs exchange information
using JSON format.

In the next section,
we will use the NBA API
to retrieve real-world sports data.
""")

print("\nLab Part 1 Completed Successfully.")
