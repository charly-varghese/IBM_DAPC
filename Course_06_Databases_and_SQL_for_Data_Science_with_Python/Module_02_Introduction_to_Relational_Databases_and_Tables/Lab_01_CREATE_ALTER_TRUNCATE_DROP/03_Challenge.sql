-- ============================================================
-- LAB 01 CHALLENGES: CREATE, ALTER, TRUNCATE, DROP
-- ============================================================
-- ============================================================
-- Challenge 1: CREATE TABLE
-- ============================================================
-- Create a PRODUCT table
CREATE TABLE PRODUCT (
    ID INTEGER NOT NULL,
    PRODUCT_NAME TEXT,
    CATEGORY TEXT,
    PRICE DECIMAL(10, 2)
);

-- ============================================================
-- Challenge 2: INSERT DATA
-- ============================================================
-- Insert product records
INSERT INTO
    PRODUCT
VALUES
    (1, 'Laptop', 'Electronics', 75000.00),
    (2, 'Smartphone', 'Electronics', 45000.00),
    (3, 'Office Chair', 'Furniture', 12000.00);

-- Verify inserted data
SELECT
    *
FROM
    PRODUCT;

-- ============================================================
-- Challenge 3: ALTER TABLE
-- ============================================================
-- Add a new STOCK column
ALTER TABLE
    PRODUCT
ADD
    COLUMN STOCK INTEGER;

-- ============================================================
-- Challenge 4: UPDATE DATA
-- ============================================================
-- Update stock values
UPDATE
    PRODUCT
SET
    STOCK = 15
WHERE
    ID = 1;

UPDATE
    PRODUCT
SET
    STOCK = 30
WHERE
    ID = 2;

UPDATE
    PRODUCT
SET
    STOCK = 20
WHERE
    ID = 3;

-- Verify updated data
SELECT
    *
FROM
    PRODUCT;

-- ============================================================
-- Challenge 5: TRUNCATE TABLE Equivalent
-- ============================================================
-- SQLite does not support TRUNCATE TABLE.
-- DELETE removes all rows while keeping the table structure.
DELETE FROM
    PRODUCT;

-- Verify the table is empty
SELECT
    *
FROM
    PRODUCT;

-- ============================================================
-- Challenge 6: DROP TABLE
-- ============================================================
-- Delete the PRODUCT table completely
DROP TABLE PRODUCT;