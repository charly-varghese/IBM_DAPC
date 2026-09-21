# IBM DAPC — Course 06

## Databases and SQL for Data Science with Python

## Module 05 — Course Assignment

## Lab 02 — Database Querying Using SQLite

---

## 📌 Lab Overview

This lab focuses on querying multiple real-world Chicago datasets
stored in a SQLite database.

The lab uses three datasets:

1. Socioeconomic Indicators in Chicago
2. Chicago Public Schools
3. Chicago Crime Data

The datasets are loaded into SQLite tables and queried using SQL to
solve ten assignment problems.

---

## 1. Learning Objectives

By completing this lab, the following skills were practiced:

1. Load CSV datasets using Pandas.
2. Create and connect to a SQLite database.
3. Store multiple datasets as database tables.
4. Query real-world data using SQL.
5. Filter records using `WHERE`.
6. Search text using `LIKE`.
7. Retrieve unique values using `DISTINCT`.
8. Use aggregate functions such as `COUNT()`, `AVG()` and `MAX()`.
9. Group records using `GROUP BY`.
10. Sort results using `ORDER BY`.
11. Restrict results using `LIMIT`.
12. Use SQL subqueries.
13. Combine database analysis with Python and Pandas.
14. Validate database tables and row counts.

---

## 2. Technologies Used

| Technology | Purpose |
| ---------- | ------- |

| Python | Main programming language |
| Pandas | CSV loading and result handling |
| SQLite | Relational database |
| SQL | Database querying and analysis |
| VS Code | Development environment |
| `.venv` | Python virtual environment |
| Git/GitHub | Version control and portfolio |

---

## 3. Project Structure

```text
Lab_02_Database_Querying_using_SQLite/
│
└── 02_My_Practice/
    │
    ├── 02_My_Practice.py
    │
    ├── CENSUS_DATA.csv
    ├── CHICAGO_PUBLIC_SCHOOLS.csv
    ├── CHICAGO_CRIME_DATA.csv
    │
    ├── FinalDB.db
    ├── 04_Debug_Notes.md
    └── README.md
4. Datasets
4.1 Chicago Public Schools

File:

CHICAGO_PUBLIC_SCHOOLS.csv

Dataset size:

Rows    : 566
Columns : 79

SQLite table:

CHICAGO_PUBLIC_SCHOOLS
4.2 Socioeconomic Indicators in Chicago

File:

CENSUS_DATA.csv

Dataset size:

Rows    : 78
Columns : 9

SQLite table:

CENSUS_DATA
4.3 Chicago Crime Data

File:

CHICAGO_CRIME_DATA.csv

Dataset size:

Rows    : 533
Columns : 21

SQLite table:

CHICAGO_CRIME_DATA
5. Database Structure

The SQLite database contains three tables:

┌──────────────────────────────┐
│         CENSUS_DATA          │
│                              │
│ Community Area               │
│ Income                       │
│ Poverty                      │
│ Hardship Index               │
└──────────────┬───────────────┘
               │
               │ Community Area
               │
┌──────────────▼───────────────┐
│    CHICAGO_PUBLIC_SCHOOLS    │
│                              │
│ School Information           │
│ Safety Score                 │
│ Attendance                   │
│ School Type                  │
└──────────────────────────────┘


┌──────────────────────────────┐
│     CHICAGO_CRIME_DATA       │
│                              │
│ Case Number                  │
│ Crime Type                   │
│ Description                  │
│ Location                     │
│ Community Area               │
└──────────────────────────────┘

The common community-area information allows crime, school and
socioeconomic information to be analyzed together.

6. Implementation Workflow

The complete workflow is:

CSV Files
    ↓
Pandas
    ↓
Dataset Loading
    ↓
SQLite Database
    ↓
Three Tables
    ↓
SQL Queries
    ↓
Filtering / Aggregation
    ↓
Grouping / Ranking
    ↓
Subqueries
    ↓
Validation
7. Single-Shot Execution

The complete lab was implemented using:

02_My_Practice.py

Instead of executing each assignment problem independently, the
Python program performs the complete workflow in a single execution.

The script:

Loads the three CSV datasets.
Displays dataset dimensions.
Creates/connects to FinalDB.db.
Creates the three required SQLite tables.
Verifies available tables.
Verifies row counts.
Executes Problems 1–10.
Performs final validation.
Closes the database connection.
8. SQL Concepts Practiced
8.1 COUNT()

Used to determine the total number of crimes.

SELECT COUNT(*) AS TOTAL_CRIMES
FROM CHICAGO_CRIME_DATA;

Result:

533
8.2 WHERE

Used to filter socioeconomic records:

WHERE CAST("PER CAPITA INCOME " AS REAL) < 11000
8.3 LIKE

Used for text pattern matching.

Example:

WHERE DESCRIPTION LIKE '%MINOR%'

and:

WHERE DESCRIPTION LIKE '%CHILD%'
8.4 DISTINCT

Used to return unique crime types:

SELECT DISTINCT PRIMARY_TYPE
FROM CHICAGO_CRIME_DATA;
8.5 AVG()

Used to calculate average school safety scores:

AVG("Safety Score")
8.6 MAX()

Used to identify the highest hardship index:

MAX("HARDSHIP INDEX")
8.7 GROUP BY

Used for grouped analysis:

GROUP BY "Elementary, Middle, or High School"

and:

GROUP BY COMMUNITY_AREA_NUMBER
8.8 ORDER BY

Used to rank records:

ORDER BY COUNT(*) DESC

and:

ORDER BY "PERCENT HOUSEHOLDS BELOW POVERTY" DESC
8.9 LIMIT

Used for Top-N analysis:

LIMIT 5;

and:

LIMIT 1;
8.10 Subqueries

Subqueries were used in Problems 9 and 10 to identify records based
on aggregate results.

9. Assignment Results
Problem 1 — Total Number of Crimes
533
Problem 2 — Per Capita Income Less Than 11000

The following community areas were returned:

West Garfield Park    10934
South Lawndale        10402
Fuller Park           10432
Riverdale              8201

Total:

4 community areas
Problem 3 — Crimes Involving Minors

Case numbers:

HL266884
HK238408
Problem 4 — Kidnapping Crimes Involving a Child

Case number:

HN144152
Problem 5 — Crime Types Recorded at Schools

Unique crime types:

ASSAULT
BATTERY
CRIMINAL DAMAGE
CRIMINAL TRESPASS
NARCOTICS
PUBLIC PEACE VIOLATION

Total:

6 crime types
Problem 6 — Average Safety Score by School Type
ES    49.520384
HS    49.623529
MS    48.000000
Problem 7 — Top 5 Community Areas by Poverty
Riverdale              56.5
Fuller Park            51.2
Englewood              46.6
North Lawndale         43.1
East Garfield Park     42.4
Problem 8 — Most Crime-Prone Community Area

Community Area Number:

25
Problem 9 — Highest Hardship Index

Community Area:

Riverdale
Problem 10 — Community Area with Most Crimes

Community Area:

Austin
10. Final Database Validation

The final SQLite database contains:

CENSUS_DATA
CHICAGO_CRIME_DATA
CHICAGO_PUBLIC_SCHOOLS

Row counts:

CHICAGO_PUBLIC_SCHOOLS : 566
CENSUS_DATA            : 78
CHICAGO_CRIME_DATA     : 533

Validation result:

[✓] Dataset row-count validation PASSED
11. Debugging Summary

The main execution issue was a CSV filename mismatch.

Initial filenames expected by Python
Chicago Public Schools.csv
Socioeconomic Indicators in Chicago.csv
ChicagoCrimeData.csv
Actual project filenames
CHICAGO_PUBLIC_SCHOOLS.csv
CENSUS_DATA.csv
CHICAGO_CRIME_DATA.csv

The Python paths were corrected to match the actual files.

After the correction, all datasets loaded successfully and all
assignment queries executed without errors.

Detailed debugging information is documented in:

04_Debug_Notes.md
12. IGLS Learning Model
EXPLAIN

Understand how multiple real-world datasets can be stored in a
relational database and queried using SQL.

SHOW

Demonstrate:

COUNT
WHERE
LIKE
DISTINCT
AVG
MAX
GROUP BY
ORDER BY
LIMIT
Subqueries
DO

Execute all ten IBM assignment problems using one Python program.

FIX

Resolve the CSV filename/path mismatch and validate the database
structure.

MASTER

Complete the workflow:

CSV
 ↓
Pandas
 ↓
SQLite
 ↓
3 Tables
 ↓
SQL Filtering
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
13. Skills Demonstrated

This lab demonstrates practical skills in:

Python
Pandas
CSV data ingestion
SQLite
SQL
Data filtering
Pattern matching
DISTINCT analysis
Aggregate functions
GROUP BY
ORDER BY
LIMIT
Subqueries
Relational data analysis
Database validation
Debugging
VS Code workflow
14. Data Analytics Connection

This lab demonstrates how multiple datasets can be transformed into
structured information for analytical purposes.

RAW DATA
   ↓
CSV DATASETS
   ↓
DATA INGESTION
   ↓
PANDAS
   ↓
SQL DATABASE
   ↓
DATA QUERYING
   ↓
AGGREGATION
   ↓
ANALYTICS
   ↓
INSIGHTS

Example analytical questions answered:

• How much crime was recorded?
• Which areas have low income?
• Which crimes involve minors?
• What crimes occur at schools?
• Which school types have higher safety scores?
• Which areas have higher poverty?
• Which community area has the most crime?
• Which area has the highest hardship?
15. Data Engineering Connection

The same concepts used in this lab form the foundation of larger
data engineering systems.

CSV / API
   ↓
Data Ingestion
   ↓
Data Cleaning
   ↓
Database Storage
   ↓
SQL Transformation
   ↓
Analytics
   ↓
BI / Reporting

The SQLite implementation can later scale conceptually to:

SQLite
   ↓
PostgreSQL / SQL Server
   ↓
Azure SQL
   ↓
Cloud Data Warehouse
   ↓
Data Engineering Pipelines
   ↓
BI
   ↓
AI-ready Data
16. Lab Deliverables
File Purpose Status
02_My_Practice.py Complete single-shot implementation ✅
CENSUS_DATA.csv Socioeconomic dataset ✅
CHICAGO_PUBLIC_SCHOOLS.csv School dataset ✅
CHICAGO_CRIME_DATA.csv Crime dataset ✅
FinalDB.db SQLite database ✅
04_Debug_Notes.md Debugging documentation ✅
README.md Lab documentation ✅
17. Final Execution Status
============================================================
LAB 02 — DATABASE QUERYING USING SQLITE
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

STATUS: COMPLETED
============================================================
```
