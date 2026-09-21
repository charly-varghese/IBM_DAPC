import csv
import sqlite3
from pathlib import Path

# ============================================================
# PATH CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "HR.db"

DATA_DIR = BASE_DIR / "data"


# ============================================================
# DATABASE CONNECTION
# ============================================================

conn = sqlite3.connect(DATABASE_PATH)

cursor = conn.cursor()


print("=" * 60)
print("IBM HR DATABASE SETUP — LAB 04")
print("=" * 60)


# ============================================================
# REMOVE OLD TABLES
# ============================================================

print("\nRemoving old tables (if they exist)...")

cursor.execute("DROP TABLE IF EXISTS JOB_HISTORY")
cursor.execute("DROP TABLE IF EXISTS LOCATIONS")
cursor.execute("DROP TABLE IF EXISTS EMPLOYEES")
cursor.execute("DROP TABLE IF EXISTS JOBS")
cursor.execute("DROP TABLE IF EXISTS DEPARTMENTS")

print("Old tables removed.")


# ============================================================
# CREATE TABLES
# ============================================================

print("\nCreating HR database tables...")


# ------------------------------------------------------------
# EMPLOYEES
# ------------------------------------------------------------

cursor.execute("""
CREATE TABLE EMPLOYEES (
    EMP_ID CHAR(9) NOT NULL,
    F_NAME VARCHAR(15) NOT NULL,
    L_NAME VARCHAR(15) NOT NULL,
    SSN CHAR(9),
    B_DATE DATE,
    SEX CHAR,
    ADDRESS VARCHAR(30),
    JOB_ID CHAR(9),
    SALARY DECIMAL(10,2),
    MANAGER_ID CHAR(9),
    DEP_ID CHAR(9) NOT NULL,
    PRIMARY KEY (EMP_ID)
)
""")


# ------------------------------------------------------------
# JOB_HISTORY
# ------------------------------------------------------------

cursor.execute("""
CREATE TABLE JOB_HISTORY (
    EMPL_ID CHAR(9) NOT NULL,
    START_DATE DATE,
    JOBS_ID CHAR(9) NOT NULL,
    DEPT_ID CHAR(9),
    PRIMARY KEY (EMPL_ID, JOBS_ID)
)
""")


# ------------------------------------------------------------
# JOBS
# ------------------------------------------------------------

cursor.execute("""
CREATE TABLE JOBS (
    JOB_IDENT CHAR(9) NOT NULL,
    JOB_TITLE VARCHAR(30),
    MIN_SALARY DECIMAL(10,2),
    MAX_SALARY DECIMAL(10,2),
    PRIMARY KEY (JOB_IDENT)
)
""")


# ------------------------------------------------------------
# DEPARTMENTS
# ------------------------------------------------------------

cursor.execute("""
CREATE TABLE DEPARTMENTS (
    DEPT_ID_DEP CHAR(9) NOT NULL,
    DEP_NAME VARCHAR(15),
    MANAGER_ID CHAR(9),
    LOC_ID CHAR(9),
    PRIMARY KEY (DEPT_ID_DEP)
)
""")


# ------------------------------------------------------------
# LOCATIONS
# ------------------------------------------------------------

cursor.execute("""
CREATE TABLE LOCATIONS (
    LOCT_ID CHAR(9) NOT NULL,
    DEP_ID_LOC CHAR(9) NOT NULL,
    PRIMARY KEY (LOCT_ID, DEP_ID_LOC)
)
""")


print("All tables created successfully.")


# ============================================================
# LOAD CSV FUNCTION
# ============================================================

def load_csv(csv_file, table_name):

    file_path = DATA_DIR / csv_file

    if not file_path.exists():

        print(f"\nERROR: File not found → {file_path}")

        return

    with open(
        file_path,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.reader(file)

        rows = list(reader)

    if not rows:

        print(
            f"{table_name:<15} → 0 rows inserted"
        )

        return

    # Number of columns
    placeholders = ",".join(
        ["?"] * len(rows[0])
    )

    insert_query = (
        f"INSERT INTO {table_name} "
        f"VALUES ({placeholders})"
    )

    cursor.executemany(
        insert_query,
        rows
    )

    print(
        f"{table_name:<15} → "
        f"{len(rows)} rows inserted"
    )

# ============================================================
# LOAD DATA
# ============================================================

print("\nLoading CSV data...\n")


load_csv("Employees.csv", "EMPLOYEES")

load_csv("JobsHistory.csv", "JOB_HISTORY")

load_csv("Jobs.csv", "JOBS")

load_csv("Departments.csv", "DEPARTMENTS")

load_csv("Locations.csv", "LOCATIONS")


# ============================================================
# COMMIT AND CLOSE
# ============================================================

conn.commit()

conn.close()


print("\n" + "=" * 60)

print("HR DATABASE SETUP COMPLETED SUCCESSFULLY")

print(f"Database created: {DATABASE_PATH}")

print("=" * 60)
