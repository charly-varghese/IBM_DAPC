# ============================================================
# LAB 02: Create and Load Tables using SQL Scripts
# CSV Data Loader
# ============================================================

import csv
import sqlite3
from pathlib import Path

# ------------------------------------------------------------
# File paths
# ------------------------------------------------------------

DATA_FOLDER = Path("data")
DATABASE_PATH = DATA_FOLDER / "lab02_database.db"


# ------------------------------------------------------------
# CSV file to database table mapping
# ------------------------------------------------------------

CSV_TABLES = {
    "PATIENTS.csv": "PATIENTS",
    "MEDICAL_HISTORY.csv": "MEDICAL_HISTORY",
    "MEDICAL_PROCEDURES.csv": "MEDICAL_PROCEDURES",
    "MEDICAL_DEPARTMENTS.csv": "MEDICAL_DEPARTMENTS",
    "MEDICAL_LOCATIONS.csv": "MEDICAL_LOCATIONS",
}


# ------------------------------------------------------------
# Connect to SQLite database
# ------------------------------------------------------------

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


# ------------------------------------------------------------
# Load CSV data into tables
# ------------------------------------------------------------

for csv_filename, table_name in CSV_TABLES.items():

    csv_path = DATA_FOLDER / csv_filename

    print("\n" + "=" * 60)
    print(f"Loading: {csv_filename}")
    print(f"Into table: {table_name}")
    print("=" * 60)

    # Read CSV file
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.reader(file)

        rows = []

        for row in reader:

            # Convert text "NULL" into actual SQL NULL
            cleaned_row = [None if value == "NULL" else value for value in row]

            rows.append(cleaned_row)

    # Get number of columns
    column_count = len(rows[0])

    # Create SQL placeholders
    placeholders = ", ".join(["?"] * column_count)

    # Insert rows
    insert_query = f"INSERT INTO {table_name} " f"VALUES ({placeholders})"

    cursor.executemany(insert_query, rows)

    print(f"Rows loaded: {len(rows)}")


# ------------------------------------------------------------
# Save changes
# ------------------------------------------------------------

connection.commit()


# ------------------------------------------------------------
# Final verification
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("FINAL DATA LOAD VERIFICATION")
print("=" * 60)

for table_name in CSV_TABLES.values():

    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")

    row_count = cursor.fetchone()[0]

    print(f"{table_name}: {row_count} rows")


# ------------------------------------------------------------
# Close connection
# ------------------------------------------------------------

connection.close()

print("\nCSV data loaded successfully.")
