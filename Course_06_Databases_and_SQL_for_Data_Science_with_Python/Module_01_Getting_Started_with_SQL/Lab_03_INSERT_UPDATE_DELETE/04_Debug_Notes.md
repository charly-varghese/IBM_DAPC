# Lab 03 — Debug Notes

## Lab

\*_INSERT, UPDATE, DELETE_

---

## Issue 1 — UNIQUE Constraint Failed

## Problem

When the `01_IBM_Lab.sql` file was executed again, the following error occurred:

```text
sqlite3.IntegrityError:
UNIQUE constraint failed: Instructor.ins_id
The error occurred while inserting:

ins_id = 4
Cause

The instructor record with ID 4 had already been inserted during a previous execution.

The ins_id column was created as:

INTEGER PRIMARY KEY

A primary key must contain a unique value.

Running the same INSERT statement again attempted to insert a duplicate ID.

Resolution

The database was reset using:

python setup_instructor_database.py

This restored the database to its initial state with only the original three instructor records.

Then the SQL file was executed again:

python run_sql.py
Key Lesson

When working with a cumulative SQL file containing INSERT statements:

Run SQL File Again
        ↓
Existing Records Already Present
        ↓
Duplicate Primary Key
        ↓
UNIQUE Constraint Error

For repeatable lab execution:

Reset Database
        ↓
Run SQL File
        ↓
Verify Results
Issue 2 — SELECT Query Was Not Detected by run_sql.py
Problem

Initially, the run_sql.py script checked whether a statement was a SELECT query using:

statement.lstrip().upper().startswith("SELECT")

However, a SQL statement containing a comment before the SELECT query was not detected correctly.

Example:

-- Verify the inserted record

SELECT *
FROM Instructor;

The program treated the statement as a non-SELECT operation.

Output:

Rows affected: -1

instead of printing the selected rows.

Cause

The statement started with a SQL comment:

--

Therefore, the Python check did not see SELECT as the first text in the statement.

Resolution

The run_sql.py script was improved to check:

cursor.description

Updated logic:

if cursor.description is not None:

    rows = cursor.fetchall()

    for row in rows:
        print(row)

else:

    connection.commit()
    print(f"Rows affected: {cursor.rowcount}")
Key Lesson

Checking the executed cursor result is more reliable than checking the SQL statement text.

Execute SQL
    ↓
Check cursor.description
    ↓
Rows Returned?
    ↓
YES → Fetch Results
NO  → Commit Database Changes
Issue 3 — Cumulative DML SQL Files Change the Database
Problem

Unlike SELECT queries, DML operations permanently modify the database.

Lab 03 included:

INSERT
UPDATE
DELETE

Each execution changed the current database state.

Cause

The SQL file was designed to execute operations in sequence:

Initial Database
       ↓
INSERT
       ↓
UPDATE
       ↓
DELETE
       ↓
Final Database State

Running the same file again without resetting the database could produce unexpected results or duplicate key errors.

Resolution

A database reset workflow was used before rerunning a complete SQL file:

python setup_instructor_database.py
python run_sql.py
Key Debugging Lessons
1. Primary Keys Must Be Unique
PRIMARY KEY
    ↓
Unique Value Required

Duplicate values produce:

UNIQUE constraint failed
2. DML Queries Modify Database State
INSERT → Adds Records

UPDATE → Modifies Records

DELETE → Removes Records

Always consider the current database state before rerunning a DML script.

3. Verify Every Database Modification

After each DML operation, use:

SELECT *
FROM Instructor;

or a filtered query such as:

SELECT *
FROM Instructor
WHERE ins_id = 4;

Verification confirms whether the operation produced the expected result.

4. Database Reset Is Useful During Practice

For repeatable testing:

Reset Database
      ↓
Execute SQL File
      ↓
Check Output
      ↓
Practice Again

This ensures each test starts from a known database state.

Lab 03 Debug Status
Database Setup                 ✅
Table Verification            ✅
INSERT Debugging               ✅
UPDATE Verification            ✅
DELETE Verification            ✅
PRIMARY KEY Error Resolved     ✅
SQL Runner Improved            ✅
Database Reset Workflow        ✅
Debugging Completed            ✅
```
