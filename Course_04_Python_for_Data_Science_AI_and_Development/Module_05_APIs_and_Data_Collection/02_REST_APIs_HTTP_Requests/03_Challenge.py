"""
IBM DAPC - Course 04
Module 05 - APIs and Data Collection

Lab 02 - REST APIs & HTTP Requests

03_Challenge.py

Challenge:
API Data Collection and Business Analysis

Objective:
Collect user data from a REST API, transform the
nested JSON response into a Pandas DataFrame,
perform business-style analysis, and export the
results to CSV files.
"""

import requests
import pandas as pd
from pathlib import Path

# =========================================================
# 1. Configuration
# =========================================================

API_URL = "https://jsonplaceholder.typicode.com/users"

OUTPUT_DIR = Path("challenge_output")

OUTPUT_DIR.mkdir(exist_ok=True)


# =========================================================
# 2. Retrieve API Data
# =========================================================

try:

    response = requests.get(API_URL, timeout=15)

    print("HTTP Status Code:")
    print(response.status_code)

    response.raise_for_status()

except requests.exceptions.Timeout:

    print("API request timed out.")
    raise SystemExit

except requests.exceptions.RequestException as error:

    print("API request failed:")
    print(error)
    raise SystemExit


# =========================================================
# 3. Convert JSON Response
# =========================================================

users = response.json()

print("\nTotal Records Retrieved:")
print(len(users))


# =========================================================
# 4. Transform Nested JSON
# =========================================================

records = []

for user in users:

    records.append(
        {
            "ID": user["id"],
            "Name": user["name"],
            "Username": user["username"],
            "Email": user["email"],
            "City": user["address"]["city"],
            "Website": user["website"],
            "Company": user["company"]["name"],
        }
    )


# =========================================================
# 5. Create DataFrame
# =========================================================

df = pd.DataFrame(records)

print("\nDataFrame:")
print(df)


# =========================================================
# 6. Business Analysis
# =========================================================

print("\n" + "=" * 60)
print("BUSINESS ANALYSIS")
print("=" * 60)


# ---------------------------------------------------------
# Analysis 1: Total Users
# ---------------------------------------------------------

total_users = len(df)

print("\n1. Total Users:")
print(total_users)


# ---------------------------------------------------------
# Analysis 2: Users by Company
# ---------------------------------------------------------

users_by_company = df["Company"].value_counts()

print("\n2. Users by Company:")
print(users_by_company)


# ---------------------------------------------------------
# Analysis 3: Users by City
# ---------------------------------------------------------

users_by_city = df["City"].value_counts()

print("\n3. Users by City:")
print(users_by_city)


# ---------------------------------------------------------
# Analysis 4: Select Users from a City
# ---------------------------------------------------------

target_city = "Gwenborough"

city_users = df[df["City"] == target_city]

print(f"\n4. Users in {target_city}:")
print(city_users)


# ---------------------------------------------------------
# Analysis 5: Company Search
# ---------------------------------------------------------

company_keyword = "Romaguera"

company_users = df[df["Company"].str.contains(company_keyword, case=False, na=False)]

print(f"\n5. Users connected to companies " f"containing '{company_keyword}':")

print(company_users)


# =========================================================
# 7. Export Main Dataset
# =========================================================

main_output = OUTPUT_DIR / "users_analysis.csv"

df.to_csv(main_output, index=False)

print("\nMain dataset saved:")
print(main_output.resolve())


# =========================================================
# 8. Export City Analysis
# =========================================================

city_output = OUTPUT_DIR / "users_by_city.csv"

users_by_city.to_csv(city_output, header=["User_Count"])

print("\nCity analysis saved:")
print(city_output.resolve())


# =========================================================
# 9. Export Company Analysis
# =========================================================

company_output = OUTPUT_DIR / "users_by_company.csv"

users_by_company.to_csv(company_output, header=["User_Count"])

print("\nCompany analysis saved:")
print(company_output.resolve())


# =========================================================
# 10. Final Summary
# =========================================================

print("\n" + "=" * 60)
print("CHALLENGE COMPLETED")
print("=" * 60)

print(f"Total users processed: {total_users}")
print(f"Output directory: {OUTPUT_DIR.resolve()}")
