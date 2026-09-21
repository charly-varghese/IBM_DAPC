# Lab 04 — Working with Multiple Tables

📚 Course Information
Item Details
Course Databases and SQL for Data Science with Python
Module Module 03 — Intermediate SQL
Lab Lab 04 — Working with Multiple Tables
Database SQLite
Database File HR.db
🎯 Lab Objective

The objective of this lab is to practice working with multiple related database tables using SQL.

The lab focuses on:

Working with multiple tables
Understanding table relationships
Combining data from related tables
Using table aliases
Writing multi-table queries
Using subqueries with multiple tables
Performing salary analysis
Analyzing department information
Working with employee job history
🗂️ Project Structure
Lab_04_Working_with_Multiple_Tables/
│
├── 01_Setup/
│ ├── setup_database.py
│ └── verify_database.py
│
├── 02_SQL/
│ ├── 01_IBM_Lab.sql
│ ├── 02_My_Practice.sql
│ └── 03_Challenge.sql
│
├── data/
│ ├── Employees.csv
│ ├── Job_History.csv
│ ├── Jobs.csv
│ ├── Departments.csv
│ └── Locations.csv
│
├── HR.db
│
├── run_sql.py
│
├── 04_Debug_Notes.md
│
└── README.md
🗄️ Database Tables

The lab uses an IBM HR database containing five related tables.

1️⃣ EMPLOYEES

Contains employee information.

Important columns:

EMP_ID
F_NAME
L_NAME
JOB_ID
SALARY
DEP_ID
MANAGER_ID
2️⃣ JOBS

Contains job information and salary ranges.

Important columns:

JOB_IDENT
JOB_TITLE
MIN_SALARY
MAX_SALARY
3️⃣ DEPARTMENTS

Contains department information.

Important columns:

DEPT_ID_DEP
DEP_NAME
MANAGER_ID
LOC_ID
4️⃣ JOB_HISTORY

Contains employee job history.

Important columns:

EMPL_ID
START_DATE
JOBS_ID
DEPT_ID
5️⃣ LOCATIONS

Contains department location information.

Important columns:

LOCT_ID
DEP_ID_LOC
🔗 Table Relationships
EMPLOYEES → JOBS
EMPLOYEES.JOB_ID
↓
JOBS.JOB_IDENT

SQL relationship:

E.JOB_ID = J.JOB_IDENT
EMPLOYEES → DEPARTMENTS
EMPLOYEES.DEP_ID
↓
DEPARTMENTS.DEPT_ID_DEP

SQL relationship:

E.DEP_ID = D.DEPT_ID_DEP
EMPLOYEES → JOB_HISTORY
EMPLOYEES.EMP_ID
↓
JOB_HISTORY.EMPL_ID

SQL relationship:

E.EMP_ID = H.EMPL_ID
⚙️ Database Setup

Run the database setup script:

python 01_Setup/setup_database.py

Expected result:

EMPLOYEES → 10 rows inserted
JOB_HISTORY → 10 rows inserted
JOBS → 10 rows inserted
DEPARTMENTS → 3 rows inserted
LOCATIONS → 3 rows inserted

HR DATABASE SETUP COMPLETED SUCCESSFULLY
🔍 Database Verification

Verify the database structure and data:

python 01_Setup/verify_database.py

Verification confirms:

EMPLOYEES → 10 rows
JOB_HISTORY → 10 rows
JOBS → 10 rows
DEPARTMENTS → 3 rows
LOCATIONS → 3 rows
▶️ Running SQL Queries

The SQL runner executes the selected SQL file against the HR.db database.

Example:

python run_sql.py

The runner displays:

SQL Query
↓
Query Result
↓
Rows Returned
📘 01_IBM_Lab.sql

The IBM Lab section focuses on foundational multiple-table SQL operations.

Topics practiced:

Subqueries with multiple tables
IN operator
Combining EMPLOYEES and JOBS
Table aliases
Matching employee job IDs
Displaying employee job information
Filtering employees by job title
Date-based filtering
Key Relationship
E.JOB_ID = J.JOB_IDENT
Example
SELECT
E.EMP_ID,
E.F_NAME,
E.L_NAME,
J.JOB_TITLE
FROM
EMPLOYEES AS E,
JOBS AS J
WHERE
E.JOB_ID = J.JOB_IDENT;
🧪 02_My_Practice.sql

The My Practice section expands the IBM Lab concepts.

Practice Topics
Employee and job analysis
Employee and department analysis
Multi-table queries
Three-table queries
Salary range comparison
Employees earning maximum job salary
Employees earning above company average
Highest average salary department
Employee job history analysis
Full HR reporting
Tables Used
EMPLOYEES
JOBS
DEPARTMENTS
JOB_HISTORY
📊 Key Practice Analyses
Employee Job Report
Employee
↓
Job ID
↓
Job Title
Employee Department Report
Employee
↓
Department ID
↓
Department Name
Full HR Report
EMPLOYEES
↓
DEPARTMENTS
↓
JOBS
↓
JOB_HISTORY

The report combines:

Employee information
Department
Job title
Salary
Job start date
🏆 03_Challenge.sql

The Challenge section integrates all concepts learned in the lab.

Challenge Topics
Query 1

Complete employee report using:

EMPLOYEES
DEPARTMENTS
JOBS
Query 2

Employees earning above their department average salary.

Uses:

Multiple tables
Correlated subquery
Query 3

Department with the highest average salary.

Result:

Architect Group
Average Salary: 86666.67
Query 4

Employee salary validation against job salary range.

Uses:

BETWEEN MIN_SALARY AND MAX_SALARY

Result:

All 10 employees were within their assigned job salary range.
Query 5

Employees who:

Salary > Company Average
AND
Salary < Job Maximum Salary

Result:

Nancy Allen
Query 6

Department analytics report.

Includes:

Department ID
Department name
Employee count
Average salary

Results:

Architect Group → 3 Employees → Average Salary 86666.67
Design Team → 3 Employees → Average Salary 66666.67
Software Group → 4 Employees → Average Salary 65000.00
Query 7

Employee job history report.

Combines:

EMPLOYEES

- JOB_HISTORY
- JOBS
  Query 8

Complete HR analytics report.

Combines:

EMPLOYEES

- DEPARTMENTS
- JOBS
- JOB_HISTORY
  🧠 SQL Concepts Practiced
  Multiple Tables
  FROM
  EMPLOYEES AS E,
  JOBS AS J
  WHERE
  E.JOB_ID = J.JOB_IDENT;
  Table Aliases
  EMPLOYEES AS E
  JOBS AS J
  DEPARTMENTS AS D
  JOB_HISTORY AS H
  Subqueries
  WHERE SALARY > (
  SELECT AVG(SALARY)
  FROM EMPLOYEES
  )
  Correlated Subqueries
  WHERE E1.SALARY > (
  SELECT AVG(E2.SALARY)
  FROM EMPLOYEES AS E2
  WHERE E2.DEP_ID = E1.DEP_ID
  )
  Aggregation
  COUNT()
  AVG()
  MAX()
  GROUP BY
  GROUP BY
  DEP_ID
  HAVING
  HAVING
  AVG(SALARY) > 70000
  Salary Range Analysis
  E.SALARY BETWEEN
  J.MIN_SALARY
  AND J.MAX_SALARY
  ORDER BY
  ORDER BY
  E.SALARY DESC
  🐛 Debugging Notes

The following issues were identified and resolved during the lab.

Duplicate Primary Key

Error:

UNIQUE constraint failed:
DEPARTMENTS.DEPT_ID_DEP

Cause:

Duplicate Department ID in Departments.csv

Fix:

Removed the duplicate department record.
Python Path Error

Error:

AttributeError:
'str' object has no attribute 'name'

Cause:

SQL_FILE was defined as a string.

Fix:

from pathlib import Path

SQL_FILE = Path("01_IBM_Lab.sql")
Important Debugging Lesson

Always verify:

Database file
↓
Tables
↓
Columns
↓
Primary keys
↓
CSV data
↓
Row counts
↓
Relationships
↓
SQL execution
🎯 Learning Outcomes

After completing this lab, I can:

Work with multiple related tables
Understand relational database relationships
Match columns between tables
Use table aliases
Write multi-table SQL queries
Combine subqueries with multiple tables
Write correlated subqueries
Perform employee salary analysis
Analyze department-level data
Validate salaries against job ranges
Combine employee and job history data
Create complete HR reports
Debug database setup and CSV import issues
🏁 Final Lab Status
Database Setup → COMPLETED
Database Verification → COMPLETED

01_IBM_Lab.sql → COMPLETED
02_My_Practice.sql → COMPLETED
03_Challenge.sql → COMPLETED

04_Debug_Notes.md → COMPLETED
README.md → COMPLETED
🏆 FINAL STATUS
LAB 04 — COMPLETED AND VERIFIED ✅

Module 03 — Intermediate SQL
Lab 04 — Working with Multiple Tables
