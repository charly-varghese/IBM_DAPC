# IBM DAPC — Course 06

## Databases and SQL for Data Science with Python

## Module 05 — Course Assignment

## Lab 01 — Working with a Real-World Data Set

---

## 📌 Lab Overview

This lab focuses on working with a real-world dataset using:

- Python
- Pandas
- SQLite
- SQL
- Data Cleaning
- Aggregation
- JOINs
- Subqueries
- Database Validation

The primary dataset contains Chicago Public Schools — Progress Report Cards (2011–2012).

A second Chicago socioeconomic dataset is used to connect school-level information with community-level socioeconomic indicators.

---

## 1. Learning Objectives

By completing this lab, the following practical skills were developed:

1. Load real-world CSV datasets using Pandas.
2. Inspect dataset structure and columns.
3. Store datasets in a SQLite database.
4. Create and query database tables.
5. Work with SQL columns containing spaces and special characters.
6. Use SQL aggregate functions.
7. Sort and limit query results.
8. Clean percentage-formatted values.
9. Clean comma-formatted numeric values.
10. Perform GROUP BY analysis.
11. Perform JOIN operations.
12. Use SQL subqueries.
13. Validate database tables and row counts.
14. Execute the complete workflow from CSV → Database → SQL Analysis.

---

## 2. Technologies Used

| Technology | Purpose |
| ---------- | ------- |

| Python | Main programming language |
| Pandas | Dataset loading and analysis |
| SQLite | Relational database |
| SQL | Data querying and analysis |
| VS Code | Development environment |
| `.venv` | Python virtual environment |
| Git/GitHub | Version control and project portfolio |

---

## 3. Project Structure

```text
Lab_01_Working_with_a_Real_World_Data_Set/
│
└── 02_My_Practice/
    │
    ├── 02_My_Practice.py
    ├── Chicago_Census_Data.csv
    ├── Chicago_Public_Schools_-_Progress_Report_Cards_(2011-2012)_20260914.csv
    ├── RealWorldData.db
    ├── 04_Debug_Notes.md
    └── README.md
4. Datasets
4.1 Chicago Public Schools Dataset

Dataset:

Chicago Public Schools — Progress Report Cards (2011–2012)

Loaded records:

Rows    : 566
Columns : 79

Stored in SQLite as:

SCHOOLS
4.2 Chicago Socioeconomic Dataset

Dataset:

Chicago Census / Socioeconomic Data

Loaded records:

Rows    : 78
Columns : 9

Stored in SQLite as:

CHICAGO_SOCIOECONOMIC_DATA

Important fields include:

COMMUNITY_AREA_NUMBER
COMMUNITY_AREA_NAME
PER_CAPITA_INCOME
HARDSHIP_INDEX

Note:

The imported dataset contains a trailing space in the actual
PER_CAPITA_INCOME column name. This was documented in
04_Debug_Notes.md.

5. Database Design

The SQLite database contains two tables:

┌──────────────────────────────┐
│           SCHOOLS             │
│                              │
│ School Information           │
│ Safety Score                 │
│ Attendance                   │
│ College Enrollment           │
│ Community Area Number        │
└──────────────┬───────────────┘
               │
               │ Community Area Number
               │
┌──────────────▼───────────────┐
│ CHICAGO_SOCIOECONOMIC_DATA   │
│                              │
│ Community Area               │
│ Income                       │
│ Poverty                      │
│ Unemployment                 │
│ Hardship Index               │
└──────────────────────────────┘

This relationship allows school-level data to be combined with
community-level socioeconomic data.

6. Implementation Workflow

The complete implementation follows:

CSV Files
    ↓
Pandas
    ↓
Dataset Inspection
    ↓
SQLite Database
    ↓
Create Tables
    ↓
SQL Queries
    ↓
Data Cleaning
    ↓
Aggregation
    ↓
JOIN
    ↓
Subquery
    ↓
Validation
7. Lab Execution

The entire lab was implemented as a single-shot Python workflow:

02_My_Practice.py

The script:

Loads the CPS dataset.
Loads the socioeconomic dataset.
Connects to SQLite.
Creates the SCHOOLS table.
Creates the CHICAGO_SOCIOECONOMIC_DATA table.
Validates available tables.
Validates row counts.
Executes Problems 1–12.
Performs final validation.
Closes the database connection.
8. SQL Concepts Practiced
8.1 COUNT()

Used to determine the number of elementary schools.

SELECT COUNT(*)
FROM SCHOOLS
WHERE "Elementary, Middle, or High School" = 'ES';
8.2 MAX()

Used to determine the highest Safety Score.

SELECT MAX("Safety Score")
FROM SCHOOLS;
8.3 ORDER BY

Used to rank schools by attendance and Safety Score.

ORDER BY "Safety Score" ASC;

and:

ORDER BY Attendance DESC;
8.4 LIMIT

Used to retrieve the top or bottom N records.

LIMIT 10;

and:

LIMIT 5;
8.5 REPLACE()

Used to remove formatting characters.

Percentage:

REPLACE("Average Student Attendance", '%', '')

Enrollment:

REPLACE(
    "College Enrollment (number of students) ",
    ',',
    ''
)
8.6 CAST()

Used to convert cleaned text into numeric values.

CAST(
    REPLACE("Average Student Attendance", '%', '')
    AS REAL
)
8.7 SUM() + GROUP BY

Used to calculate total college enrollment for each community area.

SELECT
    "Community Area Name",
    SUM(...)
FROM SCHOOLS
GROUP BY "Community Area Name";
8.8 JOIN

Used to connect school data with socioeconomic data.

JOIN CHICAGO_SOCIOECONOMIC_DATA AS CD
    ON CD.COMMUNITY_AREA_NUMBER =
       CPS."Community Area Number"
8.9 Subquery

Used to identify the community area associated with the school having
the highest college enrollment.

SELECT "Community Area Number"
FROM SCHOOLS
ORDER BY ...
DESC
LIMIT 1;

The result is then used to retrieve the corresponding hardship index.

9. Key Results
Problem 1

Number of Elementary Schools:

462
Problem 2

Highest Safety Score:

99.0
Problem 3

Schools with the highest Safety Score:

19 schools
Problem 4

Top school by Average Student Attendance:

John Charles Haines Elementary School
98.4%
Problem 5

Five schools with the lowest attendance:

Richard T Crane Technical Preparatory High School    57.9%
Barbara Vick Early Childhood & Family Center         60.9%
Dyett High School                                    62.5%
Wendell Phillips Academy High School                 63.0%
Orr Academy High School                               66.3%
Problem 6

The % sign was successfully removed from attendance values.

Example:

57.9% → 57.9
Problem 7

Schools with attendance below 70%:

8 schools
Problem 8

College enrollment was successfully aggregated by community area.

Problem 9

Five community areas with the lowest total college enrollment:

OAKLAND        140
FULLER PARK    531
BURNSIDE       549
OHARE          786
LOOP           871
Problem 10

Five schools with the lowest Safety Score:

Edmond Burke Elementary School              1.0
Luke O'Toole Elementary School              5.0
George W Tilton Elementary School           6.0
Foster Park Elementary School              11.0
Emil G Hirsch Metropolitan High School     13.0
Problem 11

Community area associated with college enrollment of 4368:

North Center
Hardship Index: 6.0
Problem 12

Community area associated with the school having the highest college enrollment:

Community Area Number : 5
Community Area Name   : North Center
Hardship Index        : 6.0
10. Validation

Final database validation:

SCHOOLS rows                    : 566
CHICAGO_SOCIOECONOMIC_DATA rows : 78

Validation result:

[✓] Dataset row-count validation PASSED

Final execution:

LAB 01 SINGLE-SHOT EXECUTION FINISHED
11. Debugging Summary

Important debugging topics encountered:

Database Path

Resolved multiple database-location issues by using:

BASE_DIR = Path(__file__).resolve().parent
Missing Table

Resolved missing SCHOOLS table by explicitly loading the CPS
dataset into SQLite.

Second Dataset Dependency

Loaded the Chicago socioeconomic dataset required for Problems 11
and 12.

Column Names

Identified spaces and trailing spaces in real-world CSV column names.

Percentage Values

Converted:

57.9%

into:

57.9

using REPLACE() and CAST().

Comma-Formatted Numbers

Converted:

14,793

into:

14793

before numeric aggregation.

12. IGLS Learning Model
EXPLAIN

Understand how real-world datasets are loaded, stored, cleaned and
queried using Python, Pandas, SQLite and SQL.

SHOW

Build the database and demonstrate SQL operations including:

COUNT
MAX
SUM
GROUP BY
ORDER BY
LIMIT
REPLACE
CAST
JOIN
Subquery
DO

Execute the complete workflow in VS Code using:

02_My_Practice.py
FIX

Resolve real-world issues involving:

File paths
Missing tables
Multiple databases
Spaces in column names
Trailing spaces
Percentage strings
Comma-formatted numbers
MASTER

Complete an end-to-end real-world data workflow:

CSV
 ↓
Pandas
 ↓
SQLite
 ↓
SQL
 ↓
Data Cleaning
 ↓
Aggregation
 ↓
JOIN
 ↓
Subquery
 ↓
Validation
13. Skills Demonstrated

This lab demonstrates practical competency in:

Python data loading
Pandas DataFrame handling
CSV processing
SQLite database creation
SQL table creation
SQL querying
Aggregate functions
Data cleaning
String manipulation
Numeric conversion
GROUP BY analysis
JOIN operations
Subqueries
Database validation
Debugging
Reproducible VS Code workflows
14. Data Analytics / Data Engineering Connection

This lab represents a simplified version of a real data pipeline:

SOURCE DATA
    ↓
CSV / External Dataset
    ↓
INGESTION
    ↓
Pandas
    ↓
STORAGE
    ↓
SQLite
    ↓
TRANSFORMATION
    ↓
SQL
    ↓
ANALYSIS
    ↓
Business Insights

The same fundamental concepts scale to:

SQLite
   ↓
PostgreSQL
   ↓
SQL Server
   ↓
Azure SQL
   ↓
Cloud Data Warehouse
   ↓
Data Engineering Pipelines
   ↓
Analytics / BI / AI
15. Lab Deliverables
File Purpose Status
02_My_Practice.py Complete single-shot implementation ✅
Chicago_Census_Data.csv Socioeconomic dataset ✅
Chicago_Public_Schools_-_Progress_Report_Cards_(2011-2012)_20260914.csv CPS dataset ✅
RealWorldData.db SQLite database ✅
04_Debug_Notes.md Debugging documentation ✅
README.md Lab documentation ✅
16. Final Status
============================================================
LAB 01 — WORKING WITH A REAL-WORLD DATA SET
============================================================

Datasets Loaded                 : PASS
SQLite Database                 : PASS
SCHOOLS Table                   : PASS
Socioeconomic Table             : PASS

SQL Problems 01–12              : PASS
JOIN Analysis                   : PASS
Subquery Analysis               : PASS
Database Validation             : PASS

STATUS: COMPLETED
============================================================
```
