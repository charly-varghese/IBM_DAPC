# Lab 02 — Debug Notes

## Lab Title

\*_Create and Load Tables using SQL Scripts_

---

## 1. SyntaxError in `run_sql.py`

## Error

```text
SyntaxError: expected 'except' or 'finally' block
Cause

A try block in run_sql.py had incorrect indentation or an incomplete structure.

Python requires every try block to be followed by:

except
finally
or both

Incorrect indentation caused Python to stop execution.

Fix

Corrected the indentation and completed the try-except structure.

After fixing the script:

python run_sql.py 02_My_Practice.sql

The SQL queries executed successfully.

Learning

Python indentation is part of the program syntax.

Always check:

try
except
finally
indentation levels

when debugging Python errors.

2. SELECT Queries Initially Did Not Display Results
Problem

The SQL runner initially executed the queries successfully but displayed:

Rows affected: -1

without showing the returned records.

Cause

The SQL execution script was not properly checking whether the executed SQL statement returned a result set.

For SELECT statements, SQLite uses cursor.description to indicate that columns were returned.

Fix

Updated run_sql.py so that after executing each SQL statement it checks:

if cursor.description is not None:

Then the script fetches and prints the query results.

Learning

Different SQL statements behave differently:

SQL Statement_Typical Result
SELECT_Returns rows
INSERT_Returns affected row count
UPDATE_Returns affected row count
DELETE_Returns affected row count
CREATE TABLE_Usually returns -1
DROP TABLE_Usually returns -1
3. Database Tables Were Created but Contained Zero Rows
Problem

Database verification initially showed:

Total Rows: 0

for all CVD database tables.

Cause

Running:

python run_sql.py 01_IBM_Lab.sql

executed the table creation script.

The script contained:

DROP TABLE IF EXISTS ...

followed by:

CREATE TABLE ...

Therefore, existing tables and their data were removed before new empty tables were created.

The CSV data had not yet been loaded again.

Fix

Reloaded the CSV data using:

python load_csv_data.py

The output confirmed:

PATIENTS: 5 rows
MEDICAL_HISTORY: 6 rows
MEDICAL_PROCEDURES: 7 rows
MEDICAL_DEPARTMENTS: 4 rows
MEDICAL_LOCATIONS: 2 rows
Learning

Always understand whether a SQL script contains:

DROP TABLE

because running it can remove existing tables and data.

For this lab, the correct execution sequence is:

1. Create tables
        ↓
2. Load CSV data
        ↓
3. Verify database
        ↓
4. Run practice queries
        ↓
5. Run challenge queries
4. Correct Lab Execution Sequence

The correct workflow for rebuilding the Lab 02 database is:

Step 1 — Create Tables
python run_sql.py 01_IBM_Lab.sql
Step 2 — Load CSV Data
python load_csv_data.py
Step 3 — Verify Database
python verify_database.py
Step 4 — Run My Practice Queries
python run_sql.py 02_My_Practice.sql
Step 5 — Run Challenge Queries
python run_sql.py 03_Challenge.sql
5. SQL Runner Improvement

The run_sql.py script was improved during this lab.

The improved runner can:

Accept a SQL filename as a command-line argument
Execute multiple SQL queries
Display query numbers
Display SQL statements
Print SELECT query results
Show affected rows for data modification statements
Commit database changes
Display execution success confirmation

Example:

python run_sql.py 02_My_Practice.sql

This makes the SQL practice environment more flexible and reusable.

6. SQLite Rows affected: -1
Observation

Some SQL commands displayed:

Rows affected: -1
Explanation

This is normal SQLite behavior for statements that do not return a meaningful row count.

Examples include:

CREATE TABLE
DROP TABLE

Some SELECT operations may also not provide a meaningful rowcount.

Learning

Do not treat:

Rows affected: -1

as an error.

Instead, verify the actual result.

For example:

SELECT
    *
FROM
    PATIENTS;

or:

SELECT name
FROM sqlite_master
WHERE type = 'table';
7. Data Persistence in SQLite
Observation

The CVD data remained available after successful loading.

Important Concept

SQLite stores the database inside a file:

data/lab02_database.db

The data remains available between program executions.

However, running a SQL script containing:

DROP TABLE IF EXISTS table_name;

will remove the table and its stored data.

Learning

SQLite databases are persistent file-based databases.

Always understand the effect of:

DROP TABLE

before executing a database setup script.

8. Final Lab Validation

The final database contained:

Table_Rows
PATIENTS_5
MEDICAL_HISTORY_6
MEDICAL_PROCEDURES_7
MEDICAL_DEPARTMENTS_4
MEDICAL_LOCATIONS_2

All database tables were successfully created and loaded.

9. Final Challenge Validation

The Challenge SQL file successfully tested:

SELECT
WHERE
ORDER BY
BETWEEN
LIKE
COUNT
GROUP BY
HAVING
CREATE TABLE
INSERT
UPDATE
DELETE

The final PATIENT_APPOINTMENTS table verification showed that:

Appointment ID 1 remained
Appointment ID 2 was deleted
Appointment ID 3 was successfully updated
Appointment ID 4 was successfully inserted

Final execution message:

SQL execution completed successfully.
10. Key Debugging Lessons
Python
Check indentation carefully.
Every try block requires except or finally.
Use clear file paths.
Test scripts after every modification.
SQLite
Understand the difference between creating tables and loading data.
DROP TABLE removes existing tables.
CREATE TABLE creates empty table structures.
Data loading must happen after table creation.
Use verification scripts to confirm data persistence.
SQL
SELECT returns result sets.
INSERT, UPDATE, and DELETE modify data.
GROUP BY creates groups.
HAVING filters grouped results.
WHERE filters rows before grouping.
ORDER BY sorts results.
Final Status
Lab 02 — Create and Load Tables using SQL Scripts

IBM Lab: Completed
My Practice: Completed
Challenge: Completed
Database Verification: Completed
Debugging: Completed
Final Validation: Successful

Status: COMPLETED

```
