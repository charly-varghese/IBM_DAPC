# 04_Debug_Notes.md

## Lab 02 — Debug Notes

## Accessing Databases with SQL Magic

**Course:** IBM Data Analyst Professional Certificate  
**Course 06:** Databases and SQL for Data Science with Python  
**Module 04:** Accessing Databases Using Python  
**Lab:** Lab 02 — Accessing Databases with SQL Magic  
**Environment:** VS Code + Jupyter Notebook + Python Virtual Environment  
**Database:** SQLite  
**Notebook:** `02_My_Practice.ipynb`

---

## 1. Lab Objective

The purpose of this lab was to practice database access using:

- `ipython-sql`
- SQL Magic commands
- SQLite
- Parameterized SQL
- SQL aggregation
- Pandas DataFrames
- Seaborn visualization

The practice database used was:

```text
MY_SQL_MAGIC_PRACTICE.db

The main table was:

SALES_PERFORMANCE
2. Debugging Summary
Issue Status Root Cause Solution
KeyError: 'DEFAULT' Fixed ipython-sql / PrettyTable compatibility issue Downgraded PrettyTable
%%sql not found Fixed SQL Magic extension not loaded after kernel restart %load_ext sql
sales_df is not defined Fixed Previous SQL assignment cell had not completed correctly Executed SQL assignment and DataFrame conversion separately
VS Code renderer error Fixed Temporary VS Code Notebook renderer issue Developer: Reload Window
Database/table missing Not encountered — Database remained intact
SQL query errors None — SQL executed successfully
3. Issue 01 — KeyError: 'DEFAULT'
Error

While executing:

%%sql
SELECT * FROM SALES_PERFORMANCE;

the following error occurred:

KeyError: 'DEFAULT'

The traceback pointed to:

ipython-sql
sql/run.py
prettytable

Specifically, the error occurred while SQL Magic was trying to render the query result.

Diagnosis

The SQL statement itself was valid.

Evidence:

Database connection succeeded.
Table creation succeeded.
8 records were inserted successfully.
The error occurred only when displaying SQL query results.

The issue was a compatibility problem between:

ipython-sql

and the installed:

PrettyTable

version.

The older SQL Magic rendering code expected a DEFAULT style entry that was no longer available in the installed PrettyTable version.

Therefore:

This was a package compatibility problem, not a SQL or SQLite problem.

Fix

The local PrettyTable package was replaced with a compatible version:

python -m pip uninstall prettytable -y
python -m pip install prettytable==3.10.2

After restarting the Jupyter kernel, SQL Magic was loaded again.

Verification
import prettytable
print(prettytable.__version__)

The compatible version was confirmed.

SQL query execution then worked successfully:

%%sql
SELECT * FROM SALES_PERFORMANCE;
4. Issue 02 — Cell magic %%sql not found
Error

After restarting/reloading the kernel, the following error appeared:

UsageError: Cell magic `%%sql` not found.
Diagnosis

Restarting the Jupyter kernel clears the previously loaded IPython extensions.

Therefore, even though ipython-sql was installed correctly, the SQL Magic extension was no longer active in the new kernel session.

Fix

Reload the SQL Magic extension:

%load_ext sql

Then reconnect to SQLite:

%sql sqlite:///MY_SQL_MAGIC_PRACTICE.db
Verification

The following query confirmed that SQL Magic and the database connection were working:

%sql SELECT COUNT(*) AS record_count FROM SALES_PERFORMANCE;

Result:

record_count
------------
8

Therefore:

SQL Magic      → SUCCESS
SQLite         → SUCCESS
Table          → SUCCESS
Records        → 8
5. Issue 03 — sales_df is not defined
Error

After executing the SQL aggregation query, the following error occurred:

NameError: name 'sales_df' is not defined
Diagnosis

The SQL query itself executed successfully, but the Python variable assignment had not completed.

The original combined operation was:

sales_summary = %sql SELECT ...
sales_df = sales_summary.DataFrame()

The SQL result was returned as:

Done.

but sales_df was not available when the next cell was executed.

This produced a cascade error.

Fix

The SQL execution and DataFrame conversion were separated into two cells.

Cell 1
sales_summary = %sql SELECT department, SUM(sales_amount) AS total_sales, AVG(sales_amount) AS average_sales FROM SALES_PERFORMANCE GROUP BY department ORDER BY total_sales DESC
Cell 2
sales_df = sales_summary.DataFrame()

print(sales_df)
print()
print("Shape:", sales_df.shape)
Verification

Output:

  department  total_sales  average_sales
0       Sales     601000.0       150250.0
1   Marketing     345000.0       115000.0
2     Finance      87000.0        87000.0

Shape: (3, 3)

This confirmed successful SQL → Python → Pandas conversion.

6. Issue 04 — VS Code Notebook Renderer Error
Error

While rerunning the visualization cell, VS Code displayed:

Error loading renderer 'vscode.builtin-renderer'

Failed to fetch dynamically imported module:
notebook-renderers/renderer-out/index.js
Diagnosis

This was a VS Code Notebook rendering issue.

It was not related to:

SQLite
Python
Pandas
Seaborn
SQL Magic
PrettyTable

The notebook execution environment itself was still functioning.

Fix

VS Code was reloaded using:

Ctrl + Shift + P

Then:

Developer: Reload Window

After VS Code reloaded, the visualization executed successfully.

7. Final Validation
Record Count
%sql SELECT COUNT(*) AS record_count FROM SALES_PERFORMANCE;

Result:

8
Department Analysis
sales_summary = %sql SELECT department, SUM(sales_amount) AS total_sales, AVG(sales_amount) AS average_sales FROM SALES_PERFORMANCE GROUP BY department ORDER BY total_sales DESC

Result:

Department Total Sales Average Sales
Sales 601,000 150,250
Marketing 345,000 115,000
Finance 87,000 87,000
City Analysis
city_analysis = %sql SELECT city, COUNT(*) AS employee_count, SUM(sales_amount) AS total_sales, AVG(sales_amount) AS average_sales FROM SALES_PERFORMANCE GROUP BY city ORDER BY total_sales DESC

Result:

City Employee Count Total Sales Average Sales
Mumbai 2 304,000 152,000
Kochi 2 240,000 120,000
Chennai 2 235,000 117,500
Delhi 1 156,000 156,000
Bengaluru 1 98,000 98,000
8. Important Analytical Observation

The analysis demonstrates why both total and average metrics are important.

Highest Total Sales
Mumbai → 304,000

Mumbai has the highest total sales because it has two employees with strong sales performance.

Highest Average Sales
Delhi → 156,000

Delhi has only one employee, but that employee has the highest average sales.

Therefore:

Highest Total ≠ Highest Average

This is an important data-analysis principle.

9. Debugging Lessons Learned
Lesson 1 — Separate Environment Errors from Code Errors

A traceback does not always mean that the SQL code is wrong.

The KeyError: 'DEFAULT' occurred during result rendering, not during SQL execution.

Lesson 2 — Package Compatibility Matters

Libraries used in the same environment must remain compatible.

In this case:

ipython-sql
       ↓
PrettyTable
       ↓
Result Rendering

A version mismatch caused the error.

Lesson 3 — Kernel Restart Resets Runtime State

Installing a package or restarting the kernel can remove previously loaded extensions.

Therefore:

%load_ext sql

may need to be executed again after a kernel restart.

Lesson 4 — Avoid Cascade Errors

An error in one cell can cause later errors such as:

NameError: sales_df is not defined

The correct debugging approach is:

Find the FIRST error
        ↓
Fix the FIRST error
        ↓
Re-run dependent cells
        ↓
Validate variables
        ↓
Continue
Lesson 5 — VS Code Rendering Errors Can Be UI-Level Problems

The VS Code renderer error did not indicate a problem with the Python program.

Reloading VS Code resolved the issue without modifying the Python environment.

10. Final Debug Status
============================================================
LAB 02 DEBUG STATUS
============================================================

SQLite Connection              : PASS
SQL Magic Extension            : PASS
PrettyTable Compatibility      : FIXED
SELECT Queries                 : PASS
Parameterized SQL              : PASS
GROUP BY                       : PASS
SUM / AVG / COUNT              : PASS
SQL → Pandas DataFrame         : PASS
Seaborn Visualization          : PASS
VS Code Notebook Renderer      : FIXED
Final City Analysis            : PASS

============================================================
DEBUGGING COMPLETE
============================================================
Final Conclusion

Lab 02 successfully demonstrated database access using SQL Magic in a Jupyter Notebook environment.

The major debugging experience was resolving the compatibility issue between ipython-sql and PrettyTable, followed by restoring SQL Magic after a kernel restart and resolving a temporary VS Code Notebook renderer problem.

The final environment is functioning correctly and the practice database has been successfully queried and analyzed.
```
