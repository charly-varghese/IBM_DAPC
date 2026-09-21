-- ============================================================
-- LAB 02 MY PRACTICE: CREATE AND LOAD TABLES USING SQL SCRIPTS
-- ============================================================
-- ============================================================
-- Practice 1: Verify PATIENTS Table
-- ============================================================
SELECT
    *
FROM
    PATIENTS;

-- ============================================================
-- Practice 2: Select Specific Patient Columns
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    SEX
FROM
    PATIENTS;

-- ============================================================
-- Practice 3: Verify MEDICAL_HISTORY Table
-- ============================================================
SELECT
    *
FROM
    MEDICAL_HISTORY;

-- ============================================================
-- Practice 4: Verify MEDICAL_PROCEDURES Table
-- ============================================================
SELECT
    *
FROM
    MEDICAL_PROCEDURES;

-- ============================================================
-- Practice 5: Verify MEDICAL_DEPARTMENTS Table
-- ============================================================
SELECT
    *
FROM
    MEDICAL_DEPARTMENTS;

-- ============================================================
-- Practice 6: Verify MEDICAL_LOCATIONS Table
-- ============================================================
SELECT
    *
FROM
    MEDICAL_LOCATIONS;

-- ============================================================
-- Practice 7: Filter Male Patients
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    SEX
FROM
    PATIENTS
WHERE
    SEX = 'M';

-- ============================================================
-- Practice 8: Filter Female Patients
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    SEX
FROM
    PATIENTS
WHERE
    SEX = 'F';

-- ============================================================
-- Practice 9: Find Patients in Department D003
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    DEPT_ID
FROM
    PATIENTS
WHERE
    DEPT_ID = 'D003';

-- ============================================================
-- Practice 10: Find Medical History for Patient P001
-- ============================================================
SELECT
    *
FROM
    MEDICAL_HISTORY
WHERE
    PATIENT_ID = 'P001';

-- ============================================================
-- Practice 11: Find Procedures in Department D003
-- ============================================================
SELECT
    PROCEDURE_ID,
    PROCEDURE_NAME,
    PROCEDURE_DATE,
    PATIENT_ID,
    DEPT_ID
FROM
    MEDICAL_PROCEDURES
WHERE
    DEPT_ID = 'D003';

-- ============================================================
-- Practice 12: Find a Specific Medical Department
-- ============================================================
SELECT
    *
FROM
    MEDICAL_DEPARTMENTS
WHERE
    DEPT_ID = 'D002';

-- ============================================================
-- Practice 13: Sort Patients by First Name
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME
FROM
    PATIENTS
ORDER BY
    FIRST_NAME ASC;

-- ============================================================
-- Practice 14: Sort Patients by Birth Date
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    BIRTH_DATE
FROM
    PATIENTS
ORDER BY
    BIRTH_DATE ASC;

-- ============================================================
-- Practice 15: Sort Medical Procedures by Date
-- ============================================================
SELECT
    PROCEDURE_ID,
    PROCEDURE_NAME,
    PROCEDURE_DATE,
    PATIENT_ID
FROM
    MEDICAL_PROCEDURES
ORDER BY
    PROCEDURE_DATE DESC;

-- ============================================================
-- Practice 16: Display Only First 3 Patients
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME
FROM
    PATIENTS
LIMIT
    3;

-- ============================================================
-- Practice 17: Display Latest 3 Medical Procedures
-- ============================================================
SELECT
    PROCEDURE_ID,
    PROCEDURE_NAME,
    PROCEDURE_DATE,
    PATIENT_ID
FROM
    MEDICAL_PROCEDURES
ORDER BY
    PROCEDURE_DATE DESC
LIMIT
    3;

-- ============================================================
-- Practice 18: Filter and Sort Patients
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    DEPT_ID
FROM
    PATIENTS
WHERE
    SEX = 'M'
ORDER BY
    LAST_NAME ASC;

-- ============================================================
-- Practice 19: Filter Patients Using AND
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    SEX,
    DEPT_ID
FROM
    PATIENTS
WHERE
    SEX = 'M'
    AND DEPT_ID = 'D003';

-- ============================================================
-- Practice 20: Filter Patients Using OR
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    DEPT_ID
FROM
    PATIENTS
WHERE
    DEPT_ID = 'D001'
    OR DEPT_ID = 'D004';

-- ============================================================
-- Practice 21: Filter Using IN
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME,
    DEPT_ID
FROM
    PATIENTS
WHERE
    DEPT_ID IN ('D001', 'D003');

-- ============================================================
-- Practice 22: Search Using LIKE
-- ============================================================
SELECT
    PATIENT_ID,
    FIRST_NAME,
    LAST_NAME
FROM
    PATIENTS
WHERE
    FIRST_NAME LIKE 'J%';

-- ============================================================
-- Practice 23: Search Medical Conditions Using LIKE
-- ============================================================
SELECT
    MEDICAL_HISTORY_ID,
    PATIENT_ID,
    MEDICAL_CONDITION
FROM
    MEDICAL_HISTORY
WHERE
    MEDICAL_CONDITION LIKE '%Heart%';

-- ============================================================
-- Practice 24: Filter Procedures Using BETWEEN
-- ============================================================
SELECT
    PROCEDURE_ID,
    PROCEDURE_NAME,
    PROCEDURE_DATE,
    PATIENT_ID
FROM
    MEDICAL_PROCEDURES
WHERE
    PROCEDURE_DATE BETWEEN '2023-08-01'
    AND '2023-08-03'
ORDER BY
    PROCEDURE_DATE ASC;

-- ============================================================
-- Practice 25: Count Total Patients
-- ============================================================
SELECT
    COUNT(*) AS TOTAL_PATIENTS
FROM
    PATIENTS;

-- ============================================================
-- Practice 26: Count Distinct Departments Used by Patients
-- ============================================================
SELECT
    COUNT(DISTINCT DEPT_ID) AS TOTAL_DEPARTMENTS
FROM
    PATIENTS;

-- ============================================================
-- Practice 27: Display Distinct Departments
-- ============================================================
SELECT
    DISTINCT DEPT_ID
FROM
    PATIENTS
ORDER BY
    DEPT_ID ASC;

-- ============================================================
-- Practice 28: Count Total Medical Procedures
-- ============================================================
SELECT
    COUNT(*) AS TOTAL_PROCEDURES
FROM
    MEDICAL_PROCEDURES;

-- ============================================================
-- Practice 29: Find Earliest Procedure Date
-- ============================================================
SELECT
    MIN(PROCEDURE_DATE) AS EARLIEST_PROCEDURE_DATE
FROM
    MEDICAL_PROCEDURES;

-- ============================================================
-- Practice 30: Find Latest Procedure Date
-- ============================================================
SELECT
    MAX(PROCEDURE_DATE) AS LATEST_PROCEDURE_DATE
FROM
    MEDICAL_PROCEDURES;

-- ============================================================
-- Practice 31: Count Patients by Sex
-- ============================================================
SELECT
    SEX,
    COUNT(*) AS TOTAL_PATIENTS
FROM
    PATIENTS
GROUP BY
    SEX;

-- ============================================================
-- Practice 32: Count Patients by Department
-- ============================================================
SELECT
    DEPT_ID,
    COUNT(*) AS TOTAL_PATIENTS
FROM
    PATIENTS
GROUP BY
    DEPT_ID
ORDER BY
    TOTAL_PATIENTS DESC;

-- ============================================================
-- Practice 33: Count Procedures by Department
-- ============================================================
SELECT
    DEPT_ID,
    COUNT(*) AS TOTAL_PROCEDURES
FROM
    MEDICAL_PROCEDURES
GROUP BY
    DEPT_ID
ORDER BY
    TOTAL_PROCEDURES DESC;

-- ============================================================
-- Practice 34: Find Departments with More Than One Patient
-- ============================================================
SELECT
    DEPT_ID,
    COUNT(*) AS TOTAL_PATIENTS
FROM
    PATIENTS
GROUP BY
    DEPT_ID
HAVING
    COUNT(*) > 1;

-- ============================================================
-- Practice 35: Find Departments with More Than One Procedure
-- ============================================================
SELECT
    DEPT_ID,
    COUNT(*) AS TOTAL_PROCEDURES
FROM
    MEDICAL_PROCEDURES
GROUP BY
    DEPT_ID
HAVING
    COUNT(*) > 1;

-- ============================================================
-- Practice 36: Count Procedures by Patient
-- ============================================================
SELECT
    PATIENT_ID,
    COUNT(*) AS TOTAL_PROCEDURES
FROM
    MEDICAL_PROCEDURES
GROUP BY
    PATIENT_ID
HAVING
    COUNT(*) >= 2;

-- ============================================================
-- Practice 37: Find Medical Conditions Appearing More Than Once
-- ============================================================
SELECT
    MEDICAL_CONDITION,
    COUNT(*) AS TOTAL_RECORDS
FROM
    MEDICAL_HISTORY
GROUP BY
    MEDICAL_CONDITION
HAVING
    COUNT(*) > 1;

-- ============================================================
-- Practice 38: Use WHERE and HAVING Together
-- ============================================================
SELECT
    DEPT_ID,
    COUNT(*) AS TOTAL_PROCEDURES
FROM
    MEDICAL_PROCEDURES
WHERE
    PROCEDURE_DATE >= '2023-08-01'
GROUP BY
    DEPT_ID
HAVING
    COUNT(*) >= 2
ORDER BY
    TOTAL_PROCEDURES DESC;

-- ============================================================
-- Practice 39: Create a Separate Practice Table
-- ============================================================
DROP TABLE IF EXISTS PATIENT_NOTES;

CREATE TABLE PATIENT_NOTES (
    NOTE_ID INTEGER PRIMARY KEY,
    PATIENT_ID CHAR(9) NOT NULL,
    NOTE_TEXT VARCHAR(100),
    NOTE_DATE DATE
);

-- ============================================================
-- Practice 40: Insert Patient Notes
-- ============================================================
INSERT INTO
    PATIENT_NOTES (
        NOTE_ID,
        PATIENT_ID,
        NOTE_TEXT,
        NOTE_DATE
    )
VALUES
    (
        1,
        'P001',
        'Initial consultation completed',
        '2023-08-01'
    ),
    (
        2,
        'P002',
        'Follow-up appointment scheduled',
        '2023-08-02'
    ),
    (
        3,
        'P003',
        'Procedure completed successfully',
        '2023-08-03'
    );

-- ============================================================
-- Practice 41: Verify Inserted Data
-- ============================================================
SELECT
    *
FROM
    PATIENT_NOTES;

-- ============================================================
-- Practice 42: Update a Patient Note
-- ============================================================
UPDATE
    PATIENT_NOTES
SET
    NOTE_TEXT = 'Follow-up appointment completed'
WHERE
    NOTE_ID = 2;

-- ============================================================
-- Practice 43: Verify Updated Data
-- ============================================================
SELECT
    *
FROM
    PATIENT_NOTES
WHERE
    NOTE_ID = 2;

-- ============================================================
-- Practice 44: Insert One Additional Patient Note
-- ============================================================
INSERT INTO
    PATIENT_NOTES (
        NOTE_ID,
        PATIENT_ID,
        NOTE_TEXT,
        NOTE_DATE
    )
VALUES
    (
        4,
        'P005',
        'Post-procedure recovery note added',
        '2023-08-04'
    );

-- ============================================================
-- Practice 45: Verify All Notes
-- ============================================================
SELECT
    *
FROM
    PATIENT_NOTES
ORDER BY
    NOTE_DATE ASC;

-- ============================================================
-- Practice 46: Delete One Patient Note
-- ============================================================
DELETE FROM
    PATIENT_NOTES
WHERE
    NOTE_ID = 3;

-- ============================================================
-- Practice 47: Verify Data After DELETE
-- ============================================================
SELECT
    *
FROM
    PATIENT_NOTES
ORDER BY
    NOTE_ID ASC;