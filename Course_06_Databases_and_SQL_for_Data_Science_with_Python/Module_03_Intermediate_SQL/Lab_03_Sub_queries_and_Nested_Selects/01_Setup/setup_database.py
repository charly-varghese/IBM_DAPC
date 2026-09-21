import sqlite3
import csv
from pathlib import Path

# --------------------------------------------------
# PATH CONFIGURATION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "HR.db"
DATA_DIR = BASE_DIR / "data"
SQL_FILE = Path(__file__).resolve().parent / "Script_Create_Tables.sql"


# --------------------------------------------------
# CREATE DATABASE CONNECTION
# --------------------------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("=" * 60)
print("IBM HR DATABASE SETUP")
print("=" * 60)


# --------------------------------------------------
# DROP OLD TABLES
# --------------------------------------------------

print("\nRemoving old tables (if they exist)...")

tables = ["EMPLOYEES", "JOB_HISTORY", "JOBS", "DEPARTMENTS", "LOCATIONS"]

for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

conn.commit()

print("Old tables removed.")


# --------------------------------------------------
# CREATE TABLES
# --------------------------------------------------

print("\nCreating HR database tables...")

with open(SQL_FILE, "r", encoding="utf-8") as file:
    sql_script = file.read()

cursor.executescript(sql_script)

print("All tables created successfully.")


# --------------------------------------------------
# FUNCTION TO LOAD CSV DATA
# --------------------------------------------------


def load_csv(table_name, csv_file):
    csv_path = DATA_DIR / csv_file

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        rows = list(reader)

    placeholders = ",".join(["?"] * len(rows[0]))

    cursor.executemany(f"INSERT INTO {table_name} VALUES ({placeholders})", rows)

    conn.commit()

    print(f"{table_name:<15} → {len(rows)} rows inserted")


# --------------------------------------------------
# LOAD CSV FILES
# --------------------------------------------------

print("\nLoading CSV data...\n")

load_csv("EMPLOYEES", "Employees.csv")
load_csv("JOB_HISTORY", "JobsHistory.csv")
load_csv("JOBS", "Jobs.csv")
load_csv("DEPARTMENTS", "Departments.csv")
load_csv("LOCATIONS", "Locations.csv")


# --------------------------------------------------
# FINAL COMMIT & CLOSE
# --------------------------------------------------

conn.commit()
conn.close()

print("\n" + "=" * 60)
print("HR DATABASE SETUP COMPLETED SUCCESSFULLY")
print(f"Database created: {DB_PATH}")
print("=" * 60)
