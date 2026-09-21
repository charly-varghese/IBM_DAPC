# Debug Notes — Lab 01: CREATE, ALTER, TRUNCATE, DROP

## Module

\*_Module 02 — Introduction to Relational Databases and Tables_

## Lab

\*_Lab 01 — CREATE, ALTER, TRUNCATE, DROP_

---

## 1. Environment

- **Editor:** VS Code
- **Database:** SQLite
- **Execution Tool:** Python `sqlite3`
- **Database File:** `data/relational_lab.db`
- **SQL Execution Script:** `run_sql.py`

---

## 2. Issue: MySQL / IBM Lab vs SQLite Differences

## Problem

The original IBM lab was designed for MySQL and phpMyAdmin.

However, this hands-on practice was completed using SQLite locally in VS Code.

Some SQL commands differ between database systems.

### Example: TRUNCATE

MySQL:

```sql
TRUNCATE TABLE PET;
SQLite does not support:

TRUNCATE TABLE
Solution

Use:

DELETE FROM PET;

This removes all rows while keeping the table structure.

3. Issue: Rows affected: -1
Problem

After running commands such as:

CREATE TABLE PETSALE (...);

or:

ALTER TABLE PETSALE
ADD COLUMN QUANTITY INTEGER;

or:

DROP TABLE PET;

the output showed:

Rows affected: -1
Explanation

This is normal SQLite behavior.

DDL operations such as:

CREATE
ALTER
DROP

do not return a meaningful number of affected rows.

Conclusion
Rows affected: -1

does not indicate an error.

4. Issue: New Column Shows None
Problem

After adding a new column:

ALTER TABLE PETSALE
ADD COLUMN QUANTITY INTEGER;

the output showed:

None

for existing records.

Explanation

Existing records do not automatically receive values when a new column is added.

The new column initially contains:

NULL

Python displays SQLite NULL values as:

None
Solution

Update the new column:

UPDATE PETSALE
SET QUANTITY = 9
WHERE ID = 1;
5. Issue: SQLite TRUNCATE Alternative
Problem

The IBM lab included the concept of:

TRUNCATE TABLE

SQLite does not support this statement.

Solution

Use:

DELETE FROM table_name;

Example:

DELETE FROM PET;

Result:

Rows affected: 3

The table structure remains available, but all rows are removed.

6. Issue: DROP TABLE Verification
Problem

After running:

DROP TABLE PET;

the table should no longer exist.

Running:

SELECT * FROM PET;

would generate an error because the table was deleted.

Solution

Verify existing tables safely using SQLite system metadata:

SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name;

Python verification showed:

[('PETSALE',)]

This confirmed:

PETSALE → Exists
PET     → Successfully dropped
7. Issue: VS Code SQL Syntax Warning
Problem

VS Code displayed a syntax warning for:

ALTER TABLE PETSALE
ADD COLUMN QUANTITY INTEGER;

The warning appeared similar to:

Incorrect syntax near 'COLUMN'
Cause

VS Code was using an MSSQL / SQL Server dialect validator instead of SQLite.

The SQL was valid for SQLite and executed successfully through:

python run_sql.py
Solution

The successful SQLite execution was treated as the actual validation.

The VS Code warning was an editor dialect warning and did not affect the database.

8. Important Reset Requirement
Problem

The SQL files are cumulative.

Running the same script multiple times without resetting the database can cause errors such as:

table already exists

or duplicate data errors.

Solution

Delete the database file:

data/relational_lab.db

Then recreate it:

python setup_database.py

Finally run:

python run_sql.py
9. Key Learning from Debugging
Database Dialects Matter

Different database systems support different SQL syntax.

Examples:

MySQL
↓
TRUNCATE TABLE supported

SQLite
↓
TRUNCATE TABLE not supported

Therefore, database-specific SQL differences must always be considered.

10. Final Debugging Lessons
SQL syntax can vary between database systems.

SQLite NULL values appear as None in Python.

Rows affected: -1 is normal for SQLite DDL commands.

DELETE FROM can be used as the SQLite equivalent
for the TRUNCATE learning objective.

DROP TABLE permanently removes a table.

VS Code SQL warnings may depend on the selected
SQL dialect and validator.

Resetting the database is important when running
cumulative SQL scripts.

```
