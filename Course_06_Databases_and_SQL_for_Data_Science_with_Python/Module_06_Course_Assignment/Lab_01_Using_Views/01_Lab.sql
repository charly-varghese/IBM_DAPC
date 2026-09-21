-- ============================================================
-- IBM DAPC - Course 06
-- Module 06 - Advanced SQL for Data Engineers
-- Lab 01 - Using Views
-- Database: HR
-- Engine: MySQL
-- ============================================================
-- ============================================================
-- TASK 1 - CREATE A VIEW
-- ============================================================
CREATE VIEW EMPSALARY AS
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    B_DATE,
    SEX,
    SALARY
FROM
    EMPLOYEES;

SELECT
    *
FROM
    EMPSALARY;

-- ============================================================
-- TASK 2 - UPDATE THE VIEW
-- ============================================================
CREATE
OR REPLACE VIEW EMPSALARY AS
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    B_DATE,
    SEX,
    JOB_TITLE,
    MIN_SALARY,
    MAX_SALARY
FROM
    EMPLOYEES,
    JOBS
WHERE
    EMPLOYEES.JOB_ID = JOBS.JOB_IDENT;

SELECT
    *
FROM
    EMPSALARY;

-- ============================================================
-- TASK 3 - DROP THE VIEW
-- ============================================================
DROP VIEW EMPSALARY;

-- Expected verification:
-- The following query should fail because EMPSALARY was dropped.
SELECT
    *
FROM
    EMPSALARY;