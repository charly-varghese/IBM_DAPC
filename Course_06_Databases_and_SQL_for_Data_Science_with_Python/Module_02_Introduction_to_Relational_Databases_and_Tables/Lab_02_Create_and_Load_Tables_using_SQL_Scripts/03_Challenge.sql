-- ============================================================
-- LAB 02 CHALLENGE
-- Create and Load Tables using SQL Scripts
-- ============================================================


-- ============================================================
-- Challenge 1: View All Patients
-- ============================================================

SELECT
    *
FROM
    PATIENTS;


-- ============================================================
-- Challenge 2: Find Male Patients
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
-- Challenge 3: Find Patients in Department D003
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
-- Challenge 4: Sort Patients by Birth Date
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
-- Challenge 5: Find Medical History for Patient P001
-- ============================================================

SELECT
    MEDICAL_HISTORY_ID,
    PATIENT_ID,
    DIAGNOSIS_DATE,
    MEDICAL_CONDITION
FROM
    MEDICAL_HISTORY
WHERE
    PATIENT_ID = 'P001';


-- ============================================================
-- Challenge 6: Find Procedures in Department D003
-- ============================================================

SELECT
    PROCEDURE_ID,
    PROCEDURE_NAME,
    PROCEDURE_DATE,
    PATIENT_ID
FROM
    MEDICAL_PROCEDURES
WHERE
    DEPT_ID = 'D003';


-- ============================================================
-- Challenge 7: Find Procedures Between Two Dates
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
    AND '2023-08-04'
ORDER BY
    PROCEDURE_DATE ASC;


-- ============================================================
-- Challenge 8: Search Patients Whose Name Starts With J
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
-- Challenge 9: Count Total Patients
-- ============================================================

SELECT
    COUNT(*) AS TOTAL_PATIENTS
FROM
    PATIENTS;


-- ============================================================
-- Challenge 10: Count Patients by Department
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
-- Challenge 11: Find Departments With More Than One Patient
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
-- Challenge 12: Count Procedures by Department
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
-- Challenge 13: Find Patients With Multiple Procedures
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
-- Challenge 14: Find Repeated Medical Conditions
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
-- Challenge 15: Create a New Practice Table
-- ============================================================

DROP TABLE IF EXISTS PATIENT_APPOINTMENTS;

CREATE TABLE PATIENT_APPOINTMENTS (
    APPOINTMENT_ID INTEGER PRIMARY KEY,
    PATIENT_ID CHAR(9) NOT NULL,
    APPOINTMENT_DATE DATE,
    APPOINTMENT_TYPE VARCHAR(50)
);


-- ============================================================
-- Challenge 16: Insert Appointment Records
-- ============================================================

INSERT INTO
    PATIENT_APPOINTMENTS (
        APPOINTMENT_ID,
        PATIENT_ID,
        APPOINTMENT_DATE,
        APPOINTMENT_TYPE
    )
VALUES
    (1, 'P001', '2023-08-05', 'Follow-up'),
    (2, 'P002', '2023-08-06', 'Consultation'),
    (3, 'P003', '2023-08-07', 'Procedure Review');


-- ============================================================
-- Challenge 17: Verify Appointment Records
-- ============================================================

SELECT
    *
FROM
    PATIENT_APPOINTMENTS;


-- ============================================================
-- Challenge 18: Update an Appointment
-- ============================================================

UPDATE
    PATIENT_APPOINTMENTS
SET
    APPOINTMENT_TYPE = 'Post-Procedure Review'
WHERE
    APPOINTMENT_ID = 3;


-- ============================================================
-- Challenge 19: Verify Updated Appointment
-- ============================================================

SELECT
    *
FROM
    PATIENT_APPOINTMENTS
WHERE
    APPOINTMENT_ID = 3;


-- ============================================================
-- Challenge 20: Add One More Appointment
-- ============================================================

INSERT INTO
    PATIENT_APPOINTMENTS (
        APPOINTMENT_ID,
        PATIENT_ID,
        APPOINTMENT_DATE,
        APPOINTMENT_TYPE
    )
VALUES
    (4, 'P005', '2023-08-08', 'Recovery Check');


-- ============================================================
-- Challenge 21: View All Appointments
-- ============================================================

SELECT
    *
FROM
    PATIENT_APPOINTMENTS
ORDER BY
    APPOINTMENT_DATE ASC;


-- ============================================================
-- Challenge 22: Delete an Appointment
-- ============================================================

DELETE FROM
    PATIENT_APPOINTMENTS
WHERE
    APPOINTMENT_ID = 2;


-- ============================================================
-- Challenge 23: Final Verification
-- ============================================================

SELECT
    *
FROM
    PATIENT_APPOINTMENTS
ORDER BY
    APPOINTMENT_ID ASC;
    