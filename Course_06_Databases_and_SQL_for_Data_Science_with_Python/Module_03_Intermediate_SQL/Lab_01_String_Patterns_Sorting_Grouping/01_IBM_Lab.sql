-- ============================================================
-- IBM Data Analyst Professional Certificate
-- Course 06: Databases and SQL for Data Science with Python
-- Module 03: Intermediate SQL
-- Lab 01: String Patterns, Sorting and Grouping
-- ============================================================
-- ============================================================
-- PART 1: STRING PATTERNS
-- ============================================================
-- Query 1:
-- Retrieve first and last names of employees
-- whose address contains 'Elgin,IL'.
SELECT
    F_NAME,
    L_NAME
FROM
    EMPLOYEES
WHERE
    ADDRESS LIKE '%Elgin,IL%';

-- ============================================================
-- Query 2:
-- Retrieve first and last names of employees
-- who were born during the 1970s.
-- ============================================================
SELECT
    F_NAME,
    L_NAME
FROM
    EMPLOYEES
WHERE
    B_DATE LIKE '197%';

-- ============================================================
-- PART 2: RANGE FILTERING
-- ============================================================
-- Query 3:
-- Retrieve all employee records where:
-- Salary is between 60000 and 70000
-- AND Department ID is 5.
SELECT
    *
FROM
    EMPLOYEES
WHERE
    (
        SALARY BETWEEN 60000
        AND 70000
    )
    AND DEP_ID = 5;

-- ============================================================
-- PART 3: SORTING
-- ============================================================
-- Query 4:
-- Retrieve employee first name, last name, and department ID.
-- Sort the results by department ID in ascending order.
SELECT
    F_NAME,
    L_NAME,
    DEP_ID
FROM
    EMPLOYEES
ORDER BY
    DEP_ID;

-- ============================================================
-- Query 5:
-- Sort employees by Department ID in descending order.
-- Within each department, sort by Last Name in descending order.
-- ============================================================
SELECT
    F_NAME,
    L_NAME,
    DEP_ID
FROM
    EMPLOYEES
ORDER BY
    DEP_ID DESC,
    L_NAME DESC;

-- ============================================================
-- PART 4: GROUPING
-- ============================================================
-- Query 6:
-- Retrieve each department ID and the number of employees
-- in that department.
SELECT
    DEP_ID,
    COUNT(*)
FROM
    EMPLOYEES
GROUP BY
    DEP_ID;

-- ============================================================
-- Query 7:
-- Retrieve each department ID, the number of employees,
-- and the average employee salary for each department.
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*),
    AVG(SALARY)
FROM
    EMPLOYEES
GROUP BY
    DEP_ID;

-- ============================================================
-- Query 8:
-- Use aliases to label the computed columns.
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS "NUM_EMPLOYEES",
    AVG(SALARY) AS "AVG_SALARY"
FROM
    EMPLOYEES
GROUP BY
    DEP_ID;

-- ============================================================
-- Query 9:
-- Group employees by department and sort the results
-- by average salary in ascending order.
-- ============================================================
SELECT
    DEP_ID,
    COUNT(*) AS "NUM_EMPLOYEES",
    AVG(SALARY) AS "AVG_SALARY"
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
ORDER BY
    AVG_SALARY;

-- ============================================================
-- PART 5: HAVING
-- ============================================================
-- Query 10:
-- Retrieve department ID, number of employees,
-- and average salary.
-- Show only departments with fewer than 4 employees.
-- Sort results by average salary.
SELECT
    DEP_ID,
    COUNT(*) AS "NUM_EMPLOYEES",
    AVG(SALARY) AS "AVG_SALARY"
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    COUNT(*) < 4
ORDER BY
    AVG_SALARY;

-- ============================================================
-- IBM PRACTICE QUESTIONS
-- ============================================================
-- Practice Question 1:
-- Retrieve first and last names of employees
-- whose first names start with 'S'.
SELECT
    F_NAME,
    L_NAME
FROM
    EMPLOYEES
WHERE
    F_NAME LIKE 'S%';

-- ============================================================
-- Practice Question 2:
-- Retrieve all employee records ordered by
-- date of birth in ascending order.
-- ============================================================
SELECT
    *
FROM
    EMPLOYEES
ORDER BY
    B_DATE ASC;

-- ============================================================
-- Practice Question 3:
-- Group employees by department.
-- Display the department ID and average salary.
-- Show only departments where the average salary
-- is greater than or equal to 60000.
-- ============================================================
SELECT
    DEP_ID,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    AVG(SALARY) >= 60000;

-- ============================================================
-- Practice Question 4:
-- Group employees by department.
-- Display the department ID and average salary.
-- Show only departments where the average salary
-- is greater than or equal to 60000.
-- Sort the results by average salary in descending order.
-- ============================================================
SELECT
    DEP_ID,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
HAVING
    AVG(SALARY) >= 60000
ORDER BY
    AVG_SALARY DESC;