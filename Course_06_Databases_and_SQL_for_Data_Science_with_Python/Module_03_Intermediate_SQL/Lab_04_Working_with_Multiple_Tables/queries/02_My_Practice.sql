-- ============================================================
-- MY PRACTICE — WORKING WITH MULTIPLE TABLES
-- Course 06 - Databases and SQL for Data Science with Python
-- Module 03 - Intermediate SQL
-- Lab 04
-- Database: HR.db
-- ============================================================
-- ============================================================
-- QUERY 1
-- Show employees with their job titles.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE
FROM
    EMPLOYEES AS E,
    JOBS AS J
WHERE
    E.JOB_ID = J.JOB_IDENT;

-- ============================================================
-- QUERY 2
-- Show employees, job titles, and salaries.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE,
    E.SALARY
FROM
    EMPLOYEES AS E,
    JOBS AS J
WHERE
    E.JOB_ID = J.JOB_IDENT
ORDER BY
    E.SALARY DESC;

-- ============================================================
-- QUERY 3
-- Show employees working in each department.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    D.DEP_NAME
FROM
    EMPLOYEES AS E,
    DEPARTMENTS AS D
WHERE
    E.DEP_ID = D.DEPT_ID_DEP
ORDER BY
    D.DEP_NAME,
    E.F_NAME;

-- ============================================================
-- QUERY 4
-- Show employee name, department, and job title.
-- Three-table implicit join.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    D.DEP_NAME,
    J.JOB_TITLE
FROM
    EMPLOYEES AS E,
    DEPARTMENTS AS D,
    JOBS AS J
WHERE
    E.DEP_ID = D.DEPT_ID_DEP
    AND E.JOB_ID = J.JOB_IDENT
ORDER BY
    D.DEP_NAME,
    E.F_NAME;

-- ============================================================
-- QUERY 5
-- Show employees earning above the minimum salary
-- defined for their job.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE,
    E.SALARY,
    J.MIN_SALARY
FROM
    EMPLOYEES AS E,
    JOBS AS J
WHERE
    E.JOB_ID = J.JOB_IDENT
    AND E.SALARY > J.MIN_SALARY;

-- ============================================================
-- QUERY 6
-- Show employees earning exactly the maximum salary
-- allowed for their job.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE,
    E.SALARY,
    J.MAX_SALARY
FROM
    EMPLOYEES AS E,
    JOBS AS J
WHERE
    E.JOB_ID = J.JOB_IDENT
    AND E.SALARY = J.MAX_SALARY;

-- ============================================================
-- QUERY 7
-- Show employees whose salary is greater than the
-- average salary of all employees.
-- Include their job title.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE,
    E.SALARY
FROM
    EMPLOYEES AS E,
    JOBS AS J
WHERE
    E.JOB_ID = J.JOB_IDENT
    AND E.SALARY > (
        SELECT
            AVG(SALARY)
        FROM
            EMPLOYEES
    )
ORDER BY
    E.SALARY DESC;

-- ============================================================
-- QUERY 8
-- Show employees who belong to the department
-- with the highest average salary.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    E.DEP_ID,
    D.DEP_NAME,
    E.SALARY
FROM
    EMPLOYEES AS E,
    DEPARTMENTS AS D
WHERE
    E.DEP_ID = D.DEPT_ID_DEP
    AND E.DEP_ID = (
        SELECT
            DEP_ID
        FROM
            EMPLOYEES
        GROUP BY
            DEP_ID
        ORDER BY
            AVG(SALARY) DESC
        LIMIT
            1
    );

-- ============================================================
-- QUERY 9
-- Show employee details with job history information.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    E.SALARY,
    H.START_DATE,
    H.JOBS_ID,
    H.DEPT_ID
FROM
    EMPLOYEES AS E,
    JOB_HISTORY AS H
WHERE
    E.EMP_ID = H.EMPL_ID
ORDER BY
    H.START_DATE;

-- ============================================================
-- QUERY 10
-- Complete employee profile:
-- Employee + Department + Job + Job History
-- Four-table implicit join.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    D.DEP_NAME,
    J.JOB_TITLE,
    E.SALARY,
    H.START_DATE AS JOB_START_DATE
FROM
    EMPLOYEES AS E,
    DEPARTMENTS AS D,
    JOBS AS J,
    JOB_HISTORY AS H
WHERE
    E.DEP_ID = D.DEPT_ID_DEP
    AND E.JOB_ID = J.JOB_IDENT
    AND E.EMP_ID = H.EMPL_ID
ORDER BY
    E.EMP_ID;