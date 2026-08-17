"""
===============================================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

Module 05 – APIs and Data Collection

Lab 01 – My Practice

Objective:
    Learn how to retrieve and process data from a public REST API.

API Used:
    JSONPlaceholder
    https://jsonplaceholder.typicode.com

Author : Charly Varghese
===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import requests
import pandas as pd

print("=" * 70)
print("MODULE 05")
print("LAB 01 - MY PRACTICE")
print("=" * 70)

# =============================================================================
# API Endpoint
# =============================================================================

url = "https://jsonplaceholder.typicode.com/users"

print("\nConnecting to API...")

# =============================================================================
# Make HTTP Request
# =============================================================================

try:

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    print("Connection Successful")

except Exception as error:

    print("Connection Failed")

    print(error)

    exit()

# =============================================================================
# Convert JSON Response
# =============================================================================

users = response.json()

print("\nJSON Successfully Retrieved")

print(f"Total Users : {len(users)}")

# =============================================================================
# Display First User
# =============================================================================

print("\nFirst User")

print(users[0])

# =============================================================================
# Convert JSON to DataFrame
# =============================================================================

df = pd.DataFrame(users)

print("\nDataFrame Created Successfully")

print(df.head())

# =============================================================================
# Select Important Columns
# =============================================================================

print("\nSelected Columns")

selected_df = df[["id", "name", "username", "email", "phone", "website"]]

print(selected_df)

# =============================================================================
# Basic Information
# =============================================================================

print("\nDataset Information")

print(selected_df.info())

# =============================================================================
# Summary Statistics
# =============================================================================

print("\nSummary")

print(selected_df.describe(include="all"))

# =============================================================================
# Display User Names
# =============================================================================

print("\nCustomer Names")

for name in selected_df["name"]:

    print(name)

# =============================================================================
# Save CSV
# =============================================================================

csv_file = "users_data.csv"

selected_df.to_csv(csv_file, index=False)

print(f"\nCSV File Saved : {csv_file}")

# =============================================================================
# Save Excel
# =============================================================================

excel_file = "users_data.xlsx"

selected_df.to_excel(excel_file, index=False)

print(f"Excel File Saved : {excel_file}")

# =============================================================================
# Final Message
# =============================================================================

print("\n" + "=" * 70)
print("MY PRACTICE COMPLETED SUCCESSFULLY")
print("=" * 70)
