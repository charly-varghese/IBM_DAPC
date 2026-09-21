import sqlite3
from pathlib import Path

# Create the data directory if it does not exist
Path("data").mkdir(exist_ok=True)

# Create/connect to the SQLite database
connection = sqlite3.connect("data/relational_lab.db")

print("SQLite database created successfully.")
print("Database: data/relational_lab.db")

connection.close()
