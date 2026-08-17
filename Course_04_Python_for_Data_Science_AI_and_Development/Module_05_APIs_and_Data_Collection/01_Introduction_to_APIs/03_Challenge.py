"""
===============================================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

Module 05 – APIs and Data Collection

Lab 01 – Challenge

Objective:
Practice working with REST APIs independently.

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
print("LAB 01 - CHALLENGE")
print("=" * 70)

# =============================================================================
# Challenge 1
# Connect to API
# =============================================================================

print("\nChallenge 1")
print("-" * 70)

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code :", response.status_code)

# =============================================================================
# Challenge 2
# Convert JSON
# =============================================================================

print("\nChallenge 2")
print("-" * 70)

users = response.json()

print("Total Users :", len(users))

# =============================================================================
# Challenge 3
# Print User Names
# =============================================================================

print("\nChallenge 3")
print("-" * 70)

for user in users:

    print(user["name"])

# =============================================================================
# Challenge 4
# Print Emails
# =============================================================================

print("\nChallenge 4")
print("-" * 70)

for user in users:

    print(user["email"])

# =============================================================================
# Challenge 5
# Convert to DataFrame
# =============================================================================

print("\nChallenge 5")
print("-" * 70)

df = pd.DataFrame(users)

print(df.head())

# =============================================================================
# Challenge 6
# Display Selected Columns
# =============================================================================

print("\nChallenge 6")
print("-" * 70)

print(df[["id", "name", "email", "phone"]])

# =============================================================================
# Challenge 7
# Find User with ID = 5
# =============================================================================

print("\nChallenge 7")
print("-" * 70)

print(df[df["id"] == 5])

# =============================================================================
# Challenge 8
# Sort Users by Name
# =============================================================================

print("\nChallenge 8")
print("-" * 70)

sorted_df = df.sort_values("name")

print(sorted_df[["id", "name"]])

# =============================================================================
# Challenge 9
# Save CSV
# =============================================================================

print("\nChallenge 9")
print("-" * 70)

df.to_csv("challenge_users.csv", index=False)

print("CSV Saved Successfully")

# =============================================================================
# Challenge 10
# Save Excel
# =============================================================================

print("\nChallenge 10")
print("-" * 70)

df.to_excel("challenge_users.xlsx", index=False)

print("Excel Saved Successfully")

# =============================================================================
# Bonus Challenge
# =============================================================================

print("\nBONUS CHALLENGE")
print("-" * 70)

company_names = []

for user in users:

    company_names.append(user["company"]["name"])

print("\nCompany Names")

for company in company_names:

    print(company)

# =============================================================================
# End
# =============================================================================

print("\n" + "=" * 70)
print("ALL CHALLENGES COMPLETED")
print("=" * 70)
