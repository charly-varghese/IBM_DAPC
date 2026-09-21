-- Active: 1789657953897@@127.0.0.1@3306@pets
-- ============================================================
-- EXERCISE 1 - RETRIEVE ALL PETSALE RECORDS
-- ============================================================
DELIMITER / / CREATE PROCEDURE RETRIEVE_ALL() BEGIN
SELECT
    *
FROM
    PETSALE;

END / / DELIMITER;

CALL RETRIEVE_ALL();