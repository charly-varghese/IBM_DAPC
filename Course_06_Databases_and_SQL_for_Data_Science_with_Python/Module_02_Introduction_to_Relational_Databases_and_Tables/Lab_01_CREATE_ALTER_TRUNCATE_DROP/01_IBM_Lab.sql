-- ============================================================
-- IBM LAB 01: CREATE, ALTER, TRUNCATE, DROP
-- ============================================================
-- Task 2a: CREATE statement
-- Create PETSALE table
CREATE TABLE PETSALE (
    ID INTEGER NOT NULL,
    PET CHAR(20),
    SALEPRICE DECIMAL(6, 2),
    PROFIT DECIMAL(6, 2),
    SALEDATE DATE
);

-- Create PET table
CREATE TABLE PET (
    ID INTEGER NOT NULL,
    ANIMAL VARCHAR(20),
    QUANTITY INTEGER
);

-- ============================================================
-- Task 2b: INSERT statement
-- ============================================================
-- Insert records into PETSALE
INSERT INTO
    PETSALE
VALUES
    (1, 'Cat', 450.09, 100.47, '2018-05-29'),
    (2, 'Dog', 666.66, 150.76, '2018-06-01'),
    (3, 'Parrot', 50.00, 8.90, '2018-06-04'),
    (4, 'Hamster', 60.60, 12.00, '2018-06-11'),
    (5, 'Goldfish', 48.48, 3.50, '2018-06-14');

-- Insert records into PET
INSERT INTO
    PET
VALUES
    (1, 'Cat', 3),
    (2, 'Dog', 4),
    (3, 'Hamster', 2);

-- Verify PETSALE data
SELECT
    *
FROM
    PETSALE;

-- Verify PET data
SELECT
    *
FROM
    PET;

-- ============================================================
-- Task 3: ALTER statement
-- ============================================================
-- Example 1: Add a new column named QUANTITY
ALTER TABLE
    PETSALE
ADD
    COLUMN QUANTITY INTEGER;

-- Verify the altered table
SELECT
    *
FROM
    PETSALE;

-- Update the QUANTITY values
UPDATE
    PETSALE
SET
    QUANTITY = 9
WHERE
    ID = 1;

UPDATE
    PETSALE
SET
    QUANTITY = 3
WHERE
    ID = 2;

UPDATE
    PETSALE
SET
    QUANTITY = 2
WHERE
    ID = 3;

UPDATE
    PETSALE
SET
    QUANTITY = 6
WHERE
    ID = 4;

UPDATE
    PETSALE
SET
    QUANTITY = 24
WHERE
    ID = 5;

-- Verify the updated table
SELECT
    *
FROM
    PETSALE;

-- ============================================================
-- ALTER TABLE: Delete a column
-- ============================================================
-- Delete the PROFIT column from PETSALE
ALTER TABLE
    PETSALE DROP COLUMN PROFIT;

-- Verify the altered table
SELECT
    *
FROM
    PETSALE;

-- ============================================================
-- Task 4: TRUNCATE statement
-- SQLite equivalent of TRUNCATE TABLE
-- ============================================================
-- Remove all rows from PET without deleting the table
DELETE FROM
    PET;

-- Verify the table is empty
SELECT
    *
FROM
    PET;

-- ============================================================
-- Task 5: DROP statement
-- ============================================================
-- Delete the PET table completely
DROP TABLE PET;