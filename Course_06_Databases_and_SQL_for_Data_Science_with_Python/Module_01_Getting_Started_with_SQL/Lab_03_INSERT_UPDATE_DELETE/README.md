# Lab 03 — INSERT, UPDATE, DELETE

## Course Information

\*_IBM Data Analyst Professional Certificate_

**Course 06:** Databases and SQL for Data Science with Python

**Module:** Module 01 — Getting Started with SQL

**Lab:** INSERT, UPDATE, DELETE

---

## Lab Objective

This lab focused on performing Data Manipulation Language (DML) operations using SQL.

The main operations practiced were:

- `INSERT` — Add new records
- `UPDATE` — Modify existing records
- `DELETE` — Remove records

All operations were verified using `SELECT` queries.

The lab environment used:

```text
VS Code
+
Python
+
SQLite
+
Instructor Database
``
Database Setup
Database
Instructor.db
Table
Instructor
Table Columns
ins_id
lastname
firstname
city
country
Initial Records

The database was created with three initial instructor records:

(1, 'Ahuja', 'Rav', 'Toronto', 'CA')
(2, 'Chong', 'Raul', 'Markham', 'CA')
(3, 'Vasudevan', 'Hima', 'Chicago', 'US')
SQL Concepts Practiced
1.INSERT

Used to add new records to a table.

Insert One Record
INSERT INTO Instructor (
    ins_id,
    lastname,
    firstname,
    city,
    country
)
VALUES (
    4,
    'Saha',
    'Sandip',
    'Edmonton',
    'CA'
);
1. INSERT Multiple Records

Multiple records can be inserted using one INSERT statement.

INSERT INTO Instructor (
    ins_id,
    lastname,
    firstname,
    city,
    country
)
VALUES
    (5, 'Doe', 'John', 'Sydney', 'AU'),
    (6, 'Doe', 'Jane', 'Dhaka', 'BD');
3. UPDATE

Used to modify existing records.

Update One Column
UPDATE Instructor
SET city = 'Toronto'
WHERE ins_id = 4;
Update Multiple Columns
UPDATE Instructor
SET
    city = 'Toronto',
    country = 'CA'
WHERE ins_id = 5;
4. DELETE

Used to remove records from a table.

DELETE FROM Instructor
WHERE ins_id = 6;
IBM Lab Execution

The IBM-style lab workflow was executed successfully.

INSERT Single Record        ✅
INSERT Multiple Records     ✅
UPDATE One Column           ✅
UPDATE Multiple Columns     ✅
DELETE Record               ✅
SELECT Verification         ✅
My Practice

Additional practice exercises were completed using new instructor records.

Practice Operations
INSERT ID 7                    ✅
INSERT IDs 8 and 9             ✅
UPDATE ID 7                    ✅
UPDATE Multiple Columns ID 8   ✅
DELETE ID 9                    ✅
SELECT Verification           ✅
Practice Workflow
INSERT
   ↓
Add Instructor ID 7

INSERT
   ↓
Add Instructor IDs 8 and 9

UPDATE
   ↓
Modify Instructor ID 7

UPDATE
   ↓
Modify Multiple Columns of ID 8

DELETE
   ↓
Remove Instructor ID 9
Challenge Queries

Five DML challenges were completed successfully.

Challenge 1 — INSERT

Inserted:

ID 10
Alex Mathew
Kochi, IN
Challenge 2 — UPDATE

Updated city:

Kochi
↓
Chennai
Challenge 3 — UPDATE Multiple Columns

Updated:

Chennai, IN
↓
Dubai, AE
Challenge 4 — INSERT Multiple Rows

Added:

ID 11 → Raj Kumar
ID 12 → David Smith
Challenge 5 — DELETE

Deleted:

ID 11

Final verification confirmed:

ID 10 → Alex Mathew, Dubai, AE
ID 12 → David Smith, London, UK
Execution Workflow

SQL queries were executed using Python and SQLite.

SQL File
   ↓
run_sql.py
   ↓
Read SQL Statements
   ↓
Split Statements
   ↓
Execute Each Statement
   ↓
Check cursor.description
   ↓
SELECT → Print Results
DML    → Commit Changes
Database Reset Workflow

Because INSERT, UPDATE, and DELETE modify the database, the database was reset before rerunning a complete SQL file.

setup_instructor_database.py
          ↓
Reset Database
          ↓
Restore Initial Records
          ↓
run_sql.py
          ↓
Execute SQL File

Commands:

python setup_instructor_database.py
python run_sql.py
Project Structure
Lab_03_INSERT_UPDATE_DELETE/
│
├── data/
│   └── Instructor.db
│
├── 01_IBM_Lab.sql
├── 02_My_Practice.sql
├── 03_Challenge.sql
│
├── 04_Debug_Notes.md
├── README.md
│
├── setup_instructor_database.py
├── verify_instructor_database.py
└── run_sql.py
Debugging Lessons
Primary Key Uniqueness

The ins_id column is a primary key.

Primary Key
     ↓
Must Be Unique

Attempting to insert the same ID again caused:

UNIQUE constraint failed
DML Changes Database State
INSERT → Adds Data
UPDATE → Modifies Data
DELETE → Removes Data

The database state must be considered before rerunning DML scripts.

Improved SQL Runner

The SQL runner originally checked SQL statement text to detect SELECT.

This was improved using:

cursor.description

This allows the program to correctly detect result-producing queries even when SQL comments appear before the statement.

Key Learning Outcomes

After completing this lab, I can:

Insert a single record using INSERT
Insert multiple records in one statement
Update one column using UPDATE
Update multiple columns using SET
Use WHERE to target specific records
Delete records using DELETE
Verify database changes using SELECT
Understand primary key uniqueness
Handle duplicate key errors
Reset a database for repeatable testing
Execute DML SQL files using Python and SQLite
Lab Status
Environment Setup          ✅
Database Creation          ✅
Database Verification      ✅
IBM Lab Queries            ✅
My Practice                ✅
Challenge Queries          ✅
Debug Notes                ✅
README                     🔄
Final Status
LAB 03 — INSERT, UPDATE, DELETE

STATUS: READY FOR FINAL COMPLETION 🏆
```
