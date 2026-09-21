# Lab 03 — Sub-queries and Nested Selects

## IBM Data Analyst Professional Certificate

### Course 06 — Databases and SQL for Data Science with Python

### Module 03 — Intermediate SQL

---

## 📌 Lab Overview

This lab focuses on understanding and practicing **Sub-queries and Nested SELECT statements** using SQL.

A subquery is a query written inside another SQL query. The result of the inner query is used by the outer query.

This lab was completed using:

- VS Code
- Python
- SQLite
- Local HR Database
- SQL Scripts

The IBM Lab concepts were adapted where necessary to ensure SQLite compatibility.

---

## 🎯 Learning Objectives

After completing this lab, I can:

- Understand what a subquery is.
- Use subqueries inside the `WHERE` clause.
- Use subqueries inside the `SELECT` clause.
- Use subqueries inside the `FROM` clause.
- Work with scalar subqueries.
- Work with multi-row subqueries using `IN`.
- Understand correlated subqueries.
- Create and use derived tables.
- Use nested subqueries for advanced analysis.
- Combine subqueries with aggregate functions.
- Perform date-based calculations using SQLite.
- Execute multiple SQL queries from a single SQL file.

---

## 🧠 Core Concept

## What is a Subquery?

A subquery is a SQL query placed inside another SQL query.

```text
Outer Query
     ↓
Uses Result From
     ↓
Inner Query (Subquery)
```

Example:

SELECT \*
FROM EMPLOYEES
WHERE SALARY > (
SELECT AVG(SALARY)
FROM EMPLOYEES
);

The inner query calculates the average salary.

The outer query finds employees earning more than that average.

🗂 Project Structure
Lab_03_Sub_queries_and_Nested_Selects
│
├── 01_Setup
│ ├── setup_database.py
│ └── verify_database.py
│
├── data
│ ├── Employees.csv
│ ├── JobsHistory.csv
│ ├── Jobs.csv
│ ├── Departments.csv
│ └── Locations.csv
│
├── queries
│ ├── 01_IBM_Lab.sql
│ ├── 02_My_Practice.sql
│ └── 03_Challenge.sql
│
├── HR.db
│
├── run_sql.py
│
├── 04_Debug_Notes.md
│
└── README.md
🗄 Database Used
HR Database

Database file:

HR.db

The database contains five tables.

EMPLOYEES

Contains employee information including:

Employee ID
First name
Last name
Birth date
Salary
Job ID
Manager ID
Department ID

Rows:

10
JOB_HISTORY

Contains employee job history information.

Rows:

10
JOBS

Contains job details including:

Job ID
Job title
Minimum salary
Maximum salary

Rows:

10
DEPARTMENTS

Contains department information.

Rows:

3
LOCATIONS

Contains location information.

Rows:

3
🔧 Database Setup

The database was created using:

python 01_Setup/setup_database.py

The setup process:

Create HR.db
↓
Create Tables
↓
Load CSV Data
↓
Commit Data
↓
Database Ready

Successful database setup:

EMPLOYEES → 10 rows
JOB_HISTORY → 10 rows
JOBS → 10 rows
DEPARTMENTS → 3 rows
LOCATIONS → 3 rows
🔍 Database Verification

Database verification command:

python 01_Setup/verify_database.py

The verification script checks:

Table names
Row counts
Column names
Column data types
Sample records

All tables were successfully verified.

📘 SQL Files
1️⃣ 01_IBM_Lab.sql

This file contains:

IBM Lab Queries
IBM Practice Questions

Topics practiced:

Subquery in WHERE
Subquery in SELECT
Subquery in FROM
Aggregate subqueries
Average salary comparison
Maximum and minimum values
Top salary analysis
Bottom salary analysis
Age comparison
Years of service comparison
Execution Status
SUCCESSFUL
🧪 02_My_Practice.sql

This file contains additional hands-on practice.

Concepts Practiced

1. Employees Above Company Average Salary
   Result: 3 Employees
2. Employee with Maximum Salary
   Result: John Thomas
   Salary: 100000
3. Employee with Minimum Salary
   Result: Steve Wells
   Salary: 50000
4. Employees Above Their Department Average

This query uses a correlated subquery.

Result: 5 Employees 5. Departments with More Than One Employee

Uses:

IN

with a multi-row subquery.

Result: 10 Employees 6. Employees with Top 3 Salaries
Result: 3 Employees 7. Employees Born Earlier Than the Average Birth Date
Result: 5 Employees 8. Company Average Salary as a Column
Company Average Salary: 72000 9. Average of Top 3 Salaries
Average Top 3 Salary: 90000 10. Employees Earning Below the Top 5 Salary Average
Result: 8 Employees
🔥 03_Challenge.sql

This file contains advanced subquery challenges.

Challenge Queries
Challenge 01 — Second Highest Salary
Result: 90000
Challenge 02 — Employee with Second Highest Salary
Result: Nancy Allen
Salary: 90000
Challenge 03 — Department with Highest Average Salary
Department: 2
Average Salary: 86666.67
Challenge 04 — Employees Earning Above Their Department Average
Result: 5 Employees

Uses a correlated subquery.

Challenge 05 — Employees Above Company Average but Below Maximum Salary
Result: 2 Employees
Challenge 06 — Oldest Employee
Result: Alice James

Age is calculated using SQLite julianday().

Challenge 07 — Most Recent Birth Date
Result: Andrea Jones
Challenge 08 — Employees Earning Above Department 5 Average Salary
Result: 6 Employees

Important:

The query calculates the average salary of Department 5 and compares that value against all employees.

Therefore, employees from other departments may also appear in the results.

🧠 Types of Subqueries Practiced

1. Scalar Subquery

Returns one value.

Example:

SELECT AVG(SALARY)
FROM EMPLOYEES;

Common operators:

=
<

> #<=
>
> 2.Multi-Row Subquery

Returns multiple values.

Example:

WHERE DEP_ID IN (
SELECT DEP_ID
FROM EMPLOYEES
);

Common operator:

IN 3. Correlated Subquery

The inner query depends on the outer query.

Example concept:

Outer Employee
↓
Outer DEP_ID
↓
Inner Query Calculates
Department Average
↓
Compare Salary 4. Derived Table

A subquery used inside the FROM clause.

Example:

SELECT AVG(SALARY)
FROM (
SELECT SALARY
FROM EMPLOYEES
ORDER BY SALARY DESC
LIMIT 5
) AS TOP_SALARIES;

Important rule:

Derived tables should have an alias.
🛠 SQLite Adaptations

The IBM Lab concepts were adapted for SQLite.

Age Calculation

SQLite:

ROUND(
(julianday('now') - julianday(B_DATE)) / 365.25,
1
)
Years of Service
ROUND(
(julianday('now') - julianday(START_DATE)) / 365.25,
1
)
⚙️ SQL Execution Utility

A reusable Python SQL execution utility was created:

run_sql.py

The utility performs:

SQL File
↓
Read SQL Content
↓
Separate Queries
↓
Execute One Query at a Time
↓
Display Results
↓
Display Row Count

This avoids the SQLite error:

You can only execute one statement at a time.
▶️ How to Run
Step 1 — Setup Database
python 01_Setup/setup_database.py
Step 2 — Verify Database
python 01_Setup/verify_database.py
Step 3 — Select SQL File

Open:

run_sql.py

Change:

SQL_FILE = BASE_DIR / "queries" / "01_IBM_Lab.sql"

To execute other files:

SQL_FILE = BASE_DIR / "queries" / "02_My_Practice.sql"

or:

SQL_FILE = BASE_DIR / "queries" / "03_Challenge.sql"
Step 4 — Execute
python run_sql.py
🐛 Debugging Highlights
Issue 1 — Running SQL File Using Python

Incorrect:

python 01_IBM_Lab.sql

Correct:

python run_sql.py

Reason:

.sql → SQL Script
.py → Python Script
Issue 2 — Multiple SQL Statements

Problem:

You can only execute one statement at a time.

Solution:

Read SQL File
↓
Split Queries
↓
Execute Individually
Issue 3 — SQLite Date Calculations

Used:

julianday()

to calculate:

Age
Years of Service
📊 Final Execution Summary
01_IBM_Lab.sql
├── IBM Lab Queries
├── IBM Practice Questions
└── VERIFIED ✅

02_My_Practice.sql
├── Queries: 10
└── VERIFIED ✅

03_Challenge.sql
├── Queries: 8
└── VERIFIED ✅
🏆 Final Results
Database Tables: 5

EMPLOYEES → 10 rows
JOB_HISTORY → 10 rows
JOBS → 10 rows
DEPARTMENTS → 3 rows
LOCATIONS → 3 rows

Total SQL Queries Executed: 25

Errors After Debugging: 0
🎓 Key Learning Outcomes

After completing this lab, I can:

✔ Write subqueries inside WHERE clauses

✔ Use scalar subqueries

✔ Use multi-row subqueries with IN

✔ Write correlated subqueries

✔ Use derived tables

✔ Write nested SELECT statements

✔ Combine subqueries with aggregate functions

✔ Find second highest values

✔ Compare values against averages

✔ Perform advanced salary analysis

✔ Perform date-based analysis in SQLite

✔ Execute multi-query SQL files using Python + SQLite
📌 Lab Completion Status
IBM Lab Queries → COMPLETED ✅

IBM Practice Questions → COMPLETED ✅

My Practice Queries → COMPLETED ✅

Challenge Queries → COMPLETED ✅

Database Setup → VERIFIED ✅

Database Verification → VERIFIED ✅

Debug Notes → COMPLETED ✅

README Documentation → COMPLETED ✅
🏁 FINAL STATUS
LAB 03 — SUB-QUERIES AND NESTED SELECTS

COMPLETED AND VERIFIED ✅
👨‍💻 Environment
VS Code
Python
SQLite
SQL
Git
GitHub
