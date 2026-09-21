# IBM DAPC — Course 06

## Module 06 — Advanced SQL for Data Engineers

### Lab 02 — Stored Procedures

---

## 📌 Lab Overview

This lab focuses on creating, executing, testing, and removing
stored procedures in MySQL.

The practical work was completed using:

- MySQL 8.0.46
- VS Code
- Database Client extension
- Database: `PETS`

---

## 🎯 Learning Objectives

This lab covered:

1. Creating a stored procedure.
2. Executing a stored procedure.
3. Using input parameters in a stored procedure.
4. Applying conditional logic with `IF / ELSEIF / ELSE`.
5. Updating table data through a stored procedure.
6. Dropping stored procedures.
7. Verifying stored-procedure behavior.

---

## 🗄️ Database Setup

Database:

```text
PETS
Main table:

PETSALE
PETSALE Structure
Column Type
ID INTEGER
ANIMAL VARCHAR(20)
SALEPRICE DECIMAL(6,2)
SALEDATE DATE
QUANTITY INTEGER
Initial Dataset
ID Animal Sale Price Sale Date Quantity
1 Cat 450.09 2018-05-29 9
2 Dog 666.66 2018-06-01 3
3 Parrot 50.00 2018-06-04 2
4 Hamster 60.60 2018-06-11 6
5 Goldfish 48.48 2018-06-14 24
🧪 Exercise 1 — RETRIEVE_ALL
Objective

Create a stored procedure that retrieves all records from PETSALE.

Procedure
CREATE PROCEDURE RETRIEVE_ALL()
BEGIN
    SELECT *
    FROM PETSALE;
END
Execution
CALL PETS.RETRIEVE_ALL();
Verification

Result:

5 records returned

All five PETSALE records were successfully retrieved.

Cleanup

The procedure was subsequently dropped and verified.

DROP PROCEDURE PETS.RETRIEVE_ALL;

Status:

RETRIEVE_ALL → Removed ✅
🧪 Exercise 2 — UPDATE_SALEPRICE
Objective

Create a stored procedure that updates an animal's sale price
according to its health condition.

Procedure Parameters
Animal_ID
Animal_Health
Business Logic
Animal Health Price Adjustment
BAD 25% reduction
WORSE 50% reduction
Other No price change
Procedure
CREATE PROCEDURE PETS.UPDATE_SALEPRICE
(
    IN Animal_ID INTEGER,
    IN Animal_Health VARCHAR(20)
)
BEGIN
    IF Animal_Health = 'BAD' THEN

        UPDATE PETSALE
        SET SALEPRICE = SALEPRICE - (SALEPRICE * 0.25)
        WHERE ID = Animal_ID;

    ELSEIF Animal_Health = 'WORSE' THEN

        UPDATE PETSALE
        SET SALEPRICE = SALEPRICE - (SALEPRICE * 0.50)
        WHERE ID = Animal_ID;

    ELSE

        UPDATE PETSALE
        SET SALEPRICE = SALEPRICE
        WHERE ID = Animal_ID;

    END IF;
END
✅ Test 1 — BAD

Execution:

CALL PETS.UPDATE_SALEPRICE(1, 'BAD');

Original price:

450.09

Verified result:

337.57

Calculation:

450.09 × 0.75 = 337.5675

Stored as:

337.57

Status:

BAD → 25% reduction → PASSED ✅
✅ Test 2 — WORSE

Execution:

CALL PETS.UPDATE_SALEPRICE(3, 'WORSE');

Original price:

50.00

Verified result:

25.00

Calculation:

50.00 × 0.50 = 25.00

Status:

WORSE → 50% reduction → PASSED ✅
🧹 Procedure Cleanup

After testing, the procedure was removed:

DROP PROCEDURE PETS.UPDATE_SALEPRICE;

The procedure was then verified as removed.

🧠 Key SQL Concepts Practiced
CREATE PROCEDURE
CALL
DROP PROCEDURE
Stored-procedure input parameters
IF
ELSEIF
ELSE
UPDATE
Conditional data modification
Procedure verification using:
SHOW PROCEDURE STATUS
🛠️ Environment
Editor       : VS Code
Database Tool: Database Client
DBMS         : MySQL 8.0.46
Database     : PETS
Connection   : IBM_DAPC_MySQL
⚠️ Execution Notes

During execution, an initial database-context issue caused
RETRIEVE_ALL to be created in the wrong database.

This was identified and corrected by explicitly using:

USE PETS;

and subsequently verifying the procedure with:

SHOW PROCEDURE STATUS
WHERE Db = 'pets';

The final procedures were created and tested successfully in
the intended PETS database.

✅ Lab Completion Checklist
 Create PETS database
 Create and populate PETSALE
 Verify 5 records
 Create RETRIEVE_ALL
 Execute RETRIEVE_ALL
 Verify returned records
 Drop RETRIEVE_ALL
 Create UPDATE_SALEPRICE
 Test BAD
 Verify 25% reduction
 Test WORSE
 Verify 50% reduction
 Drop UPDATE_SALEPRICE
 Verify procedure cleanup
🏁 Final Status

LAB 02 — STORED PROCEDURES: COMPLETE ✅
```
