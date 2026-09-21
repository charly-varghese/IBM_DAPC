-- ============================================================
-- IBM Data Analyst Professional Certificate
-- Course 06: Databases and SQL for Data Science with Python
-- Module 03: Intermediate SQL
-- Lab 01: String Patterns, Sorting and Grouping
--
-- File: 03_Challenge.sql
-- ============================================================
-- ============================================================
-- CHALLENGE 01
-- Find employees whose first name starts with 'A'
-- and display their name, salary, and department.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    SALARY,
    DEP_ID
FROM
    EMPLOYEES
WHERE
    F_NAME LIKE 'A%';

-- ============================================================
-- CHALLENGE 02
-- Find employees born between 1975 and 1985 inclusive.
--
-- Since dates are stored in YYYY-MM-DD format,
-- use a date range for accurate filtering.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    B_DATE
FROM
    EMPLOYEES
WHERE
    B_DATE BETWEEN '1975-01-01'
    AND '1985-12-31'
ORDER BY
    B_DATE ASC;

-- ============================================================
-- CHALLENGE 03
-- Find employees with salaries between 65000 and 90000.
-- Sort results by salary from highest to lowest.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    SALARY
FROM
    EMPLOYEES
WHERE
    SALARY BETWEEN 65000
    AND 90000
ORDER BY
    SALARY DESC;

-- ============================================================
-- CHALLENGE 04
-- Display employees from Department 7.
-- Sort by salary from highest to lowest,
-- then by last name in ascending order.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    SALARY,
    DEP_ID
FROM
    EMPLOYEES
WHERE
    DEP_ID = 7
ORDER BY
    SALARY DESC,
    L_NAME ASC;

-- ============================================================
-- CHALLENGE 05
-- Create a department salary summary showing:
-- Department ID
-- Number of employees
-- Minimum salary
-- Maximum salary
-- Average salary
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    MIN(SALARY) AS MIN_SALARY,
    MAX(SALARY) AS MAX_SALARY,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID;

-- ============================================================
-- CHALLENGE 06
-- Find departments where:
-- The average salary is greater than 65000.
--
-- Sort by average salary from highest to lowest.
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    AVG(SALARY) > 65000
ORDER BY
    AVG_SALARY DESC;

-- ============================================================
-- CHALLENGE 07
-- Find departments where:
-- Total salary is greater than or equal to 250000.
--
-- Display:
-- Department ID
-- Employee count
-- Total salary
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    SUM(SALARY) AS TOTAL_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    SUM(SALARY) >= 250000
ORDER BY
    TOTAL_SALARY DESC;

-- ============================================================
-- CHALLENGE 08
-- Find the department with the highest average salary.
--
-- First create grouped department summaries,
-- then sort by average salary from highest to lowest.
--
-- Use LIMIT to return only the top department.
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
ORDER BY
    AVG_SALARY DESC
LIMIT
    1;