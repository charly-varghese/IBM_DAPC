import sqlite3
from pathlib import Path

# --------------------------------------------------
# PATH CONFIGURATION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "HR.db"


# --------------------------------------------------
# CONNECT TO DATABASE
# --------------------------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


print("=" * 70)
print("IBM HR DATABASE VERIFICATION")
print("=" * 70)


# --------------------------------------------------
# VERIFY TABLES
# --------------------------------------------------

tables = ["EMPLOYEES", "JOB_HISTORY", "JOBS", "DEPARTMENTS", "LOCATIONS"]


for table in tables:

    print(f"\n{'-' * 70}")
    print(f"TABLE: {table}")
    print("-" * 70)

    # Row Count
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    row_count = cursor.fetchone()[0]

    print(f"Row Count: {row_count}")

    # Table Structure
    cursor.execute(f"PRAGMA table_info({table})")
    columns = cursor.fetchall()

    print("\nColumns:")

    for column in columns:
        print(f"  {column[1]:<15} " f"{column[2]:<15}")

    # Sample Data
    cursor.execute(f"SELECT * FROM {table} LIMIT 3")
    rows = cursor.fetchall()

    print("\nSample Data:")

    for row in rows:
        print(row)


conn.close()


print("\n" + "=" * 70)
print("DATABASE VERIFICATION COMPLETED")
print("=" * 70)
