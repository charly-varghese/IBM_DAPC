import csv
import sqlite3
from pathlib import Path

DB_PATH = Path("data/FilmLocations.db")
CSV_PATH = Path("data/Film_Locations_in_San_Francisco.csv")

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS FilmLocations")
cursor.execute("""
CREATE TABLE IF NOT EXISTS FilmLocations (
    Title TEXT,
    ReleaseYear INTEGER,
    Locations TEXT,
    FunFacts TEXT,
    ProductionCompany TEXT,
    Distributor TEXT,
    Director TEXT,
    Writer TEXT,
    Actor1 TEXT,
    Actor2 TEXT,
    Actor3 TEXT
)
""")

with open(CSV_PATH, encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    rows = [
        (
            row["Title"],
            int(row["Release Year"]) if row["Release Year"] else None,
            row["Locations"],
            row["Fun Facts"],
            row["Production Company"],
            row["Distributor"],
            row["Director"],
            row["Writer"],
            row["Actor 1"],
            row["Actor 2"],
            row["Actor 3"],
        )
        for row in reader
    ]

cursor.executemany(
    """
INSERT INTO FilmLocations (
    Title,
    ReleaseYear,
    Locations,
    FunFacts,
    ProductionCompany,
    Distributor,
    Director,
    Writer,
    Actor1,
    Actor2,
    Actor3
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
    rows,
)

connection.commit()
connection.close()

print("FilmLocations table created successfully.")
print("Rows imported:", len(rows))
