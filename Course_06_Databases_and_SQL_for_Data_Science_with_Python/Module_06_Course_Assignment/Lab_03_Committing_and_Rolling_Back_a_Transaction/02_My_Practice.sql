-- Active: 1789657953897@@127.0.0.1@3306@transaction_lab
USE mysql;

DROP PROCEDURE IF EXISTS TRANSACTION_ROSE;

DELIMITER / / CREATE PROCEDURE TRANSACTION_ROSE() BEGIN DECLARE EXIT HANDLER FOR SQLEXCEPTION BEGIN ROLLBACK;

RESIGNAL;

END;

START TRANSACTION;

UPDATE
    BankAccounts
SET
    Balance = Balance - 200
WHERE
    AccountNumber = 'B001';

UPDATE
    BankAccounts
SET
    Balance = Balance + 200
WHERE
    AccountNumber = 'B003';

UPDATE
    ShoeShop
SET
    Stock = Stock - 1
WHERE
    Product = 'Boots';

COMMIT;

END / / DELIMITER;

SELECT
    DATABASE();

SHOW TABLES;

CREATE DATABASE IF NOT EXISTS TRANSACTION_LAB;

USE TRANSACTION_LAB;

SELECT
    DATABASE();

SELECT
    *
FROM
    BankAccounts;

SELECT
    *
FROM
    ShoeShop;

USE TRANSACTION_LAB;

DROP PROCEDURE IF EXISTS TRANSACTION_ROSE;

DELIMITER / / CREATE PROCEDURE TRANSACTION_ROSE() BEGIN DECLARE EXIT HANDLER FOR SQLEXCEPTION BEGIN ROLLBACK;

RESIGNAL;

END;

START TRANSACTION;

UPDATE
    BankAccounts
SET
    Balance = Balance - 200
WHERE
    AccountNumber = 'B001';

UPDATE
    BankAccounts
SET
    Balance = Balance + 200
WHERE
    AccountNumber = 'B003';

UPDATE
    ShoeShop
SET
    Stock = Stock - 1
WHERE
    Product = 'Boots';

COMMIT;

END / / DELIMITER;

SHOW PROCEDURE STATUS
WHERE
    Db = 'transaction_lab'
    AND Name = 'TRANSACTION_ROSE';

COMMIT;

USE TRANSACTION_LAB;

DROP PROCEDURE IF EXISTS TRANSACTION_ROSE;

DELIMITER / / CREATE PROCEDURE TRANSACTION_ROSE() BEGIN DECLARE EXIT HANDLER FOR SQLEXCEPTION BEGIN ROLLBACK;

END;

START TRANSACTION;

-- Rose buys Boots for 200
UPDATE
    BankAccounts
SET
    Balance = Balance - 200
WHERE
    AccountNumber = 'B001';

UPDATE
    BankAccounts
SET
    Balance = Balance + 200
WHERE
    AccountNumber = 'B003';

UPDATE
    ShoeShop
SET
    Stock = Stock - 1
WHERE
    Product = 'Boots';

-- Second purchase: Trainers for 300
UPDATE
    BankAccounts
SET
    Balance = Balance - 300
WHERE
    AccountNumber = 'B001';

UPDATE
    BankAccounts
SET
    Balance = Balance + 300
WHERE
    AccountNumber = 'B003';

UPDATE
    ShoeShop
SET
    Stock = Stock - 1
WHERE
    Product = 'Trainers';

COMMIT;

END / / DELIMITER;

CALL TRANSACTION_ROSE();

SELECT
    *
FROM
    BankAccounts;

SELECT
    *
FROM
    ShoeShop;

SELECT
    *
FROM
    BankAccounts
WHERE
    AccountName = 'James';

SELECT
    *
FROM
    ShoeShop
WHERE
    Product IN ('Trainers', 'Brogues');

USE TRANSACTION_LAB;

DROP PROCEDURE IF EXISTS TRANSACTION_JAMES;

DELIMITER / / CREATE PROCEDURE TRANSACTION_JAMES() BEGIN DECLARE EXIT HANDLER FOR SQLEXCEPTION BEGIN ROLLBACK;

END;

START TRANSACTION;

-- James buys 4 pairs of Trainers
UPDATE
    BankAccounts
SET
    Balance = Balance - 1200
WHERE
    AccountName = 'James';

UPDATE
    BankAccounts
SET
    Balance = Balance + 1200
WHERE
    AccountName = 'Shoe Shop';

UPDATE
    ShoeShop
SET
    Stock = Stock - 4
WHERE
    Product = 'Trainers';

-- James attempts to buy 1 pair of Brogues
UPDATE
    BankAccounts
SET
    Balance = Balance - 150
WHERE
    AccountName = 'James'
    AND Balance >= 150;

IF ROW_COUNT() = 0 THEN SIGNAL SQLSTATE '45000'
SET
    MESSAGE_TEXT = 'Insufficient balance for Brogues';

END IF;

UPDATE
    BankAccounts
SET
    Balance = Balance + 150
WHERE
    AccountName = 'Shoe Shop';

UPDATE
    ShoeShop
SET
    Stock = Stock - 1
WHERE
    Product = 'Brogues';

COMMIT;

END / / DELIMITER;

SHOW PROCEDURE STATUS
WHERE
    Db = 'transaction_lab'
    AND Name = 'TRANSACTION_JAMES';

CALL TRANSACTION_JAMES();

SELECT
    *
FROM
    BankAccounts
WHERE
    AccountName IN ('James', 'Shoe Shop');

SELECT
    *
FROM
    ShoeShop
WHERE
    Product IN ('Trainers', 'Brogues');