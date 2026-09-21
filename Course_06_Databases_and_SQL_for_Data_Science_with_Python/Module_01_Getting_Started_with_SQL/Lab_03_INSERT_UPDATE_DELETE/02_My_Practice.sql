-- ============================================================
-- LAB 03 MY PRACTICE: INSERT, UPDATE, DELETE
-- ============================================================
-- Practice 1: INSERT
-- Insert a new instructor record
INSERT INTO
    Instructor (
        ins_id,
        lastname,
        firstname,
        city,
        country
    )
VALUES
    (
        7,
        'Thomas',
        'George',
        'Kochi',
        'IN'
    );

-- Verify Practice 1
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 7;

-- Practice 2: INSERT Multiple Rows
-- Insert two additional instructor records
INSERT INTO
    Instructor (
        ins_id,
        lastname,
        firstname,
        city,
        country
    )
VALUES
    (8, 'Varghese', 'Paul', 'Mumbai', 'IN'),
    (9, 'Joseph', 'Anna', 'Delhi', 'IN');

-- Verify Practice 2
SELECT
    *
FROM
    Instructor
WHERE
    country = 'IN';

-- Practice 3: UPDATE
-- Update the city of instructor ID 7
UPDATE
    Instructor
SET
    city = 'Bengaluru'
WHERE
    ins_id = 7;

-- Verify Practice 3
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 7;

-- Practice 4: UPDATE Multiple Columns
-- Update city and country of instructor ID 8
UPDATE
    Instructor
SET
    city = 'London',
    country = 'UK'
WHERE
    ins_id = 8;

-- Verify Practice 4
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 8;

-- Practice 5: DELETE
-- Delete instructor ID 9
DELETE FROM
    Instructor
WHERE
    ins_id = 9;

-- Verify Practice 5
SELECT
    *
FROM
    Instructor
WHERE
    ins_id IN (7, 8, 9);