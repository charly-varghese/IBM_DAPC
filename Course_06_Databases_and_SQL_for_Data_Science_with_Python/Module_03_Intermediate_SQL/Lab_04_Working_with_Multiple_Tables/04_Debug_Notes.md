# Debug Notes — Lab 04: Working with Multiple Tables

📌 Course Information
Course: Databases and SQL for Data Science with Python
Module: Module 03 — Intermediate SQL
Lab: Lab 04 — Working with Multiple Tables
Database: SQLite
Database File: HR.db
1.Database Setup Error — Duplicate Department ID
❌ Error
sqlite3.IntegrityError:
UNIQUE constraint failed: DEPARTMENTS.DEPT_ID_DEP
🔍 Cause

The Departments.csv file contained a duplicate department ID:

2,Architect Group,30001,L0001
5,Software Group,30002,L0002
7,Design Team,30003,L0003
5,Software Group,30004,L0004

The department ID 5 appeared twice.

The DEPT_ID_DEP column was defined as the primary key:

PRIMARY KEY (DEPT_ID_DEP)

A primary key must contain unique values.

✅ Fix

Removed the duplicate row from Departments.csv.

Corrected data:

2,Architect Group,30001,L0001
5,Software Group,30002,L0002
7,Design Team,30003,L0003
🎯 Result

Database setup completed successfully.

EMPLOYEES → 10 rows inserted
JOB_HISTORY → 10 rows inserted
JOBS → 10 rows inserted
DEPARTMENTS → 3 rows inserted
LOCATIONS → 3 rows inserted

HR DATABASE SETUP COMPLETED SUCCESSFULLY
1.Initial Dataset Row Count Issue
❌ Problem

During the first database setup attempt, some tables showed only 9 rows instead of 10.

Example:

EMPLOYEES → 9 rows inserted
JOB_HISTORY → 9 rows inserted
JOBS → 9 rows inserted
🔍 Cause

The CSV data files were not fully aligned with the expected IBM HR dataset structure.

✅ Fix

The CSV files were checked and corrected.

After correction:

EMPLOYEES → 10 rows inserted
JOB_HISTORY → 10 rows inserted
JOBS → 10 rows inserted
🎯 Lesson

Always verify:

Row counts
CSV formatting
Primary keys
Duplicate records

before importing data into a database.

3.run_sql.py Error — .name Attribute
❌ Error
AttributeError:
'str' object has no attribute 'name'

The error occurred at:

print(f"EXECUTING: {SQL_FILE.name}")
🔍 Cause

SQL_FILE was defined as a string instead of a Path object.

Example:

SQL_FILE = "01_IBM_Lab.sql"

A Python string does not have a .name attribute.

✅ Fix

Converted SQL_FILE into a Path object.

Example:

from pathlib import Path

SQL_FILE = Path("01_IBM_Lab.sql")
🎯 Lesson

Use Path objects when working with file properties such as:

SQL_FILE.name
SQL_FILE.exists()
SQL_FILE.read_text()
1.Understanding Table Relationships

The HR database contains multiple related tables.

EMPLOYEES → JOBS

Relationship:

EMPLOYEES.JOB_ID
↓
JOBS.JOB_IDENT

Example:

WHERE E.JOB_ID = J.JOB_IDENT
EMPLOYEES → DEPARTMENTS

Relationship:

EMPLOYEES.DEP_ID
↓
DEPARTMENTS.DEPT_ID_DEP

Example:

WHERE E.DEP_ID = D.DEPT_ID_DEP
EMPLOYEES → JOB_HISTORY

Relationship:

EMPLOYEES.EMP_ID
↓
JOB_HISTORY.EMPL_ID

Example:

WHERE E.EMP_ID = H.EMPL_ID
1.Table Aliases

When working with multiple tables, aliases improve readability.

Example:

FROM EMPLOYEES AS E,
JOBS AS J

Then columns can be referenced as:

E.EMP_ID
E.F_NAME
J.JOB_TITLE
🎯 Lesson

Aliases help:

Reduce query length
Improve readability
Avoid ambiguity
Make multi-table queries easier to manage
1.Avoiding Ambiguous Columns

When multiple tables contain similar column names, always specify the table alias.

Instead of:

SELECT EMP_ID

Use:

SELECT E.EMP_ID

For example:

SELECT
E.EMP_ID,
E.F_NAME,
J.JOB_TITLE
FROM
EMPLOYEES AS E,
JOBS AS J
WHERE
E.JOB_ID = J.JOB_IDENT;
1.Multi-Table Query Logic

When using multiple tables, every relationship must be defined correctly.

Example:

SELECT
E.F_NAME,
D.DEP_NAME,
J.JOB_TITLE
FROM
EMPLOYEES AS E,
DEPARTMENTS AS D,
JOBS AS J
WHERE
E.DEP_ID = D.DEPT_ID_DEP
AND E.JOB_ID = J.JOB_IDENT;
🔍 Important

If the relationship conditions are missing, SQL can create a Cartesian product.

Example of a risky query:

SELECT \*
FROM EMPLOYEES, JOBS;

This can combine every employee with every job.

✅ Correct Approach

Always define the relationship:

WHERE EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;
1.Subquery with Multiple Tables

A subquery can be combined with a multi-table query.

Example:

SELECT
E.EMP_ID,
E.F_NAME,
J.JOB_TITLE,
E.SALARY
FROM
EMPLOYEES AS E,
JOBS AS J
WHERE
E.JOB_ID = J.JOB_IDENT
AND E.SALARY > (
SELECT AVG(SALARY)
FROM EMPLOYEES
);
🎯 Logic
Step 1 → Calculate company average salary

Step 2 → Select employees above that average

Step 3 → Match employees with their jobs

Step 4 → Display employee and job information
1.Correlated Subquery

A correlated subquery can compare an employee's salary with the average salary of their own department.

Example:

SELECT
E1.EMP_ID,
E1.F_NAME,
E1.SALARY
FROM
EMPLOYEES AS E1
WHERE
E1.SALARY > (
SELECT
AVG(E2.SALARY)
FROM
EMPLOYEES AS E2
WHERE
E2.DEP_ID = E1.DEP_ID
);
🎯 Logic
Employee
↓
Find employee department
↓
Calculate average salary for that department
↓
Compare employee salary
1.Salary Range Validation

The JOBS table contains:

MIN_SALARY
MAX_SALARY

Employee salaries can be checked against the allowed job salary range.

Example:

SELECT
E.F_NAME,
J.JOB_TITLE,
E.SALARY
FROM
EMPLOYEES AS E,
JOBS AS J
WHERE
E.JOB_ID = J.JOB_IDENT
AND E.SALARY BETWEEN J.MIN_SALARY
AND J.MAX_SALARY;
🎯 Result

All 10 employees had salaries within their assigned job salary ranges.

11.Database Verification Before Query Execution

Before running SQL queries, the database was verified.

Verification included:

EMPLOYEES → 10 rows
JOB_HISTORY → 10 rows
JOBS → 10 rows
DEPARTMENTS → 3 rows
LOCATIONS → 3 rows
🎯 Lesson

Always verify:

Database file exists
Tables exist
Column structure is correct
Row counts are correct
Sample records are correct

before running SQL practice queries.

12.Final Lab Validation

The following SQL files executed successfully:

01_IBM_Lab.sql
02_My_Practice.sql
03_Challenge.sql
Execution Status
IBM Lab Queries → SUCCESS
My Practice Queries → SUCCESS
Challenge Queries → SUCCESS
Database Setup → SUCCESS
Database Verification → SUCCESS
🧠 Key Debugging Lessons
Primary key values must be unique.

Always validate CSV data before database import.

Check row counts after importing data.

Use Path objects for file properties like `.name`.

Define table relationships correctly.

Use aliases for multi-table queries.

Qualify columns to avoid ambiguity.

join conditions can create Cartesian products.

Verify the database before running SQL queries.

Combine subqueries and multiple tables for advanced analysis.

🏆 Lab 04 Final Debug Status
Database Setup → VERIFIED
Database Structure → VERIFIED
CSV Data → VERIFIED
Table Relationships → VERIFIED
IBM Lab → VERIFIED
My Practice → VERIFIED
Challenge Queries → VERIFIED
🎯 FINAL STATUS
LAB 04 DEBUGGING COMPLETED SUCCESSFULLY
