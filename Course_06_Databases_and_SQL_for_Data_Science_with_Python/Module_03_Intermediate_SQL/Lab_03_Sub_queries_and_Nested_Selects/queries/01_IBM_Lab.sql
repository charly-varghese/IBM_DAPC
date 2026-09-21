-- ==================================================
-- IBM LAB 03: SUB-QUERIES AND NESTED SELECTS
-- SQLite Adapted Practice
-- ==================================================
-- --------------------------------------------------
-- QUERY 1
-- Find employees earning less than the average salary
-- --------------------------------------------------
SELECT
    *
FROM
    EMPLOYEES
WHERE
    SALARY < (
        SELECT
            AVG(SALARY)
        FROM
            EMPLOYEES
    );

-- --------------------------------------------------
-- QUERY 2
-- Display each employee's ID and salary along with
-- the maximum salary in the company
-- --------------------------------------------------
SELECT
    EMP_ID,
    SALARY,
    (
        SELECT
            MAX(SALARY)
        FROM
            EMPLOYEES
    ) AS MAX_SALARY
FROM
    EMPLOYEES;

-- --------------------------------------------------
-- QUERY 3
-- Find the first and last name of the oldest employee
-- --------------------------------------------------
SELECT
    F_NAME,
    L_NAME
FROM
    EMPLOYEES
WHERE
    B_DATE = (
        SELECT
            MIN(B_DATE)
        FROM
            EMPLOYEES
    );

-- --------------------------------------------------
-- QUERY 4
-- Find the average salary of the top 5 earners
-- --------------------------------------------------
SELECT
    AVG(SALARY) AS AVG_TOP_5_SALARIES
FROM
    (
        SELECT
            SALARY
        FROM
            EMPLOYEES
        ORDER BY
            SALARY DESC
        LIMIT
            5
    ) AS SALARY_TABLE;

-- ==================================================
-- IBM PRACTICE QUESTIONS
-- ==================================================
-- --------------------------------------------------
-- PRACTICE 1
-- Find the average salary of the five least-earning
-- employees
-- --------------------------------------------------
SELECT
    AVG(SALARY) AS AVG_BOTTOM_5_SALARIES
FROM
    (
        SELECT
            SALARY
        FROM
            EMPLOYEES
        ORDER BY
            SALARY ASC
        LIMIT
            5
    ) AS LOWEST_SALARIES;

-- --------------------------------------------------
-- PRACTICE 2
-- Find employees older than the average age
-- of all employees
--
-- SQLite Adaptation:
-- julianday() is used for date calculations.
-- --------------------------------------------------
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    B_DATE,
    ROUND(
        (julianday('now') - julianday(B_DATE)) / 365.25,
        1
    ) AS AGE
FROM
    EMPLOYEES
WHERE
    (julianday('now') - julianday(B_DATE)) > (
        SELECT
            AVG(
                julianday('now') - julianday(B_DATE)
            )
        FROM
            EMPLOYEES
    );

-- --------------------------------------------------
-- PRACTICE 3
-- From JOB_HISTORY, display:
-- Employee ID
-- Years of Service
-- Average Years of Service
--
-- SQLite Adaptation:
-- Current date is calculated using julianday().
-- --------------------------------------------------
SELECT
    EMPL_ID,
    ROUND(
        (julianday('now') - julianday(START_DATE)) / 365.25,
        1
    ) AS YEARS_OF_SERVICE,
    (
        SELECT
            ROUND(
                AVG(
                    (julianday('now') - julianday(START_DATE)) / 365.25
                ),
                1
            )
        FROM
            JOB_HISTORY
    ) AS AVG_YEARS_OF_SERVICE
FROM
    JOB_HISTORY;