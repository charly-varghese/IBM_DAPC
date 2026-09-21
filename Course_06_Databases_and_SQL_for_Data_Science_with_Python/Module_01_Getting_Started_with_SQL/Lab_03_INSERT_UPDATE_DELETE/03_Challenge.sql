-- ============================================================
-- LAB 03 CHALLENGES: INSERT, UPDATE, DELETE
-- ============================================================
-- Challenge 1: INSERT
-- Insert a new instructor
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
        10,
        'Mathew',
        'Alex',
        'Kochi',
        'IN'
    );

-- Verify Challenge 1
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 10;

-- Challenge 2: UPDATE
-- Update the instructor's city
UPDATE
    Instructor
SET
    city = 'Chennai'
WHERE
    ins_id = 10;

-- Verify Challenge 2
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 10;

-- Challenge 3: UPDATE Multiple Columns
-- Update both city and country
UPDATE
    Instructor
SET
    city = 'Dubai',
    country = 'AE'
WHERE
    ins_id = 10;

-- Verify Challenge 3
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 10;

-- Challenge 4: INSERT Multiple Rows
-- Add two more instructors
INSERT INTO
    Instructor (
        ins_id,
        lastname,
        firstname,
        city,
        country
    )
VALUES
    (11, 'Kumar', 'Raj', 'Mumbai', 'IN'),
    (12, 'Smith', 'David', 'London', 'UK');

-- Verify Challenge 4
SELECT
    *
FROM
    Instructor
WHERE
    ins_id IN (10, 11, 12);

-- Challenge 5: DELETE
-- Delete instructor ID 11
DELETE FROM
    Instructor
WHERE
    ins_id = 11;

-- Final Verification
SELECT
    *
FROM
    Instructor
WHERE
    ins_id IN (10, 11, 12);