import sqlite3
from pathlib import Path

# --------------------------------------------------
# PATH CONFIGURATION
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "HR.db"

# Change this filename when executing another SQL file
SQL_FILE = BASE_DIR / "queries" / "03_Challenge.sql"


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# --------------------------------------------------
# READ SQL FILE
# --------------------------------------------------

with open(SQL_FILE, "r", encoding="utf-8") as file:
    sql_script = file.read()


# --------------------------------------------------
# SPLIT QUERIES
# --------------------------------------------------

queries = [query.strip() for query in sql_script.split(";") if query.strip()]


# --------------------------------------------------
# EXECUTE QUERIES
# --------------------------------------------------

print("=" * 80)
print(f"EXECUTING: {SQL_FILE.name}")
print("=" * 80)


for number, query in enumerate(queries, start=1):

    # Ignore comment-only sections
    cleaned_lines = [
        line for line in query.splitlines() if not line.strip().startswith("--")
    ]

    executable_query = "\n".join(cleaned_lines).strip()

    if not executable_query:
        continue

    print(f"\n{'=' * 80}")
    print(f"QUERY {number}")
    print("=" * 80)

    print("\nSQL:")
    print(executable_query)

    try:
        cursor.execute(executable_query)

        # SELECT query result
        if executable_query.upper().startswith("SELECT"):

            rows = cursor.fetchall()

            column_names = [description[0] for description in cursor.description]

            print("\nRESULT:")

            print(" | ".join(column_names))
            print("-" * 80)

            for row in rows:
                print(" | ".join(str(value) for value in row))

            print(f"\nRows Returned: {len(rows)}")

        else:
            conn.commit()

            print("\nQuery executed successfully.")

    except sqlite3.Error as error:
        print(f"\n❌ SQLITE ERROR: {error}")


# --------------------------------------------------
# CLOSE CONNECTION
# --------------------------------------------------

conn.close()

print("\n" + "=" * 80)
print("SQL EXECUTION COMPLETED")
print("=" * 80)
