-- ============================================================
-- LAB 01 MY PRACTICE: CREATE, ALTER, TRUNCATE, DROP
-- ============================================================
-- ============================================================
-- Practice 1: CREATE TABLE
-- ============================================================
-- Create a new table for employee information
CREATE TABLE EMPLOYEE (
    ID INTEGER NOT NULL,
    NAME TEXT,
    DEPARTMENT TEXT,
    SALARY DECIMAL(10, 2)
);

-- ============================================================
-- Practice 2: INSERT DATA
-- ============================================================
-- Insert employee records
INSERT INTO
    EMPLOYEE
VALUES
    (1, 'Anil', 'Sales', 45000.00),
    (2, 'Beena', 'Marketing', 52000.00),
    (3, 'Charles', 'IT', 60000.00);

-- ============================================================
-- Verify the inserted data
-- ============================================================
SELECT
    *
FROM
    EMPLOYEE;

-- ============================================================
-- Practice 3: ALTER TABLE
-- ============================================================
-- Add a new column for employee city
ALTER TABLE
    EMPLOYEE
ADD
    COLUMN CITY TEXT;

-- Verify the altered table
SELECT
    *
FROM
    EMPLOYEE;

-- ============================================================
-- Practice 4: UPDATE DATA
-- ============================================================
-- Add city values for existing employees
UPDATE
    EMPLOYEE
SET
    CITY = 'Kochi'
WHERE
    ID = 1;

UPDATE
    EMPLOYEE
SET
    CITY = 'Mumbai'
WHERE
    ID = 2;

UPDATE
    EMPLOYEE
SET
    CITY = 'Bengaluru'
WHERE
    ID = 3;

-- Verify the updated data
SELECT
    *
FROM
    EMPLOYEE;

-- ============================================================
-- Practice 5: TRUNCATE TABLE Equivalent
-- ============================================================
-- SQLite does not support TRUNCATE TABLE.
-- DELETE removes all rows but keeps the table structure.
DELETE FROM
    EMPLOYEE;

-- Verify that the table is empty
SELECT
    *
FROM
    EMPLOYEE;

-- ============================================================
-- Practice 6: DROP TABLE
-- ============================================================
-- Delete the EMPLOYEE table completely
DROP TABLE EMPLOYEE;