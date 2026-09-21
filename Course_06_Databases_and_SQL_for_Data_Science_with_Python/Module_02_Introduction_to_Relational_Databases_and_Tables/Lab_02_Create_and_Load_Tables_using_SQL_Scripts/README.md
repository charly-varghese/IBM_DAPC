# Lab 02: Create and Load Tables using SQL Scripts

📌 Lab Overview
This lab focuses on creating a relational database structure using SQL scripts and loading data from CSV files into SQLite tables.

The lab is based on a Cardiovascular Disease (CVD) database and provides practical experience with:

Creating multiple relational tables
Executing SQL scripts
Loading CSV data into SQLite
Verifying database records
Querying multiple tables
Filtering and sorting data
Using aggregate functions
Using GROUP BY and HAVING
Performing INSERT, UPDATE, and DELETE operations
🎯 Learning Objectives

After completing this lab, I am able to:

Create database tables using SQL scripts
Understand table structures and primary keys
Execute multiple SQL statements using Python
Load CSV data into SQLite tables
Verify database tables and records
Query data using SELECT
Filter records using WHERE
Sort data using ORDER BY
Limit results using LIMIT
Use logical operators such as AND and OR
Filter values using IN
Search text using LIKE
Filter ranges using BETWEEN
Perform aggregations using COUNT, MIN, and MAX
Group records using GROUP BY
Filter grouped results using HAVING
Insert new records using INSERT
Modify records using UPDATE
Remove records using DELETE
🗂️ Project Structure
Lab_02_Create_and_Load_Tables_using_SQL_Scripts/
│
├── data/
│ ├── lab02_database.db
│ │
│ ├── PATIENTS.csv
│ ├── MEDICAL_HISTORY.csv
│ ├── MEDICAL_PROCEDURES.csv
│ ├── MEDICAL_DEPARTMENTS.csv
│ └── MEDICAL_LOCATIONS.csv
│
├── 01_IBM_Lab.sql
├── 02_My_Practice.sql
├── 03_Challenge.sql
│
├── setup_database.py
├── run_sql.py
├── load_csv_data.py
├── inspect_csv_files.py
├── verify_database.py
│
├── 04_Debug_Notes.md
└── README.md
🏥 CVD Database Structure

The database contains five main tables.

1️⃣ PATIENTS

Stores patient information.

Column Description
PATIENT_ID Unique patient identifier
FIRST_NAME Patient first name
LAST_NAME Patient last name
SSN Social Security Number
BIRTH_DATE Patient birth date
SEX Patient gender
ADDRESS Patient address
DEPT_ID Department identifier
2️⃣ MEDICAL_HISTORY

Stores patient medical history.

Column Description
MEDICAL_HISTORY_ID Unique medical history identifier
PATIENT_ID Patient identifier
DIAGNOSIS_DATE Diagnosis date
DIAGNOSIS_CODE Medical diagnosis code
MEDICAL_CONDITION Medical condition
DEPT_ID Department identifier
3️⃣ MEDICAL_PROCEDURES

Stores medical procedures performed on patients.

Column Description
PROCEDURE_ID Unique procedure identifier
PROCEDURE_NAME Name of procedure
PROCEDURE_DATE Date of procedure
PATIENT_ID Patient identifier
DEPT_ID Department identifier
4️⃣ MEDICAL_DEPARTMENTS

Stores medical department information.

Column Description
DEPT_ID Unique department identifier
DEPT_NAME Department name
MANAGER_ID Department manager identifier
LOCATION_ID Location identifier
5️⃣ MEDICAL_LOCATIONS

Stores hospital and medical location information.

Column_Description
LOCATION_ID_Location identifier
DEPT_ID_Department identifier
LOCATION_NAME_Name of location
📊 CSV Data Files

The following CSV files were used to load data into the database:

PATIENTS.csv
MEDICAL_HISTORY.csv
MEDICAL_PROCEDURES.csv
MEDICAL_DEPARTMENTS.csv
MEDICAL_LOCATIONS.csv
Data Loaded
Table_Rows Loaded
PATIENTS_5
MEDICAL_HISTORY_6
MEDICAL_PROCEDURES_7
MEDICAL_DEPARTMENTS_4
MEDICAL_LOCATIONS_2
🔄 Lab Execution Workflow

The complete workflow followed during this lab was:

CSV Files
│
▼
Inspect CSV Structure
│
▼
Create SQLite Database
│
▼
Execute SQL Table Creation Script
│
▼
Load CSV Data
│
▼
Verify Database
│
▼
Run SQL Practice Queries
│
▼
Run SQL Challenge Queries
│
▼
Debug and Document
🚀 How to Run the Lab

Open the terminal inside the lab folder:

Lab_02_Create_and_Load_Tables_using_SQL_Scripts
Step 1: Create the Database

Run:

python setup_database.py

Expected result:

SQLite database created successfully.
Step 2: Inspect CSV Files

Run:

python inspect_csv_files.py

This verifies:

Number of rows
Number of columns
First record
Second record
Step 3: Create Database Tables

Run the IBM SQL table creation script:

python run_sql.py 01_IBM_Lab.sql

This creates the following tables:

PATIENTS
MEDICAL_HISTORY
MEDICAL_PROCEDURES
MEDICAL_DEPARTMENTS
MEDICAL_LOCATIONS
Step 4: Load CSV Data

Run:

python load_csv_data.py

This loads data from the CSV files into the SQLite database.

Expected result:

PATIENTS: 5 rows
MEDICAL_HISTORY: 6 rows
MEDICAL_PROCEDURES: 7 rows
MEDICAL_DEPARTMENTS: 4 rows
MEDICAL_LOCATIONS: 2 rows
Step 5: Verify the Database

Run:

python verify_database.py

This verifies:

Database tables
Total row counts
Records loaded into each table
💻 IBM Lab SQL

File:

01_IBM_Lab.sql

This SQL script performs the following tasks:

DROP TABLE IF EXISTS PATIENTS;

DROP TABLE IF EXISTS MEDICAL_HISTORY;

DROP TABLE IF EXISTS MEDICAL_PROCEDURES;

DROP TABLE IF EXISTS MEDICAL_DEPARTMENTS;

DROP TABLE IF EXISTS MEDICAL_LOCATIONS;

Then the script creates all five CVD database tables.

This demonstrates the importance of SQL scripts for creating complete database structures in a repeatable way.

🧠 My Practice SQL

File:

02_My_Practice.sql

My practice was divided into multiple learning sections.

Part 1: Basic Table Verification

Practiced:

Viewing complete tables
Selecting specific columns

Example:

SELECT \*
FROM
PATIENTS;
SELECT
PATIENT_ID,
FIRST_NAME,
LAST_NAME,
SEX
FROM
PATIENTS;
Part 2: Filtering Data

Practiced:

WHERE
Filtering male patients
Filtering female patients
Filtering department records
Finding patient-specific medical history
Filtering procedures

Example:

SELECT
PATIENT_ID,
FIRST_NAME,
LAST_NAME,
SEX
FROM
PATIENTS
WHERE
SEX = 'M';
Part 3: Sorting and Limiting Data

Practiced:

ORDER BY
Ascending sorting
Descending sorting
LIMIT

Example:

SELECT
PATIENT_ID,
FIRST_NAME,
LAST_NAME
FROM
PATIENTS
ORDER BY
FIRST_NAME ASC;

Example using LIMIT:

SELECT
PATIENT_ID,
FIRST_NAME,
LAST_NAME
FROM
PATIENTS
LIMIT
3;
Part 4: Advanced Filtering

Practiced:

AND
OR
IN
LIKE
BETWEEN

Example:

SELECT
PATIENT_ID,
FIRST_NAME,
LAST_NAME
FROM
PATIENTS
WHERE
DEPT_ID IN ('D001', 'D003');

Example using LIKE:

SELECT
PATIENT_ID,
FIRST_NAME,
LAST_NAME
FROM
PATIENTS
WHERE
FIRST_NAME LIKE 'J%';

Example using BETWEEN:

SELECT
PROCEDURE_ID,
PROCEDURE_NAME,
PROCEDURE_DATE
FROM
MEDICAL_PROCEDURES
WHERE
PROCEDURE_DATE BETWEEN '2023-08-01'
AND '2023-08-03';
📊 Aggregate Functions

Practiced:

COUNT()
COUNT(DISTINCT)
MIN()
MAX()

Example:

SELECT
COUNT(\*) AS TOTAL_PATIENTS
FROM
PATIENTS;

Example:

SELECT
MIN(PROCEDURE_DATE) AS EARLIEST_PROCEDURE_DATE
FROM
MEDICAL_PROCEDURES;

Example:

SELECT
MAX(PROCEDURE_DATE) AS LATEST_PROCEDURE_DATE
FROM
MEDICAL_PROCEDURES;
📈 GROUP BY

Used GROUP BY to summarize records.

Example:

SELECT
SEX,
COUNT(\*) AS TOTAL_PATIENTS
FROM
PATIENTS
GROUP BY
SEX;

Result:

F → 2 patients
M → 3 patients
🔍 HAVING

Used HAVING to filter grouped results.

Example:

SELECT
DEPT*ID,
COUNT(*) AS TOTAL*PATIENTS
FROM
PATIENTS
GROUP BY
DEPT_ID
HAVING
COUNT(*) > 1;

Result:

D003 → 2 patients
⚡ WHERE vs HAVING

One of the important concepts practiced in this lab:

WHERE
↓
Filters rows BEFORE grouping

GROUP BY
↓
Creates groups

HAVING
↓
Filters groups AFTER grouping

Example:

SELECT
DEPT*ID,
COUNT(*) AS TOTAL*PROCEDURES
FROM
MEDICAL_PROCEDURES
WHERE
PROCEDURE_DATE >= '2023-08-01'
GROUP BY
DEPT_ID
HAVING
COUNT(*) >= 2;
✏️ INSERT, UPDATE and DELETE Practice

A separate practice table was created:

PATIENT_NOTES
Create Table
CREATE TABLE PATIENT_NOTES (
NOTE_ID INTEGER PRIMARY KEY,
PATIENT_ID CHAR(9) NOT NULL,
NOTE_TEXT VARCHAR(100),
NOTE_DATE DATE
);
INSERT

Inserted multiple patient notes.

INSERT INTO
PATIENT_NOTES (
NOTE_ID,
PATIENT_ID,
NOTE_TEXT,
NOTE_DATE
)
VALUES
(1, 'P001', 'Initial consultation completed', '2023-08-01');
UPDATE

Updated an existing patient note.

UPDATE
PATIENT_NOTES
SET
NOTE_TEXT = 'Follow-up appointment completed'
WHERE
NOTE_ID = 2;
DELETE

Deleted a specific patient note.

DELETE FROM
PATIENT_NOTES
WHERE
NOTE_ID = 3;
🏆 Challenge Queries

File:

03_Challenge.sql

The challenge section was designed to test the complete set of SQL concepts practiced in this lab.

The challenge included:

Basic SELECT
Column selection
WHERE
ORDER BY
LIMIT
AND
OR
IN
LIKE
BETWEEN
COUNT
DISTINCT
MIN
MAX
GROUP BY
HAVING
INSERT
UPDATE
DELETE
🛠️ Python Utility Scripts
setup_database.py

Creates the SQLite database.

data/lab02_database.db
run_sql.py

Executes SQL queries from a selected SQL file.

Example:

python run_sql.py 01_IBM_Lab.sql
python run_sql.py 02_My_Practice.sql
python run_sql.py 03_Challenge.sql

The script prints:

Query number
SQL query
Query results
Rows affected
inspect_csv_files.py

Inspects CSV files before loading them into the database.

Checks:

Row count
Column count
First row
Second row
load_csv_data.py

Loads CSV records into their corresponding SQLite tables.

verify_database.py

Performs final database verification.

Checks:

Tables
Row counts
Loaded records
🐛 Debugging Experience

During this lab, I encountered an important database workflow issue.

Issue

The database tables were recreated using:

DROP TABLE IF EXISTS

followed by:

CREATE TABLE

As a result, previously loaded data was removed when the table creation script was executed again.

The verification output showed:

Total Rows: 0
Solution

The correct workflow was followed:

1. Run table creation script
   ↓
2. Load CSV data
   ↓
3. Verify database
   ↓
4. Run practice queries

Commands:

python run_sql.py 01_IBM_Lab.sql
python load_csv_data.py
python verify_database.py

After following this workflow, all records were successfully restored.

🎓 Key Learning Insights
SQL Script Execution

SQL scripts allow multiple database operations to be organized and executed systematically.

Database Recreation

When using:

DROP TABLE

the entire table structure and its data are removed.

Therefore:

DROP TABLE
↓
CREATE TABLE
↓
LOAD DATA

is the correct sequence.

Data Loading

CSV files can be used as a source for populating relational database tables.

Workflow:

CSV
↓
Python
↓
SQLite
↓
SQL Queries
Aggregation Workflow

A useful SQL execution model:

FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
↓
LIMIT

This helps understand how complex SQL queries process data.

🧠 SQL Concepts Practiced
Concept Status
CREATE TABLE ✅
DROP TABLE ✅
SELECT ✅
WHERE ✅
ORDER BY ✅
LIMIT ✅
AND ✅
OR ✅
IN ✅
LIKE ✅
BETWEEN ✅
COUNT ✅
DISTINCT ✅
MIN ✅
MAX ✅
GROUP BY ✅
HAVING ✅
INSERT ✅
UPDATE ✅
DELETE ✅
CSV Data Loading ✅
Database Verification ✅
🏁 Final Lab Status
IBM Lab: COMPLETED
Database Creation: COMPLETED
CSV Inspection: COMPLETED
CSV Data Loading: COMPLETED
Database Verification: COMPLETED
My Practice: COMPLETED
Challenge Queries: COMPLETED
Debugging: COMPLETED
README Documentation: COMPLETED
🎯 Final Learning Outcome

This lab provided hands-on experience in building and working with a complete relational database environment.

I successfully practiced the full workflow:

SQL Script
↓
Database Tables
↓
CSV Data
↓
Python Data Loading
↓
SQLite Database
↓
SQL Queries
↓
Filtering
↓
Aggregation
↓
Data Modification
↓
Verification

The lab strengthened my practical understanding of SQL table creation, database loading, data querying, filtering, aggregation, grouping, data modification, and database workflow management.
