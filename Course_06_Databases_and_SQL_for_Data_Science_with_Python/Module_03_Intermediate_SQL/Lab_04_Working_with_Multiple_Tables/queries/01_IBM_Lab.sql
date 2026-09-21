-- ============================================================
-- IBM LAB 04: WORKING WITH MULTIPLE TABLES
-- Course 06 - Databases and SQL for Data Science with Python
-- Module 03 - Intermediate SQL
-- Database: HR.db
-- ============================================================
-- ============================================================
-- PART 1: ACCESSING MULTIPLE TABLES WITH SUB-QUERIES
-- ============================================================
-- ------------------------------------------------------------
-- QUERY 1
-- Retrieve only the EMPLOYEES records corresponding to jobs
-- in the JOBS table.
-- ------------------------------------------------------------
SELECT
    *
FROM
    EMPLOYEES
WHERE
    JOB_ID IN (
        SELECT
            JOB_IDENT
        FROM
            JOBS
    );

-- ------------------------------------------------------------
-- QUERY 2
-- Retrieve JOB information for employees earning over $70,000.
-- ------------------------------------------------------------
SELECT
    JOB_TITLE,
    MIN_SALARY,
    MAX_SALARY,
    JOB_IDENT
FROM
    JOBS
WHERE
    JOB_IDENT IN (
        SELECT
            JOB_ID
        FROM
            EMPLOYEES
        WHERE
            SALARY > 70000
    );

-- ============================================================
-- PART 2: ACCESSING MULTIPLE TABLES WITH IMPLICIT JOINS
-- ============================================================
-- ------------------------------------------------------------
-- QUERY 3
-- Retrieve EMPLOYEES records corresponding to jobs
-- in the JOBS table using an implicit join.
-- ------------------------------------------------------------
SELECT
    *
FROM
    EMPLOYEES,
    JOBS
WHERE
    EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;

-- ------------------------------------------------------------
-- QUERY 4
-- Redo the previous query using shorter table aliases.
-- ------------------------------------------------------------
SELECT
    *
FROM
    EMPLOYEES E,
    JOBS J
WHERE
    E.JOB_ID = J.JOB_IDENT;

-- ------------------------------------------------------------
-- QUERY 5
-- Retrieve Employee ID, First Name, Last Name, and Job Title.
-- ------------------------------------------------------------
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    JOB_TITLE
FROM
    EMPLOYEES E,
    JOBS J
WHERE
    E.JOB_ID = J.JOB_IDENT;

-- ------------------------------------------------------------
-- QUERY 6
-- Redo the previous query using fully qualified column names
-- with table aliases.
-- ------------------------------------------------------------
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE
FROM
    EMPLOYEES E,
    JOBS J
WHERE
    E.JOB_ID = J.JOB_IDENT;

-- ============================================================
-- IBM PRACTICE QUESTIONS
-- ============================================================
-- ============================================================
-- PRACTICE QUESTION 1A
-- Retrieve only the list of employees whose JOB_TITLE
-- is 'Jr. Designer'.
-- Using Subquery
-- ============================================================
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    JOB_ID
FROM
    EMPLOYEES
WHERE
    JOB_ID IN (
        SELECT
            JOB_IDENT
        FROM
            JOBS
        WHERE
            JOB_TITLE = 'Jr. Designer'
    );

-- ============================================================
-- PRACTICE QUESTION 1B
-- Retrieve only the list of employees whose JOB_TITLE
-- is 'Jr. Designer'.
-- Using Implicit Join
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE
FROM
    EMPLOYEES E,
    JOBS J
WHERE
    E.JOB_ID = J.JOB_IDENT
    AND J.JOB_TITLE = 'Jr. Designer';

-- ============================================================
-- PRACTICE QUESTION 2A
-- Retrieve JOB information and a list of employees
-- whose birth year is after 1976.
-- Using Subquery
-- SQLite Version
-- ============================================================
SELECT
    JOB_IDENT,
    JOB_TITLE,
    MIN_SALARY,
    MAX_SALARY
FROM
    JOBS
WHERE
    JOB_IDENT IN (
        SELECT
            JOB_ID
        FROM
            EMPLOYEES
        WHERE
            strftime('%Y', B_DATE) > '1976'
    );

-- ============================================================
-- PRACTICE QUESTION 2B
-- Retrieve JOB information and employee details
-- for employees whose birth year is after 1976.
-- Using Implicit Join
-- SQLite Version
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    E.B_DATE,
    J.JOB_IDENT,
    J.JOB_TITLE,
    J.MIN_SALARY,
    J.MAX_SALARY
FROM
    EMPLOYEES E,
    JOBS J
WHERE
    E.JOB_ID = J.JOB_IDENT
    AND strftime('%Y', E.B_DATE) > '1976';
    