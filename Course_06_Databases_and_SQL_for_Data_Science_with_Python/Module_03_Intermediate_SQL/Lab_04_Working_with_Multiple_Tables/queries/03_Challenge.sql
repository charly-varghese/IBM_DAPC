-- ============================================================
-- CHALLENGE QUERIES — WORKING WITH MULTIPLE TABLES
-- Course 06 - Databases and SQL for Data Science with Python
-- Module 03 - Intermediate SQL
-- Lab 04
-- Database: HR.db
-- ============================================================
-- ============================================================
-- CHALLENGE 1
-- Show each employee with their department and job title.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    D.DEP_NAME,
    J.JOB_TITLE,
    E.SALARY
FROM
    EMPLOYEES AS E,
    DEPARTMENTS AS D,
    JOBS AS J
WHERE
    E.DEP_ID = D.DEPT_ID_DEP
    AND E.JOB_ID = J.JOB_IDENT
ORDER BY
    E.EMP_ID;

-- ============================================================
-- CHALLENGE 2
-- Find employees whose salary is greater than
-- the average salary of their own department.
-- ============================================================
SELECT
    E1.EMP_ID,
    E1.F_NAME,
    E1.L_NAME,
    D.DEP_NAME,
    E1.SALARY
FROM
    EMPLOYEES AS E1,
    DEPARTMENTS AS D
WHERE
    E1.DEP_ID = D.DEPT_ID_DEP
    AND E1.SALARY > (
        SELECT
            AVG(E2.SALARY)
        FROM
            EMPLOYEES AS E2
        WHERE
            E2.DEP_ID = E1.DEP_ID
    )
ORDER BY
    E1.DEP_ID,
    E1.SALARY DESC;

-- ============================================================
-- CHALLENGE 3
-- Find the department with the highest
-- average employee salary.
-- ============================================================
SELECT
    D.DEPT_ID_DEP,
    D.DEP_NAME,
    AVG(E.SALARY) AS AVG_DEPARTMENT_SALARY
FROM
    EMPLOYEES AS E,
    DEPARTMENTS AS D
WHERE
    E.DEP_ID = D.DEPT_ID_DEP
GROUP BY
    D.DEPT_ID_DEP,
    D.DEP_NAME
HAVING
    AVG(E.SALARY) = (
        SELECT
            MAX(AVG_SALARY)
        FROM
            (
                SELECT
                    AVG(SALARY) AS AVG_SALARY
                FROM
                    EMPLOYEES
                GROUP BY
                    DEP_ID
            ) AS DEPARTMENT_AVERAGES
    );

-- ============================================================
-- CHALLENGE 4
-- Show employees earning within the salary range
-- defined for their assigned job.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    J.JOB_TITLE,
    E.SALARY,
    J.MIN_SALARY,
    J.MAX_SALARY
FROM
    EMPLOYEES AS E,
    JOBS AS J
WHERE
    E.JOB_ID = J.JOB_IDENT
    AND E.SALARY BETWEEN J.MIN_SALARY
    AND J.MAX_SALARY
ORDER BY
    E.SALARY DESC;

-- ============================================================
-- CHALLENGE 5
-- Find employees whose salary is above the
-- company average but below the maximum salary
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
    AND E.SALARY > (
        SELECT
            AVG(SALARY)
        FROM
            EMPLOYEES
    )
    AND E.SALARY < J.MAX_SALARY
ORDER BY
    E.SALARY DESC;

-- ============================================================
-- CHALLENGE 6
-- Show the number of employees and average salary
-- for each department.
-- ============================================================
SELECT
    D.DEPT_ID_DEP,
    D.DEP_NAME,
    COUNT(E.EMP_ID) AS EMPLOYEE_COUNT,
    ROUND(AVG(E.SALARY), 2) AS AVG_SALARY
FROM
    EMPLOYEES AS E,
    DEPARTMENTS AS D
WHERE
    E.DEP_ID = D.DEPT_ID_DEP
GROUP BY
    D.DEPT_ID_DEP,
    D.DEP_NAME
ORDER BY
    AVG_SALARY DESC;

-- ============================================================
-- CHALLENGE 7
-- Show each employee with their job history
-- and current job title.
-- ============================================================
SELECT
    E.EMP_ID,
    E.F_NAME,
    E.L_NAME,
    H.START_DATE,
    J.JOB_TITLE,
    E.SALARY
FROM
    EMPLOYEES AS E,
    JOB_HISTORY AS H,
    JOBS AS J
WHERE
    E.EMP_ID = H.EMPL_ID
    AND E.JOB_ID = J.JOB_IDENT
ORDER BY
    H.START_DATE;

-- ============================================================
-- CHALLENGE 8
-- Create a complete employee report using
-- four related tables.
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
    D.DEP_NAME,
    E.SALARY DESC;