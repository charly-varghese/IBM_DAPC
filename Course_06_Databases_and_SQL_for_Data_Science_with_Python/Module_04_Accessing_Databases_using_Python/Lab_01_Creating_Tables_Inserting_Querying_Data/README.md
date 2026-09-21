# Lab 01 — Creating Tables, Inserting and Querying Data

## IBM Data Analyst Professional Certificate

**Course 06 — Databases and SQL for Data Science with Python**  
**Module 04 — Accessing Databases Using Python**  
**Lab 01 — Creating Tables, Inserting and Querying Data**

---

## 1. Lab Objective

The objective of this lab is to practice accessing a SQLite database using Python and the Python DB-API.

The lab demonstrates how to:

- Create a SQLite database
- Establish a database connection
- Create a database cursor
- Create a SQL table
- Insert records
- Execute SQL queries
- Retrieve query results using cursor fetch methods
- Update existing records
- Commit database changes
- Load SQL data into a Pandas DataFrame
- Perform basic DataFrame analysis
- Properly close database resources

---

## 2. Learning Workflow

The core database workflow practiced in this lab is:

```text
Python
   ↓
SQLite
   ↓
Connection
   ↓
Cursor
   ↓
Execute SQL
   ↓
Fetch Results
   ↓
Process with Python / Pandas
   ↓
Commit Changes
   ↓
Close Resources
``
3.Environment
Component Version / Environment
Operating System Windows
IDE Visual Studio Code
Python 3.14.0
Virtual Environment .venv
SQLite 3.50.4
Pandas 3.0.5

The project virtual environment was used for execution.

4.Folder Structure
Lab_01_Creating_Tables_Inserting_Querying_Data/
│
├── data/
│   ├── INSTRUCTOR.db
│   └── MY_PRACTICE.db
│
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 04_Debug_Notes.md
└── README.md
5.IBM Lab Implementation
Database

The IBM exercise uses a SQLite database:

INSTRUCTOR.db

The database contains the following table:

INSTRUCTOR
Table Structure
Column Type Constraint
ID INTEGER PRIMARY KEY, NOT NULL
FNAME VARCHAR(20) —
LNAME VARCHAR(20) —
CITY VARCHAR(20) —
CCODE CHAR(2) —
1. IBM Lab Operations
Database Connection
conn = sqlite3.connect(DB_PATH)
Cursor Creation
cursor_obj = conn.cursor()
Table Creation
CREATE TABLE INSTRUCTOR (...)
Data Insertion

Three instructor records were inserted successfully.

Data Retrieval

The lab demonstrated:

fetchall()
fetchmany(2)

and a column-specific query using:

SELECT FNAME FROM INSTRUCTOR
Update Operation

The bonus task updated Rav's city:

TORONTO → MOOSETOWN
Pandas Integration

The database result was loaded into Pandas:

df = pd.read_sql("SELECT * FROM INSTRUCTOR", conn)

The resulting DataFrame contained:

3 rows × 5 columns
Resource Management

The cursor and database connection were closed successfully.

7.Independent Practice

The IBM example was extended through an independent practice implementation in:

02_My_Practice.py

A separate database was created:

MY_PRACTICE.db

with the table:

EMPLOYEE
Employee Table
Column Purpose
EMP_ID Employee identifier
NAME Employee name
DEPARTMENT Department
CITY Employee city
SALARY Employee salary

Four employee records were inserted.

8.Additional SQL and Python Concepts Practiced

The independent practice demonstrated:

executemany()
Parameterized SQL INSERT
SELECT
WHERE
ORDER BY
fetchone()
fetchmany()
fetchall()
UPDATE
COUNT(*)
commit()
Pandas read_sql()
1. Basic Data Analysis

The employee data was loaded into Pandas and analyzed.

Total Employees
4
Average Salary
57250.0
Highest Salary
68000.0
Department Distribution
Sales        1
Marketing    1
IT           1
Finance      1

The independent practice successfully connected database operations with basic analytical processing in Pandas.

10.Debugging Experience

During the first execution attempt, the following error occurred:

ModuleNotFoundError: No module named 'pandas'
Root Cause

The terminal was not running inside the project's .venv virtual environment.

Resolution

The existing virtual environment was activated:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\activate.bat

The active Python interpreter was then verified.

After activating .venv, Pandas was successfully detected and the lab executed without errors.

Detailed debugging information is documented in:

04_Debug_Notes.md
1.  Key Technical Lessons
Python DB-API

The lab reinforced the standard database programming workflow:

connect()
    ↓
cursor()
    ↓
execute()
    ↓
fetchone() / fetchmany() / fetchall()
    ↓
commit()
    ↓
close()
SQLite

SQLite provides a lightweight relational database that can be accessed directly from Python without requiring a separate database server.

Pandas Integration

SQL query results can be transferred directly into a Pandas DataFrame:

pd.read_sql()

This creates a practical bridge between:

Database
   ↓
SQL
   ↓
Python
   ↓
Pandas
   ↓
Data Analysis
12. Skills Demonstrated

This lab demonstrates practical ability in:

Python database programming
SQLite
Python DB-API
SQL table creation
SQL INSERT operations
SQL SELECT operations
SQL UPDATE operations
Cursor-based result retrieval
Transaction commits
Pandas SQL integration
Basic DataFrame analysis
Python virtual environment management
Database resource management
Troubleshooting Python environment issues
13. Execution Status
Component Status
IBM Lab — Task 1 ✅ Completed
IBM Lab — Task 2 ✅ Completed
IBM Lab — Task 3 ✅ Completed
IBM Lab — Task 4 ✅ Completed
IBM Lab — Bonus UPDATE ✅ Completed
IBM Lab — Task 5 ✅ Completed
IBM Lab — Task 6 ✅ Completed
My Independent Practice ✅ Completed
Debugging ✅ Completed
Pandas Integration ✅ Completed
Database Verification ✅ Completed
🏆 Final Status

LAB 01 — COMPLETED SUCCESSFULLY

The lab successfully demonstrated the complete workflow for accessing and manipulating a SQLite database using Python, followed by integration with Pandas for basic data analysis.

Status: GitHub Ready
```
