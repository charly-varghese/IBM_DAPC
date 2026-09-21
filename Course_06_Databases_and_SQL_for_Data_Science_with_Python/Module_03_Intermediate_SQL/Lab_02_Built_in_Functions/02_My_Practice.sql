-- ============================================================
-- IBM Data Analyst Professional Certificate
-- Course 06: Databases and SQL for Data Science with Python
-- Module 03: Intermediate SQL
-- Lab 02: Built-in Functions
--
-- MY PRACTICE
-- Database: PETRESCUE.db
-- Engine: SQLite
-- ============================================================
-- ============================================================
-- MY PRACTICE 01
-- Display the total number of rescue records.
-- ============================================================
SELECT
    COUNT(*) AS TOTAL_RESCUES
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 02
-- Display the total number of animals rescued.
-- ============================================================
SELECT
    SUM(QUANTITY) AS TOTAL_ANIMALS_RESCUED
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 03
-- Display the total rescue cost rounded to 2 decimals.
-- ============================================================
SELECT
    ROUND(SUM(COST), 2) AS TOTAL_RESCUE_COST
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 04
-- Display the average number of animals rescued
-- per rescue operation.
-- ============================================================
SELECT
    ROUND(AVG(QUANTITY), 2) AS AVG_ANIMALS_PER_RESCUE
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 05
-- Display the minimum and maximum rescue cost.
-- ============================================================
SELECT
    MIN(COST) AS MIN_RESCUE_COST,
    MAX(COST) AS MAX_RESCUE_COST
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 06
-- Display animal names in uppercase
-- along with the length of each name.
-- ============================================================
SELECT
    ANIMAL,
    UPPER(ANIMAL) AS ANIMAL_UPPERCASE,
    LENGTH(ANIMAL) AS NAME_LENGTH
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 07
-- Display unique animal types in lowercase.
-- ============================================================
SELECT
    DISTINCT LOWER(ANIMAL) AS ANIMAL_NAME
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 08
-- Display rescue ID, original date,
-- day, month, and year.
-- ============================================================
SELECT
    ID,
    RESCUEDATE,
    strftime('%d', RESCUEDATE) AS RESCUE_DAY,
    strftime('%m', RESCUEDATE) AS RESCUE_MONTH,
    strftime('%Y', RESCUEDATE) AS RESCUE_YEAR
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 09
-- Display the date 7 days after each rescue.
-- ============================================================
SELECT
    ID,
    RESCUEDATE,
    date(RESCUEDATE, '+7 days') AS FOLLOW_UP_DATE
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 10
-- Display the date 1 month before each rescue.
-- ============================================================
SELECT
    ID,
    RESCUEDATE,
    date(RESCUEDATE, '-1 month') AS ONE_MONTH_BEFORE
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 11
-- Display the rescue records with costs
-- rounded to the nearest integer.
-- ============================================================
SELECT
    ID,
    ANIMAL,
    COST,
    ROUND(COST) AS ROUNDED_COST
FROM
    PETRESCUE;

-- ============================================================
-- MY PRACTICE 12
-- Find the total rescue cost for dogs.
-- ============================================================
SELECT
    ROUND(SUM(COST), 2) AS TOTAL_DOG_RESCUE_COST
FROM
    PETRESCUE
WHERE
    LOWER(ANIMAL) = 'dog';

-- ============================================================
-- MY PRACTICE 13
-- Find the total number of animals rescued
-- for each animal type.
-- ============================================================
SELECT
    ANIMAL,
    SUM(QUANTITY) AS TOTAL_ANIMALS
FROM
    PETRESCUE
GROUP BY
    ANIMAL;

-- ============================================================
-- MY PRACTICE 14
-- Display the average rescue cost
-- for each animal type.
-- ============================================================
SELECT
    ANIMAL,
    ROUND(AVG(COST), 2) AS AVG_RESCUE_COST
FROM
    PETRESCUE
GROUP BY
    ANIMAL;

-- ============================================================
-- END OF MY PRACTICE
-- ============================================================