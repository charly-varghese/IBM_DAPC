# Debug Notes — Lab 02: Built-in Functions

## IBM Data Analyst Professional Certificate

**Course 06:** Databases and SQL for Data Science with Python  
**Module 03:** Intermediate SQL  
**Lab 02:** Built-in Functions  
**Database:** PETRESCUE.db  
**Database Engine:** SQLite

---

## 1. Lab Execution Status

| Section | Status |
| ------- | ------ |

| Database Setup | ✅ Completed |
| Database Verification | ✅ Completed |
| IBM Lab Queries | ✅ Completed |
| IBM Practice Questions | ✅ Completed |
| My Practice Queries | ✅ Completed |
| Challenge Queries | ✅ Completed |
| SQL Errors | ✅ None |
| Overall Lab Status | 🟢 Successful |

---

## 2. Database Setup Verification

The PETRESCUE database was created successfully.

Database file:

```text
database/PETRESCUE.db
The PETRESCUE table contained:

9 records

Verified columns:

Column Data Type
ID INTEGER
ANIMAL VARCHAR(20)
QUANTITY INTEGER
COST DECIMAL(6,2)
RESCUEDATE DATE

Database verification completed successfully.

3. Key Learning Areas

This lab focused on SQL built-in functions.

The main categories practiced were:

Aggregation Functions
Scalar Functions
String Functions
Date Functions
Date Calculations
Filtering with Functions
GROUP BY with Functions
HAVING with Aggregate Functions
Professional Data Formatting
4. Aggregation Functions Practiced

The following aggregate functions were successfully used:

COUNT()
SUM()
AVG()
MIN()
MAX()

Examples:

SELECT
    SUM(COST)
FROM
    PETRESCUE;
SELECT
    AVG(COST)
FROM
    PETRESCUE;
SELECT
    MIN(COST),
    MAX(COST)
FROM
    PETRESCUE;
Important Learning

Aggregate functions summarize multiple rows into calculated results.

Examples:

COUNT() → Counts records.
SUM() → Adds values.
AVG() → Calculates the average.
MIN() → Finds the smallest value.
MAX() → Finds the largest value.
5. ROUND() Function

The ROUND() function was used to control decimal values.

Example:

SELECT
    ROUND(COST)
FROM
    PETRESCUE;

Example with decimal precision:

SELECT
    ROUND(COST, 2)
FROM
    PETRESCUE;
Professional Lesson

Currency calculations can sometimes produce long floating-point values.

Example observed:

1064.6299999999999

This happened when calculating:

SUM(COST)

for dog rescues.

The professional solution is:

SELECT
    ROUND(
        SUM(COST),
        2
    )
FROM
    PETRESCUE;

Result:

1064.63
Debug Learning

This was not a database error.

It was a floating-point precision behavior.

For financial reporting, calculated values should be rounded appropriately.

6. String Functions Practiced

The following string functions were successfully used:

UPPER()
LOWER()
LENGTH()

Example:

SELECT
    UPPER(ANIMAL)
FROM
    PETRESCUE;

Example:

SELECT
    LOWER(ANIMAL)
FROM
    PETRESCUE;

Example:

SELECT
    LENGTH(ANIMAL)
FROM
    PETRESCUE;
Learning

String functions allow SQL queries to transform and analyze text values.

Examples:

Cat → CAT
Dog → dog
Goldfish → Length 8
7. Case-Insensitive Filtering

The following query was used:

SELECT
    *
FROM
    PETRESCUE
WHERE
    LOWER(ANIMAL) = 'cat';
Why This Is Useful

The stored value might contain:

Cat
CAT
cat

Using:

LOWER(ANIMAL)

converts the value to lowercase before comparison.

This makes the query more consistent.

8. DISTINCT Query Formatting

During My Practice, the following syntax executed successfully:

SELECT
    DISTINCT LOWER(ANIMAL) AS ANIMAL_NAME
FROM
    PETRESCUE;

However, the clearer and more standard professional style is:

SELECT DISTINCT
    LOWER(ANIMAL) AS ANIMAL_NAME
FROM
    PETRESCUE;
Preferred Style

Use:

SELECT DISTINCT

instead of placing DISTINCT on the next line after SELECT.

Both may execute correctly depending on formatting and SQL parsing, but the second format is clearer and easier to read.

9. Date Functions in SQLite

The IBM lab used SQL date functions that required adaptation for SQLite.

Examples:

Concept IBM / MySQL Style SQLite Style
Day DAY(date) strftime('%d', date)
Month MONTH(date) strftime('%m', date)
Year YEAR(date) strftime('%Y', date)

Example:

SELECT
    strftime(
        '%d',
        RESCUEDATE
    ) AS RESCUE_DAY
FROM
    PETRESCUE;

Month:

SELECT
    strftime(
        '%m',
        RESCUEDATE
    ) AS RESCUE_MONTH
FROM
    PETRESCUE;

Year:

SELECT
    strftime(
        '%Y',
        RESCUEDATE
    ) AS RESCUE_YEAR
FROM
    PETRESCUE;
10. SQLite Date Arithmetic

SQLite uses the date() function with modifiers.

Example:

SELECT
    date(
        RESCUEDATE,
        '+3 days'
    )
FROM
    PETRESCUE;

Other examples practiced:

'+7 days'
'+14 days'
'-3 days'
'-1 month'
'+2 months'
'+1 year'
Examples

Add 7 days:

date(
    RESCUEDATE,
    '+7 days'
)

Subtract one month:

date(
    RESCUEDATE,
    '-1 month'
)

Add one year:

date(
    RESCUEDATE,
    '+1 year'
)
11. Date Difference Calculation

The IBM/MySQL concept:

DATEDIFF(
    CURRENT_DATE,
    RESCUEDATE
)

was adapted for SQLite.

SQLite solution:

CAST(
    julianday('now')
    -
    julianday(RESCUEDATE)
    AS INTEGER
)
Learning

SQLite does not use the same DATEDIFF() syntax as MySQL.

Instead:

julianday()

converts dates into Julian day numbers.

Subtracting the values gives the difference in days.

12. GROUP BY with Aggregate Functions

The following type of query was practiced:

SELECT
    ANIMAL,
    SUM(QUANTITY)
FROM
    PETRESCUE
GROUP BY
    ANIMAL;

This produced totals for each animal type.

Example results included:

Cat       → 10 animals
Dog       → 7 animals
Goldfish  → 24 animals
Hamster   → 6 animals
Parrot    → 2 animals
13. HAVING with Aggregate Functions

HAVING was used to filter grouped results.

Example:

SELECT
    ANIMAL,
    SUM(COST) AS TOTAL_COST
FROM
    PETRESCUE
GROUP BY
    ANIMAL
HAVING
    SUM(COST) > 200;
Important Rule
WHERE  → Filters rows before grouping.
HAVING → Filters groups after grouping.

This is an important SQL concept.

14. Challenge Learning

The Challenge section combined multiple concepts.

Examples included:

Aggregation Functions
ROUND()
UPPER()
strftime()
date()
GROUP BY
HAVING
ORDER BY
LIMIT

This helped transform individual SQL concepts into more realistic analytical queries.

15. Highest and Lowest Value Analysis

The highest cost rescue was found using:

ORDER BY
    COST DESC
LIMIT
    1;

Result:

Dog
Cost: 666.66

The lowest cost rescue was found using:

ORDER BY
    COST ASC
LIMIT
    1;

Result:

Cat
Cost: 44.44
Professional Learning

This pattern is commonly used for:

Highest Sale
Lowest Sale
Top Customer
Most Expensive Product
Least Expensive Product
Top Performing Category
16. Important Challenge Results
Total Rescue Summary
Total Rescue Records      : 9
Total Animals Rescued     : 49
Total Rescue Cost         : 1718.24
Average Rescue Cost       : 190.92
Minimum Rescue Cost       : 44.44
Maximum Rescue Cost       : 666.66
17. June 2018 Analysis

The following query counted rescues in June 2018:

SELECT
    COUNT(*)
FROM
    PETRESCUE
WHERE
    strftime(
        '%Y-%m',
        RESCUEDATE
    ) = '2018-06';

Result:

8 rescues
Learning

Using:

strftime('%Y-%m', date_column)

allows month and year-based filtering in SQLite.

18. SQL Runner Observation

The current run_sql.py script splits SQL statements using:

statements = sql_script.split(";")

Because of this approach, the final comment section:

-- END OF MY PRACTICE

or:

-- END OF CHALLENGES

was processed as an additional query.

The output showed:

Rows affected: -1
Important

This was not an SQL error.

The actual SQL queries executed successfully.

Future Improvement

The SQL runner could later be improved to:

Ignore comment-only statements.
Skip statements that do not contain executable SQL.
Display only real SQL query numbers.

For the current lab, the runner worked correctly for all learning purposes.

19. Final Debug Status
Database Errors              : 0
SQL Syntax Errors            : 0
Execution Failures           : 0
IBM Lab Completion           : Successful
My Practice Completion       : Successful
Challenge Completion         : Successful
Database Verification        : Successful
20. Master Takeaways

The most important concepts learned in Lab 02 are:

1. Aggregate functions summarize data.

2. Scalar functions transform individual values.

3. ROUND() is important for professional financial reporting.

4. UPPER(), LOWER(), and LENGTH() manipulate text data.

5. SQLite date functions differ from MySQL functions.

6. strftime() extracts date components in SQLite.

7. date() performs date arithmetic in SQLite.

8. julianday() can calculate date differences.

9. GROUP BY creates category-level summaries.

10. HAVING filters aggregated groups.

11. ORDER BY + LIMIT is useful for top and bottom analysis.

12. Functions can be combined to create professional analytical queries.
21. Lab Completion Status
==================================================
LAB 02 — BUILT-IN FUNCTIONS
==================================================

Database Setup             : COMPLETED
Database Verification      : COMPLETED
IBM Lab                    : COMPLETED
IBM Practice Questions     : COMPLETED
My Practice                : COMPLETED
Challenge Queries          : COMPLETED
Debug Notes                : COMPLETED

Overall Status             : SUCCESSFULLY COMPLETED
```
