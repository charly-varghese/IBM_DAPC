# ============================================================
# IBM Data Analyst Professional Certificate
# Course 06: Databases and SQL for Data Science with Python
# Module 03: Intermediate SQL
# Lab 01: String Patterns, Sorting and Grouping
#
# Reusable SQL File Runner
# ============================================================

import sqlite3
import sys
from pathlib import Path

# ============================================================
# DATABASE PATH
# ============================================================

DATABASE_PATH = Path("database") / "HR.db"


# ============================================================
# CHECK COMMAND-LINE ARGUMENT
# ============================================================

if len(sys.argv) != 2:

    print("\nUsage:")
    print("python run_sql.py <SQL_FILE_NAME>")

    sys.exit()


SQL_FILE_PATH = Path(sys.argv[1])


# ============================================================
# CHECK SQL FILE
# ============================================================

if not SQL_FILE_PATH.exists():

    print(f"\nError: File not found: {SQL_FILE_PATH}")

    sys.exit()


# ============================================================
# CONNECT TO DATABASE
# ============================================================

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()


# ============================================================
# READ SQL FILE
# ============================================================

sql_script = SQL_FILE_PATH.read_text(encoding="utf-8")


# ============================================================
# SPLIT AND EXECUTE SQL STATEMENTS
# ============================================================

statements = sql_script.split(";")

query_number = 0


for statement in statements:

    statement = statement.strip()

    # Skip empty statements
    if not statement:
        continue

    query_number += 1

    print(f"\n--- Query {query_number} ---")

    print(statement)

    try:

        cursor.execute(statement)

        # ----------------------------------------------------
        # IF QUERY RETURNS RESULTS
        # ----------------------------------------------------

        if cursor.description is not None:

            rows = cursor.fetchall()

            if rows:

                for row in rows:

                    print(row)

            else:

                print("No rows returned.")

        # ----------------------------------------------------
        # CREATE / INSERT / UPDATE / DELETE
        # ----------------------------------------------------

        else:

            print(f"Rows affected: {cursor.rowcount}")

    except sqlite3.Error as error:

        print(f"\nSQL Error: {error}")

        connection.rollback()

        connection.close()

        sys.exit()


# ============================================================
# SAVE CHANGES
# ============================================================

connection.commit()


# ============================================================
# CLOSE CONNECTION
# ============================================================

connection.close()


print("\nSQL execution completed successfully.")
