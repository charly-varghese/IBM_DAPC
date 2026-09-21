# Lab 02 — Built-in Functions

## IBM Data Analyst Professional Certificate

**Course 06:** Databases and SQL for Data Science with Python  
**Module 03:** Intermediate SQL  
**Lab 02:** Built-in Functions

---

## 📌 Lab Overview

This lab focuses on using SQL built-in functions to analyze and transform data.

The practical work was completed using a local SQLite database containing animal rescue data.

The lab covered:

- Aggregate Functions
- Scalar Functions
- String Functions
- Date Functions
- Date Calculations
- Filtering with Functions
- GROUP BY
- HAVING
- ORDER BY
- LIMIT

---

## 🎯 Learning Objectives

By completing this lab, I practiced how to:

- Calculate totals using `SUM()`.
- Count records using `COUNT()`.
- Calculate averages using `AVG()`.
- Find minimum and maximum values using `MIN()` and `MAX()`.
- Round numerical values using `ROUND()`.
- Convert text to uppercase using `UPPER()`.
- Convert text to lowercase using `LOWER()`.
- Calculate text length using `LENGTH()`.
- Extract day, month, and year from dates.
- Perform date calculations in SQLite.
- Calculate dates before and after a given date.
- Filter records using built-in functions.
- Group data using `GROUP BY`.
- Filter aggregated data using `HAVING`.
- Identify highest and lowest values using `ORDER BY` and `LIMIT`.

---

## 🛠️ Technologies Used

- VS Code
- Python
- SQLite
- SQL
- GitHub

---

## 📂 Project Structure

```text
Lab_02_Built_in_Functions/
│
├── database/
│   └── PETRESCUE.db
│
├── data/
│   └── PETRESCUE.csv
│
├── sql/
│   └── Script_Create_PETRESCUE.sql
│
├── 01_setup_database.py
├── 02_verify_database.py
├── run_sql.py
│
├── 01_IBM_Lab.sql
├── 02_My_Practice.sql
├── 03_Challenge.sql
│
├── 04_Debug_Notes.md
└── README.md
```

---

## 🗄️ Database Information

**Database Name:** `PETRESCUE.db`

**Table Name:** `PETRESCUE`

The database contains **9 rescue records**.

## Table Structure

| Column | Data Type | Description |
| ------ | --------- | ----------- |

| ID | INTEGER | Unique rescue record ID |
| ANIMAL | VARCHAR(20) | Type of animal rescued |
| QUANTITY | INTEGER | Number of animals rescued |
| COST | DECIMAL(6,2) | Rescue cost |
| RESCUEDATE | DATE | Date of rescue |

---

## ▶️ How to Run the Lab

## 1. Create the Database

```powershell
python 01_setup_database.py
```

This creates:

```text
database/PETRESCUE.db
```

---

## 2. Verify the Database

```powershell
python 02_verify_database.py
```

Expected verification:

```text
Total Records: 9

PETRESCUE Table:
ID
ANIMAL
QUANTITY
COST
RESCUEDATE
```

---

## 3. Run the IBM Lab

```powershell
python run_sql.py 01_IBM_Lab.sql
```

---

## 4. Run My Practice Queries

```powershell
python run_sql.py 02_My_Practice.sql
```

---

## 5. Run Challenge Queries

```powershell
python run_sql.py 03_Challenge.sql
```

---

## 🧠 SQL Concepts Practiced

## 1. Aggregate Functions

Aggregate functions summarize data from multiple rows.

### Functions Used

```sql
COUNT()
SUM()
AVG()
MIN()
MAX()
```

Example:

```sql
SELECT
    SUM(COST) AS TOTAL_COST
FROM
    PETRESCUE;
```

---

## 2. ROUND()

The `ROUND()` function controls the number of decimal places.

Example:

```sql
SELECT
    ROUND(COST, 2)
FROM
    PETRESCUE;
```

For financial calculations:

```sql
SELECT
    ROUND(
        SUM(COST),
        2
    ) AS TOTAL_COST
FROM
    PETRESCUE;
```

---

## 3. String Functions

The following string functions were practiced:

```sql
UPPER()
LOWER()
LENGTH()
```

Example:

```sql
SELECT
    ANIMAL,
    UPPER(ANIMAL) AS ANIMAL_UPPERCASE
FROM
    PETRESCUE;
```

---

## 4. Date Functions in SQLite

SQLite uses `strftime()` to extract date components.

### Extract Day

```sql
strftime('%d', RESCUEDATE)
```

### Extract Month

```sql
strftime('%m', RESCUEDATE)
```

### Extract Year

```sql
strftime('%Y', RESCUEDATE)
```

---

## 5. Date Arithmetic

SQLite uses the `date()` function with modifiers.

### Add Days

```sql
date(
    RESCUEDATE,
    '+7 days'
)
```

### Subtract Days

```sql
date(
    RESCUEDATE,
    '-3 days'
)
```

### Add Months

```sql
date(
    RESCUEDATE,
    '+2 months'
)
```

### Add Years

```sql
date(
    RESCUEDATE,
    '+1 year'
)
```

---

## 🔄 SQL Compatibility Learning

The IBM lab concepts were adapted from MySQL-style syntax to SQLite.

| Operation | MySQL Style | SQLite Style |
| --------- | ----------- | ------------ |

| Extract Day | `DAY(date)` | `strftime('%d', date)` |
| Extract Month | `MONTH(date)` | `strftime('%m', date)` |
| Extract Year | `YEAR(date)` | `strftime('%Y', date)` |
| Add Days | `DATE_ADD()` | `date()` |
| Date Difference | `DATEDIFF()` | `julianday()` |

Example SQLite date difference:

```sql
CAST(
    julianday('now')
    -
    julianday(RESCUEDATE)
    AS INTEGER
)
```

---

## 📊 Key Results

## Rescue Summary

| Metric | Result |
| ------ | -----: |

| Total Rescue Records | 9 |
| Total Animals Rescued | 49 |
| Total Rescue Cost | 1718.24 |
| Average Rescue Cost | 190.92 |
| Minimum Rescue Cost | 44.44 |
| Maximum Rescue Cost | 666.66 |

---

## Highest Cost Rescue

```text
Animal: Dog
Cost: 666.66
```

---

## Lowest Cost Rescue

```text
Animal: Cat
Cost: 44.44
```

---

## Rescues in June 2018

```text
8 rescues
```

---

## 💡 Professional SQL Learnings

### 1. Round Financial Values

Floating-point calculations may produce values such as:

```text
1064.6299999999999
```

For reporting, use:

```sql
ROUND(
    SUM(COST),
    2
)
```

Result:

```text
1064.63
```

---

### 2. WHERE vs HAVING

```text
WHERE  → Filters individual rows before grouping.

HAVING → Filters grouped results after aggregation.
```

Example:

```sql
SELECT
    ANIMAL,
    SUM(COST)
FROM
    PETRESCUE
GROUP BY
    ANIMAL
HAVING
    SUM(COST) > 200;
```

---

### 3. Finding Top and Bottom Values

Highest value:

```sql
ORDER BY
    COST DESC
LIMIT
    1;
```

Lowest value:

```sql
ORDER BY
    COST ASC
LIMIT
    1;
```

This pattern can be used for:

- Highest sale
- Lowest sale
- Most expensive product
- Cheapest product
- Top customer
- Top performing category

---

## 🐛 Debugging Notes

No SQL execution errors occurred during the lab.

### Runner Observation

The reusable SQL runner splits SQL statements using:

```python
statements = sql_script.split(";")
```

Because of this, final comment blocks such as:

```sql
-- END OF CHALLENGES
```

may appear as an additional query.

The output:

```text
Rows affected: -1
```

was not an SQL error.

All actual SQL queries executed successfully.

Detailed debugging notes are available in:

```text
04_Debug_Notes.md
```

---

## 📁 Files Included

| File | Purpose |
| ---- | ------- |

| `01_setup_database.py` | Creates the PETRESCUE database |
| `02_verify_database.py` | Verifies database records and structure |
| `run_sql.py` | Reusable SQL execution tool |
| `01_IBM_Lab.sql` | IBM lab implementation |
| `02_My_Practice.sql` | Additional SQL practice |
| `03_Challenge.sql` | Challenge queries |
| `04_Debug_Notes.md` | Debugging notes and learning observations |
| `README.md` | Lab documentation |

---

## 🏆 Lab Completion Status

```text
==================================================

LAB 02 — BUILT-IN FUNCTIONS

==================================================

Database Setup             : COMPLETED ✅
Database Verification      : COMPLETED ✅
IBM Lab                    : COMPLETED ✅
IBM Practice Questions     : COMPLETED ✅
My Practice                : COMPLETED ✅
Challenge Queries          : COMPLETED ✅
Debug Notes                : COMPLETED ✅
README Documentation       : COMPLETED ✅

SQL Errors                 : 0

OVERALL STATUS             : COMPLETED SUCCESSFULLY ✅

==================================================
```

---

## 🚀 Next Lab

\*_Module 03 — Intermediate SQL_

### Lab 03: Sub-queries and Nested SELECTs

Next, the focus will move from single-table SQL queries to more advanced SQL analysis using:

- Subqueries
- Nested SELECT statements
- Scalar subqueries
- Column expressions with subqueries
- Subqueries in `WHERE`
- Subqueries in `FROM`
- Multi-step analytical queries

---

**IBM Data Analyst Professional Certificate — Course 06**  
**Module 03: Intermediate SQL**  
**Lab 02: Built-in Functions — Completed Successfully**
