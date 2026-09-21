# Lab 01 — Simple SELECT Queries

## 📌 Course Information

**Course:** IBM Data Analyst Professional Certificate  
**Course 06:** Databases and SQL for Data Science with Python  
**Module:** Module 01 — Getting Started with SQL  
**Lab:** Lab 01 — Simple SELECT Queries

---

## 🎯 Lab Objective

The objective of this lab was to practice fundamental SQL querying using the `SELECT` statement.

The lab focused on:

- Retrieving all columns from a table
- Selecting specific columns
- Filtering records using the `WHERE` clause
- Using comparison operators
- Using the `<>` (not equal) operator

---

## 🛠️ Technologies Used

- SQL
- SQLite
- Python
- VS Code

---

## 📂 Dataset

The lab uses the **Film Locations in San Francisco** dataset.

The dataset was imported into a local SQLite database.

## Database

```text
data/FilmLocations.db
``
Table
FilmLocations
Records
2214 rows
Table Columns
Title
ReleaseYear
Locations
FunFacts
ProductionCompany
Distributor
Director
Writer
Actor1
Actor2
Actor3
📁 Lab Structure
Lab_01_Simple_SELECT/
│
├── data/
│   ├── FilmLocations.db
│   └── Film_Locations_in_San_Francisco.csv
│
├── 01_IBM_Lab.sql
├── 02_My_Practice.sql
├── 03_Challenge.sql
├── 04_Debug_Notes.md
│
├── setup_database.py
├── verify_database.py
├── run_sql.py
│
└── README.md
🧪 IBM Lab Practice

The IBM lab exercises included the following SQL concepts.

1. Retrieve All Columns
SELECT *
FROM FilmLocations;
2. Retrieve Specific Columns
SELECT
    Title,
    Director,
    Writer
FROM FilmLocations;
3. Filter Records Using WHERE
SELECT
    Title,
    ReleaseYear,
    Locations
FROM FilmLocations
WHERE ReleaseYear >= 2001;
4. Retrieve Fun Facts and Locations
SELECT
    FunFacts,
    Locations
FROM FilmLocations;
5. Films Released in 2000 and Earlier
SELECT
    Title,
    Locations,
    ReleaseYear
FROM FilmLocations
WHERE ReleaseYear <= 2000;
6. Films Not Written by James Cameron
SELECT
    Title,
    ProductionCompany,
    Locations,
    ReleaseYear
FROM FilmLocations
WHERE Writer <> 'James Cameron';
💻 My Practice

Additional practice queries were created to reinforce:

Selecting all records
Selecting specific columns
Filtering records by release year
Using comparison operators
Using the <> operator

File:

02_My_Practice.sql
🔥 SQL Challenge

A separate challenge file was created to test understanding of the concepts.

The challenges included:

Challenge 1

Retrieve films released from 2020 onwards.

Challenge 2

Retrieve films produced by Netflix.

Challenge 3

Retrieve films released after 2010 that were not directed by Steven Spielberg.

File:

03_Challenge.sql
🐞 Debugging Experience

During this lab, several practical issues were identified and resolved.

Issues Encountered
Relative database path problems
SQLite database file verification
Multiple SQL statements passed to cursor.execute()
SQL statement termination errors

Detailed explanations and solutions are available in:

04_Debug_Notes.md
🧠 Key Learning Outcomes

After completing this lab, I can:

Write basic SELECT queries
Retrieve all columns using SELECT *
Select specific columns
Filter records using WHERE
Use comparison operators such as:
>=
<=
>
<
Use the SQL not-equal operator:
<>
Execute SQL queries against a local SQLite database
Debug common SQLite and SQL execution errors
Work with SQL files using Python
🔄 Practical Workflow
CSV Dataset
      ↓
Inspect Dataset
      ↓
Create SQLite Database
      ↓
Create FilmLocations Table
      ↓
Import Data
      ↓
Verify Database
      ↓
Write SQL Queries
      ↓
Execute SQL
      ↓
Debug Errors
      ↓
Practice
      ↓
Challenge
🚀 Status
Lab 01 — Simple SELECT Queries

Environment Setup      ✅
Database Creation      ✅
Data Import            ✅
Database Verification  ✅
IBM Lab                ✅
My Practice            ✅
Challenge              ✅
Debug Notes            ✅
README                 ✅

STATUS: COMPLETED 🎉
👨‍💻 Author

Charly Varghese

IBM Data Analyst Professional Certificate
Course 06 — Databases and SQL for Data Science with Python
```
