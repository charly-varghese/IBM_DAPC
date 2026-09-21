import sqlite3

connection = sqlite3.connect("data/Instructor.db")

cursor = connection.cursor()

# Check row count
cursor.execute("SELECT COUNT(*) FROM Instructor")
row_count = cursor.fetchone()[0]

print("Instructor row count:", row_count)

# Display table structure
cursor.execute("PRAGMA table_info(Instructor)")

print("\nTable Columns:")

for column in cursor.fetchall():
    print(column[1], "-", column[2])

# Display initial records
cursor.execute("SELECT * FROM Instructor")

print("\nInitial Records:")

for row in cursor.fetchall():
    print(row)

connection.close()
