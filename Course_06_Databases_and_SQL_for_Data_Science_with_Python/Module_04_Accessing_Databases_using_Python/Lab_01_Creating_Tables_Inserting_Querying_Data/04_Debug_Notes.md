# Debug Notes — Lab 01

## Course Information

- **Program:** IBM Data Analyst Professional Certificate
- **Course:** Course 06 — Databases and SQL for Data Science with Python
- **Module:** Module 04 — Accessing Databases Using Python
- **Lab:** Lab 01 — Creating Tables, Inserting and Querying Data
- **Environment:** VS Code + Python Virtual Environment
- **Python Version:** 3.14.0
- **SQLite Version:** 3.50.4
- **Pandas Version:** 3.0.5

---

## 1. Issue — Pandas ModuleNotFoundError

## Error

During the first attempt to execute `01_IBM_Lab.py`, the following error occurred:

```text
ModuleNotFoundError: No module named 'pandas'
The error occurred at:

import pandas as pd
Root Cause

The terminal was running outside the project's virtual environment.

The terminal prompt did not contain:

(.venv)

Therefore, the script was executed using the system/global Python interpreter instead of the project's .venv interpreter.

The global Python environment did not have Pandas available.

2. Diagnosis

The Python interpreter was checked using:

where python

Before activating the virtual environment, the system Python interpreter was being used.

The project's virtual environment was then activated using:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\activate.bat

After activation, the terminal prompt changed to:

(.venv)

The active interpreter was verified with:

python -c "import sys; print(sys.executable)"

Result:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\python.exe
3. Package Verification

The required Python components were verified inside the virtual environment.

Verification command:

python -c "import sys, sqlite3, pandas as pd; print('Python:', sys.executable); print('Python Version:', sys.version.split()[0]); print('SQLite Version:', sqlite3.sqlite_version); print('Pandas Version:', pd.__version__)"

Verified environment:

Python: D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\python.exe
Python Version: 3.14.0
SQLite Version: 3.50.4
Pandas Version: 3.0.5

No additional package installation was required.

4. Resolution

The existing project virtual environment was activated before running the lab:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\activate.bat

The lab was then executed again:

python 01_IBM_Lab.py

The complete lab executed successfully.

5. VS Code Interpreter Verification

The VS Code Python interpreter was also configured to use the project virtual environment:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\python.exe

This ensures that:

VS Code Interpreter
        ↓
      .venv
        ↓
Python 3.14.0
        ↓
Pandas 3.0.5
        ↓
SQLite 3.50.4

The terminal and VS Code workspace were therefore aligned to the same Python environment.

6. Database Execution Verification

After resolving the environment issue, the following database operations executed successfully:

SQLite database creation
Database connection
Cursor creation
CREATE TABLE
INSERT
SELECT
fetchall()
fetchmany(2)
Column-specific SELECT
UPDATE
commit()
Pandas read_sql()
DataFrame inspection
Cursor closure
Database connection closure
7. Important Database Debugging Lessons
Lesson 1 — Verify the Python Interpreter

A package may be installed in one Python environment but unavailable in another.

Always verify:

where python

and:

import sys
print(sys.executable)

before troubleshooting package-related errors.

Lesson 2 — Activate the Correct Virtual Environment

The presence of a .venv folder does not automatically mean that the current terminal is using it.

The terminal should show:

(.venv)

when the virtual environment is activated.

Lesson 3 — SQLite Connection Creates the Database

The lab uses:

sqlite3.connect("INSTRUCTOR.db")

SQLite can create the database file automatically if it does not already exist.

Lesson 4 — Cursor Executes SQL

The database connection provides access to the database, while the cursor is used to execute SQL statements:

cursor_obj.execute(...)
Lesson 5 — Commit Changes

Data modification operations such as:

INSERT
UPDATE

should be committed:

conn.commit()

so that the changes are saved to the database.

Lesson 6 — Fetch Methods

Different cursor fetch methods retrieve query results differently:

fetchone()
fetchmany(n)
fetchall()

Understanding the difference is essential when working with Python DB-API.

Lesson 7 — Pandas Bridges SQL and Data Analysis

The SQL result can be loaded directly into a Pandas DataFrame:

df = pd.read_sql("SELECT * FROM INSTRUCTOR", conn)

This creates a bridge between:

SQL Database
     ↓
Python
     ↓
Pandas DataFrame
     ↓
Data Analysis
8. Final Debug Status
Initial Environment Issue       RESOLVED
Virtual Environment             VERIFIED
Python Interpreter              VERIFIED
Pandas                          VERIFIED
SQLite                          VERIFIED
Database Connection             SUCCESS
SQL Operations                  SUCCESS
Pandas Integration              SUCCESS
Lab Execution                   SUCCESS



```
