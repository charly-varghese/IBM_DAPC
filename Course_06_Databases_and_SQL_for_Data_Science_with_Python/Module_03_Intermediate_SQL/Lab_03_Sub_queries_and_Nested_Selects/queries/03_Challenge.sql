-- ==================================================
-- CHALLENGE QUERIES
-- LAB 03: SUB-QUERIES AND NESTED SELECTS
-- ==================================================
-- --------------------------------------------------
-- CHALLENGE 01
-- Find the second highest salary
-- --------------------------------------------------
SELECT
    MAX(SALARY) AS SECOND_HIGHEST_SALARY
FROM
    EMPLOYEES
WHERE
    SALARY < (
        SELECT
            MAX(SALARY)
        FROM
            EMPLOYEES
    );

-- --------------------------------------------------
-- CHALLENGE 02
-- Find employees earning the second highest salary
-- --------------------------------------------------
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY
FROM
    EMPLOYEES
WHERE
    SALARY = (
        SELECT
            MAX(SALARY)
        FROM
            EMPLOYEES
        WHERE
            SALARY < (
                SELECT
                    MAX(SALARY)
                FROM
                    EMPLOYEES
            )
    );

-- --------------------------------------------------
-- CHALLENGE 03
-- Find the department with the highest
-- average employee salary
-- --------------------------------------------------
SELECT
    DEP_ID,
    AVG(SALARY) AS AVG_DEPARTMENT_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    AVG(SALARY) = (
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

-- --------------------------------------------------
-- CHALLENGE 04
-- Find employees earning more than
-- their department average salary
-- --------------------------------------------------
SELECT
    E1.EMP_ID,
    E1.F_NAME,
    E1.L_NAME,
    E1.DEP_ID,
    E1.SALARY
FROM
    EMPLOYEES AS E1
WHERE
    E1.SALARY > (
        SELECT
            AVG(E2.SALARY)
        FROM
            EMPLOYEES AS E2
        WHERE
            E2.DEP_ID = E1.DEP_ID
    );

-- --------------------------------------------------
-- CHALLENGE 05
-- Find employees who earn more than
-- the overall average salary but less than
-- the maximum salary
-- --------------------------------------------------
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY
FROM
    EMPLOYEES
WHERE
    SALARY > (
        SELECT
            AVG(SALARY)
        FROM
            EMPLOYEES
    )
    AND SALARY < (
        SELECT
            MAX(SALARY)
        FROM
            EMPLOYEES
    );

-- --------------------------------------------------
-- CHALLENGE 06
-- Find the oldest employee
-- and display their age
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
    B_DATE = (
        SELECT
            MIN(B_DATE)
        FROM
            EMPLOYEES
    );

-- --------------------------------------------------
-- CHALLENGE 07
-- Find the newest employee based on
-- the most recent birth date
-- --------------------------------------------------
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    B_DATE
FROM
    EMPLOYEES
WHERE
    B_DATE = (
        SELECT
            MAX(B_DATE)
        FROM
            EMPLOYEES
    );

-- --------------------------------------------------
-- CHALLENGE 08
-- Find employees whose salary is higher
-- than the average salary of employees
-- in department 5
-- --------------------------------------------------
SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    DEP_ID,
    SALARY
FROM
    EMPLOYEES
WHERE
    SALARY > (
        SELECT
            AVG(SALARY)
        FROM
            EMPLOYEES
        WHERE
            DEP_ID = '5'
    );