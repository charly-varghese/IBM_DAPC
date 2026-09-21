# Debug Notes — Lab 03

## Analyzing a Real-World Data Set

**Course:** IBM Data Analyst Professional Certificate  
**Course 06:** Databases and SQL for Data Science with Python  
**Module 04:** Accessing Databases Using Python  
**Lab:** Lab 03 — Analyzing a Real-World Data Set

---

## 1. Lab Overview

This lab demonstrates an end-to-end data analysis workflow using:

- Python
- Pandas
- SQLite
- SQL
- Matplotlib
- Pearson correlation

The Chicago socioeconomic dataset was loaded from the Chicago Open Data source, stored locally for reproducibility, imported into SQLite, analyzed using SQL, and visualized using Python.

---

## 2. Debug Issue — Wrong Python Interpreter in VS Code

## Symptom

Running `01_IBM_Lab.py` initially produced:

```text
ModuleNotFoundError: No module named 'pandas'
``
Cause

VS Code was using the system Python interpreter:

C:\Python314\python.exe

instead of the project's virtual environment.

The required Pandas package was installed in:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\
Diagnosis

The correct environment was verified using:

python --version
python -c "import pandas as pd; print(pd._version__)"

Result:

Pandas: 3.0.5

The Python executable was:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\python.exe
Fix

The VS Code Python interpreter was changed to:

.venv (3.14.0.final.0)

The virtual environment was also activated manually when required:

d:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\activate.bat
Lesson Learned

Always verify the active Python interpreter before debugging a package-related error.

Useful checks:

where python
python --version
python -c "import pandas as pd; print(pd._version__)"
3. Debug Issue — Chicago Open Data API Returned HTTP 503
Symptom

The live dataset URL initially worked:

https://data.cityofchicago.org/resource/jcxq-k9xf.csv

but a later execution produced:

urllib.error.HTTPError: HTTP Error 503: Service Unavailable
Cause

HTTP 503 means the remote service was temporarily unavailable.

The problem was not caused by:

Python
Pandas
SQLite
the SQL queries
the dataset-processing code
Fix

The dataset was downloaded once and stored locally:

data/chicago_socioeconomic_data.csv

The download was verified as:

78 rows x 9 columns

The script was then changed to read the local file.

Lesson Learned

For reproducible portfolio projects, analysis should not depend unnecessarily on a live external API.

A local project dataset provides:

reproducibility
stability
faster execution
protection against temporary API outages
easier GitHub project setup
4. Debug Issue — Actual Dataset Column Name
Observation

The actual Chicago dataset contained:

per_capita_income_

with a trailing underscore.

The complete column list was:

[
    'ca',
    'community_area_name',
    'percent_of_housing_crowded',
    'percent_households_below_poverty',
    'percent_aged_16_unemployed',
    'percent_aged_25_without_high_school_diploma',
    'percent_aged_under_18_or_over_64',
    'per_capita_income_',
    'hardship_index'
]
Potential Problem

Using:

per_capita_income

instead of:

per_capita_income_

would result in an SQL error because the actual SQLite column name contains the trailing underscore.

Fix

All SQL queries were written using the actual schema:

per_capita_income_
Lesson Learned

Never assume column names.

Always inspect the schema first:

print(df.columns.tolist())

or:

PRAGMA table_info(chicago_socioeconomic_data);
5. Debug Improvement — Script-Relative File Paths
Initial Approach

The database was initially created using:

sqlite3.connect("socioeconomic.db")

This depends on the current working directory.

Potential Problem

If the script is executed from another directory, SQLite may create or open the database in a different location.

Professional Fix

The project directory was determined using:

BASE_DIR = Path(_file__).resolve().parent

The database path was then defined as:

DB_PATH = BASE_DIR / "socioeconomic.db"

The CSV path was defined as:

CSV_PATH = BASE_DIR / "data" / "chicago_socioeconomic_data.csv"

The database connection became:

con = sqlite3.connect(DB_PATH)

and the dataset loading became:

df = pd.read_csv(CSV_PATH)
Lesson Learned

Script-relative paths make Python projects more portable and reproducible.

6.Debug Issue — SQLite Data Verification

After importing the Pandas DataFrame into SQLite, the table was verified using:

SELECT COUNT(*)
FROM chicago_socioeconomic_data;

Result:

78

The first five records were also verified.

This confirmed:

CSV
 ↓
Pandas
 ↓
SQLite

was successful.

7.Debug Issue — 77 Rows Used for Correlation
Observation

The original dataset contained:

78 rows

However, the scatter plot preparation reported:

Rows: 77
Cause

The analysis intentionally used:

WHERE per_capita_income_IS NOT NULL
  AND hardship_index IS NOT NULL

This removes rows where either variable required for the scatter plot is missing.

Therefore:

Total dataset rows = 78
Valid income/hardship pairs = 77
Lesson Learned

Different analytical operations may legitimately use different row counts.

For correlation and scatter plots, both variables must have valid values.

Missing-value handling should therefore be explicit.

8.Problem 1 — Row Count

SQL:

SELECT COUNT(*)
FROM chicago_socioeconomic_data;

Result:

78

Status:

PASS
1. Problem 2 — Hardship Index Greater Than 50

SQL:

SELECT COUNT(*)
FROM chicago_socioeconomic_data
WHERE hardship_index > 50;

Result:

38

Status:

PASS
10. Problem 3 — Maximum Hardship Index

SQL:

SELECT MAX(hardship_index)
FROM chicago_socioeconomic_data;

Result:

98.0

Status:

PASS
11. Problem 4 — Community with Highest Hardship

A subquery was used:

SELECT community_area_name, hardship_index
FROM chicago_socioeconomic_data
WHERE hardship_index = (
    SELECT MAX(hardship_index)
    FROM chicago_socioeconomic_data
);

Result:

Community Area: Riverdale
Hardship Index: 98.0

Status:

PASS
12. Problem 5 — Per Capita Income Greater Than $60,000

SQL:

SELECT community_area_name, per_capita_income_
FROM chicago_socioeconomic_data
WHERE per_capita_income_ > 60000;

Results:

Lake View       60058
Lincoln Park    71551
Near North Side 88669
Loop            65526

Number of qualifying community areas:

4

Status:

PASS
13. Problem 6 — Correlation Analysis

The required variables were extracted from SQLite:

SELECT
    per_capita_income_,
    hardship_index
FROM chicago_socioeconomic_data
WHERE per_capita_income_IS NOT NULL
  AND hardship_index IS NOT NULL;

Valid observations:

77

A scatter plot was created using Matplotlib.

The Pearson correlation coefficient was calculated using Pandas:

correlation = plot_df["per_capita_income"].corr(
    plot_df["hardship_index"]
)

Result:

-0.8491674629307862

Rounded:

r = -0.8492
Interpretation

The result indicates a strong negative linear correlation between:

Per Capita Income
Hardship Index

In general:

Higher Per Capita Income
            ↓
Lower Hardship Index
Important Statistical Note

Correlation does not establish causation.

The result demonstrates a strong statistical association between the two variables, but it does not prove that higher income directly causes lower hardship.

Status:

PASS
14. Final Verification

The complete 01_IBM_Lab.py was executed successfully using the project virtual environment.

Final environment:

Python: Project .venv
Pandas: 3.0.5
SQLite: Working

All six IBM problems executed successfully.

15.Final Lab Results
Problem Result Status
Number of rows 78 PASS
Hardship Index > 50 38 PASS
Maximum Hardship Index 98.0 PASS
Highest Hardship Community Riverdale PASS
Income > $60,000 4 communities PASS
Valid correlation observations 77 PASS
Pearson correlation-0.8492 PASS
16.Key Debugging Lessons
Environment Management

Always verify:

Python interpreter
Virtual environment
Installed packages

before debugging application code.

Data Source Reliability

External APIs can temporarily fail.

For reproducible analysis:

Download → Validate → Store locally → Analyze
Schema Awareness

Always inspect actual column names before writing SQL.

File Path Management

Prefer:

Path(_file_).resolve().parent

for portable project paths.

Missing Data

Always understand why the number of rows changes during analysis.

Statistical Interpretation

A correlation coefficient describes association, not causation.

17.Lab 03 Debug Status
Environment Debugging       : COMPLETE
Data Source Debugging       : COMPLETE
Schema Verification         : COMPLETE
SQLite Verification         : COMPLETE
SQL Problem Verification   : COMPLETE
Visualization Verification : COMPLETE
Correlation Verification   : COMPLETE
Documentation              : COMPLETE

```
