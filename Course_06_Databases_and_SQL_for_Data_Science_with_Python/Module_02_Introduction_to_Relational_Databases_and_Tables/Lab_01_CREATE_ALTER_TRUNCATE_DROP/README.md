# Lab 01 — CREATE, ALTER, TRUNCATE, DROP

## Module

\*_Module 02 — Introduction to Relational Databases and Tables_

## Course

**IBM Data Analyst Professional Certificate**  
**Course 06 — Databases and SQL for Data Science with Python**

---

## 📌 Lab Overview

This lab provides hands-on practice with essential SQL Data Definition Language (DDL) and Data Manipulation Language (DML) operations.

The lab was originally designed using MySQL and phpMyAdmin in the IBM Skills Network environment. For local hands-on practice, the lab was implemented using:

- SQLite
- Python `sqlite3`
- VS Code

The lab demonstrates the complete lifecycle of a database table:

```text
CREATE
   ↓
INSERT DATA
   ↓
ALTER TABLE
   ↓
UPDATE DATA
   ↓
DELETE ALL ROWS
   ↓
DROP TABLE

🎯 Objectives

After completing this lab, the following SQL operations were practiced:

Create database tables.
Insert records into tables.
Modify existing table structures.
Add new columns using ALTER TABLE.
Update existing records.
Remove all rows from a table.
Delete tables completely.
Verify database objects after table deletion.
🛠️ Technologies Used
Technology-Purpose
SQLite-Local relational database
Python-Database execution
Python sqlite3-SQLite database connection and execution
VS Code-Code editor and development environment
SQL-Database querying and manipulation
📂 Lab Structure
Lab_01_CREATE_ALTER_TRUNCATE_DROP/
│
├── 01_IBM_Lab.sql
├── 02_My_Practice.sql
├── 03_Challenge.sql
├── 04_Debug_Notes.md
├── README.md
├── run_sql.py
├── setup_database.py
│
└── data/
    └── relational_lab.db
1️⃣ IBM Lab Practice

File:

01_IBM_Lab.sql

The IBM lab workflow was adapted for SQLite and included the following operations.

CREATE TABLE

Created two tables:

PETSALE
PET

Example:

CREATE TABLE PETSALE (
    ID INTEGER NOT NULL,
    PET CHAR(20),
    SALEPRICE DECIMAL(6, 2),
    PROFIT DECIMAL(6, 2),
    SALEDATE DATE
);
INSERT Data

Inserted records into:

PETSALE
PET

Example:

INSERT INTO PETSALE VALUES
    (1, 'Cat', 450.09, 100.47, '2018-05-29');
ALTER TABLE

Added a new column:

ALTER TABLE PETSALE
ADD COLUMN QUANTITY INTEGER;

Updated quantity values using:

UPDATE PETSALE
SET QUANTITY = 9
WHERE ID = 1;
DROP COLUMN

The PROFIT column was removed from the PETSALE table.

Final table structure included:

ID
PET
SALEPRICE
SALEDATE
QUANTITY
TRUNCATE Learning Objective

The original IBM/MySQL concept:

TRUNCATE TABLE PET;

SQLite does not support TRUNCATE TABLE.

Therefore, the SQLite equivalent used was:

DELETE FROM PET;

This removed all rows while keeping the table structure.

DROP TABLE

The PET table was permanently removed:

DROP TABLE PET;

Final database verification confirmed that only the PETSALE table remained after the IBM Lab workflow.

2️⃣ My Practice

File:

02_My_Practice.sql

A separate EMPLOYEE table was created to independently practice the concepts.

CREATE
CREATE TABLE EMPLOYEE (
    ID INTEGER NOT NULL,
    NAME TEXT,
    DEPARTMENT TEXT,
    SALARY DECIMAL(10, 2)
);
INSERT

Three employee records were inserted.

Anil
Beena
Charles
ALTER

A new column was added:

ALTER TABLE EMPLOYEE
ADD COLUMN CITY TEXT;
UPDATE

Employee city values were updated:

Anil     → Kochi
Beena    → Mumbai
Charles  → Bengaluru
DELETE All Rows
DELETE FROM EMPLOYEE;

The table remained available, but all employee records were removed.

DROP TABLE
DROP TABLE EMPLOYEE;

Final database verification returned:

[]

This confirmed that no tables remained in the practice database after the table was dropped.

3️⃣ Challenge Practice

File:

03_Challenge.sql

A PRODUCT table was created to complete an independent SQL challenge.

Operations Completed
CREATE TABLE

Created:

PRODUCT
INSERT

Inserted three products:

Laptop
Smartphone
Office Chair
ALTER

Added:

STOCK

column to the table.

UPDATE

Stock values were updated:

Laptop       → 15
Smartphone   → 30
Office Chair → 20
DELETE All Rows
DELETE FROM PRODUCT;

All three records were successfully removed.

DROP TABLE
DROP TABLE PRODUCT;

The PRODUCT table was successfully deleted.

🔄 SQLite vs MySQL Compatibility

The original IBM lab was designed for MySQL.

This local implementation used SQLite.

TRUNCATE

MySQL:

TRUNCATE TABLE table_name;

SQLite:

DELETE FROM table_name;

For this lab, DELETE FROM was used to achieve the same learning objective of removing all rows while preserving the table structure.

⚠️ Important Debugging Notes
Rows affected: -1

SQLite may display:

Rows affected: -1

for DDL operations such as:

CREATE TABLE
ALTER TABLE
DROP TABLE

This is normal behavior and does not indicate an error.

None Values

When a new column is added to existing records:

ALTER TABLE EMPLOYEE
ADD COLUMN CITY TEXT;

existing rows initially contain:

None

in Python output.

This represents SQLite:

NULL

values.

VS Code SQL Warning

VS Code may show SQL syntax warnings when the SQL language validator is configured for a different database dialect.

The actual database execution was performed using:

python run_sql.py

Successful SQLite execution was used as the final validation.

For detailed troubleshooting information, see:

04_Debug_Notes.md
▶️ How to Run the Lab
Step 1 — Navigate to the Lab Folder
cd Lab_01_CREATE_ALTER_TRUNCATE_DROP
Step 2 — Create the Database
python setup_database.py

Expected result:

SQLite database created successfully.
Database: data/relational_lab.db
Step 3 — Execute SQL Files

The run_sql.py script executes the SQL practice files.

Run:

python run_sql.py

The script executes SQL statements sequentially and displays:

Query number
SQL statement
Query results
Rows affected
🧠 Key Learning Outcomes

After completing this lab, I can:

CREATE tables
      ↓
INSERT records
      ↓
ALTER table structures
      ↓
ADD new columns
      ↓
UPDATE existing data
      ↓
DELETE all records
      ↓
DROP tables permanently

I also learned:

Differences between MySQL and SQLite.
SQLite TRUNCATE alternatives.
The difference between deleting rows and dropping a table.
How SQL DDL commands behave differently from DML commands.
How to verify database tables using SQLite metadata.
How to execute SQL locally using Python.
🏆 Final Lab Status
01_IBM_Lab.sql        ✅ COMPLETED
02_My_Practice.sql    ✅ COMPLETED
03_Challenge.sql      ✅ COMPLETED
04_Debug_Notes.md     ✅ COMPLETED
README.md             ✅ COMPLETED
🎓 Lab Completion

Module 02 — Introduction to Relational Databases and Tables

Lab 01 — CREATE, ALTER, TRUNCATE, DROP

STATUS: COMPLETED SUCCESSFULLY
```
