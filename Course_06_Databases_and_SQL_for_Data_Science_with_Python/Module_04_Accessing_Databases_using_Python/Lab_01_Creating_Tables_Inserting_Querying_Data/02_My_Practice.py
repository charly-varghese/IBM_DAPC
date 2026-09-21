"""
IBM Data Analyst Professional Certificate
Course 06 - Databases and SQL for Data Science with Python
Module 04 - Accessing Databases Using Python
Lab 01 - My Independent Practice

Objective:
Demonstrate independent use of Python DB-API with SQLite
and Pandas for creating, inserting, querying, updating,
and analyzing database records.
"""

import sqlite3
from pathlib import Path

import pandas as pd

# ============================================================
# 1. PROJECT / DATABASE SETUP
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "MY_PRACTICE.db"

print("=" * 70)
print("LAB 01 - MY INDEPENDENT DATABASE PRACTICE")
print("=" * 70)

print("\n[1] Database Setup")
print(f"Database: {DB_PATH}")


# ============================================================
# 2. DATABASE CONNECTION
# ============================================================

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("Connection: SUCCESS")
print("Cursor: SUCCESS")


# ============================================================
# 3. CREATE EMPLOYEE TABLE
# ============================================================

print("\n[2] Creating EMPLOYEE table...")

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

create_table = """
CREATE TABLE EMPLOYEE (
    EMP_ID INTEGER PRIMARY KEY NOT NULL,
    NAME VARCHAR(30) NOT NULL,
    DEPARTMENT VARCHAR(30),
    CITY VARCHAR(30),
    SALARY REAL
)
"""

cursor.execute(create_table)

print("EMPLOYEE table: CREATED")


# ============================================================
# 4. INSERT EMPLOYEE DATA
# ============================================================

print("\n[3] Inserting employee records...")

employees = [
    (101, "Arun", "Sales", "Kochi", 45000),
    (102, "Meera", "Marketing", "Chennai", 52000),
    (103, "Rahul", "IT", "Bengaluru", 68000),
    (104, "Anita", "Finance", "Mumbai", 61000),
]

insert_sql = """
INSERT INTO EMPLOYEE
(EMP_ID, NAME, DEPARTMENT, CITY, SALARY)
VALUES (?, ?, ?, ?, ?)
"""

cursor.executemany(insert_sql, employees)

conn.commit()

print(f"{cursor.rowcount} employee records inserted.")


# ============================================================
# 5. SELECT - FETCH ALL
# ============================================================

print("\n[4] SELECT * FROM EMPLOYEE")

cursor.execute("SELECT * FROM EMPLOYEE")

all_employees = cursor.fetchall()

for employee in all_employees:
    print(employee)


# ============================================================
# 6. FETCHONE
# ============================================================

print("\n[5] FETCHONE - First Employee")

cursor.execute("SELECT * FROM EMPLOYEE")

first_employee = cursor.fetchone()

print(first_employee)


# ============================================================
# 7. FETCHMANY
# ============================================================

print("\n[6] FETCHMANY(2) - First Two Employees")

cursor.execute("SELECT * FROM EMPLOYEE")

first_two = cursor.fetchmany(2)

for employee in first_two:
    print(employee)


# ============================================================
# 8. FILTERED QUERY
# ============================================================

print("\n[7] Employees with Salary >= 60000")

cursor.execute("""
    SELECT EMP_ID, NAME, DEPARTMENT, SALARY
    FROM EMPLOYEE
    WHERE SALARY >= 60000
    ORDER BY SALARY DESC
    """)

high_salary_employees = cursor.fetchall()

for employee in high_salary_employees:
    print(employee)


# ============================================================
# 9. UPDATE
# ============================================================

print("\n[8] Updating Arun's salary...")

cursor.execute("""
    UPDATE EMPLOYEE
    SET SALARY = 48000
    WHERE EMP_ID = 101
    """)

conn.commit()

print("Arun's salary updated successfully.")


# Verify UPDATE
cursor.execute("""
    SELECT EMP_ID, NAME, SALARY
    FROM EMPLOYEE
    WHERE EMP_ID = 101
    """)

print("Updated record:", cursor.fetchone())


# ============================================================
# 10. PANDAS - READ SQL DATA
# ============================================================

print("\n[9] Loading database data into Pandas...")

df = pd.read_sql("SELECT * FROM EMPLOYEE ORDER BY EMP_ID", conn)

print("\nEmployee DataFrame:")
print(df)


# ============================================================
# 11. BASIC DATA ANALYSIS
# ============================================================

print("\n[10] Basic Data Analysis")

print("\nTotal Employees:")
print(len(df))

print("\nAverage Salary:")
print(df["SALARY"].mean())

print("\nHighest Salary:")
print(df["SALARY"].max())

print("\nEmployees by Department:")
print(df["DEPARTMENT"].value_counts())


# ============================================================
# 12. DATABASE ROW COUNT
# ============================================================

cursor.execute("SELECT COUNT(*) FROM EMPLOYEE")

row_count = cursor.fetchone()[0]

print("\nDatabase Row Count:")
print(row_count)


# ============================================================
# 13. CLOSE CONNECTION
# ============================================================

print("\n[11] Closing database...")

cursor.close()
conn.close()

print("Cursor: CLOSED")
print("Connection: CLOSED")


# ============================================================
# FINAL STATUS
# ============================================================

print("\n" + "=" * 70)
print("MY PRACTICE EXECUTION COMPLETED SUCCESSFULLY")
print("=" * 70)
