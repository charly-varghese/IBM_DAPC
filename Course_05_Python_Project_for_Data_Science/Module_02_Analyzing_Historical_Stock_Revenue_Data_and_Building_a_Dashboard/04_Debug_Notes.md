# Debug Notes — Module 02

## Analyzing Historical Stock/Revenue Data and Building a Dashboard

### Project

**Course:** Course 05 — Python Project for Data Science  
**Module:** Module 02 — Analyzing Historical Stock/Revenue Data and Building a Dashboard

---

## 1. Environment

- Python: 3.14
- Virtual Environment: `.venv`
- IDE: VS Code
- Operating System: Windows
- Main Libraries:
  - `pandas`
  - `yfinance`
  - `requests`
  - `beautifulsoup4`
  - `matplotlib`

---

## 2. Issue — Revenue Table Column Names

### Error

While developing `02_My_Practice.py`, the following error occurred:

````text
KeyError: "None of [Index(['Date', 'Revenue'], dtype='str')] are in the [columns]"

Cause

The code initially assumed that the selected HTML table would already contain columns named:

Date
Revenue

However, the HTML table extracted using pandas.read_html() did not expose those names directly.

Incorrect Approach
revenue_data = tables[table_index]

revenue_data = revenue_data[["Date", "Revenue"]]
Solution

The correct table was selected first, and the expected column names were explicitly assigned:

revenue_data = tables[table_index].copy()

revenue_data.columns = ["Date", "Revenue"]
Result

The revenue DataFrame was successfully created with:

Date
Revenue
3. Issue — Table Detection Approach
Problem

The first version attempted to identify the revenue table by searching for existing column names:

if "Date" in columns and "Revenue" in columns:

This failed because the source table did not expose those column names in the extracted DataFrame.

Solution

The implementation was aligned with the structure of the IBM project source:

tables = pd.read_html(StringIO(response.text))

revenue_data = tables[1].copy()

revenue_data.columns = ["Date", "Revenue"]
Lesson

pandas.read_html() can successfully extract an HTML table even when the resulting DataFrame does not contain meaningful column labels.

Always inspect the extracted DataFrame before assuming column names.

4. Revenue Data Cleaning

Revenue values can contain formatting characters such as:

$21,454
$16,934

These values must be converted into numeric values before performing calculations.

Cleaning approach
revenue_data["Revenue"] = (
    revenue_data["Revenue"]
    .astype(str)
    .str.replace(r"[$,]", "", regex=True)
    .str.strip()
)

revenue_data["Revenue"] = pd.to_numeric(
    revenue_data["Revenue"],
    errors="coerce"
)

Invalid records were removed using:

revenue_data.dropna(
    subset=["Date", "Revenue"],
    inplace=True
)
5. Date Conversion

The scraped revenue dates were converted into pandas datetime values:

revenue_data["Date"] = pd.to_datetime(
    revenue_data["Date"],
    errors="coerce"
)

This allowed the dates to be used correctly for time-series analysis and visualization.

6. Stock Data Extraction

Historical stock data was extracted using:

ticker = yf.Ticker(ticker_symbol)

stock_data = ticker.history(
    period="max"
)

The resulting data was reset to a normal DataFrame structure:

stock_data.reset_index(inplace=True)

This provided a Date column for analysis and visualization.

7. Validation

After debugging, both practice programs executed successfully.

02_My_Practice.py

Successfully completed:

Tesla stock extraction
Tesla revenue extraction
GameStop stock extraction
GameStop revenue extraction
Revenue cleaning
Data-type conversion
Basic stock analysis
Tesla visualization
GameStop visualization

Final output:

PRACTICE COMPLETE
03_Challenge.py

Successfully completed:

Tesla stock extraction
Tesla revenue extraction
GameStop stock extraction
GameStop revenue extraction
Revenue cleaning
Statistical analysis
Company comparison
Tesla visualization
GameStop visualization

Final output:

CHALLENGE COMPLETE
8. Key Debugging Lessons
Lesson 1 — Inspect before assuming

Do not assume an HTML table has the expected column names.

Use:

print(dataframe.columns)

to inspect the actual structure.

Lesson 2 — HTML tables may require normalization

After extraction, column names may need to be explicitly normalized:

dataframe.columns = ["Date", "Revenue"]
Lesson 3 — Clean financial data before calculations

Currency symbols and thousands separators must be removed before numeric analysis.

Lesson 4 — Validate data types

Use:

print(dataframe.dtypes)

to confirm that dates and financial values have the correct types.

Lesson 5 — Separate extraction, cleaning, and analysis

Reusable functions make the workflow easier to debug and maintain:

Extract
   ↓
Clean
   ↓
Analyze
   ↓
Visualize
9. Final Debug Status
Component_Status
IBM Project_Notebook✅ Passed

Tesla stock_extraction✅ Passed
Tesla revenue extraction✅ Passed
GameStop stock extraction✅ Passed
GameStop revenue extraction✅ Passed
Revenue cleaning✅ Passed
Date conversion✅ Passed
Statistical analysis✅ Passed
Visualizations✅ Passed
02_My_Practice.py✅ Passed
03_Challenge.py✅ Passed
10. Final Status

Module 02 practical implementation successfully validated.

The debugging process improved the understanding of:

HTML table extraction
pandas.read_html()
DataFrame structure inspection
Financial-data cleaning
Datetime conversion
Numeric conversion
Reusable extraction functions
Time-series analysis
Stock/revenue visualization

### Why this is good for our portfolio

This isn't just a list of errors. It documents the actual **debugging journey**:

```text
Error
  ↓
Identify cause
  ↓
Inspect data structure
  ↓
Correct extraction
  ↓
Clean data
  ↓
Validate
  ↓
Successful execution

That makes the file useful later when you're revising web scraping + Pandas + financial data pipelines.

````
