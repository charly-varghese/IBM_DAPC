-- ============================================================
-- IBM DAPC - Course 06
-- Module 06 - Advanced SQL for Data Engineers
-- Lab 01 - Using Views
-- My Practice
-- Database: HR
-- Engine: MySQL
-- ============================================================
-- ============================================================
-- PRACTICE 1 - CREATE EMP_DEPT VIEW
-- ============================================================
CREATE VIEW EMP_DEPT AS
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    DEP_ID
FROM
    EMPLOYEES;

SELECT
    *
FROM
    EMP_DEPT;

-- ============================================================
-- PRACTICE 2 - MODIFY VIEW WITH DEPARTMENT NAME
-- ============================================================
CREATE
OR REPLACE VIEW EMP_DEPT AS
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    E.DEP_ID,
    D.DEP_NAME
FROM
    EMPLOYEES AS E
    JOIN DEPARTMENTS AS D ON E.DEP_ID = D.DEPT_ID_DEP;

SELECT
    *
FROM
    EMP_DEPT;

-- ============================================================
-- PRACTICE 3 - DROP VIEW
-- ============================================================
DROP VIEW EMP_DEPT;

-- Expected verification:
-- The following query should fail because EMP_DEPT was dropped.
SELECT
    *
FROM
    EMP_DEPT;