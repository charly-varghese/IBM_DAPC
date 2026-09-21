-- ==================================================
-- MY PRACTICE
-- LAB 03: SUB-QUERIES AND NESTED SELECTS
-- ==================================================


-- --------------------------------------------------
-- PRACTICE 01
-- Find employees earning more than the average salary
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY
FROM EMPLOYEES
WHERE SALARY > (
    SELECT AVG(SALARY)
    FROM EMPLOYEES
);


-- --------------------------------------------------
-- PRACTICE 02
-- Find employees earning the maximum salary
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY
FROM EMPLOYEES
WHERE SALARY = (
    SELECT MAX(SALARY)
    FROM EMPLOYEES
);


-- --------------------------------------------------
-- PRACTICE 03
-- Find employees earning the minimum salary
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY
FROM EMPLOYEES
WHERE SALARY = (
    SELECT MIN(SALARY)
    FROM EMPLOYEES
);


-- --------------------------------------------------
-- PRACTICE 04
-- Find employees whose salary is above
-- their department's average salary
--
-- Correlated Subquery
-- --------------------------------------------------

SELECT
    E1.EMP_ID,
    E1.F_NAME,
    E1.L_NAME,
    E1.DEP_ID,
    E1.SALARY
FROM EMPLOYEES AS E1
WHERE E1.SALARY > (
    SELECT AVG(E2.SALARY)
    FROM EMPLOYEES AS E2
    WHERE E2.DEP_ID = E1.DEP_ID
);


-- --------------------------------------------------
-- PRACTICE 05
-- Find employees who work in departments
-- that have more than one employee
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    DEP_ID
FROM EMPLOYEES
WHERE DEP_ID IN (
    SELECT DEP_ID
    FROM EMPLOYEES
    GROUP BY DEP_ID
    HAVING COUNT(*) > 1
);


-- --------------------------------------------------
-- PRACTICE 06
-- Display employees whose salary belongs to
-- the top 3 highest salaries
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY
FROM EMPLOYEES
WHERE SALARY IN (
    SELECT SALARY
    FROM EMPLOYEES
    ORDER BY SALARY DESC
    LIMIT 3
);


-- --------------------------------------------------
-- PRACTICE 07
-- Find employees whose birth date is earlier
-- than the average birth date
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    B_DATE
FROM EMPLOYEES
WHERE julianday(B_DATE) < (
    SELECT AVG(julianday(B_DATE))
    FROM EMPLOYEES
);


-- --------------------------------------------------
-- PRACTICE 08
-- Show each employee with:
-- Employee Salary
-- Company Average Salary
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY,

    (
        SELECT ROUND(AVG(SALARY), 2)
        FROM EMPLOYEES
    ) AS COMPANY_AVG_SALARY

FROM EMPLOYEES;


-- --------------------------------------------------
-- PRACTICE 09
-- Find the average salary of the top 3 earners
-- --------------------------------------------------

SELECT AVG(SALARY) AS AVG_TOP_3_SALARIES
FROM (
    SELECT SALARY
    FROM EMPLOYEES
    ORDER BY SALARY DESC
    LIMIT 3
) AS TOP_3_SALARIES;


-- --------------------------------------------------
-- PRACTICE 10
-- Find employees earning less than the
-- average salary of the top 5 earners
-- --------------------------------------------------

SELECT
    EMP_ID,
    F_NAME,
    L_NAME,
    SALARY
FROM EMPLOYEES
WHERE SALARY < (

    SELECT AVG(SALARY)
    FROM (
        SELECT SALARY
        FROM EMPLOYEES
        ORDER BY SALARY DESC
        LIMIT 5
    ) AS TOP_5_SALARIES

);
