# Lab 02 — COUNT, DISTINCT, LIMIT

## Course Information

\*_IBM Data Analyst Professional Certificate_

**Course 06:** Databases and SQL for Data Science with Python

**Module:** Module 01 — Getting Started with SQL

**Lab:** COUNT, DISTINCT, LIMIT

---

## Lab Objective

This lab focused on using SQL queries to:

- Count records using `COUNT()`
- Retrieve unique values using `DISTINCT`
- Limit the number of returned rows using `LIMIT`
- Skip rows using `OFFSET`

The lab was completed using:

```text
VS Code
+
Python
+
SQLite
+
FilmLocations Database

```

Dataset
Database
FilmLocations.db
Table
FilmLocations
Total Records
2214
Main Columns Used
Title
ReleaseYear
Locations
ProductionCompany
Distributor
Director
Writer
Actor1
SQL Concepts Practiced

1. COUNT()

Used to count rows and values.

Example:

SELECT COUNT(\*)
FROM FilmLocations;

Result:

2214

Other examples included counting records using WHERE conditions.

2.DISTINCT

Used to retrieve unique values from a column or combination of columns.

Example:

SELECT DISTINCT Title
FROM FilmLocations;

Also practiced:

DISTINCT Title + ReleaseYear
DISTINCT Director + Title
COUNT(DISTINCT Distributor) 3. LIMIT

Used to control the number of rows returned.

Example:

SELECT \*
FROM FilmLocations
LIMIT 25; 4. OFFSET

Used together with LIMIT to skip rows before retrieving results.

Example:

SELECT \*
FROM FilmLocations
LIMIT 15 OFFSET 10;

Logic:

Skip first 10 rows
↓
Retrieve next 15 rows
IBM Lab Examples

The following concepts were executed successfully:

COUNT(\*) ✅
COUNT(Locations) ✅
DISTINCT Title ✅
COUNT(DISTINCT ReleaseYear) ✅
LIMIT ✅
LIMIT + OFFSET ✅
My Practice

The following IBM practice exercises were completed:

COUNT Practice
├── Count locations directed by Woody Allen ✅
├── Count films shot at Russian Hill ✅
└── Count films released before 1950 ✅

DISTINCT Practice
├── Unique films released from 2001 onwards ✅
├── Directors and films shot at City Hall ✅
└── Count distinct distributors for Clint Eastwood ✅

LIMIT Practice
├── Retrieve first 50 film names ✅
├── Retrieve first 10 films released in 2015 ✅
└── Retrieve next 3 films after first 5 in 2015 ✅
Challenge Queries

Three additional challenge queries were completed.

Challenge 1 — COUNT

Count film records directed by Woody Allen.

Result:

31
Challenge 2 — DISTINCT

Retrieve unique production companies for films released in 2015.

Result:

Multiple unique production companies returned successfully.
Challenge 3 — LIMIT + OFFSET

Retrieve five film titles after skipping the first ten rows.

Result:

Sense8
The Wedding Planner
Quitters
Outerlands
Time After Time
Execution Method

SQL queries were stored in separate .sql files.

The execution workflow was:

SQL File
↓
run_sql.py
↓
Read SQL Statements
↓
Split Multiple Statements
↓
Execute Using SQLite
↓
Print Results
Project Structure
Lab_02_COUNT_DISTINCT_LIMIT/
│
├── data/
│ └── FilmLocations.db
│
├── 01_IBM_Lab.sql
├── 02_My_Practice.sql
├── 03_Challenge.sql
│
├── 04_Debug_Notes.md
├── README.md
│
└── run_sql.py
Debugging Lessons
SQL Dialect Mismatch

VS Code showed syntax warnings because the SQL files were validated as:

MSSQL

However, the lab database used:

SQLite

SQLite supports:

LIMIT 25;

LIMIT 15 OFFSET 10;

The queries executed successfully using Python's SQLite engine.

Zero Results Are Not Always Errors

An SQL query can execute successfully and return:

0

This may indicate that no records match the specified condition.

Always verify:

Query Syntax

- Column Name
- Actual Dataset Values
  Key Learning Outcomes

After completing this lab, I can:

Use COUNT() to count records
Use COUNT(column) to count non-null values
Use DISTINCT to retrieve unique values
Use COUNT(DISTINCT column) for unique counts
Use LIMIT to restrict result size
Use OFFSET to skip rows
Execute multiple SQL statements from one file
Debug SQL dialect warnings
Verify query results using SQLite
Lab Status
Environment Setup ✅
Database Connection ✅
IBM Lab Queries ✅
My Practice ✅
Challenge Queries ✅
Debug Notes ✅
README 🔄
Final Status
LAB 02 — COUNT, DISTINCT, LIMIT

STATUS: READY FOR FINAL COMPLETION 🏆
