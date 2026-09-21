"""
IBM Data Analyst Professional Certificate
Course 06 - Databases and SQL for Data Science with Python
Module 04 - Accessing Databases Using Python
Lab 01 - Creating Tables, Inserting and Querying Data

IBM Lab Objective:
Create and access a SQLite database using Python.
"""

# ============================================================
# TASK 1 - CREATE SQLITE DATABASE
# ============================================================

import sqlite3
from pathlib import Path

import pandas as pd

print("=" * 70)
print("IBM COURSE 06 - MODULE 04 - LAB 01")
print("CREATE & ACCESS SQLITE DATABASE USING PYTHON")
print("=" * 70)


# Create database inside the Lab 01 data folder
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "INSTRUCTOR.db"

print("\n[TASK 1] Creating SQLite database...")
print(f"Database path: {DB_PATH}")

conn = sqlite3.connect(DB_PATH)

print("Database connection: SUCCESS")


# Create cursor
cursor_obj = conn.cursor()

print("Cursor creation: SUCCESS")


# ============================================================
# TASK 2 - CREATE TABLE
# ============================================================

print("\n[TASK 2] Creating INSTRUCTOR table...")

# Remove the table if it already exists.
# This keeps repeated executions clean and reproducible.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

create_table = """
CREATE TABLE INSTRUCTOR (
    ID INTEGER PRIMARY KEY NOT NULL,
    FNAME VARCHAR(20),
    LNAME VARCHAR(20),
    CITY VARCHAR(20),
    CCODE CHAR(2)
)
"""

cursor_obj.execute(create_table)

print("INSTRUCTOR table: CREATED")


# ============================================================
# TASK 3 - INSERT DATA
# ============================================================

print("\n[TASK 3] Inserting data into INSTRUCTOR...")

# Insert first row
cursor_obj.execute("""
    INSERT INTO INSTRUCTOR
    VALUES (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')
    """)

# Insert remaining two rows
cursor_obj.execute("""
    INSERT INTO INSTRUCTOR
    VALUES
        (2, 'Raul', 'Chong', 'Markham', 'CA'),
        (3, 'Hima', 'Vasudevan', 'Chicago', 'US')
    """)

# Save INSERT operations
conn.commit()

print("3 records inserted successfully")


# ============================================================
# TASK 4 - QUERY DATA
# ============================================================

print("\n[TASK 4] Querying INSTRUCTOR table...")

# ------------------------------------------------------------
# 4A - FETCH ALL ROWS
# ------------------------------------------------------------

statement = "SELECT * FROM INSTRUCTOR"

cursor_obj.execute(statement)

output_all = cursor_obj.fetchall()

print("\n4A - All records:")
for row in output_all:
    print(row)


# ------------------------------------------------------------
# 4B - FETCH TWO ROWS
# ------------------------------------------------------------

cursor_obj.execute(statement)

output_many = cursor_obj.fetchmany(2)

print("\n4B - First two records using fetchmany(2):")
for row in output_many:
    print(row)


# ------------------------------------------------------------
# 4C - FETCH ONLY FNAME
# ------------------------------------------------------------

statement_fname = "SELECT FNAME FROM INSTRUCTOR"

cursor_obj.execute(statement_fname)

output_fname = cursor_obj.fetchall()

print("\n4C - Instructor first names:")
for row in output_fname:
    print(row)


# ------------------------------------------------------------
# BONUS - UPDATE RAV'S CITY
# ------------------------------------------------------------

print("\nBONUS - Updating Rav's city...")

query_update = """
UPDATE INSTRUCTOR
SET CITY = 'MOOSETOWN'
WHERE FNAME = 'Rav'
"""

cursor_obj.execute(query_update)

# Save UPDATE operation
conn.commit()

print("Rav's city updated to MOOSETOWN")


# Verify UPDATE
cursor_obj.execute("SELECT * FROM INSTRUCTOR")

updated_data = cursor_obj.fetchall()

print("\nUpdated INSTRUCTOR data:")
for row in updated_data:
    print(row)


# ============================================================
# TASK 5 - RETRIEVE DATA INTO PANDAS
# ============================================================

print("\n[TASK 5] Retrieving data into Pandas DataFrame...")

df = pd.read_sql("SELECT * FROM INSTRUCTOR", conn)

print("\nPandas DataFrame:")
print(df)


# First instructor's last name
print("\nFirst instructor's last name:")
print(df["LNAME"].iloc[0])


# DataFrame shape
print("\nDataFrame shape:")
print(df.shape)


# ============================================================
# TASK 6 - CLOSE DATABASE CONNECTION
# ============================================================

print("\n[TASK 6] Closing database connection...")

cursor_obj.close()
conn.close()

print("Cursor: CLOSED")
print("Database connection: CLOSED")


# ============================================================
# FINAL STATUS
# ============================================================

print("\n" + "=" * 70)
print("LAB 01 EXECUTION COMPLETED SUCCESSFULLY")
print("=" * 70)
