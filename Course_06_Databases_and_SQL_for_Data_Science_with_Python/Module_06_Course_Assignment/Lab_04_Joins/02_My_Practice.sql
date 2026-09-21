USE HR;

-- ============================================================
-- Lab 04: Joins
-- My Practice - IBM Practice Problems
-- ============================================================
-- Practice Problem 1
-- Retrieve names, job start dates, and job titles
-- of all employees who work for department number 5.
SELECT
    E.F_NAME,
    E.L_NAME,
    JH.START_DATE,
    J.JOB_TITLE
FROM
    EMPLOYEES AS E
    INNER JOIN JOB_HISTORY AS JH ON E.EMP_ID = JH.EMPL_ID
    INNER JOIN JOBS AS J ON JH.JOBS_ID = J.JOB_IDENT
WHERE
    E.DEP_ID = '5';

-- ============================================================
-- Practice Problem 2
-- Retrieve employee ID, last name, and department ID
-- for all employees, but department names only for
-- employees born before 1980.
SELECT
    E.EMP_ID,
    E.L_NAME,
    E.DEP_ID,
    CASE
        WHEN E.B_DATE < '1980-01-01' THEN D.DEP_NAME
        ELSE NULL
    END AS DEP_NAME
FROM
    EMPLOYEES AS E
    LEFT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID = D.DEPT_ID_DEP;

-- ============================================================
-- Practice Problem 3
-- Retrieve first name and last name of all employees,
-- but department ID and department names only for
-- male employees.
SELECT
    E.F_NAME,
    E.L_NAME,
    CASE
        WHEN E.SEX = 'M' THEN E.DEP_ID
        ELSE NULL
    END AS DEP_ID,
    CASE
        WHEN E.SEX = 'M' THEN D.DEP_NAME
        ELSE NULL
    END AS DEP_NAME
FROM
    EMPLOYEES AS E
    LEFT OUTER JOIN DEPARTMENTS AS D ON E.DEP_ID = D.DEPT_ID_DEP;