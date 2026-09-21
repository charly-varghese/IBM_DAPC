# 04_Debug_Notes.md

## IBM DAPC — Course 06

## Module 05 — Course Assignment

### Lab 01 — Working with a Real-World Data Set

---

## 1. Debugging Objective

This file records the important errors, root causes, fixes, and lessons encountered while executing:

\*_Lab 01 — Working with a Real-World Data Set_

Execution environment:

- Windows 11
- VS Code
- Python 3.x
- Virtual Environment: `.venv`
- Pandas
- SQLite
- IBM DAPC Course 06

---

## 2. Issue 01 — Database Created but Required Table Missing

## Error

Initial execution produced an error related to the missing:

```text
SCHOOLS
table.

Root Cause

The following SQLite command:

conn = sqlite3.connect("RealWorldData.db")

automatically creates a new database file if the database does not already exist.

However, creating the database does not create the required tables.

Therefore, SQL queries against:

SELECT ...
FROM SCHOOLS;

failed because the table had not yet been loaded.

Fix

The CPS dataset was explicitly loaded into SQLite:

schools_df.to_sql(
    "SCHOOLS",
    conn,
    if_exists="replace",
    index=False
)

The table was then verified using:

SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name;
Result
CHICAGO_SOCIOECONOMIC_DATA
SCHOOLS

Both required tables were successfully created.

3. Issue 02 — Multiple RealWorldData.db Files
Observation

During debugging, more than one:

RealWorldData.db

file existed in different folders.

Root Cause

Using a relative database path can create a database in the current working directory rather than the directory containing the Python script.

This can result in:

Empty database in one folder
Working database in another folder
SQL queries appearing to fail even though the table exists elsewhere
Fix

The script was changed to use the script's own directory:

BASE_DIR = Path(__file__).resolve().parent

DB_FILE = BASE_DIR / "RealWorldData.db"
Result

The active database is now explicitly located inside:

02_My_Practice\

This makes execution location-independent and reduces database-path errors.

4. Issue 03 — Socioeconomic Table Required for Problems 11 and 12
Observation

Problems 11 and 12 require:

CHICAGO_SOCIOECONOMIC_DATA

in addition to:

SCHOOLS
Root Cause

The CPS school dataset alone cannot answer the hardship-index questions.

Problems 11 and 12 require a second dataset containing:

COMMUNITY_AREA_NUMBER
COMMUNITY_AREA_NAME
HARDSHIP_INDEX
Fix

The IBM-provided Chicago Census / Socioeconomic CSV was loaded into SQLite:

census_df.to_sql(
    "CHICAGO_SOCIOECONOMIC_DATA",
    conn,
    if_exists="replace",
    index=False
)
Validation

The database contains:

SCHOOLS                         566 rows
CHICAGO_SOCIOECONOMIC_DATA      78 rows
5. Issue 04 — STEP 8 Column Name Error
Error

STEP 8 initially returned:

ERROR: no such column: PER_CAPITA_INCOME
Root Cause

The actual CSV column contains a trailing space:

'PER_CAPITA_INCOME '

rather than:

'PER_CAPITA_INCOME'

The imported SQLite column therefore retained the trailing space.

Evidence

The imported columns were displayed as:

COMMUNITY_AREA_NUMBER
COMMUNITY_AREA_NAME
PERCENT OF HOUSING CROWDED
PERCENT HOUSEHOLDS BELOW POVERTY
PERCENT AGED 16+ UNEMPLOYED
PERCENT AGED 25+ WITHOUT HIGH SCHOOL DIPLOMA
PERCENT AGED UNDER 18 OR OVER 64
PER_CAPITA_INCOME
HARDSHIP_INDEX
Correct SQL Approach

When a column contains unusual characters or spaces, quote the identifier:

SELECT
    "PER_CAPITA_INCOME "
FROM CHICAGO_SOCIOECONOMIC_DATA;
Lesson

Always inspect imported column names before writing SQL against external CSV data.

Useful Python check:

for column in census_df.columns:
    print(repr(column))

Using:

repr(column)

makes invisible leading/trailing spaces visible.

6. Issue 05 — Percentage Stored as Text
Observation

The CPS field:

Average Student Attendance

contains values such as:

98.4%
97.8%
57.9%
Root Cause

The % character means the values cannot be directly treated as numeric values.

Fix

Remove % and convert the result to numeric:

CAST(
    REPLACE("Average Student Attendance", '%', '')
    AS REAL
)
Example
57.9% → 57.9
98.4% → 98.4
Lesson

Real-world datasets frequently contain numeric values stored as strings because of formatting characters.

Typical cleaning pattern:

Raw String
    ↓
REPLACE()
    ↓
CAST()
    ↓
Numeric Value
7. Issue 06 — College Enrollment Contains Commas
Observation

The CPS column:

College Enrollment (number of students)

contains formatted values such as:

14,793
10,933
4,368
Root Cause

Comma separators make the values unsuitable for direct numeric aggregation.

Fix

Remove commas and convert to INTEGER:

CAST(
    REPLACE(
        "College Enrollment (number of students) ",
        ',',
        ''
    ) AS INTEGER
)
Lesson

Data cleaning is often required before aggregation.

Pattern:

"14,793"
      ↓
REPLACE(',', '')
      ↓
"14793"
      ↓
CAST(... AS INTEGER)
      ↓
14793
8. Issue 07 — SQL Columns Containing Spaces
Observation

The CPS dataset contains column names such as:

Name of School
Safety Score
Average Student Attendance
Community Area Name
College Enrollment (number of students)
Root Cause

SQL identifiers containing spaces must be quoted in SQLite.

Correct Syntax
SELECT "Name of School"
FROM SCHOOLS;

and:

SELECT "Safety Score"
FROM SCHOOLS;
Lesson

SQLite supports quoted identifiers.

For real-world datasets, always inspect the schema before constructing queries.

9. Issue 08 — P11 JOIN Logic
Requirement

Find the hardship index for the community area associated with:

College Enrollment = 4368
Solution

The school and socioeconomic datasets were joined using:

Community Area Number

SQL:

SELECT
    CD.COMMUNITY_AREA_NAME,
    CD.HARDSHIP_INDEX
FROM CHICAGO_SOCIOECONOMIC_DATA AS CD
JOIN SCHOOLS AS CPS
    ON CD.COMMUNITY_AREA_NUMBER =
       CPS."Community Area Number"
WHERE CAST(
    REPLACE(
        CPS."College Enrollment (number of students) ",
        ',',
        ''
    ) AS INTEGER
) = 4368;
Result
North Center    6.0
Lesson

This demonstrates a practical relational-database workflow:

SCHOOLS
   |
   | Community Area Number
   |
   ↓
CHICAGO_SOCIOECONOMIC_DATA
10. Issue 09 — P12 Subquery Logic
Requirement

Find the hardship index for the community area containing the school with the highest college enrollment.

Solution

First identify the community area of the school with the highest enrollment:

SELECT "Community Area Number"
FROM SCHOOLS
ORDER BY
    CAST(
        REPLACE(
            "College Enrollment (number of students) ",
            ',',
            ''
        ) AS INTEGER
    ) DESC
LIMIT 1;

Then use the result to retrieve the socioeconomic information.

Final Result
Community Area Number : 5
Community Area Name   : North Center
Hardship Index        : 6.0
Lesson

This demonstrates the use of:

ORDER BY
DESC
LIMIT
Subqueries
Cross-table analysis
11. Final Validation

The final database validation produced:

SCHOOLS rows                    : 566
CHICAGO_SOCIOECONOMIC_DATA rows: 78

Validation:

[✓] Dataset row-count validation PASSED

The complete Lab 01 execution finished successfully.

12. Final Debugging Lessons
Lesson 1 — Database Creation ≠ Table Creation
sqlite3.connect()

creates the database file, but tables must still be created or loaded.

Lesson 2 — Always Control File Paths

Prefer:

BASE_DIR = Path(__file__).resolve().parent

instead of relying on the current working directory.

Lesson 3 — Inspect External Dataset Schemas

Use:

print(df.columns)

or:

for column in df.columns:
    print(repr(column))

before writing SQL.

Lesson 4 — Clean Formatted Numeric Data

Common real-world transformations:

57.9%  → 57.9
14,793 → 14793

using:

REPLACE()
CAST()
Lesson 5 — Quote SQL Identifiers

For column names containing spaces or special characters:

"Column Name"
Lesson 6 — JOIN Requires a Common Key

The two datasets were connected using:

COMMUNITY_AREA_NUMBER

This allowed school-level information to be combined with socioeconomic information.

Lesson 7 — Validate Before Declaring Success

Always verify:

Database exists
Tables exist
Row counts are correct
Queries execute successfully
Expected results are returned
13. Lab 01 Final Status
============================================================
LAB 01 — WORKING WITH A REAL-WORLD DATA SET
============================================================

CPS Dataset                    : PASS
Socioeconomic Dataset          : PASS
SQLite Database                : PASS
SCHOOLS Table                  : PASS
CHICAGO_SOCIOECONOMIC_DATA     : PASS

Problem 01                    : PASS
Problem 02                    : PASS
Problem 03                    : PASS
Problem 04                    : PASS
Problem 05                    : PASS
Problem 06                    : PASS
Problem 07                    : PASS
Problem 08                    : PASS
Problem 09                    : PASS
Problem 10                    : PASS
Problem 11                    : PASS
Problem 12                    : PASS

Final Validation               : PASS

STATUS: COMPLETED
============================================================
```
