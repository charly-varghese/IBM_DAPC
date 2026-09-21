# Lab 03 — Analyzing a Real-World Data Set

## IBM Data Analyst Professional Certificate

**Course 06:** Databases and SQL for Data Science with Python  
**Module 04:** Accessing Databases Using Python  
**Lab:** Analyzing a Real-World Data Set

---

## 1. Overview

This lab demonstrates an end-to-end data analytics workflow using a real-world socioeconomic dataset from the City of Chicago Open Data platform.

The project integrates:

- Python
- Pandas
- SQLite
- SQL
- Matplotlib
- Statistical correlation analysis

The dataset is first stored locally for reproducibility, loaded into Pandas, transferred into a SQLite database, analyzed using SQL, and finally visualized and statistically evaluated using Python.

---

## 2. Learning Objectives

By completing this lab, the following skills were practiced:

- Connect Python to a SQLite database
- Create and access SQLite tables
- Load CSV data using Pandas
- Transfer Pandas DataFrames into SQLite
- Execute SQL queries from Python
- Filter and aggregate real-world data
- Use SQL subqueries
- Retrieve SQL results into Pandas
- Create data visualizations using Matplotlib
- Calculate Pearson correlation
- Interpret relationships between socioeconomic variables
- Apply reproducible file-path practices
- Debug Python environment and data-source issues

---

## 3. Dataset

### Chicago Socioeconomic Data

The dataset contains socioeconomic indicators for Chicago community areas.

### Dataset Source

Chicago Open Data:

```text
https://data.cityofchicago.org/resource/jcxq-k9xf.csv
For reproducibility, the dataset was downloaded and stored locally.

Local Dataset
data/chicago_socioeconomic_data.csv
Dataset Dimensions
Rows:    78
Columns: 9
Columns
ca
community_area_name
percent_of_housing_crowded
percent_households_below_poverty
percent_aged_16_unemployed
percent_aged_25_without_high_school_diploma
percent_aged_under_18_or_over_64
per_capita_income_
hardship_index

Schema Note: The actual dataset uses per_capita_income_ with a trailing underscore. All SQL queries therefore use the actual column name.

4. Project Structure
Lab_03_Analyzing_a_Real_World_Data_Set/
│
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 04_Debug_Notes.md
├── README.md
│
├── socioeconomic.db
│
└── data/
    └── chicago_socioeconomic_data.csv
5. Technology Stack
Technology Purpose
Python 3.14 Programming language
Pandas 3.0.5 Data loading and analysis
SQLite Relational database
SQL Data querying and analysis
Matplotlib Data visualization
VS Code Development environment
Python .venv Isolated project environment
6. End-to-End Data Workflow
Chicago Open Data
       │
       ▼
Local CSV Dataset
       │
       ▼
Pandas DataFrame
       │
       ▼
SQLite Database
       │
       ▼
SQL Analysis
       │
       ▼
Pandas DataFrame
       │
       ▼
Visualization
       │
       ▼
Statistical Analysis
7. SQLite Database

Database:

socioeconomic.db

Table:

chicago_socioeconomic_data

The Pandas DataFrame was imported into SQLite using:

df.to_sql(
    "chicago_socioeconomic_data",
    con,
    if_exists="replace",
    index=False
)

The resulting table was verified using SQL.

Verification
SELECT COUNT(*)
FROM chicago_socioeconomic_data;

Result:

78
8. IBM Lab Analysis

The IBM lab contains six analytical problems.

Problem 1 — Count the Number of Rows
SQL
SELECT COUNT(*)
FROM chicago_socioeconomic_data;
Result
78

Status: PASS

Problem 2 — Community Areas with Hardship Index > 50
SQL
SELECT COUNT(*)
FROM chicago_socioeconomic_data
WHERE hardship_index > 50;
Result
38 community areas

Status: PASS

Problem 3 — Maximum Hardship Index
SQL
SELECT MAX(hardship_index)
FROM chicago_socioeconomic_data;
Result
98.0

Status: PASS

Problem 4 — Community Area with Highest Hardship Index

A SQL subquery was used to identify the community corresponding to the maximum hardship value.

SQL
SELECT community_area_name, hardship_index
FROM chicago_socioeconomic_data
WHERE hardship_index = (
    SELECT MAX(hardship_index)
    FROM chicago_socioeconomic_data
);
Result
Community Area: Riverdale
Hardship Index: 98.0

Status: PASS

Problem 5 — Communities with Per Capita Income > $60,000
SQL
SELECT
    community_area_name,
    per_capita_income_
FROM chicago_socioeconomic_data
WHERE per_capita_income_ > 60000;
Results
Community Area Per Capita Income
Lake View $60,058
Lincoln Park $71,551
Near North Side $88,669
Loop $65,526
Result
4 community areas

Status: PASS

9. Problem 6 — Income vs Hardship Analysis

The analysis examined the relationship between:

Per Capita Income
        vs
Hardship Index

Only rows containing valid values for both variables were used.

WHERE per_capita_income_ IS NOT NULL
  AND hardship_index IS NOT NULL
Valid observations
77

The original dataset contains 78 rows, but one observation does not contain valid values for both variables.

Scatter Plot

A Matplotlib scatter plot was created with:

X-axis → Per Capita Income
Y-axis → Hardship Index

The plot showed a clear downward relationship.

Pearson Correlation

The Pearson correlation coefficient was calculated using Pandas.

Result
r = -0.8491674629307862

Rounded:

r ≈ -0.8492
Interpretation

The result indicates a strong negative linear correlation between per-capita income and hardship index.

In general:

Higher Per Capita Income
            ↓
Lower Hardship Index

This means Chicago community areas with higher per-capita income generally tend to have lower hardship index values.

Statistical caution: Correlation indicates association, not causation. This analysis does not establish that higher income directly causes lower hardship.

10. My Practice — Analyst-Level Extensions

The IBM problems were extended into an independent practice analysis in:

02_My_Practice.py

Additional analysis included:

Ranking
Top 10 communities by income
Bottom 10 communities by income
Top 10 communities by hardship
Descriptive Statistics
Minimum income
Maximum income
Average income
Minimum hardship
Maximum hardship
Average hardship
Conditional Analysis

Examples:

High Income + Low Hardship
High Hardship + Low Income
Derived Analytical Metric

A custom socioeconomic priority score was created for practice:

Priority Score
=
Hardship Index × 100000 / Per Capita Income

This was used only as an educational analytical exercise and is not an official Chicago socioeconomic metric.

SQL → Pandas

SQL query results were loaded into Pandas for further analysis and visualization.

11. Key SQL Concepts Practiced
SELECT
WHERE
AND
ORDER BY
ASC
DESC
LIMIT
COUNT()
MIN()
MAX()
AVG()
IS NOT NULL
Subqueries
Calculated expressions
12. Key Python Concepts Practiced
Database Connection
sqlite3.connect()
Cursor Operations
con.cursor()
cur.execute()
fetchone()
fetchall()
Pandas
pd.read_csv()
pd.read_sql_query()
DataFrame
corr()
Visualization
plt.scatter()
plt.bar()
plt.xlabel()
plt.ylabel()
plt.title()
plt.grid()
plt.tight_layout()
plt.show()
13. Reproducibility

The project uses script-relative paths rather than relying on the current working directory.

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "socioeconomic.db"

CSV_PATH = BASE_DIR / "data" / "chicago_socioeconomic_data.csv"

This makes the project more portable and reduces path-related execution errors.

14. Debugging Highlights

Several real-world development issues were encountered and resolved.

Issue 1 — Incorrect Python Interpreter

VS Code initially selected:

C:\Python314\python.exe

instead of the project virtual environment.

This caused:

ModuleNotFoundError: No module named 'pandas'
Resolution

The correct interpreter was selected:

.venv (3.14.0.final.0)
Issue 2 — External API HTTP 503

The Chicago Open Data API temporarily returned:

HTTP Error 503: Service Unavailable
Resolution

The dataset was downloaded locally and used as the reproducible project source.

Issue 3 — Column Name Difference

The actual dataset contained:

per_capita_income_

rather than:

per_capita_income

The actual schema was verified before writing SQL queries.

Issue 4 — Database Path

The original database connection depended on the current working directory.

It was replaced with a script-relative path using pathlib.

Issue 5 — Missing Values

The dataset contains 78 rows, but only 77 rows contain both valid income and hardship values.

Explicit IS NOT NULL filtering was therefore applied before correlation analysis.

15. Key Analytical Findings
Metric Result
Total community records 78
Hardship Index > 50 38
Maximum Hardship Index 98.0
Highest hardship community Riverdale
Communities with income > $60,000 4
Valid income/hardship observations 77
Pearson correlation -0.8492
16. Data Analytics Interpretation

The analysis demonstrates a strong inverse relationship between income and hardship.

The Pearson coefficient:

-0.8492

indicates that the variables move in opposite directions with substantial linear association.

This provides an example of how a data analyst can combine:

SQL Querying
     +
Statistical Analysis
     +
Visualization

to derive meaningful insights from real-world data.

17. Professional Skills Demonstrated

This lab goes beyond basic SQL syntax and demonstrates an integrated analytics workflow:

Data Acquisition
       ↓
Data Validation
       ↓
Data Storage
       ↓
SQL Querying
       ↓
Data Transformation
       ↓
Statistical Analysis
       ↓
Visualization
       ↓
Insight Generation

These skills are directly applicable to:

Data Analyst
Business Analyst
BI Analyst
Junior Data Scientist
Analytics Engineer
18. Final Learning Outcomes

After completing this lab, the following workflow can be performed independently:

Obtain a real-world dataset.
Validate its structure.
Store it locally for reproducibility.
Load it into Pandas.
Create a SQLite database.
Import the dataset into SQLite.
Verify database integrity.
Execute SQL analytical queries.
Use SQL subqueries.
Retrieve SQL results into Pandas.
Create analytical visualizations.
Calculate Pearson correlation.
Interpret statistical relationships.
Document debugging and reproducibility practices.
19. Completion Status
Environment Setup              : COMPLETE
Dataset Acquisition            : COMPLETE
Dataset Validation             : COMPLETE
SQLite Database Creation       : COMPLETE
SQLite Verification            : COMPLETE
IBM Problem 1                  : COMPLETE
IBM Problem 2                  : COMPLETE
IBM Problem 3                  : COMPLETE
IBM Problem 4                  : COMPLETE
IBM Problem 5                  : COMPLETE
IBM Problem 6                  : COMPLETE
My Practice                    : COMPLETE
Debug Documentation            : COMPLETE
README Documentation           : COMPLETE
```
