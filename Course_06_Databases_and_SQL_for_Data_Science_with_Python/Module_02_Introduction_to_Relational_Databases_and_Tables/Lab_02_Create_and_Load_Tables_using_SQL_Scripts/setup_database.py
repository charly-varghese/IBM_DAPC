# ============================================================
# LAB 02: Create and Load Tables using SQL Scripts
# Database Setup Script
# ============================================================

import sqlite3
from pathlib import Path

# ------------------------------------------------------------
# Define database location
# ------------------------------------------------------------

DATA_FOLDER = Path("data")
DATABASE_PATH = DATA_FOLDER / "lab02_database.db"


# ------------------------------------------------------------
# Create data folder if it does not exist
# ------------------------------------------------------------

DATA_FOLDER.mkdir(exist_ok=True)


# ------------------------------------------------------------
# Create SQLite database
# ------------------------------------------------------------

connection = sqlite3.connect(DATABASE_PATH)

print("SQLite database created successfully.")
print(f"Database: {DATABASE_PATH}")

connection.close()
