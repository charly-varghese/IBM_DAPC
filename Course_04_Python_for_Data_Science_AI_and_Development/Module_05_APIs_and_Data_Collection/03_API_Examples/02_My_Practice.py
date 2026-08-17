"""
IBM DAPC - Course 04
Module 05 - APIs and Data Collection

Lab 03 - API Examples

02_My_Practice.py

Purpose:
Build a professional API data collection workflow using
the Random User API, data validation, Pandas DataFrame,
basic analysis, and CSV export.
"""

from pathlib import Path

import pandas as pd
from randomuser import RandomUser

# =========================================================
# 1. Configuration
# =========================================================

NUMBER_OF_USERS = 20

OUTPUT_DIR = Path("practice_output")
OUTPUT_FILE = OUTPUT_DIR / "random_users.csv"


# Create output directory if it does not exist
OUTPUT_DIR.mkdir(exist_ok=True)


# =========================================================
# 2. Collect User Data
# =========================================================

print("=" * 60)
print("RANDOM USER API - DATA COLLECTION")
print("=" * 60)

users = RandomUser.generate_users(NUMBER_OF_USERS)

print("\nUsers Generated:")
print(len(users))


# =========================================================
# 3. Extract Required Fields
# =========================================================

user_records = []

for user in users:

    user_records.append(
        {
            "Name": user.get_full_name(),
            "Gender": user.get_gender(),
            "City": user.get_city(),
            "State": user.get_state(),
            "Email": user.get_email(),
            "DOB": user.get_dob(),
            "Picture": user.get_picture(),
        }
    )


# =========================================================
# 4. Create Pandas DataFrame
# =========================================================

df = pd.DataFrame(user_records)

print("\nDataFrame Created Successfully.")


# =========================================================
# 5. Data Validation
# =========================================================

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# =========================================================
# 6. Display Sample Records
# =========================================================

print("\n" + "=" * 60)
print("SAMPLE DATA")
print("=" * 60)

print(df.head())


# =========================================================
# 7. Basic Analysis
# =========================================================

print("\n" + "=" * 60)
print("BASIC ANALYSIS")
print("=" * 60)


# ---------------------------------------------------------
# Gender Distribution
# ---------------------------------------------------------

gender_distribution = df["Gender"].value_counts()

print("\nGender Distribution:")
print(gender_distribution)


# ---------------------------------------------------------
# Users by State
# ---------------------------------------------------------

state_distribution = df["State"].value_counts()

print("\nTop States:")
print(state_distribution.head(10))


# ---------------------------------------------------------
# Users by City
# ---------------------------------------------------------

city_distribution = df["City"].value_counts()

print("\nTop Cities:")
print(city_distribution.head(10))


# =========================================================
# 8. Data Quality Check
# =========================================================

print("\n" + "=" * 60)
print("DATA QUALITY CHECK")
print("=" * 60)

required_columns = [
    "Name",
    "Gender",
    "City",
    "State",
    "Email",
    "DOB",
    "Picture",
]

missing_columns = [column for column in required_columns if column not in df.columns]

if not missing_columns:

    print("All required columns are present.")

else:

    print("Missing columns:")
    print(missing_columns)


# =========================================================
# 9. Export Main Dataset
# =========================================================

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig",
)


# =========================================================
# 10. Verify Output File
# =========================================================

output_path = OUTPUT_FILE.resolve()

print("\n" + "=" * 60)
print("EXPORT INFORMATION")
print("=" * 60)

print("\nData saved successfully.")
print("Output File:")
print(OUTPUT_FILE)

print("\nOutput Path:")
print(output_path)

print("\nFile Exists:")
print(output_path.exists())

if output_path.exists():

    print("\nFile Size:")
    print(f"{output_path.stat().st_size} bytes")


# =========================================================
# 11. Final Summary
# =========================================================

print("\n" + "=" * 60)
print("API DATA COLLECTION COMPLETED")
print("=" * 60)

print(f"Users processed: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Output file: {OUTPUT_FILE}")
