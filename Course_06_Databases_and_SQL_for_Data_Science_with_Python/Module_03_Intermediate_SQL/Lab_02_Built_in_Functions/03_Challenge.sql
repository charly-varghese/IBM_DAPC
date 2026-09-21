-- ============================================================
-- IBM Data Analyst Professional Certificate
-- Course 06: Databases and SQL for Data Science with Python
-- Module 03: Intermediate SQL
-- Lab 02: Built-in Functions
--
-- CHALLENGE QUERIES
-- Database: PETRESCUE.db
-- Engine: SQLite
-- ============================================================
-- ============================================================
-- CHALLENGE 01
-- Display the total number of animals rescued
-- and the total rescue cost.
-- ============================================================
SELECT
    SUM(QUANTITY) AS TOTAL_ANIMALS,
    ROUND(SUM(COST), 2) AS TOTAL_COST
FROM
    PETRESCUE;

-- ============================================================
-- CHALLENGE 02
-- Find the rescue with the highest cost.
-- Display the ID, animal, quantity, and cost.
-- ============================================================
SELECT
    ID,
    ANIMAL,
    QUANTITY,
    COST
FROM
    PETRESCUE
ORDER BY
    COST DESC
LIMIT
    1;

-- ============================================================
-- CHALLENGE 03
-- Find the rescue with the lowest cost.
-- Display the ID, animal, quantity, and cost.
-- ============================================================
SELECT
    ID,
    ANIMAL,
    QUANTITY,
    COST
FROM
    PETRESCUE
ORDER BY
    COST ASC
LIMIT
    1;

-- ============================================================
-- CHALLENGE 04
-- Display each animal type and:
-- Number of rescue records
-- Total animals rescued
-- Total rescue cost
-- ============================================================
SELECT
    ANIMAL,
    COUNT(*) AS NUMBER_OF_RESCUES,
    SUM(QUANTITY) AS TOTAL_ANIMALS,
    ROUND(SUM(COST), 2) AS TOTAL_COST
FROM
    PETRESCUE
GROUP BY
    ANIMAL;

-- ============================================================
-- CHALLENGE 05
-- Display animal types where the total rescue cost
-- is greater than 200.
-- Sort by total cost from highest to lowest.
-- ============================================================
SELECT
    ANIMAL,
    ROUND(SUM(COST), 2) AS TOTAL_COST
FROM
    PETRESCUE
GROUP BY
    ANIMAL
HAVING
    SUM(COST) > 200
ORDER BY
    TOTAL_COST DESC;

-- ============================================================
-- CHALLENGE 06
-- Display each rescue with the animal name in uppercase
-- and the cost rounded to the nearest whole number.
-- ============================================================
SELECT
    ID,
    UPPER(ANIMAL) AS ANIMAL_NAME,
    ROUND(COST) AS ROUNDED_COST
FROM
    PETRESCUE;

-- ============================================================
-- CHALLENGE 07
-- Display rescue ID, animal, rescue date,
-- and the follow-up date 14 days after rescue.
-- ============================================================
SELECT
    ID,
    ANIMAL,
    RESCUEDATE,
    date(RESCUEDATE, '+14 days') AS FOLLOW_UP_DATE
FROM
    PETRESCUE;

-- ============================================================
-- CHALLENGE 08
-- Count how many rescues happened in June 2018.
-- ============================================================
SELECT
    COUNT(*) AS JUNE_2018_RESCUES
FROM
    PETRESCUE
WHERE
    strftime('%Y-%m', RESCUEDATE) = '2018-06';

-- ============================================================
-- CHALLENGE 09
-- Find the average rescue cost per animal type.
-- Display only animal types where the average cost
-- is greater than 100.
-- ============================================================
SELECT
    ANIMAL,
    ROUND(AVG(COST), 2) AS AVG_COST
FROM
    PETRESCUE
GROUP BY
    ANIMAL
HAVING
    AVG(COST) > 100
ORDER BY
    AVG_COST DESC;

-- ============================================================
-- CHALLENGE 10
-- Create a complete rescue summary.
--
-- Display:
-- Total rescue records
-- Total animals rescued
-- Average rescue cost
-- Minimum rescue cost
-- Maximum rescue cost
-- ============================================================
SELECT
    COUNT(*) AS TOTAL_RESCUE_RECORDS,
    SUM(QUANTITY) AS TOTAL_ANIMALS_RESCUED,
    ROUND(AVG(COST), 2) AS AVG_RESCUE_COST,
    ROUND(MIN(COST), 2) AS MIN_RESCUE_COST,
    ROUND(MAX(COST), 2) AS MAX_RESCUE_COST
FROM
    PETRESCUE;

-- ============================================================
-- END OF CHALLENGES
-- ============================================================