# ============================================================
# IBM Data Analyst Professional Certificate
# Course 06: Databases and SQL for Data Science with Python
# Module 03: Intermediate SQL
# Lab 02: Built-in Functions
#
# Database Setup Script
# ============================================================

import sqlite3
from pathlib import Path

# ------------------------------------------------------------
# Project Paths
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATABASE_DIR = BASE_DIR / "database"
DATABASE_PATH = DATABASE_DIR / "PETRESCUE.db"

SQL_FILE_PATH = BASE_DIR / "sql" / "PETRESCUE-CREATE.sql"


# ------------------------------------------------------------
# Create Database Directory
# ------------------------------------------------------------

DATABASE_DIR.mkdir(exist_ok=True)


# ------------------------------------------------------------
# Remove Existing Database
# ------------------------------------------------------------

if DATABASE_PATH.exists():
    DATABASE_PATH.unlink()


print("\nCreating PETRESCUE Database...")
print("-" * 50)


# ------------------------------------------------------------
# Connect to SQLite
# ------------------------------------------------------------

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


# ------------------------------------------------------------
# Read IBM SQL Script
# ------------------------------------------------------------

sql_script = SQL_FILE_PATH.read_text(encoding="utf-8")


# ------------------------------------------------------------
# Execute SQL Script
# ------------------------------------------------------------

cursor.executescript(sql_script)

connection.commit()


print(f"Database created: {DATABASE_PATH}")
print("PETRESCUE table created successfully.")


# ------------------------------------------------------------
# Verify Data
# ------------------------------------------------------------

print("\nVerifying Database...")
print("-" * 50)


cursor.execute("""
    SELECT COUNT(*)
    FROM PETRESCUE
    """)

row_count = cursor.fetchone()[0]

print(f"PETRESCUE : {row_count} rows")


# ------------------------------------------------------------
# Display Table Structure
# ------------------------------------------------------------

print("\nPETRESCUE Table Columns:")
print("-" * 50)


cursor.execute("""
    PRAGMA table_info(PETRESCUE)
    """)

columns = cursor.fetchall()

for column in columns:

    print(f"{column[1]} | {column[2]}")


# ------------------------------------------------------------
# Close Connection
# ------------------------------------------------------------

connection.close()


print("\n" + "=" * 50)
print("PETRESCUE DATABASE SETUP COMPLETED SUCCESSFULLY!")
print("=" * 50)
