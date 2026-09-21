# Debug Notes — Lab 01: Simple SELECT

## Issue 1: SQLite database file appeared as 0 KB

### Problem

After running `setup_database.py`, the database file initially appeared empty.

### Cause

The database connection created the SQLite file, but the table and data had not yet been imported from the CSV dataset.

### Fix

Imported the Film Locations CSV data into the `FilmLocations` table.

### Result

- FilmLocations table created successfully
- Rows imported: 2214

---

## Issue 2: Unable to open database file

### Error

````text
sqlite3.OperationalError: unable to open database file

Cause

The script was executed from a different working directory, so the relative database path could not be found.

Fix

Changed to the correct Lab directory before running:

cd Lab_01_Simple_SELECT

Then executed:

python verify_database.py
Lesson

Relative paths depend on the current working directory.

Issue 3: Multiple SQL statements error
Error
sqlite3.ProgrammingError: You can only execute one statement at a time.
Cause

01_IBM_Lab.sql contained multiple SQL statements, but Python cursor.execute() was receiving the entire SQL file as one statement.

Fix

Updated run_sql.py to split the SQL file into individual statements and execute them one at a time.

Lesson

cursor.execute() executes one SQL statement per call.

Issue 4: SQL syntax error near SELECT
Error
sqlite3.OperationalError: near "SELECT": syntax error
Cause

A SQL query ended with a period (.) instead of a semicolon (;).

This caused the next SELECT statement to be joined incorrectly with the previous query.

Fix

Replaced:

WHERE ReleaseYear >= 2001.

with:

WHERE ReleaseYear >= 2001;
Lesson

Each SQL statement must be properly terminated with a semicolon when multiple statements are stored in the same SQL file.


Save it. **No need to run anything for this file.**

---

# Step 2 — Small improvement to `run_sql.py`

Before we finish, I recommend one small improvement.

Instead of manually changing:

```python
with open("01_IBM_Lab.sql")

then:

with open("02_My_Practice.sql")

then:

with open("03_Challenge.sql")

we will later make the runner easier to use. But don't change it now—we'll keep Lab 01 stable.





````
