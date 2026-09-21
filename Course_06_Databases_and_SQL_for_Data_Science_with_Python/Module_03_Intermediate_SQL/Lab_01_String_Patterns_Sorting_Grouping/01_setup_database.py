# ============================================================
# IBM Data Analyst Professional Certificate
# Course 06: Databases and SQL for Data Science with Python
# Module 03: Intermediate SQL
# Lab 01: String Patterns, Sorting and Grouping
#
# File: 01_setup_database.py
# Purpose: Create and load the HR SQLite database
# ============================================================

import csv
import sqlite3
from pathlib import Path

# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).parent

DATABASE_PATH = BASE_DIR / "database" / "HR.db"
SQL_SCRIPT_PATH = BASE_DIR / "sql" / "Script_Create_Tables.sql"
DATA_DIR = BASE_DIR / "data"


# ============================================================
# CREATE DATABASE AND TABLES
# ============================================================


def create_database():
    """Create the SQLite HR database and tables."""

    # Remove old database if it already exists
    if DATABASE_PATH.exists():
        DATABASE_PATH.unlink()
        print("Existing HR.db removed.")

    # Connect to SQLite database
    connection = sqlite3.connect(DATABASE_PATH)

    print(f"Database created: {DATABASE_PATH}")

    # Read SQL table creation script
    with open(SQL_SCRIPT_PATH, "r", encoding="utf-8") as file:
        sql_script = file.read()

    # Execute all CREATE TABLE statements
    connection.executescript(sql_script)

    print("All tables created successfully.")

    connection.close()


# ============================================================
# LOAD CSV DATA
# ============================================================


def load_csv(connection, filename, table_name, columns):
    """Load CSV data into a SQLite table."""

    file_path = DATA_DIR / filename

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:

        reader = csv.reader(file)

        placeholders = ", ".join(["?"] * len(columns))

        column_names = ", ".join(columns)

        insert_query = f"""
        INSERT INTO {table_name} ({column_names})
        VALUES ({placeholders});
        """

        rows = list(reader)

        connection.executemany(insert_query, rows)

        print(f"{len(rows)} rows loaded into {table_name}.")


# ============================================================
# LOAD ALL TABLES
# ============================================================


def load_all_data():
    """Load all HR CSV files into the database."""

    connection = sqlite3.connect(DATABASE_PATH)

    # --------------------------------------------------------
    # DEPARTMENTS
    # --------------------------------------------------------

    load_csv(
        connection,
        "Departments.csv",
        "DEPARTMENTS",
        [
            "DEPT_ID_DEP",
            "DEP_NAME",
            "MANAGER_ID",
            "LOC_ID",
        ],
    )

    # --------------------------------------------------------
    # JOBS
    # --------------------------------------------------------

    load_csv(
        connection,
        "Jobs.csv",
        "JOBS",
        [
            "JOB_IDENT",
            "JOB_TITLE",
            "MIN_SALARY",
            "MAX_SALARY",
        ],
    )

    # --------------------------------------------------------
    # JOB_HISTORY
    # --------------------------------------------------------

    load_csv(
        connection,
        "JobsHistory.csv",
        "JOB_HISTORY",
        [
            "EMPL_ID",
            "START_DATE",
            "JOBS_ID",
            "DEPT_ID",
        ],
    )

    # --------------------------------------------------------
    # LOCATIONS
    # --------------------------------------------------------

    load_csv(
        connection,
        "Locations.csv",
        "LOCATIONS",
        [
            "LOCT_ID",
            "DEP_ID_LOC",
        ],
    )

    # --------------------------------------------------------
    # EMPLOYEES
    # --------------------------------------------------------

    load_csv(
        connection,
        "Employees.csv",
        "EMPLOYEES",
        [
            "EMP_ID",
            "F_NAME",
            "L_NAME",
            "SSN",
            "B_DATE",
            "SEX",
            "ADDRESS",
            "JOB_ID",
            "SALARY",
            "MANAGER_ID",
            "DEP_ID",
        ],
    )

    # Save changes
    connection.commit()

    print("\nAll CSV data loaded successfully.")

    connection.close()


# ============================================================
# VERIFY DATABASE
# ============================================================


def verify_database():
    """Verify the row count in each table."""

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    tables = [
        "EMPLOYEES",
        "JOB_HISTORY",
        "JOBS",
        "DEPARTMENTS",
        "LOCATIONS",
    ]

    print("\n" + "=" * 50)
    print("HR DATABASE VERIFICATION")
    print("=" * 50)

    for table in tables:

        cursor.execute(f"SELECT COUNT(*) FROM {table};")

        count = cursor.fetchone()[0]

        print(f"{table:<15}: {count} rows")

    print("=" * 50)

    connection.close()


# ============================================================
# MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("\nCreating HR Database...")
    print("-" * 50)

    create_database()

    print("\nLoading HR Data...")
    print("-" * 50)

    load_all_data()

    verify_database()

    print("\nHR Database setup completed successfully!")
