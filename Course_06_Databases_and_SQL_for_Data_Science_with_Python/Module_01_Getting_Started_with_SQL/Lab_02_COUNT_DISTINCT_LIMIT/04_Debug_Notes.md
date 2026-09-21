# Lab 02 — Debug Notes

## Lab

\*_COUNT, DISTINCT, LIMIT_

---

## Issue 1 — VS Code Showing Incorrect Syntax Errors for LIMIT

## Problem

VS Code showed errors such as:

```text
Incorrect syntax near '25'.
Incorrect syntax near '15'.
Incorrect syntax near '5'.
The errors appeared in queries using:

LIMIT 25;

LIMIT 15 OFFSET 10;

LIMIT 5 OFFSET 10;
Cause

The SQL files were being validated by VS Code as:

MSSQL

However, the database used in this lab is:

SQLite

LIMIT and OFFSET syntax is valid in SQLite, but the MSSQL validator does not recognize the same syntax.

Verification

The queries were executed using:

Python
↓
sqlite3
↓
FilmLocations.db

All queries executed successfully.

Examples:

LIMIT 25 → 25 rows returned
LIMIT 15 OFFSET 10 → 15 rows returned
LIMIT 5 OFFSET 10 → 5 rows returned
Resolution

No changes were required to the SQLite queries.

The queries were confirmed as valid by the SQLite database engine.

The VS Code Problems warnings were identified as a SQL dialect mismatch.

Issue 2 — Challenge Query Returned Zero Results
Problem

The initial Challenge 1 query used:

SELECT
    COUNT(*)
FROM
    FilmLocations
WHERE
    Director = "James Cameron";

Result:

(0,)
Cause

The dataset did not contain an exact matching record where:

Director = "James Cameron"

James Cameron was present in the dataset as a writer in other records, but not as an exact matching Director value for this query.

Resolution

The challenge query was changed to use an existing director:

SELECT
    COUNT(*)
FROM
    FilmLocations
WHERE
    Director = "Woody Allen";

Result:

(31,)
Key Debugging Lessons
1. SQL Dialect Matters

Different database systems support different SQL syntax.

SQLite
≠
Microsoft SQL Server

Always confirm which SQL engine is executing the query.

2. Execution Result Is the Final Verification

VS Code syntax warnings should be checked against the actual database execution.

VS Code Warning
        ↓
Check SQL Dialect
        ↓
Execute Query
        ↓
Verify Database Result
3. Zero Results Are Not Always SQL Errors

A query can execute successfully and still return:

(0,)

This usually means no records matched the specified condition.

Lab 02 Debug Status
Database Connection       ✅
COUNT Queries             ✅
DISTINCT Queries          ✅
LIMIT Queries             ✅
OFFSET Queries            ✅
Multiple SQL Statements   ✅
Debugging Completed       ✅
```
