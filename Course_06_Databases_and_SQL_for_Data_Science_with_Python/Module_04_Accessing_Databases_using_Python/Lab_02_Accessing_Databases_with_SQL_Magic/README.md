# README.md

## Lab 02 — Accessing Databases with SQL Magic

**IBM Data Analyst Professional Certificate**  
**Course 06 — Databases and SQL for Data Science with Python**  
**Module 04 — Accessing Databases Using Python**

---

## 📌 Lab Overview

This lab demonstrates how to access and analyze a SQLite database using **SQL Magic commands inside a Jupyter Notebook**.

The practical workflow integrates:

- SQL Magic (`%sql`, `%%sql`)
- SQLite
- Python
- Pandas
- Seaborn
- SQL aggregation
- Parameterized SQL queries

The lab demonstrates the complete workflow from connecting to a database and querying data to converting SQL results into a Pandas DataFrame and visualizing the results.

---

## 🎯 Learning Objectives

By completing this lab, I practiced how to:

1. Load the SQL Magic extension.
2. Connect to a SQLite database using SQL Magic.
3. Create database tables using SQL.
4. Insert records into a SQLite table.
5. Retrieve records using SQL queries.
6. Use parameterized SQL queries.
7. Perform aggregation using:
   - `COUNT()`
   - `SUM()`
   - `AVG()`
8. Group data using `GROUP BY`.
9. Sort aggregated results using `ORDER BY`.
10. Convert SQL Magic results into a Pandas DataFrame.
11. Create a visualization using Seaborn.
12. Interpret aggregated business data.

---

## 🗂️ Lab Structure

```text
Lab_02_Accessing_Databases_with_SQL_Magic/
│
├── 01_IBM_Lab.ipynb
├── 02_My_Practice.ipynb
├── 04_Debug_Notes.md
└── README.md
🛠️ Technologies & Tools
Tool / Technology Purpose
Python Programming and data analysis
Jupyter Notebook Interactive execution environment
SQL Magic Execute SQL directly from Jupyter
SQLite Relational database
Pandas Data manipulation and analysis
Seaborn Data visualization
Matplotlib Visualization support
VS Code Development environment
📦 Python Packages

The following packages were used:

ipython-sql
prettytable
pandas
seaborn
matplotlib
Important Environment Note

A compatibility issue was encountered between ipython-sql and newer PrettyTable versions.

A compatible PrettyTable version was used:

prettytable==3.10.2

Detailed troubleshooting is documented in:

04_Debug_Notes.md
🗄️ Practice Database

The independent practice used:

MY_SQL_MAGIC_PRACTICE.db

Main table:

SALES_PERFORMANCE
Table Structure
Column Description
employee_id Employee identifier
employee_name Employee name
department Employee department
city Employee city
sales_amount Sales amount
📊 Practice Dataset

The practice dataset contains 8 employee records across three departments:

Sales
Marketing
Finance

Example records:

Employee ID Employee Department City Sales
101 Arun Sales Kochi 125,000
102 Meera Sales Chennai 148,000
103 Rahul Marketing Bengaluru 98,000
104 Anita Sales Mumbai 172,000
105 Vivek Marketing Kochi 115,000
106 Priya Sales Delhi 156,000
107 Suresh Finance Chennai 87,000
108 Neha Marketing Mumbai 132,000
🔌 1. Loading SQL Magic

The SQL Magic extension was loaded using:

%load_ext sql

This enables SQL commands to be executed directly from Jupyter Notebook cells.

🔗 2. Connecting to SQLite

The practice database was connected using:

%sql sqlite:///MY_SQL_MAGIC_PRACTICE.db

The connection was validated by querying the SQLite metadata and counting records.

🔎 3. Querying Data

SQL Magic supports both line and cell magic commands.

Line Magic
%sql SELECT * FROM SALES_PERFORMANCE;
Cell Magic
%%sql
SELECT *
FROM SALES_PERFORMANCE;

Both approaches were practiced.

🎯 4. Parameterized SQL Query

A Python variable was passed into SQL using parameter substitution:

department = "Sales"

%sql SELECT * FROM SALES_PERFORMANCE WHERE department = :department

This returned the four Sales employees.

This demonstrates how Python variables can be integrated into SQL Magic queries.

📈 5. Department-Level Analysis

The following SQL aggregation was performed:

sales_summary = %sql SELECT department, SUM(sales_amount) AS total_sales, AVG(sales_amount) AS average_sales FROM SALES_PERFORMANCE GROUP BY department ORDER BY total_sales DESC

The SQL result was converted into a Pandas DataFrame:

sales_df = sales_summary.DataFrame()
Result
Department Total Sales Average Sales
Sales 601,000 150,250
Marketing 345,000 115,000
Finance 87,000 87,000
Key Observation

The Sales department generated the highest total sales:

601,000
📊 6. Visualization

The department-level sales results were visualized using Seaborn:

plt.figure(figsize=(8, 5))

sns.barplot(
    x="department",
    y="total_sales",
    data=sales_df
)

plt.title("Total Sales by Department")
plt.xlabel("Department")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

The visualization clearly showed the relative sales performance of the three departments.

🌍 7. City-Level Analysis

A second aggregation was performed to analyze sales performance by city:

city_analysis = %sql SELECT city, COUNT(*) AS employee_count, SUM(sales_amount) AS total_sales, AVG(sales_amount) AS average_sales FROM SALES_PERFORMANCE GROUP BY city ORDER BY total_sales DESC
Result
City Employees Total Sales Average Sales
Mumbai 2 304,000 152,000
Kochi  2 240,000  120,000
Chennai2 235,000 117,500
Delhi 1  156,000 156,000
Bengaluru 1 98,000 98,000
🧠 Business Insight

The city analysis demonstrates an important analytical distinction.

Highest Total Sales
Mumbai → 304,000

Mumbai generated the highest total sales.

Highest Average Sales
Delhi → 156,000

Delhi had the highest average sales per employee.

Therefore:

Highest Total Sales ≠ Highest Average Sales

This demonstrates why analysts should evaluate multiple metrics before drawing business conclusions.

🔄 End-to-End Workflow

The practical workflow can be summarized as:

Jupyter Notebook
       │
       ▼
Load SQL Magic
       │
       ▼
Connect to SQLite
       │
       ▼
Create / Access Table
       │
       ▼
Execute SQL Queries
       │
       ▼
Parameterized SQL
       │
       ▼
GROUP BY + Aggregation
       │
       ▼
SQL Result
       │
       ▼
Pandas DataFrame
       │
       ▼
Seaborn Visualization
       │
       ▼
Business Insights
🧪 Validation

The database was validated using:

%sql SELECT COUNT(*) AS record_count FROM SALES_PERFORMANCE;

Result:

record_count
------------
8

Therefore:

Database Connection       : PASS
Table Availability        : PASS
Record Count              : 8
SQL Magic                 : PASS
Parameterized Query       : PASS
Aggregation               : PASS
Pandas Conversion         : PASS
Visualization             : PASS
🐞 Debugging

Several practical debugging scenarios were encountered and resolved:

1. PrettyTable Compatibility
KeyError: 'DEFAULT'

Resolved by using a compatible PrettyTable version.

2. SQL Magic After Kernel Restart
UsageError: Cell magic `%%sql` not found

Resolved by reloading:

%load_ext sql
3. DataFrame Variable
NameError: name 'sales_df' is not defined

Resolved by separating SQL execution from DataFrame conversion.

4. VS Code Notebook Renderer
Error loading renderer 'vscode.builtin-renderer'

Resolved by reloading the VS Code window.

Full troubleshooting details are documented in:

04_Debug_Notes.md
🎓 Skills Demonstrated

This lab demonstrates practical ability in:

SQL
SELECT
WHERE
Parameterized queries
COUNT()
SUM()
AVG()
GROUP BY
ORDER BY
Python
SQL Magic integration
Python variables in SQL
SQL result handling
Pandas
SQL-to-DataFrame conversion
DataFrame inspection
Shape validation
Visualization
Seaborn bar charts
Basic chart formatting
Business-oriented visualization
Database
SQLite connection
Table access
Query execution
Debugging
Package compatibility troubleshooting
Kernel state management
Notebook extension management
VS Code renderer troubleshooting
Root-cause analysis
🏆 Lab Outcome

Lab 02 — Accessing Databases with SQL Magic: COMPLETED

The lab successfully demonstrated the integration of:

SQL + SQLite + Python + Pandas + Visualization

The practical exercise strengthened the ability to move from raw database records to aggregated analytical results and finally to business insights.

📌 Portfolio Value

This lab forms part of my IBM Data Analyst Professional Certificate practical portfolio and demonstrates a real-world data workflow:

Database
   ↓
SQL Query
   ↓
Data Aggregation
   ↓
Python
   ↓
Pandas
   ↓
Visualization
   ↓
Business Insight

It establishes a foundation for more advanced database-driven analytics and Python-based data analysis workflows.
```
