# Debug Notes — Lab 03: Extracting Stock Data Using Web Scraping

## Course Information

- **Course:** Course 05 — Python Project for Data Science
- **Module:** Module 01 — Crowdsourcing Short Squeeze Dashboard
- **Lab:** Lab 03 — Extracting Stock Data Using Web Scraping

---

## 1. Debugging Overview

This lab involved extracting historical stock data from HTML web pages
using Requests, BeautifulSoup, and Pandas.

The main debugging issues occurred during the development of the
`02_My_Practice.py` program.

### Debugging Summary

| Issue | Type | Status |
| ----- | ---- | ------ |

| `KeyError: 'Close'` | DataFrame column mismatch | Fixed |
| `TypeError: NoneType has no len()` | Missing function return | Fixed |
| `Apython` command error | Terminal typing error | Resolved |

---

## 2. Debug Issue 1 — KeyError: 'Close'

## Error

```text
KeyError: 'Close'
``
The error occurred when the program attempted:

amazon_data["Close"]
Observed Data

The actual scraped columns were:

['Date', 'Open', 'High', 'Low', 'Close*', 'Adj Close**', 'Volume']

The scraped column was therefore:

Close*

rather than:

Close
Root Cause

BeautifulSoup extracts the text exactly as it appears in the HTML.

The Yahoo Finance table contained:

Close*
Adj Close**

BeautifulSoup therefore created DataFrame columns with those exact
names.

The program incorrectly assumed that the column would be named:

Close
Incorrect Approach
amazon_data["Close"]

This produced:

KeyError: 'Close'
Fix

Instead of hard-coding the Yahoo Finance display names throughout the
analysis code, the scraped column names were normalized.

def normalize_stock_columns(dataframe):
    """Normalize Yahoo Finance column names."""

dataframe = dataframe.rename(
        columns={
            "Close*": "Close",
            "Adj Close**": "Adj Close",
        }
    )

return dataframe

The normalization was applied to both datasets:

netflix_data = normalize_stock_columns(netflix_data)
amazon_data = normalize_stock_columns(amazon_data)
Result

Both datasets now use the consistent schema:

Date
Open
High
Low
Close
Adj Close
Volume
Lesson Learned

When working with scraped data, never assume that web-page labels
match the column names expected by the analysis code.

A robust pipeline should:

Extract
   ↓
Normalize
   ↓
Clean
   ↓
Analyze
3. Debug Issue 2 — NoneType Error
Error
TypeError: object of type 'NoneType' has no len()

The error occurred at:

print("Rows:", len(netflix_data))
Root Cause

The clean_numeric_columns() function was accidentally left empty
during the code modification.

The function was effectively:

def clean_numeric_columns(dataframe):
    """Convert scraped financial columns into numeric values."""

A Python function without a return statement returns:

None

Therefore:

netflix_data = clean_numeric_columns(netflix_data)

changed the variable from a DataFrame into:

None

The following operation then failed:

len(netflix_data)

because None has no length.

Additional Code-Structure Problem

During the modification, the numeric-cleaning code was accidentally
placed after:

return dataframe

inside another function.

For example:

return dataframe

numeric_columns = ...

Any code after return is unreachable.

Fix

The cleaning function was reconstructed correctly:

def clean_numeric_columns(dataframe):
    """Convert scraped financial columns into numeric values."""

numeric_columns = [
        column
        for column in dataframe.columns
        if column != "Date"
    ]

    for column in numeric_columns:
        dataframe[column] = (
            dataframe[column]
            .str.replace(",", "", regex=False)
            .astype(float)
        )

    return dataframe
Result

The function now:

Identifies financial columns.
Removes commas from scraped values.
Converts strings to floating-point numbers.
Returns the cleaned DataFrame.

Example:

"71,528,900"
      ↓
"71528900"
      ↓
71528900.0
Lesson Learned

When a function is used like:

result = some_function(data)

the function must explicitly return the expected object.

Also, statements placed after return cannot execute.

4.Minor Terminal Issue — Apython
Command Entered
Apython 02_My_Practice.py
Error
'Apython' is not recognized as an internal or external command,
operable program or batch file.
Root Cause

This was a terminal typing error.

The correct command is:

python 02_My_Practice.py
Result

The corrected command executed successfully.

Lesson Learned

This was not a Python program error. It was simply an incorrect
terminal command.

5.Final Validation After Debugging

After the fixes, 02_My_Practice.py completed successfully.

Netflix
Records: 70
Average Close: $286.04
Highest Close: $540.73
Highest Volume: 497,401,200
Amazon
Records: 61
Average Close: $1,601.44
Highest Close: $3,450.96
Highest Volume: 183,220,800

The Challenge program also completed successfully.

Combined Dataset
Total records: 131
NFLX: 70 records
AMZN: 61 records
Highest-Volume Stock
NFLX
497,401,200
Highest Average Closing Price
AMZN
$1,601.44
1.Key Debugging Lessons
Lesson 1 — Inspect the Actual Data

When a DataFrame raises:

KeyError

inspect the real column names:

print(dataframe.columns.tolist())

Do not guess the column name.

Lesson 2 — Normalize External Data

Web pages may contain labels such as:

Close*
Adj Close**

Normalize them before analysis:

Raw Web Data
     ↓
Column Normalization
     ↓
Standard Data Schema
Lesson 3 — Functions Must Return Expected Objects

If a function is expected to return a DataFrame:

return dataframe

must be present.

Otherwise:

result = function(...)

may produce:

None
Lesson 4 — Return Ends Function Execution

Code after:

return dataframe

will not execute.

Always check indentation and code order when modifying functions.

Lesson 5 — Debug the Actual Failure

The scraping function itself was working correctly.

The failures occurred later during:

Column handling
      ↓
Data cleaning
      ↓
Analysis

Therefore, we fixed the affected stages instead of unnecessarily
rewriting the scraper.

8.Final Debugging Status
BeautifulSoup extraction       → PASS
Pandas DataFrame creation     → PASS
Column normalization           → PASS
Numeric data cleaning          → PASS
Multi-stock processing         → PASS
Stock analysis                → PASS
Challenge pipeline            → PASS

Lab 03 debugging status: COMPLETE
```
