# IBM DAPC — Course 06

## Module 06 — Advanced SQL for Data Engineers

## Lab 03 — Committing and Rolling Back a Transaction

## 📌 Overview

This lab demonstrates transaction control in MySQL using:

- `START TRANSACTION`
- `COMMIT`
- `ROLLBACK`
- Stored Procedures
- Exception Handling

The practical scenario uses two tables:

- `BankAccounts`
- `ShoeShop`

Database:

```text
TRANSACTION_LAB
Engine:

MySQL 8.0.46

Environment:

VS Code
Database Client Extension
MySQL Server
📁 Lab Files
Lab_03_Committing_and_Rolling_Back_a_Transaction/
│
├── 01_Lab.sql
├── 02_My_Practice.sql
├── BankAccounts-CREATE.sql
├── ShoeShop-CREATE.sql
└── README.md
1. Database Setup

A dedicated database was created for this lab:

CREATE DATABASE IF NOT EXISTS TRANSACTION_LAB;

USE TRANSACTION_LAB;

The supplied scripts were then executed to create and populate:

BankAccounts
ShoeShop
Initial BankAccounts Data
Account Balance
Rose 300.00
James 1345.00
Shoe Shop 124200.00
Corner Shop 76000.00
Initial ShoeShop Data
Product Stock Price
Boots 11 200.00
Brogues 10 150.00
High heels 8 600.00
Trainers 14 300.00
2. IBM Exercise — TRANSACTION_ROSE

A stored procedure named:

TRANSACTION_ROSE

was created to demonstrate transaction processing.

The scenario:

Rose purchases Boots.
Rose's balance is reduced.
Shoe Shop's balance is increased.
Boots stock is reduced.
Rose then attempts to purchase Trainers.
The transaction encounters a failure.
The exception handler performs ROLLBACK.

The transaction therefore does not permanently save the intermediate changes.

Result

After execution and verification:

Rose       = 300.00
Shoe Shop  = 124200.00
Boots      = 11
Trainers   = 14

The original values were restored successfully.

3. Practice Exercise — TRANSACTION_JAMES

A second stored procedure was created:

TRANSACTION_JAMES

Scenario:

James attempts to purchase 4 pairs of Trainers.
James's balance is reduced by 1200.
Shoe Shop's balance is increased by 1200.
Trainers stock is reduced by 4.
James then attempts to purchase 1 pair of Brogues.
James does not have sufficient balance for the second purchase.
The transaction is rolled back.
Result

After execution:

James       = 1345.00
Shoe Shop   = 124200.00
Trainers    = 14
Brogues     = 10

The original values were restored successfully.

4. Transaction Concepts Practiced
START TRANSACTION

Begins a transaction so that multiple operations can be treated as one logical unit.

START TRANSACTION;
COMMIT

Permanently saves successful transaction changes.

COMMIT;
ROLLBACK

Reverses the changes made during the transaction when the transaction fails.

ROLLBACK;
Exception Handler

The stored procedures use an exception handler to perform rollback when a SQL exception occurs.

DECLARE EXIT HANDLER FOR SQLEXCEPTION
BEGIN
    ROLLBACK;
END;
5. Verification

Both transaction scenarios were verified by querying the affected tables after procedure execution.

TRANSACTION_ROSE
BankAccounts
    Rose       300.00
    Shoe Shop  124200.00

ShoeShop
    Boots      11
    Trainers   14
TRANSACTION_JAMES
BankAccounts
    James      1345.00
    Shoe Shop  124200.00

ShoeShop
    Trainers   14
    Brogues    10

The original values were restored, confirming successful rollback behavior.

6. Key Learning Outcomes

Completed practical work on:

Transactions
START TRANSACTION
COMMIT
ROLLBACK
Stored Procedures
Exception Handling
Multi-table transactional updates
Transaction failure handling
Verification of rollback results
7. Lab Completion Status
Component Status
Database setup ✅ Complete
BankAccounts table ✅ Complete
ShoeShop table ✅ Complete
TRANSACTION_ROSE ✅ Complete
Rose rollback verification ✅ Complete
TRANSACTION_JAMES ✅ Complete
James rollback verification ✅ Complete
COMMIT / ROLLBACK practice ✅ Complete
Lab verification ✅ Complete
🏁 Final Status

Lab 03 — Committing and Rolling Back a Transaction: COMPLETE ✅
Database:

TRANSACTION_LAB

Engine:

MySQL 8.0.46

Environment:

VS Code + MySQL Database Client
```
