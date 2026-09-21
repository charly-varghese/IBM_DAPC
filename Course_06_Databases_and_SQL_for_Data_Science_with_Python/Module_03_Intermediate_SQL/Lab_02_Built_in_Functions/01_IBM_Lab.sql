-- ============================================================
-- IBM Data Analyst Professional Certificate
-- Course 06: Databases and SQL for Data Science with Python
-- Module 03: Intermediate SQL
-- Lab 02: Built-in Functions
--
-- Database: PETRESCUE.db
-- Engine: SQLite
--
-- IBM Concepts Adapted from MySQL to SQLite
-- ============================================================


-- ============================================================
-- PART 1: AGGREGATION FUNCTIONS
-- ============================================================


-- Query 1:
-- Calculate the total cost of all animal rescues.
SELECT
    SUM(COST) AS SUM_OF_COST
FROM
    PETRESCUE;


-- Query 2:
-- Display the maximum quantity of animals rescued.
SELECT
    MAX(QUANTITY) AS MAX_QUANTITY
FROM
    PETRESCUE;


-- Query 3:
-- Display the minimum quantity of animals rescued.
SELECT
    MIN(QUANTITY) AS MIN_QUANTITY
FROM
    PETRESCUE;


-- Query 4:
-- Display the average rescue cost.
SELECT
    AVG(COST) AS AVG_COST
FROM
    PETRESCUE;


-- ============================================================
-- PART 2: SCALAR FUNCTIONS
-- ============================================================


-- Query 5:
-- Display the rounded integral cost of each rescue.
SELECT
    ID,
    COST,
    ROUND(COST) AS ROUNDED_COST
FROM
    PETRESCUE;


-- Query 6:
-- Display the rescue cost rounded to 2 decimal places.
SELECT
    ID,
    COST,
    ROUND(COST, 2) AS COST_2_DECIMALS
FROM
    PETRESCUE;


-- ============================================================
-- PART 3: STRING FUNCTIONS
-- ============================================================


-- Query 7:
-- Display the length of each animal name.
SELECT
    ANIMAL,
    LENGTH(ANIMAL) AS NAME_LENGTH
FROM
    PETRESCUE;


-- Query 8:
-- Display each animal name in uppercase.
-- IBM MySQL: UCASE()
-- SQLite: UPPER()
SELECT
    ANIMAL,
    UPPER(ANIMAL) AS ANIMAL_UPPERCASE
FROM
    PETRESCUE;


-- Query 9:
-- Display each animal name in lowercase.
-- IBM MySQL: LCASE()
-- SQLite: LOWER()
SELECT
    ANIMAL,
    LOWER(ANIMAL) AS ANIMAL_LOWERCASE
FROM
    PETRESCUE;


-- ============================================================
-- PART 4: DATE FUNCTIONS
-- ============================================================


-- Query 10:
-- Display the day part of each rescue date.
-- IBM MySQL: DAY(RESCUEDATE)
-- SQLite: strftime('%d', RESCUEDATE)
SELECT
    RESCUEDATE,
    strftime('%d', RESCUEDATE) AS RESCUE_DAY
FROM
    PETRESCUE;


-- Query 11:
-- Display the month part of each rescue date.
-- IBM MySQL: MONTH(RESCUEDATE)
-- SQLite: strftime('%m', RESCUEDATE)
SELECT
    RESCUEDATE,
    strftime('%m', RESCUEDATE) AS RESCUE_MONTH
FROM
    PETRESCUE;


-- Query 12:
-- Display the year part of each rescue date.
-- IBM MySQL: YEAR(RESCUEDATE)
-- SQLite: strftime('%Y', RESCUEDATE)
SELECT
    RESCUEDATE,
    strftime('%Y', RESCUEDATE) AS RESCUE_YEAR
FROM
    PETRESCUE;


-- Query 13:
-- Animals rescued should see the vet within 3 days.
-- Display the third day after each rescue.
--
-- IBM MySQL:
-- DATE_ADD(RESCUEDATE, INTERVAL 3 DAY)
--
-- SQLite:
SELECT
    ID,
    RESCUEDATE,
    date(
        RESCUEDATE,
        '+3 days'
    ) AS VET_DATE
FROM
    PETRESCUE;


-- Query 14:
-- Display the date 2 months after each rescue.
SELECT
    ID,
    RESCUEDATE,
    date(
        RESCUEDATE,
        '+2 months'
    ) AS DATE_PLUS_2_MONTHS
FROM
    PETRESCUE;


-- Query 15:
-- Display the date 3 days before each rescue.
SELECT
    ID,
    RESCUEDATE,
    date(
        RESCUEDATE,
        '-3 days'
    ) AS DATE_MINUS_3_DAYS
FROM
    PETRESCUE;


-- Query 16:
-- Display the number of days between
-- the current date and the rescue date.
--
-- IBM MySQL:
-- DATEDIFF(CURRENT_DATE, RESCUEDATE)
--
-- SQLite:
SELECT
    ID,
    RESCUEDATE,
    CAST(
        julianday('now')
        -
        julianday(RESCUEDATE)
        AS INTEGER
    ) AS DAYS_SINCE_RESCUE
FROM
    PETRESCUE;


-- ============================================================
-- PART 5: IBM PRACTICE QUESTIONS
-- ============================================================


-- Query 17:
-- Display the average cost of rescuing a single dog.
--
-- Cost per dog may vary by rescue.
-- Therefore:
-- Average rescue cost / quantity
-- for each Dog rescue, then average the result.
SELECT
    AVG(
        COST * 1.0 / QUANTITY
    ) AS AVG_COST_PER_DOG
FROM
    PETRESCUE
WHERE
    LOWER(ANIMAL) = 'dog';


-- Query 18:
-- Display the animal name in each rescue
-- in uppercase without duplicates.
SELECT DISTINCT
    UPPER(ANIMAL) AS ANIMAL_NAME
FROM
    PETRESCUE;


-- Query 19:
-- Display all columns where the rescued animals are cats.
-- Use 'cat' in lowercase in the query.
SELECT
    *
FROM
    PETRESCUE
WHERE
    LOWER(ANIMAL) = 'cat';


-- Query 20:
-- Display the number of rescues
-- in the 5th month.
SELECT
    COUNT(*) AS NUMBER_OF_RESCUES
FROM
    PETRESCUE
WHERE
    strftime('%m', RESCUEDATE) = '05';


-- Query 21:
-- Display the ID and target date.
--
-- Animals should find homes within 1 year
-- of their rescue date.
SELECT
    ID,
    RESCUEDATE,
    date(
        RESCUEDATE,
        '+1 year'
    ) AS TARGET_DATE
FROM
    PETRESCUE;


-- ============================================================
-- END OF IBM LAB
-- ============================================================
