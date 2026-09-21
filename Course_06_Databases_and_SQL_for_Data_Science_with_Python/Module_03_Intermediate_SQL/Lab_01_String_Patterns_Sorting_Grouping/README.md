# Lab 01 — String Patterns, Sorting and Grouping

## IBM Data Analyst Professional Certificate

### Course 06: Databases and SQL for Data Science with Python

### Module 03: Intermediate SQL

---

## 📌 Lab Overview

This lab focuses on intermediate SQL techniques used to filter, sort, summarize, and analyze relational database data.

The practical work was completed using a local SQLite HR database and a professional VS Code-based project structure.

The lab covered:

- String pattern matching using `LIKE`
- Range filtering using `BETWEEN`
- Combining conditions using `AND`
- Sorting results using `ORDER BY`
- Multi-column sorting
- Aggregate functions
- Grouping data using `GROUP BY`
- Filtering grouped data using `HAVING`
- Column aliases
- Limiting query results using `LIMIT`

---

## 🛠 Practice Environment

- **Code Editor:** Visual Studio Code
- **Programming Language:** Python
- **Database Engine:** SQLite
- **Python Database Library:** `sqlite3`
- **Database:** `HR.db`
- **SQL Files:** `.sql`
- **Data Source:** CSV files
- **Execution Method:** Reusable Python SQL Runner

---

## 📁 Project Structure

```text
Lab_01_String_Patterns_Sorting_Grouping/
│
├── data/
│   ├── Departments.csv
│   ├── Employees.csv
│   ├── Jobs.csv
│   ├── JobHistory.csv
│   └── Locations.csv
│
├── database/
│   └── HR.db
│
├── sql/
│   └── Script_Create_Tables.sql
│
├── 01_IBM_Lab.sql
├── 01_setup_database.py
├── 02_My_Practice.sql
├── 03_Challenge.sql
├── 04_Debug_Notes.md
├── README.md
└── run_sql.py
🗄 Database Setup

The HR database was created locally using:

HR.db

The database contains the following tables:

EMPLOYEES
JOB_HISTORY
JOBS
DEPARTMENTS
LOCATIONS
Database Verification
Table Rows Loaded
EMPLOYEES 10
JOB_HISTORY 10
JOBS 10
DEPARTMENTS 3
LOCATIONS 3

All CSV data was successfully loaded and verified.

📚 SQL Concepts Practiced
1. String Pattern Matching

The LIKE operator was used to search for text patterns.

Example
SELECT
    F_NAME,
    L_NAME
FROM
    EMPLOYEES
WHERE
    F_NAME LIKE 'S%';
Pattern Symbols
'S%'   → Starts with S
'%a%'  → Contains a
'%IL'  → Ends with IL
2. Range Filtering

The BETWEEN operator was used to filter values within an inclusive range.

Example
SELECT
    F_NAME,
    L_NAME,
    SALARY
FROM
    EMPLOYEES
WHERE
    SALARY BETWEEN 60000 AND 80000;

BETWEEN includes both boundary values.

60000 ≤ SALARY ≤ 80000
3. Combining Conditions

Multiple conditions were combined using AND.

Example
SELECT
    F_NAME,
    L_NAME,
    SALARY,
    DEP_ID
FROM
    EMPLOYEES
WHERE
    DEP_ID = 5
    AND SALARY >= 60000;

Both conditions must be true.

4. Sorting Data

Results were sorted using ORDER BY.

Ascending Order
ORDER BY DEP_ID ASC;
Descending Order
ORDER BY SALARY DESC;
5. Multi-Column Sorting

Multiple columns can be used to control sorting.

Example
ORDER BY
    DEP_ID ASC,
    SALARY DESC;

SQL first sorts by DEP_ID.

Then, within each department, it sorts by salary.

6. Aggregate Functions

Aggregate functions summarize multiple rows into a calculated result.

Functions Practiced
Function Purpose
COUNT() Counts rows
SUM() Calculates total
AVG() Calculates average
MIN() Finds minimum value
MAX() Finds maximum value
Example
SELECT
    COUNT(*) AS TOTAL_EMPLOYEES,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES;
7. GROUP BY

GROUP BY divides data into groups before performing aggregate calculations.

Example
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID;
Conceptual Flow
EMPLOYEES
    ↓
GROUP BY DEP_ID
    ↓
Department Groups
    ↓
COUNT + AVG
    ↓
Department Summary
8. HAVING

HAVING filters grouped results.

Example
SELECT
    DEP_ID,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    AVG(SALARY) > 65000;
🧠 WHERE vs HAVING
WHERE
    ↓
Filters individual rows
    ↓
GROUP BY
    ↓
Creates groups
    ↓
HAVING
    ↓
Filters grouped results
Key Rule
Clause Filters
WHERE Individual rows
HAVING Groups
9. Column Aliases

Aliases provide meaningful names for calculated columns.

Example
COUNT(*) AS NUM_EMPLOYEES
AVG(SALARY) AS AVG_SALARY

Aliases improve the readability of query results.

10. LIMIT

LIMIT restricts the number of rows returned.

Example
SELECT
    DEP_ID,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
ORDER BY
    AVG_SALARY DESC
LIMIT 1;

This query returns the department with the highest average salary.

🧪 IBM Lab Implementation

The IBM lab implementation was completed in:

01_IBM_Lab.sql
Queries Completed
Query Concept
1 LIKE — Address pattern
2 LIKE — Birth year pattern
3 BETWEEN + AND
4 ORDER BY ASC
5 Multi-column sorting
6 GROUP BY + COUNT()
7 GROUP BY + COUNT() + AVG()
8 Column aliases
9 GROUP BY + ORDER BY
10 HAVING
11 IBM Practice — String pattern
12 IBM Practice — Date sorting
13 IBM Practice — HAVING AVG()
14 IBM Practice — HAVING + ORDER BY DESC
Status
IBM Queries Completed: 14 / 14
Execution Errors: 0
Status: SUCCESS
🧠 My Practice

Additional practice was completed in:

02_My_Practice.sql
Practice Coverage
String pattern matching
Salary range filtering
Combined conditions
Salary sorting
Multi-column sorting
Employee counting
Minimum and maximum salary
Total salary calculation
Average salary calculation
Department-level aggregation
HAVING with averages
HAVING with counts
HAVING with salary totals
Status
Practice Queries Completed: 14 / 14
Execution Errors: 0
Status: SUCCESS
🔥 Challenge Section

Advanced practice was completed in:

03_Challenge.sql
Challenge Coverage
First-name pattern filtering
Date range filtering
Salary range analysis
Multi-column sorting
Department salary summary
Filtering departments using average salary
Filtering departments using total salary
Identifying the department with the highest average salary
Status
Challenge Queries Completed: 8 / 8
Execution Errors: 0
Status: SUCCESS
🧮 Execution Summary
IBM Lab Queries       : 14
My Practice Queries   : 14
Challenge Queries     : 8
--------------------------------
Total Queries         : 36
SQL Execution Errors  : 0
Database Engine       : SQLite
Database              : HR.db
Final Status          : SUCCESS
🐍 Reusable SQL Runner

A reusable Python SQL runner was used to execute SQL files.

Execution Command
python run_sql.py <SQL_FILE_NAME>
Examples
python run_sql.py 01_IBM_Lab.sql
python run_sql.py 02_My_Practice.sql
python run_sql.py 03_Challenge.sql

The runner:

Reads the SQL file.
Separates SQL statements.
Executes each statement individually.
Retrieves query results.
Displays results in the terminal.
Stops execution if an SQL error occurs.
🐛 Debugging Highlights
Multiple SQL Statements

SQLite's cursor.execute() executes one statement at a time.

Solution:

Read SQL File
    ↓
Split Statements
    ↓
Execute Individually
SQL Dialect Awareness

VS Code displayed an MSSQL syntax warning for:

LIMIT 1;

However, the project uses SQLite.

The query executed successfully through Python's sqlite3 module.

Important Lesson
IDE SQL Dialect
        ≠
Actual Database Engine

Always verify SQL syntax using the actual database engine.

Equal Sorting Values

Two departments had equal total salaries.

DEP_ID 2 → 260000
DEP_ID 5 → 260000

When sorting equal values, a secondary sorting column can provide deterministic ordering.

ORDER BY
    TOTAL_SALARY DESC,
    DEP_ID ASC;
🎯 Key Learning Outcomes

After completing this lab, I can:

Use LIKE to search for string patterns.
Use % as a wildcard in SQL pattern matching.
Filter ranges using BETWEEN.
Combine conditions using AND.
Sort data using ORDER BY.
Sort using multiple columns.
Use aggregate functions.
Calculate COUNT, SUM, AVG, MIN, and MAX.
Group data using GROUP BY.
Filter grouped results using HAVING.
Understand the difference between WHERE and HAVING.
Create meaningful column aliases.
Use LIMIT in SQLite queries.
Execute multiple SQL statements using a reusable Python runner.
Understand SQL dialect differences between SQLite and SQL Server.
🏆 Lab Completion Status
Lab Name:
String Patterns, Sorting and Grouping

IBM Lab Implementation:
COMPLETED AND VERIFIED

My Practice:
COMPLETED AND VERIFIED

Challenge:
COMPLETED AND VERIFIED

Debug Notes:
COMPLETED

Total Queries Executed:
36

SQL Errors:
0

Database:
HR.db

Database Engine:
SQLite

Final Lab Status:
COMPLETED AND VERIFIED ✅
🚀 Next Lab

Lab 02 — Built-in Functions

The next lab will focus on SQL built-in functions and their use in data analysis.

IBM Data Analyst Professional Certificate — Course 06
Module 03 — Intermediate SQL
Lab 01 — Completed Successfully 🎉
```
