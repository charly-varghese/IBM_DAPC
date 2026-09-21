# ============================================================
# LAB 02: Create and Load Tables using SQL Scripts
# Final Database Verification Script
# ============================================================

import sqlite3
from pathlib import Path

# ------------------------------------------------------------
# Database path
# ------------------------------------------------------------

DATABASE_PATH = Path("data") / "lab02_database.db"


# ------------------------------------------------------------
# Connect to database
# ------------------------------------------------------------

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


# ------------------------------------------------------------
# Tables to verify
# ------------------------------------------------------------

TABLES = [
    "PATIENTS",
    "MEDICAL_HISTORY",
    "MEDICAL_PROCEDURES",
    "MEDICAL_DEPARTMENTS",
    "MEDICAL_LOCATIONS",
]


print("\n" + "=" * 70)
print("FINAL CVD DATABASE VERIFICATION")
print("=" * 70)


# ------------------------------------------------------------
# Verify each table
# ------------------------------------------------------------

for table_name in TABLES:

    print("\n" + "-" * 70)
    print(f"TABLE: {table_name}")
    print("-" * 70)

    # Row count
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")

    row_count = cursor.fetchone()[0]

    print(f"\nTotal Rows: {row_count}")

    # Display all records
    print("\nRecords:")

    cursor.execute(f"SELECT * FROM {table_name}")

    rows = cursor.fetchall()

    for row in rows:
        print(row)


# ------------------------------------------------------------
# Close connection
# ------------------------------------------------------------

connection.close()

print("\n" + "=" * 70)
print("DATABASE VERIFICATION COMPLETED SUCCESSFULLY")
print("=" * 70)
