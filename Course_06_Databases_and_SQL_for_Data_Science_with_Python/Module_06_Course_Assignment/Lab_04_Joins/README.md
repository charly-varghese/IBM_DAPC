# Lab 04 — Joins

## Overview

This lab demonstrates how SQL JOIN operations combine data from
multiple related tables in the HR database.

The lab was completed using MySQL in VS Code with the Database Client
and MySQL CLI.

---

## Environment

- MySQL Server 8.0.46
- MySQL Workbench 8.0.47
- VS Code
- MySQL — Database Client
- Database: `HR`

---

## HR Database Tables

The following five tables were created and populated:

- `EMPLOYEES`
- `JOB_HISTORY`
- `JOBS`
- `DEPARTMENTS`
- `LOCATIONS`

### Dataset Validation

| Table | Expected Rows | Status |
| ----- | ------------: | ------ |

| EMPLOYEES | 10 | ✅ |
| JOB_HISTORY | 10 | ✅ |
| JOBS | 10 | ✅ |
| DEPARTMENTS | 3 | ✅ |
| LOCATIONS | 3 | ✅ |

---

## Learning Objectives

- Query multiple tables using `INNER JOIN`
- Query multiple tables using `LEFT OUTER JOIN`
- Query multiple tables using `RIGHT OUTER JOIN`
- Implement a `FULL OUTER JOIN` in MySQL using `UNION`

---

## IBM Lab Exercises

## Exercise 1 — INNER JOIN

Retrieve employee names and job start dates for employees
working in department 5.

Tables:

- `EMPLOYEES`
- `JOB_HISTORY`

Join condition:

```sql
E.EMP_ID = JH.EMPL_ID
Filter:

E.DEP_ID = '5'

Result: 4 employees

Exercise 2 — LEFT OUTER JOIN

Retrieve employee ID, last name, department ID, and department name
for all employees.

Tables:

EMPLOYEES
DEPARTMENTS

Join condition:

E.DEP_ID = D.DEPT_ID_DEP

Result: 10 employees

Exercise 3 — FULL OUTER JOIN

MySQL does not use a direct FULL OUTER JOIN statement in this lab.

The IBM approach combines:

LEFT OUTER JOIN
       +
RIGHT OUTER JOIN
       +
UNION

Result: 10 rows

The result contains the employee records together with the department
records represented by the full outer join operation.

My Practice
Practice Problem 1

Retrieve:

First name
Last name
Job start date
Job title

for employees working in department 5.

Tables used:

EMPLOYEES
JOB_HISTORY
JOBS
Practice Problem 2

Retrieve:

Employee ID
Last name
Department ID
Department name

for all employees, with department names shown only for employees
born before 1980.

Tables used:

EMPLOYEES
DEPARTMENTS
Practice Problem 3

Retrieve:

First name
Last name
Department ID
Department name

for all employees, with department information shown only for
male employees.

Tables used:

EMPLOYEES
DEPARTMENTS
Important Debugging Note

During CSV loading, the Windows CRLF line ending caused a hidden
carriage-return character (\r) to remain in the last column of some
imported values.

This initially caused:

INNER JOIN filtering to return 0 rows
Department names to appear as NULL

The affected values were cleaned using:

UPDATE EMPLOYEES
SET DEP_ID = TRIM(REPLACE(DEP_ID, '\r', ''));

UPDATE JOB_HISTORY
SET DEPT_ID = TRIM(REPLACE(DEPT_ID, '\r', ''));

After cleaning, all JOIN queries produced the expected results.

Future CSV Import

For Windows CRLF CSV files, prefer:

LINES TERMINATED BY '\r\n';

when appropriate.

Key SQL Concepts
INNER JOIN

Returns rows where matching values exist in both tables.

LEFT JOIN

Returns all rows from the left table and matching rows from the
right table.

RIGHT JOIN

Returns all rows from the right table and matching rows from the
left table.

FULL OUTER JOIN

Returns rows from both sides. In this MySQL lab it is implemented
using LEFT JOIN, RIGHT JOIN, and UNION.

Files
Lab_04_Joins/
├── 01_Lab.sql
├── 02_My_Practice.sql
├── Script_Create_Tables.sql
├── Departments.csv
├── Employees.csv
├── Jobs.csv
├── JobsHistory.csv
├── Locations.csv
└── README.md
Completion Status
Component Status
HR database created ✅
Five tables created ✅
Five CSV datasets loaded ✅
INNER JOIN ✅
LEFT OUTER JOIN ✅
FULL OUTER JOIN ✅
IBM practice problems ✅
README ✅
Lab Status: COMPLETED ✅
```
