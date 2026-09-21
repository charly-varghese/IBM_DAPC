-- ============================================================
-- IBM LAB 03: INSERT, UPDATE, DELETE
-- ============================================================
-- Example 1: Insert a single instructor record
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
        4,
        'Saha',
        'Sandip',
        'Edmonton',
        'CA'
    );

-- Verify the inserted record
SELECT
    *
FROM
    Instructor;

-- Example 2: Insert multiple instructor records
INSERT INTO
    Instructor (
        ins_id,
        lastname,
        firstname,
        city,
        country
    )
VALUES
    (5, 'Doe', 'John', 'Sydney', 'AU'),
    (6, 'Doe', 'Jane', 'Dhaka', 'BD');

-- Verify all instructor records
SELECT
    *
FROM
    Instructor;

-- ============================================================
-- UPDATE EXAMPLES
-- ============================================================
-- Example 3: Update the city of Sandip Saha
UPDATE
    Instructor
SET
    city = 'Toronto'
WHERE
    ins_id = 4;

-- Verify the updated record
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 4;

-- Example 4: Update the city and country of John Doe
UPDATE
    Instructor
SET
    city = 'Toronto',
    country = 'CA'
WHERE
    ins_id = 5;

-- Verify the updated record
SELECT
    *
FROM
    Instructor
WHERE
    ins_id = 5;

-- ============================================================
-- DELETE EXAMPLES
-- ============================================================
-- Example 5: Delete the instructor record with ID 6
DELETE FROM
    Instructor
WHERE
    ins_id = 6;

-- Verify the remaining instructor records
SELECT
    *
FROM
    Instructor;