-- ============================================================
-- IBM Data Analyst Professional Certificate
-- Course 06: Databases and SQL for Data Science with Python
-- Module 03: Intermediate SQL
-- Lab 01: String Patterns, Sorting and Grouping
--
-- File: 02_My_Practice.sql
-- ============================================================
-- ============================================================
-- MY PRACTICE 01
-- Find employees whose first name contains the letter 'a'.
-- ============================================================
SELECT
    F_NAME,
    L_NAME
FROM
    EMPLOYEES
WHERE
    F_NAME LIKE '%a%';

-- ============================================================
-- MY PRACTICE 02
-- Find employees whose address ends with 'IL'.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    ADDRESS
FROM
    EMPLOYEES
WHERE
    ADDRESS LIKE '%IL';

-- ============================================================
-- MY PRACTICE 03
-- Find employees with salaries between 60000 and 80000.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    SALARY
FROM
    EMPLOYEES
WHERE
    SALARY BETWEEN 60000
    AND 80000;

-- ============================================================
-- MY PRACTICE 04
-- Find employees in Department 5 with a salary
-- greater than or equal to 60000.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    SALARY,
    DEP_ID
FROM
    EMPLOYEES
WHERE
    DEP_ID = 5
    AND SALARY >= 60000;

-- ============================================================
-- MY PRACTICE 05
-- Sort employees by salary from highest to lowest.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    SALARY
FROM
    EMPLOYEES
ORDER BY
    SALARY DESC;

-- ============================================================
-- MY PRACTICE 06
-- Sort employees by Department ID in ascending order
-- and salary in descending order.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    DEP_ID,
    SALARY
FROM
    EMPLOYEES
ORDER BY
    DEP_ID ASC,
    SALARY DESC;

-- ============================================================
-- MY PRACTICE 07
-- Display the total number of employees.
-- ============================================================
SELECT
    COUNT(*) AS TOTAL_EMPLOYEES
FROM
    EMPLOYEES;

-- ============================================================
-- MY PRACTICE 08
-- Display the minimum and maximum employee salary.
-- ============================================================
SELECT
    MIN(SALARY) AS MIN_SALARY,
    MAX(SALARY) AS MAX_SALARY
FROM
    EMPLOYEES;

-- ============================================================
-- MY PRACTICE 09
-- Display the total salary paid to all employees.
-- ============================================================
SELECT
    SUM(SALARY) AS TOTAL_SALARY
FROM
    EMPLOYEES;

-- ============================================================
-- MY PRACTICE 10
-- Display the overall average employee salary.
-- ============================================================
SELECT
    AVG(SALARY) AS OVERALL_AVG_SALARY
FROM
    EMPLOYEES;

-- ============================================================
-- MY PRACTICE 11
-- Group employees by department and display:
-- department ID,
-- number of employees,
-- total salary,
-- average salary.
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    SUM(SALARY) AS TOTAL_SALARY,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID;

-- ============================================================
-- MY PRACTICE 12
-- Display departments where the average salary
-- is greater than 65000.
-- ============================================================
SELECT
    DEP_ID,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    AVG(SALARY) > 65000;

-- ============================================================
-- MY PRACTICE 13
-- Display departments with at least 3 employees.
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    COUNT(*) >= 3;

-- ============================================================
-- MY PRACTICE 14
-- Display departments where the total salary
-- is greater than 200000.
-- Sort by total salary from highest to lowest.
-- ============================================================
SELECT
    DEP_ID,
    SUM(SALARY) AS TOTAL_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    SUM(SALARY) > 200000
ORDER BY
    TOTAL_SALARY DESC;