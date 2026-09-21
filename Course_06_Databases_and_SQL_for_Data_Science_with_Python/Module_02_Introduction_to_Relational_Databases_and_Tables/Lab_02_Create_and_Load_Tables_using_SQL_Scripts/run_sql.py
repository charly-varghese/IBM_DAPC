# ============================================================
# LAB 02: Create and Load Tables using SQL Scripts
# Reusable SQL File Runner
# ============================================================

import sqlite3
import sys
from pathlib import Path

DATABASE_PATH = Path("data") / "lab02_database.db"


# ------------------------------------------------------------
# Check command-line argument
# ------------------------------------------------------------

if len(sys.argv) != 2:
    print("\nUsage:")
    print("python run_sql.py <SQL_FILE_NAME>")
    sys.exit()


SQL_FILE_PATH = Path(sys.argv[1])


# ------------------------------------------------------------
# Check SQL file
# ------------------------------------------------------------

if not SQL_FILE_PATH.exists():
    print(f"\nError: File not found: {SQL_FILE_PATH}")
    sys.exit()


# ------------------------------------------------------------
# Connect to database
# ------------------------------------------------------------

connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()


# ------------------------------------------------------------
# Read SQL file
# ------------------------------------------------------------

sql_script = SQL_FILE_PATH.read_text(encoding="utf-8")


# ------------------------------------------------------------
# Split and execute SQL statements
# ------------------------------------------------------------

statements = sql_script.split(";")

query_number = 0


for statement in statements:

    statement = statement.strip()

    if not statement:
        continue

    query_number += 1

    print(f"\n--- Query {query_number} ---")
    print(statement)

    try:

        cursor.execute(statement)

        # If query returns a result set
        if cursor.description is not None:

            rows = cursor.fetchall()

            if rows:

                for row in rows:
                    print(row)

            else:

                print("No rows returned.")

        # For CREATE, INSERT, UPDATE, DELETE, etc.
        else:

            print(f"Rows affected: {cursor.rowcount}")

    except sqlite3.Error as error:

        print(f"\nSQL Error: {error}")

        connection.rollback()
        connection.close()

        sys.exit()


# ------------------------------------------------------------
# Save changes
# ------------------------------------------------------------

connection.commit()


# ------------------------------------------------------------
# Close connection
# ------------------------------------------------------------

connection.close()

print("\nSQL execution completed successfully.")
