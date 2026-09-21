USE HR;

-- ============================================================
-- Lab 04: Working with Joins
-- IBM Lab Exercises
-- ============================================================
-- Exercise 1: INNER JOIN
-- Retrieve names and job start dates of employees
-- who work for department number 5.
SELECT
    E.F_NAME,
    E.L_NAME,
    JH.START_DATE
FROM
    EMPLOYEES AS E
    INNER JOIN JOB_HISTORY AS JH ON E.EMP_ID = JH.EMPL_ID
WHERE
    E.DEP_ID = '5';

-- Exercise 2: LEFT OUTER JOIN
-- Retrieve employee ID, last name, department ID,
-- and department name for all employees.
SELECT
    E.EMP_ID,
    E.L_NAME,
    E.DEP_ID,
    D.DEP_NAME
FROM
    EMPLOYEES AS E
    LEFT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID = D.DEPT_ID_DEP;

-- Exercise 3: FULL OUTER JOIN
-- MySQL implementation using LEFT JOIN + RIGHT JOIN + UNION.
SELECT
    E.F_NAME,
    E.L_NAME,
    D.DEP_NAME
FROM
    EMPLOYEES AS E
    LEFT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID = D.DEPT_ID_DEP
UNION
SELECT
    E.F_NAME,
    E.L_NAME,
    D.DEP_NAME
FROM
    EMPLOYEES AS E
    RIGHT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID = D.DEPT_ID_DEP;