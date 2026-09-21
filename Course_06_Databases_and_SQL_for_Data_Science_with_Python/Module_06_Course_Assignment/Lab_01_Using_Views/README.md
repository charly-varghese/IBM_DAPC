# IBM DAPC - Course 06

## Module 06 - Advanced SQL for Data Engineers

### Lab 01 - Using Views

---

## 1. Lab Overview

This lab focuses on creating, modifying, querying, and dropping SQL Views using MySQL.

The practical work was performed using the IBM HR sample database in a local MySQL environment through VS Code and the Database Client extension.

---

## 2. Environment

| Item | Details |
| ---- | ------- |

| Course | IBM Data Analyst Professional Certificate |
| Course | Course 06 - Databases and SQL for Data Science with Python |
| Module | Module 06 - Advanced SQL for Data Engineers |
| Lab | Lab 01 - Using Views |
| Database Engine | MySQL |
| MySQL Version | 8.0.46 |
| Database | HR |
| IDE | Visual Studio Code |
| Database Tool | Database Client |
| Connection | IBM_DAPC_MySQL |
| Execution Database | HR |

---

## 3. HR Database

The lab uses the following HR database tables:

```text
HR
├── departments
├── employees
├── job_history
├── jobs
└── locations
Loaded Record Counts
Table Records
departments 3
employees 10
job_history 10
jobs 10
locations 3
4. Lab Objectives

The practical objectives are:

Create a SQL View.
Modify a View to combine information from multiple tables.
Query and validate a View.
Drop a View.
Verify that the View has been removed.
5. IBM Lab Tasks
Task 1 - Create a View

Created the EMPSALARY View from the EMPLOYEES table.

The View demonstrated selecting employee identification, personal information, and salary-related columns.

Concept practiced:

CREATE VIEW
Task 2 - Modify the View

The EMPSALARY View was modified to combine data from:

EMPLOYEES
+
JOBS

The join connects:

EMPLOYEES.JOB_ID
        =
JOBS.JOB_IDENT

Concepts practiced:

CREATE OR REPLACE VIEW
JOIN

The resulting View included employee information together with:

JOB_TITLE
MIN_SALARY
MAX_SALARY
Task 3 - Drop the View

The View was removed using:

DROP VIEW EMPSALARY;

A subsequent query against the deleted View produced the expected error indicating that the View no longer existed.

This was used as the verification step for the DROP VIEW operation.

6. My Practice
Practice 1 - Create EMP_DEPT View

Created:

CREATE VIEW EMP_DEPT AS
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    DEP_ID
FROM EMPLOYEES;

The View was queried successfully and returned:

10 employee records
Practice 2 - Modify View with Department Name

The EMP_DEPT View was modified to include the department name.

Tables used:

EMPLOYEES
+
DEPARTMENTS

Join condition:

E.DEP_ID = D.DEPT_ID_DEP

Final View structure:

EMP_ID
F_NAME
L_NAME
DEP_ID
DEP_NAME

The verification query returned:

10 employee records

Department mappings were successfully validated for:

2 → Architect Group
5 → Software Group
7 → Design Team
Practice 3 - Drop EMP_DEPT View

The View was removed using:

DROP VIEW EMP_DEPT;

Verification was then performed with:

SELECT *
FROM EMP_DEPT;

The query intentionally failed with a MySQL error indicating:

Table 'hr.emp_dept' doesn't exist

This failure is expected and confirms that the View was successfully dropped.

7. Key SQL Concepts Practiced
CREATE VIEW
CREATE OR REPLACE VIEW
SELECT FROM VIEW
JOIN
DROP VIEW
View validation
Important Concept

A SQL View is a virtual table based on a SQL query.

It can simplify repeated queries and provide a reusable way to present selected data from one or more tables.

8. VS Code Execution Workflow

The final execution workflow used for this lab was:

VS Code
   ↓
Database Client Extension
   ↓
IBM_DAPC_MySQL Connection
   ↓
HR Database
   ↓
SQL Query
   ↓
MySQL Execution
   ↓
Result Verification

The MySQL connection was independently verified with:

SELECT COUNT(*) AS employee_count
FROM employees;

Expected and actual result:

employee_count
--------------
10
9. Files
Lab_01_Using_Views/
│
├── 01_Lab.sql
├── 02_My_Practice.sql
├── HR_Database_Create_Tables_Script.sql
├── Employees_updated.csv
├── Departments.csv
├── Jobs.csv
├── JobsHistory.csv
├── Locations.csv
└── README.md
File Purpose
File Purpose
01_Lab.sql IBM lab/reference SQL
02_My_Practice.sql Personal practice and execution script
HR_Database_Create_Tables_Script.sql HR database/table creation script
Employees_updated.csv Employee data
Departments.csv Department data
Jobs.csv Job data
JobsHistory.csv Job history data
Locations.csv Location data
README.md Lab documentation
10. Validation Summary
Component Status
MySQL Server ✅ Verified
HR Database ✅ Verified
HR Tables ✅ 5 tables
Employee Records ✅ 10
IBM View Tasks ✅ Completed
Practice 1 ✅ Completed
Practice 2 ✅ Completed
Practice 3 ✅ Completed
View Verification ✅ Completed
VS Code MySQL Execution ✅ Verified
11. Learning Outcome

After completing this lab, the following practical SQL skills were demonstrated:

Creating SQL Views.
Querying Views.
Replacing an existing View.
Combining tables inside a View using JOIN.
Dropping Views.
Validating database objects after modification.
Executing MySQL SQL directly from VS Code.
Working with a real MySQL database connection in a development environment.
12. Completion Status

Lab 01 - Using Views: COMPLETED ✅

Module 06 - Lab 01 Status: COMPLETE
```
