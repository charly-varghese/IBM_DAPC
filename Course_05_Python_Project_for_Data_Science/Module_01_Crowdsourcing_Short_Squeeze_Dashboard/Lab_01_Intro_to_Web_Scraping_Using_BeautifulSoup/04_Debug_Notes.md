# Debug Notes – Lab 01

## Course 05 – Python Project for Data Science

### Module 01 – Crowdsourcing Short Squeeze Dashboard

---

## 1. Purpose

This file records the important debugging issues encountered while completing Lab 01.

The objective is not only to fix errors, but to understand **why the errors occurred** and how to prevent them in future Python projects.

---

## 2. Issue – Virtual Environment

### Situation

The Python virtual environment needed to be activated before running the lab.

### Solution

```bat
.venv\Scripts\activate.bat
After activation:

(.venv)

appeared in the terminal prompt.

Verification
where.exe python

The first Python executable was:

D:\MASTER_BRAIN_ENV_2025\IBM_DAPC\.venv\Scripts\python.exe
Lesson

Always verify that the project is using the intended virtual environment before installing packages or running code.

3. Issue – Package Import Warnings
Situation

VS Code initially displayed warnings such as:

Import "bs4" could not be resolved
Import "requests" could not be resolved
Verification

The packages were tested directly from the activated virtual environment:

python -c "import requests, bs4, pandas; print('requests:', requests.__version__); print('BeautifulSoup: OK'); print('pandas:', pandas.__version__)"

Result:

requests: 2.34.2
BeautifulSoup: OK
pandas: 3.0.5
Lesson

A VS Code/Pylance warning does not always mean the Python program cannot run.

Always verify the actual runtime environment from the terminal.

4. Issue – Variable Name and Case Sensitivity
Error
NameError: name 'table_index' is not defined
Cause

Python variable names are case-sensitive.

For example:

table_index

and:

table_Index

are different variables.

Lesson

Use consistent variable naming throughout the program.

Recommended:

table_index
5. Issue – Table Not Found
Situation

The population webpage returned:

Population Page Status Code: 403
Number of tables: 0
Selected table index: None
Cause

The website refused the request with HTTP status code 403.

Because no HTML tables were returned:

tables = soup.find_all("table")

produced an empty list.

Therefore, the target table could not be located.

Lesson

Web scraping depends on the response received from the target website.

Possible problems include:

HTTP 403 restrictions
robots/access restrictions
changed HTML structure
dynamic JavaScript-generated content
network problems

Always check the HTTP status code before assuming the page contains the expected data.

6. Issue – Unsafe Table Index Access
Problem

Using:

print(tables[table_index].prettify())

without confirming that a table was found can cause an error.

Safer Approach
if table_index is not None:
    print(tables[table_index].prettify())
else:
    print("Target table was not found.")
Lesson

Validate data before using an index.

This is an important defensive programming practice.

7. Issue – Duplicate Output
Situation

During the Challenge exercise, the same three records appeared multiple times.

Example:

AAPL Apple 220 5000000
MSFT Microsoft 510 3200000
TSLA Tesla 340 7100000

The records were printed repeatedly.

Cause

The extraction/printing code had been duplicated.

Solution

The duplicate block was removed.

The corrected program produced exactly:

AAPL Apple 220 5000000
MSFT Microsoft 510 3200000
TSLA Tesla 340 7100000
Lesson

When output is duplicated, check:

Loop structure
Duplicate code blocks
Function calls
Indentation
Whether the same list is being processed multiple times
8. Issue – Scraped Values Stored as Strings
Situation

BeautifulSoup extracts HTML content as text.

For example:

Price = "220"
Volume = "5000000"

These values are strings.

Solution

Convert them to numeric values when required:

stock_df["Price"] = pd.to_numeric(stock_df["Price"])
stock_df["Volume"] = pd.to_numeric(stock_df["Volume"])
Lesson

Web scraping produces raw data.

Before analysis, the data often needs:

Extraction
    ↓
Cleaning
    ↓
Type Conversion
    ↓
Analysis
9. Issue – DataFrame Analysis

After conversion to numeric types, the stock data could be analyzed.

Average Price
356.67
Total Trading Volume
15,300,000
Highest Volume Stock
TSLA
Highest Price Stock
MSFT
Lesson

The real value of web scraping is not simply collecting HTML.

The goal is to transform:

Web Data
   ↓
Structured Data
   ↓
Clean Data
   ↓
Analyzable Data
10. Debugging Workflow Learned

The following workflow was used throughout the lab:

Run Program
     ↓
Observe Error / Unexpected Output
     ↓
Read Error Message
     ↓
Identify the Problem
     ↓
Check the Relevant Code
     ↓
Fix the Code
     ↓
Run Again
     ↓
Verify Output
11. Key Debugging Lessons
Lesson 1

Do not immediately assume the library is broken.

First check:

Python environment
Package installation
Import
Code
Input
Output
Lesson 2

Always read the complete error message.

For example:

NameError

immediately tells us that Python cannot find the referenced variable.

Lesson 3

Validate external data.

When scraping:

response.status_code

is an important first check.

Lesson 4

Do not assume a webpage will always return the expected HTML.

Websites can change or block automated requests.

Lesson 5

Separate extraction from analysis.

A professional workflow is:

Extract
   ↓
Validate
   ↓
Clean
   ↓
Transform
   ↓
Analyze
12. Final Debug Status
## 12. Final Debug Status

| Issue | Status |
|---|---|
| Virtual environment | Fixed |
| Package verification | Verified |
| BeautifulSoup import | Verified |
| Variable naming | Fixed |
| Undefined `table_index` | Fixed |
| HTTP 403 handling | Handled |
| Missing table handling | Fixed |
| Duplicate output | Fixed |
| Data type conversion | Completed |
| DataFrame analysis | Completed |
13. Lab Status
Lab 01 Debugging – COMPLETED ✅
```
