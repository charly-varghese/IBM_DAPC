# Lab 03 — Extracting Stock Data Using Web Scraping

## Course 05 — Python Project for Data Science

\*_Module 01 — Crowdsourcing Short Squeeze Dashboard_

---

## 1. Overview

This lab focuses on extracting historical stock market data from HTML
web pages using Python web-scraping techniques.

The implementation uses:

- `requests` to retrieve web-page content
- `BeautifulSoup` to parse HTML
- `Pandas` to create and analyze DataFrames

The lab builds on the basic web-scraping concepts introduced in the
previous lab and applies them to a real stock-data extraction workflow.

The practical implementation progresses from IBM's original lab
exercise to a reusable multi-stock scraping and analysis pipeline.

---

## 2. Learning Objectives

By completing this lab, I practiced how to:

- Retrieve HTML content from a web page.
- Parse HTML using BeautifulSoup.
- Locate HTML tables.
- Extract table headers and rows.
- Convert scraped HTML data into Pandas DataFrames.
- Use `pandas.read_html()` for table extraction.
- Normalize inconsistent scraped column names.
- Clean financial values containing commas.
- Convert scraped strings into numeric values.
- Build reusable scraping functions.
- Process multiple stock datasets.
- Combine DataFrames using `pd.concat()`.
- Analyze stock data using Pandas.
- Group data using `groupby()`.
- Generate summary metrics.
- Debug real-world data extraction issues.

---

## 3. Technologies Used

| Technology    | Purpose                              |
| ------------- | ------------------------------------ |
| Python        | Programming language                 |
| Requests      | HTTP requests and web-page retrieval |
| BeautifulSoup | HTML parsing and data extraction     |
| Pandas        | DataFrames and data analysis         |
| VS Code       | Development environment              |
| Git           | Version control                      |
| GitHub        | Portfolio and source-code management |

---

## 4. Web Scraping Workflow

The core scraping workflow used in this lab is:

````text
Stock Web Page
      ↓
requests.get()
      ↓
HTML Response
      ↓
BeautifulSoup
      ↓
HTML Table
      ↓
Rows and Cells
      ↓
Pandas DataFrame
      ↓
Normalize Columns
      ↓
Clean Numeric Values
      ↓
Analyze Stock Data
A second extraction approach was also demonstrated:

Stock Web Page
      ↓
pandas.read_html()
      ↓
List of DataFrames
      ↓
Selected DataFrame
5. IBM Lab Implementation
File
01_IBM_Lab.py

The IBM implementation demonstrates two approaches to extracting
historical stock data.

Approach 1 — BeautifulSoup

The HTML page is retrieved using Requests and parsed using BeautifulSoup.

The program extracts:

Date
Open
High
Low
Close
Volume
Adjusted Close where applicable
Approach 2 — Pandas read_html()

Pandas can directly identify HTML tables using:

pd.read_html(url)

This provides a convenient alternative when the required information
is already contained in an HTML table.

IBM Lab Validation

The implementation successfully:

Retrieved the Netflix webpage.
Retrieved the Amazon webpage.
Received HTTP status code 200.
Parsed the HTML content.
Extracted the required stock tables.
Created Pandas DataFrames.
Retrieved the required Amazon values.
6. My Practice
File
02_My_Practice.py

The IBM implementation was converted into a more reusable workflow.

Instead of repeating the scraping logic for every stock, a reusable
function was created:

scrape_stock_table(url)

The function performs:

URL
 ↓
HTTP Request
 ↓
HTML Parsing
 ↓
Table Detection
 ↓
Header Extraction
 ↓
Row Extraction
 ↓
DataFrame
Data Cleaning

Scraped financial values initially arrive as strings.

For example:

"71,528,900"

The program removes commas and converts the value to a numeric type.

"71,528,900"
      ↓
"71528900"
      ↓
71528900.0
Column Normalization

Yahoo Finance table labels included:

Close*
Adj Close**

These were normalized to:

Close
Adj Close

This creates a consistent schema for downstream analysis.

My Practice Results
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
7. Challenge
File
03_Challenge.py

The Challenge extends the My Practice implementation into a
multi-stock data pipeline.

Pipeline
Multiple Stock URLs
        ↓
Reusable Scraper
        ↓
Normalize Columns
        ↓
Clean Numeric Values
        ↓
Add Ticker
        ↓
Combine DataFrames
        ↓
Group by Ticker
        ↓
Generate Stock Summary
Stocks Processed
NFLX — Netflix
AMZN — Amazon
Combined Dataset
Total Records: 131

NFLX: 70 records
AMZN: 61 records
Generated Metrics

For each stock, the Challenge calculates:

Record count
Average closing price
Highest closing price
Lowest closing price
Average trading volume
Highest trading volume
Challenge Results
Metric AMZN NFLX
Records 61 70
Average Close $1,601.44 $286.04
Highest Close $3,450.96 $540.73
Lowest Close $552.52 $90.03
Average Volume ~92.35M ~194.79M
Highest Volume 183.22M 497.40M
Highest-Volume Stock
NFLX
497,401,200
Highest Average Closing Price
AMZN
$1,601.44
8. Debugging Experience

This lab included several practical debugging situations.

Issue 1 — KeyError: 'Close'

The scraped Yahoo Finance table contained:

Close*

rather than:

Close

The solution was to normalize the scraped column names before analysis.

dataframe = dataframe.rename(
    columns={
        "Close*": "Close",
        "Adj Close**": "Adj Close",
    }
)
Issue 2 — NoneType Error

The cleaning function initially failed to return the DataFrame.

This caused:

TypeError:
object of type 'NoneType' has no len()

The solution was to correctly return the DataFrame:

return dataframe
Issue 3 — Terminal Command Typo

An incorrect command:

Apython 02_My_Practice.py

was entered instead of:

python 02_My_Practice.py

This was a terminal input error rather than a Python program error.

9. Key Technical Lessons
Web scraping is an ETL-style process

The practical workflow developed in this lab can be viewed as:

Extract
   ↓
Normalize
   ↓
Clean
   ↓
Transform
   ↓
Analyze
External data should not be trusted blindly

Web pages may contain:

Unexpected column names
Formatting characters
Missing values
Different table structures
Changing HTML structures

Therefore, scraped data should be inspected and validated before
analysis.

Reusable functions improve maintainability

Instead of duplicating scraping logic, the Challenge uses reusable
functions:

scrape_stock_table()
normalize_stock_columns()
clean_numeric_columns()
prepare_stock_data()

This makes the implementation easier to extend to additional stocks.

10. Portfolio Architecture

The final Lab 03 structure is:

Lab_03_Extracting_Stock_Data_Using_Web_Scraping/
│
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 03_Challenge.py
├── 04_Debug_Notes.md
└── README.md
File Responsibilities
File Purpose
01_IBM_Lab.py(IBM lab implementation)

02_My_Practice.py (Reusable personal implementation)
03_Challenge.py (Multi-stock portfolio challenge)
04_Debug_Notes.md (Debugging record and lessons)
README.md (Project documentation)
11. Relationship to Module 01

This lab contributes to the larger:

Crowdsourcing Short Squeeze Dashboard

pipeline.

The current learning progression is:

Web Scraping
     ↓
Stock Data Collection
     ↓
Data Cleaning
     ↓
Data Standardization
     ↓
Multi-Stock Dataset
     ↓
Stock-Level Analysis
     ↓
Future Dashboard

The Challenge introduces the basic architecture required for
processing multiple stocks before applying more advanced short-squeeze
analysis.

12. Validation Checklist
IBM Lab
 HTTP request successful
 HTML content retrieved
 BeautifulSoup parsing successful
 Netflix data extracted
 Amazon data extracted
 Pandas read_html() tested
My Practice
 Reusable scraper created
 Multiple stocks processed
 Column names normalized
 Financial values cleaned
 Numeric conversion completed
 Stock comparison completed
 Highest-volume periods identified
Challenge
 Multi-stock pipeline implemented
 Ticker column added
 DataFrames combined
 groupby() analysis completed
 Stock summary generated
 Highest-volume stock identified
 Highest average closing price identified
Documentation
 04_Debug_Notes.md
 README.md
 VS Code validation
 Git/GitHub-ready structure
13. Final Status

Lab 03 — Extracting Stock Data Using Web Scraping

STATUS: COMPLETED

The lab successfully demonstrates a complete practical workflow for
extracting, cleaning, standardizing, combining, and analyzing stock
data obtained through web scraping.

The implementation is structured as a reusable portfolio project and
provides a foundation for the subsequent stock-analysis components of
the Crowdsourcing Short Squeeze Dashboard.


## ✅ README Design

This README is intentionally structured around the **portfolio story**:

```text
IBM Concept
    ↓
My Implementation
    ↓
Debugging
    ↓
Challenge
    ↓
Reusable Pipeline
    ↓
Module 01 Dashboard Foundation

So when you later put this on GitHub, someone looking at the repository can understand what you learned, what you built, what broke, how you fixed it, and why the lab matters to the larger project.

Lab 03 status now
01_IBM_Lab.py       ✅
02_My_Practice.py   ✅
03_Challenge.py     ✅
04_Debug_Notes.md   ✅
README.md           ✅
````
