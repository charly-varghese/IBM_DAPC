"""
IBM DAPC - Course 04
Module 05 - APIs and Data Collection

Lab 02 - REST APIs & HTTP Requests

02_My_Practice.py

Purpose:
Build a practical API data collection workflow using
HTTP GET requests, JSON responses, error handling,
Pandas DataFrames, and CSV export.
"""

import requests
import pandas as pd

# =========================================================
# 1. API Configuration
# =========================================================

API_URL = "https://jsonplaceholder.typicode.com/users"

OUTPUT_FILE = "api_users.csv"


# =========================================================
# 2. Send GET Request
# =========================================================

try:

    response = requests.get(API_URL, timeout=15)

    print("HTTP Status Code:")
    print(response.status_code)

    response.raise_for_status()

except requests.exceptions.Timeout:

    print("Request timed out.")
    raise SystemExit

except requests.exceptions.RequestException as error:

    print("API request failed:")
    print(error)
    raise SystemExit


# =========================================================
# 3. Convert JSON Response
# =========================================================

users = response.json()

print("\nResponse Data Type:")
print(type(users))

print("\nNumber of Users:")
print(len(users))


# =========================================================
# 4. Inspect One Record
# =========================================================

print("\nFirst User:")
print(users[0])


# =========================================================
# 5. Extract Selected Fields
# =========================================================

selected_users = []

for user in users:

    selected_users.append(
        {
            "ID": user["id"],
            "Name": user["name"],
            "Username": user["username"],
            "Email": user["email"],
            "City": user["address"]["city"],
            "Company": user["company"]["name"],
        }
    )


# =========================================================
# 6. Convert to Pandas DataFrame
# =========================================================

df = pd.DataFrame(selected_users)

print("\nDataFrame:")
print(df)


# =========================================================
# 7. Basic Data Inspection
# =========================================================

print("\nDataFrame Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)


# =========================================================
# 8. Simple Data Analysis
# =========================================================

print("\nUsers by City:")

city_counts = df["City"].value_counts()

print(city_counts)


# =========================================================
# 9. Save Data to CSV
# =========================================================

from pathlib import Path

output_path = Path(OUTPUT_FILE).resolve()

df.to_csv(output_path, index=False)

print("\nData saved successfully.")
print("Output File:", OUTPUT_FILE)
print("Output Path:", output_path)
