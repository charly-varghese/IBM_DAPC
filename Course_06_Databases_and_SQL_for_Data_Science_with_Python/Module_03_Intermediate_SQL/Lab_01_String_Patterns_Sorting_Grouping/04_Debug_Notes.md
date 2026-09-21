# Debug Notes — Lab 01: String Patterns, Sorting and Grouping

## Course Information

- **IBM Data Analyst Professional Certificate**
- **Course 06:** Databases and SQL for Data Science with Python
- **Module 03:** Intermediate SQL
- **Lab 01:** String Patterns, Sorting and Grouping

---

## Debug Issue 01 — Multiple SQL Statements Execution

## Problem

While developing the SQL workflow, multiple SQL queries needed to be executed from a single `.sql` file.

Using:

```python
cursor.execute(sql_script)
can cause the following error when the SQL file contains multiple statements:

sqlite3.ProgrammingError:
You can only execute one statement at a time.
Cause

The SQLite cursor.execute() method is designed to execute a single SQL statement at a time.

However, our SQL practice files contain multiple queries separated by semicolons.

Example:

SELECT * FROM EMPLOYEES;

SELECT COUNT(*) FROM EMPLOYEES;

Passing both statements directly into one cursor.execute() call causes the error.

Solution

The reusable SQL runner separates the SQL script into individual statements:

statements = sql_script.split(";")

Each statement is then executed individually:

for statement in statements:

    statement = statement.strip()

    if not statement:
        continue

    cursor.execute(statement)
Lesson Learned

For SQL files containing multiple statements:

Read SQL file
    ↓
Split statements
    ↓
Remove empty statements
    ↓
Execute one statement at a time
    ↓
Fetch and display results

This approach allowed all SQL practice and challenge queries to be executed using a single reusable Python runner.

Debug Issue 02 — VS Code MSSQL Syntax Warning for LIMIT
Problem

While writing Challenge 08, VS Code displayed the following error:

Incorrect syntax near ';'

The error appeared near:

LIMIT 1;
SQL Query
SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID
ORDER BY
    AVG_SALARY DESC
LIMIT 1;
Cause

The VS Code SQL language mode was configured for:

MSSQL

Microsoft SQL Server does not support:

LIMIT

However, this project uses:

Python sqlite3
        +
SQLite Database

SQLite supports:

LIMIT 1;

Therefore, the query itself was valid for the database used in this project.

Solution

The query was executed using the project's Python SQLite runner:

python run_sql.py 03_Challenge.sql

The query executed successfully and returned:

('2', 3, 86666.66666666667)

This confirmed that:

SQLite Query Syntax → Correct
VS Code MSSQL Diagnostic → Database Dialect Mismatch
Lesson Learned

Always verify which SQL dialect is being used.

Different database systems support different SQL syntax.

Example:

SQLite
MySQL
PostgreSQL
SQL Server
Oracle

Although SQL has common standards, some commands and syntax vary between database systems.

For example:

SQLite / MySQL / PostgreSQL

LIMIT 1

while SQL Server commonly uses:

SELECT TOP 1

Therefore:

IDE Warning
    ≠
Actual Database Execution Result

The final validation should always be performed using the actual database engine used by the project.

Debug Issue 03 — Column Aliases Not Visible in Terminal Output
Problem

Queries using aliases such as:

SELECT
    DEP_ID,
    COUNT(*) AS NUM_EMPLOYEES,
    AVG(SALARY) AS AVG_SALARY
FROM
    EMPLOYEES
GROUP BY
    DEP_ID;

produced output similar to:

('2', 3, 86666.66666666667)
('5', 4, 65000.0)
('7', 3, 66666.66666666667)

The column aliases were not visible in the terminal.

Cause

The current reusable SQL runner prints only row values:

rows = cursor.fetchall()

for row in rows:
    print(row)

It does not print column names from:

cursor.description

Therefore, aliases were applied correctly by SQLite but were not displayed in the terminal output.

Lesson Learned

SQL aliases affect the result-set column names.

They do not change the underlying table structure.

Example:

COUNT(*) AS NUM_EMPLOYEES

The alias:

NUM_EMPLOYEES

exists in the query result metadata.

Future improvement to the SQL runner could include printing:

cursor.description

to display column headers.

Debug Issue 04 — Understanding HAVING vs WHERE
Problem

When working with grouped data, it can be confusing to decide whether to use:

WHERE

or:

HAVING
Correct Rule
WHERE
    ↓
Filters individual rows BEFORE grouping

GROUP BY
    ↓
Creates groups

HAVING
    ↓
Filters grouped results AFTER grouping
Example

Incorrect:

WHERE COUNT(*) < 4

Correct:

GROUP BY DEP_ID
HAVING COUNT(*) < 4;
Lesson Learned

Use:

WHERE

for individual rows.

Use:

HAVING

for aggregate or grouped results.

Debug Issue 05 — Equal Values and Sorting
Problem

In a grouped salary query, two departments had the same total salary:

DEP_ID 5 → 260000
DEP_ID 2 → 260000

The query used:

ORDER BY TOTAL_SALARY DESC;

The departments appeared in one valid order, but their order could change.

Cause

Both rows had the same value for:

TOTAL_SALARY

When values are equal, SQL does not guarantee a secondary order unless one is explicitly specified.

Solution

To create a deterministic order, add a secondary sorting column:

ORDER BY
    TOTAL_SALARY DESC,
    DEP_ID ASC;
Lesson Learned

When multiple rows may have equal sorting values, use additional columns in ORDER BY if a consistent order is required.

Debug Issue 06 — SQL Dialect Awareness
Key Observation

This lab used:

VS Code
    ↓
Python
    ↓
sqlite3
    ↓
SQLite
    ↓
HR.db

Therefore, all SQL queries were validated primarily against SQLite.

Lesson Learned

Before debugging SQL syntax, always identify:

The database engine.
The SQL dialect.
The execution environment.
Whether an IDE extension is configured for a different database.

Example:

VS Code SQL Extension → MSSQL

Actual Database Engine → SQLite

This mismatch can produce editor warnings even when the SQL query executes correctly.

Reusable SQL Debugging Checklist

Before assuming that an SQL query is incorrect:

Step 1 — Check the Database Engine
SQLite?
MySQL?
PostgreSQL?
SQL Server?
Oracle?
Step 2 — Check the SQL Dialect

Verify whether the SQL syntax is supported by the selected database.

Examples:

LIMIT
TOP
FETCH FIRST

may differ depending on the database engine.

Step 3 — Check the Execution Method

Determine whether the SQL file contains:

One SQL statement

or:

Multiple SQL statements

If multiple statements exist, ensure the execution method supports them.

Step 4 — Check Aggregate Queries

Remember:

WHERE
    ↓
Before GROUP BY

HAVING
    ↓
After GROUP BY
Step 5 — Check Sorting Logic

For predictable sorting:

ORDER BY
    PRIMARY_COLUMN,
    SECONDARY_COLUMN;
Step 6 — Verify Using the Actual Database

Always perform the final verification using the real database engine used by the project.

Editor Warning
        ↓
Check SQL Dialect
        ↓
Run Query
        ↓
Verify Database Output
        ↓
Confirm Final Result
Final Debug Status
Issue Status
Multiple SQL statement execution Resolved and reusable runner implemented
MSSQL warning for SQLite LIMIT syntax Identified as SQL dialect mismatch
SQLite query execution Verified successfully
Column aliases Working correctly
HAVING vs WHERE Understood and verified
Equal-value sorting behavior Understood and documented
All Challenge Queries Executed successfully
Final Result
Total IBM Demonstration Queries : 14
Total My Practice Queries      : 14
Total Challenge Queries        : 8
-----------------------------------
Total SQL Queries Executed     : 36

SQL Execution Errors           : 0
Database                       : HR.db
Database Engine                : SQLite
Lab Status                     : SUCCESS
```
