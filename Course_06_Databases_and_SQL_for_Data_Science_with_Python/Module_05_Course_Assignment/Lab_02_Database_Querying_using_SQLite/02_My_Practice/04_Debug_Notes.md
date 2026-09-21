# 04_Debug_Notes.md

## IBM DAPC — Course 06

## Databases and SQL for Data Science with Python

### Module 05 — Course Assignment

### Lab 02 — Database Querying Using SQLite

---

## 1. Debugging Objective

This file records the important errors, root causes, fixes, validation
steps, and technical lessons encountered while executing:

\*_Lab 02 — Database Querying Using SQLite_

Environment:

- Windows 11
- VS Code
- Python
- Pandas
- SQLite
- `.venv`
- IBM Data Analyst Professional Certificate
- Course 06 — Databases and SQL for Data Science with Python

---

## 2. Issue 01 — CSV Filename Mismatch

## Error

The first execution failed during dataset loading:

```text
FileNotFoundError:
No such file or directory:
'...\02_My_Practice\Chicago Public Schools.csv'
``
Root Cause

The Python script expected:

Chicago Public Schools.csv
Socioeconomic Indicators in Chicago.csv
ChicagoCrimeData.csv

However, the actual files in the Lab 02 folder were:

CHICAGO_PUBLIC_SCHOOLS.csv
CENSUS_DATA.csv
CHICAGO_CRIME_DATA.csv

The files were present, but the filenames in the Python script
did not match the actual filenames.

3.Fix — Correct Dataset Paths

The filename definitions were changed to:

SCHOOLS_CSV = BASE_DIR / "CHICAGO_PUBLIC_SCHOOLS.csv"

CENSUS_CSV = BASE_DIR / "CENSUS_DATA.csv"

CRIME_CSV = BASE_DIR / "CHICAGO_CRIME_DATA.csv"

The files were intentionally not renamed.

This keeps the local project naming aligned with the IBM assignment
dataset/table terminology.

4.Result After Fix

After correcting the filenames, all three datasets loaded successfully.

Chicago Public Schools dataset
Rows    : 566
Columns : 79
Socioeconomic Indicators dataset
Rows    : 78
Columns : 9
Chicago Crime dataset
Rows    : 533
Columns : 21
1. Issue 02 — Correct IBM Table Names

The IBM assignment requires three database tables:

CENSUS_DATA
CHICAGO_PUBLIC_SCHOOLS
CHICAGO_CRIME_DATA

The Python script therefore created exactly these tables.

schools_df.to_sql(
    "CHICAGO_PUBLIC_SCHOOLS",
    conn,
    if_exists="replace",
    index=False
)

census_df.to_sql(
    "CENSUS_DATA",
    conn,
    if_exists="replace",
    index=False
)

crime_df.to_sql(
    "CHICAGO_CRIME_DATA",
    conn,
    if_exists="replace",
    index=False
)
Result

SQLite successfully created:

CENSUS_DATA
CHICAGO_CRIME_DATA
CHICAGO_PUBLIC_SCHOOLS
6. Issue 03 — Database Path Control

The database path is controlled using:

BASE_DIR = Path(__file__).resolve().parent

DB_FILE = BASE_DIR / "FinalDB.db"

This ensures that FinalDB.db is created in the same directory as
the Python script.

Database location:

Lab_02_Database_Querying_using_SQLite
└── 02_My_Practice
    └── FinalDB.db
Lesson

Using an explicit script-relative path prevents accidental creation
of databases in unrelated working directories.

7.SQL/Data Handling — Problem 2
Requirement

List community area names and numbers with per capita income less
than 11000.

Technique

The query filters the socioeconomic dataset:

WHERE CAST("PER CAPITA INCOME " AS REAL) < 11000
Result
West Garfield Park    10934
South Lawndale        10402
Fuller Park           10432
Riverdale              8201
Lesson

Real-world numeric fields may need explicit numeric conversion before
comparison.

8.SQL/Data Handling — Problem 3
Requirement

List all case numbers for crimes involving minors.

Technique

Pattern matching was performed using:

DESCRIPTION LIKE '%MINOR%'
Result
HL266884
HK238408
Lesson

LIKE is useful when the required information is embedded within
text fields.

9.SQL/Data Handling — Problem 4
Requirement

List kidnapping crimes involving a child.

Technique

Two conditions were combined:

PRIMARY_TYPE = 'KIDNAPPING'
AND DESCRIPTION LIKE '%CHILD%'
Result
HN144152
Lesson

Multiple filtering conditions can be combined with AND.

10.SQL/Data Handling — Problem 5
Requirement

List the kinds of crimes recorded at schools with no repetitions.

Technique

Used:

SELECT DISTINCT PRIMARY_TYPE

with:

LOCATION_DESCRIPTION LIKE '%SCHOOL%'
Result
ASSAULT
BATTERY
CRIMINAL DAMAGE
CRIMINAL TRESPASS
NARCOTICS
PUBLIC PEACE VIOLATION
Lesson

DISTINCT removes duplicate values from query results.

11.SQL/Data Handling — Problem 6
Requirement

List school types along with the average safety score for each type.

Technique

Used:

AVG("Safety Score")

with:

GROUP BY "Elementary, Middle, or High School"
Result
ES    49.520384
HS    49.623529
MS    48.000000
Lesson

GROUP BY + aggregate functions are fundamental to grouped
business/data analysis.

12.SQL/Data Handling — Problem 7
Requirement

List five community areas with the highest percentage of households
below the poverty line.

Technique

Used:

ORDER BY "PERCENT HOUSEHOLDS BELOW POVERTY" DESC
LIMIT 5
Result
Riverdale              56.5
Fuller Park            51.2
Englewood              46.6
North Lawndale         43.1
East Garfield Park     42.4
Lesson

ORDER BY DESC + LIMIT is a standard Top-N analysis pattern.

13.SQL/Data Handling — Problem 8
Requirement

Determine the most crime-prone community area and display the
community area number only.

Technique

Crimes were grouped by community area:

GROUP BY COMMUNITY_AREA_NUMBER

and ranked using:

ORDER BY COUNT(*) DESC
LIMIT 1
Result
25
Lesson

Crime concentration can be identified using:

GROUP BY
    +
COUNT()
    +
ORDER BY
    +
LIMIT
1.  SQL/Data Handling — Problem 9
Requirement

Use a subquery to find the community area with the highest hardship
index.

Technique

The maximum hardship index was identified using:

SELECT MAX("HARDSHIP INDEX")
FROM CENSUS_DATA

The corresponding community area was then returned using a
subquery.

Result
Riverdale
Lesson

A subquery can be used to compare rows against an aggregate result.

15.SQL/Data Handling — Problem 10
Requirement

Use a subquery to determine the Community Area Name with the most
number of crimes.

Technique

The inner query identifies the community area number having the
highest crime count:

SELECT COMMUNITY_AREA_NUMBER
FROM CHICAGO_CRIME_DATA
GROUP BY COMMUNITY_AREA_NUMBER
ORDER BY COUNT(*) DESC
LIMIT 1

The outer query retrieves the corresponding community area name
from CENSUS_DATA.

Result
Austin
Lesson

This demonstrates a practical:

Aggregate
   ↓
GROUP BY
   ↓
ORDER BY
   ↓
LIMIT
   ↓
Subquery
   ↓
Lookup

workflow.

16.Final Validation

The final database contains the three required tables:

CENSUS_DATA
CHICAGO_CRIME_DATA
CHICAGO_PUBLIC_SCHOOLS

Row counts:

CHICAGO_PUBLIC_SCHOOLS rows : 566
CENSUS_DATA rows            : 78
CHICAGO_CRIME_DATA rows     : 533

Validation result:

[✓] Dataset row-count validation PASSED

17.Final Execution Status

============================================================
LAB 02-DATABASE QUERYING USING SQLITE

============================================================

Dataset Loading              : PASS
SQLite Database              : PASS

CENSUS_DATA                  : PASS
CHICAGO_PUBLIC_SCHOOLS       : PASS
CHICAGO_CRIME_DATA           : PASS

Problem 01                   : PASS
Problem 02                   : PASS
Problem 03                   : PASS
Problem 04                   : PASS
Problem 05                   : PASS
Problem 06                   : PASS
Problem 07                   : PASS
Problem 08                   : PASS
Problem 09                   : PASS
Problem 10                   : PASS

Final Row Validation         : PASS

STATUS:COMPLETED

============================================================
18.Debugging Lessons
Lesson 1 — File Names Must Match Exactly

Python file loading is sensitive to the actual path and filename.

Always verify:

Script expectation
        ↓
Actual file name

before debugging the Python logic.

Lesson 2 — Use Script-Relative Paths

Preferred pattern:

BASE_DIR = Path(__file__).resolve().parent

This makes the project more portable and reproducible.

Lesson 3 — Preserve IBM Naming

For assignment work, database table names should match the IBM
requirements whenever possible:

CENSUS_DATA
CHICAGO_PUBLIC_SCHOOLS
CHICAGO_CRIME_DATA
Lesson 4 — Inspect Data Before Querying

Before writing SQL against an external dataset, verify:

Number of rows
Number of columns
Column names
Data types
Missing values
Formatting issues
Lesson 5 — SQL Filtering

Important filtering techniques practiced:

WHERE
LIKE
AND
Lesson 6 — SQL Aggregation

Important aggregation techniques practiced:

COUNT()
AVG()
MAX()
GROUP BY
Lesson 7 — Ranking

Important ranking pattern:

ORDER BY ... DESC
LIMIT N
Lesson 8 — DISTINCT

Use:

SELECT DISTINCT ...

when only unique values are required.

Lesson 9 — Subqueries

Subqueries allow one SQL query to use the result of another query.

This was demonstrated in Problems 9 and 10.

19.IGLS Mastery Summary
EXPLAIN

Understand how three related Chicago datasets can be loaded into
SQLite and queried using SQL.

SHOW

Demonstrate:

Database creation
Table creation
Filtering
Pattern matching
DISTINCT
COUNT
AVG
MAX
GROUP BY
ORDER BY
LIMIT
Subqueries
DO

Execute all ten assignment problems in one single-shot Python
workflow.

FIX

Resolve:

CSV filename mismatch
Dataset path configuration
SQLite database path
Real-world data formatting
MASTER

Complete the workflow:

CSV
 ↓
Pandas
 ↓
SQLite
 ↓
3 Relational Tables
 ↓
SQL Queries
 ↓
Filtering
 ↓
Aggregation
 ↓
Grouping
 ↓
Ranking
 ↓
Subqueries
 ↓
Validation
1.  Data Analytics / Data Engineering Connection

This lab demonstrates a simplified analytics pipeline:

SOURCE DATA
    ↓
CSV Files
    ↓
DATA INGESTION
    ↓
Pandas
    ↓
DATABASE STORAGE
    ↓
SQLite
    ↓
SQL TRANSFORMATION
    ↓
ANALYTICS
    ↓
BUSINESS INSIGHTS

These concepts scale naturally to:

SQLite
   ↓
PostgreSQL / SQL Server
   ↓
Azure SQL
   ↓
Cloud Data Platforms
   ↓
Data Engineering Pipelines
   ↓
BI / Analytics
   ↓
AI-ready Data
21. Final Lab 02 Mastery Statement

Lab 02 — Database Querying Using SQLite has been successfully
completed using a VS Code-centric, single-shot execution workflow.

The lab successfully demonstrated:

Python + Pandas
       +
SQLite
       +
SQL
       +
Real-World Data
       +
Data Analysis
       +
Subqueries

with all 10 assignment problems successfully executed and
validated.
```
