# ============================================================
# PETRESCUE Database Verification
# ============================================================

import sqlite3
from pathlib import Path


DATABASE_PATH = (
    Path("database")
    / "PETRESCUE.db"
)


connection = sqlite3.connect(
    DATABASE_PATH
)

cursor = connection.cursor()


print("\n" + "=" * 60)
print("PETRESCUE DATABASE VERIFICATION")
print("=" * 60)


# ------------------------------------------------------------
# Row Count
# ------------------------------------------------------------

cursor.execute(
    """
    SELECT COUNT(*)
    FROM PETRESCUE
    """
)

row_count = cursor.fetchone()[0]

print(
    f"\nTotal Records: {row_count}"
)


# ------------------------------------------------------------
# Display Records
# ------------------------------------------------------------

print("\nPETRESCUE Records:")
print("-" * 60)


cursor.execute(
    """
    SELECT
        ID,
        ANIMAL,
        QUANTITY,
        COST,
        RESCUEDATE
    FROM
        PETRESCUE
    ORDER BY
        ID
    """
)

rows = cursor.fetchall()

for row in rows:
    print(row)


connection.close()


print("\n" + "=" * 60)
print("DATABASE VERIFIED SUCCESSFULLY")
print("=" * 60)
