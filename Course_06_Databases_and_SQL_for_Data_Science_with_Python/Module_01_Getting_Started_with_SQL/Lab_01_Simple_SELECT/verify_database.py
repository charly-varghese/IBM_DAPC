import sqlite3

connection = sqlite3.connect("data/FilmLocations.db")
cursor = connection.cursor()

cursor.execute("SELECT COUNT(*) FROM FilmLocations")
count = cursor.fetchone()[0]

print("FilmLocations row count:", count)

cursor.execute("PRAGMA table_info(FilmLocations)")
columns = cursor.fetchall()

print("\nColumns:")
for column in columns:
    print(column[1])

connection.close()
