# Debug Notes — Lab 03: Sub-queries and Nested Selects

## Course

IBM Data Analyst Professional Certificate

## Course 06

Databases and SQL for Data Science with Python

## Module 03

Intermediate SQL

## Lab 03

Sub-queries and Nested Selects

---

## 1. Database Setup

## Problem

The IBM Lab uses a sample HR database with five tables:

- EMPLOYEES
- JOB_HISTORY
- JOBS
- DEPARTMENTS
- LOCATIONS

The original IBM lab environment uses MySQL through IBM Skills Network Labs.

Our local practice environment uses:

- VS Code
- Python
- SQLite

Therefore, the IBM database structure and CSV data needed to be recreated locally.

## Solution

Created a local SQLite database:

```text
HR.db
Created the five HR tables using the IBM table schema.

Loaded the following CSV files:

Employees.csv
JobsHistory.csv
Jobs.csv
Departments.csv
Locations.csv
Result

Database setup completed successfully.

EMPLOYEES       → 10 rows
JOB_HISTORY     → 10 rows
JOBS            → 10 rows
DEPARTMENTS     → 3 rows
LOCATIONS       → 3 rows

Status:

DATABASE SETUP SUCCESSFUL
2. Database Verification Issue
Problem

When verify_database.py was executed for the first time, the output showed:

IBM HR DATABASE SETUP

instead of:

IBM HR DATABASE VERIFICATION

The output was identical to the database setup process.

Cause

The content of setup_database.py had accidentally been copied into verify_database.py.

Therefore, running:

python 01_Setup/verify_database.py

executed the database setup logic again.

Solution

Replaced the content of verify_database.py with the correct verification script.

The corrected script verifies:

Table names
Row counts
Column names
Column data types
Sample records
Result

All five tables were successfully verified.

EMPLOYEES       → 10 rows
JOB_HISTORY     → 10 rows
JOBS            → 10 rows
DEPARTMENTS     → 3 rows
LOCATIONS       → 3 rows

Status:

DATABASE VERIFICATION SUCCESSFUL
3. Attempting to Run a SQL File with Python
Problem

The following command was executed:

python 01_IBM_Lab.sql

This generated the error:

SyntaxError: leading zeros in decimal integer literals are not permitted
Cause

The .sql file was executed using the Python interpreter.

Python attempted to read SQL comments and SQL syntax as Python code.

For example:

-- IBM LAB 03: SUB-QUERIES AND NESTED SELECTS

is valid SQL syntax but not valid Python syntax.

Important Lesson
Python files
↓
Run using Python

python filename.py
SQL files
↓
Run using a database engine or SQL execution tool

Do NOT use:

python filename.sql
Solution

Created a Python SQL execution utility:

run_sql.py

The Python file reads the SQL file and sends each query to the SQLite database.

Result

SQL files can now be executed through:

python run_sql.py

Status:

ISSUE RESOLVED
4. Multiple SQL Statements Execution Issue
Previous Issue

In earlier SQL practice, executing a SQL file containing multiple statements produced:

sqlite3.ProgrammingError:
You can only execute one statement at a time.
Cause

SQLite's:

cursor.execute()

can execute only one SQL statement at a time.

Example:

cursor.execute(sql_script)

fails when sql_script contains multiple SQL queries.

Solution

The run_sql.py utility reads the SQL file and separates queries.

Each query is executed individually.

Concept:

SQL File
    ↓
Read SQL Content
    ↓
Separate Queries
    ↓
Execute Query 1
    ↓
Display Result
    ↓
Execute Query 2
    ↓
Display Result
    ↓
Continue Until Completed
Result

All Lab 03 SQL files were executed successfully.

Status:

MULTI-QUERY EXECUTION SUCCESSFUL
5. SQLite Date Function Adaptation
Problem

The IBM Lab is designed for MySQL.

Some practice problems require:

Age calculation
Years of service calculation

Date calculations vary between SQL database systems.

SQLite Solution

Used:

julianday('now')

and:

julianday(date_column)

Example:

julianday('now') - julianday(B_DATE)

This calculates the number of days between:

Current Date
      and
Birth Date

Approximate age calculation:

ROUND(
    (julianday('now') - julianday(B_DATE)) / 365.25,
    1
)

Years of service:

ROUND(
    (julianday('now') - julianday(START_DATE)) / 365.25,
    1
)
Result

All date-related practice queries executed successfully.

Status:

SQLITE DATE ADAPTATION SUCCESSFUL
6. Subquery in WHERE Clause
Concept Tested

Find employees earning less than the average salary.

SELECT *
FROM EMPLOYEES
WHERE SALARY < (
    SELECT AVG(SALARY)
    FROM EMPLOYEES
);
Result
7 employees returned
Learning

The inner query runs first:

SELECT AVG(SALARY)

The result is then used by the outer query.

Status:

VERIFIED SUCCESSFULLY
7. Subquery as a Column Expression
Concept Tested

Display employee salary together with the company maximum salary.

SELECT
    EMP_ID,
    SALARY,
    (
        SELECT MAX(SALARY)
        FROM EMPLOYEES
    ) AS MAX_SALARY
FROM EMPLOYEES;
Result
10 rows returned
Maximum Salary = 100000

The same maximum salary value appears for every employee.

Learning

A scalar subquery can be used as a column expression.

Status:

VERIFIED SUCCESSFULLY
8. Subquery for Oldest Employee
Concept Tested

Find the employee with the earliest birth date.

SELECT
    F_NAME,
    L_NAME
FROM EMPLOYEES
WHERE B_DATE = (
    SELECT MIN(B_DATE)
    FROM EMPLOYEES
);
Result
Alice James
Learning

The subquery finds:

MIN(B_DATE)

The outer query retrieves the employee associated with that date.

Status:

VERIFIED SUCCESSFULLY
9. Derived Table Subquery
Concept Tested

Find the average salary of the top five earners.

SELECT AVG(SALARY)
FROM (
    SELECT SALARY
    FROM EMPLOYEES
    ORDER BY SALARY DESC
    LIMIT 5
) AS SALARY_TABLE;
Result
Average Top 5 Salary = 82000
Learning

The inner query creates a temporary derived table.

The outer query performs aggregation on that derived table.

Important rule:

Derived tables should have an alias.

Status:

VERIFIED SUCCESSFULLY
10. Correlated Subquery
Concept Tested

Find employees earning more than the average salary of their own department.

SELECT
    E1.EMP_ID,
    E1.F_NAME,
    E1.L_NAME,
    E1.DEP_ID,
    E1.SALARY
FROM EMPLOYEES AS E1
WHERE E1.SALARY > (
    SELECT AVG(E2.SALARY)
    FROM EMPLOYEES AS E2
    WHERE E2.DEP_ID = E1.DEP_ID
);
Result
5 employees returned
Learning

The inner query depends on:

E1.DEP_ID

from the outer query.

Therefore, this is a:

CORRELATED SUBQUERY

Status:

VERIFIED SUCCESSFULLY
11. Nested Subquery
Concept Tested

Find the second highest salary.

SELECT MAX(SALARY)
FROM EMPLOYEES
WHERE SALARY < (
    SELECT MAX(SALARY)
    FROM EMPLOYEES
);
Result
Second Highest Salary = 90000
Learning Flow
Find Maximum Salary
        ↓
Find Salaries Below Maximum
        ↓
Find Maximum Again
        ↓
Second Highest Salary

Status:

VERIFIED SUCCESSFULLY
12. Challenge Query Verification

All challenge queries were executed successfully.

Challenge 01 → Second Highest Salary
Challenge 02 → Employee with Second Highest Salary
Challenge 03 → Department with Highest Average Salary
Challenge 04 → Above Department Average
Challenge 05 → Above Average but Below Maximum
Challenge 06 → Oldest Employee with Age
Challenge 07 → Most Recent Birth Date
Challenge 08 → Salary Above Department 5 Average

Results:

Queries Executed: 8
Errors: 0

Status:

CHALLENGE QUERIES VERIFIED
13. Final Lab Execution Summary
01_IBM_Lab.sql
├── IBM Lab Queries
├── IBM Practice Questions
└── Status: VERIFIED

02_My_Practice.sql
├── Practice Queries: 10
└── Status: VERIFIED

03_Challenge.sql
├── Challenge Queries: 8
└── Status: VERIFIED

Total:

Total Queries Executed = 25
Errors = 0
Key Lessons Learned
1. A subquery is a query inside another query.

2. Subqueries can be used in:

   WHERE
   SELECT
   FROM

3. Scalar subqueries return a single value.

4. IN is useful when a subquery returns multiple values.

5. Correlated subqueries reference values from the outer query.

6. Derived tables are created using subqueries in the FROM clause.

7. Derived tables should have an alias.

8. SQL files should not be executed directly using Python.

9. Multiple SQL statements require an appropriate execution strategy.

10. SQLite date calculations can be performed using julianday().
Final Debug Status
DATABASE SETUP           → SUCCESS
DATABASE VERIFICATION    → SUCCESS
IBM LAB QUERIES          → SUCCESS
IBM PRACTICE QUERIES     → SUCCESS
MY PRACTICE QUERIES      → SUCCESS
CHALLENGE QUERIES        → SUCCESS

TOTAL ERRORS AFTER FIXES → 0
LAB 03 DEBUG STATUS
COMPLETED AND VERIFIED
