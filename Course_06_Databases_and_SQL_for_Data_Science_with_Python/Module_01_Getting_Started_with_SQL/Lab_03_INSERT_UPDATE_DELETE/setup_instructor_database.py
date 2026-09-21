import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("data/Instructor.db")

cursor = connection.cursor()

# Create the Instructor table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Instructor (
    ins_id INTEGER PRIMARY KEY,
    lastname TEXT,
    firstname TEXT,
    city TEXT,
    country TEXT
)
""")

# Clear existing records for a clean lab setup
cursor.execute("DELETE FROM Instructor")

# Insert initial IBM-style records
initial_data = [
    (1, "Ahuja", "Rav", "Toronto", "CA"),
    (2, "Chong", "Raul", "Markham", "CA"),
    (3, "Vasudevan", "Hima", "Chicago", "US")
]

cursor.executemany("""
INSERT INTO Instructor
(ins_id, lastname, firstname, city, country)
VALUES (?, ?, ?, ?, ?)
""", initial_data)

connection.commit()

print("Instructor database created successfully.")
print("Initial records inserted:", len(initial_data))

connection.close()
