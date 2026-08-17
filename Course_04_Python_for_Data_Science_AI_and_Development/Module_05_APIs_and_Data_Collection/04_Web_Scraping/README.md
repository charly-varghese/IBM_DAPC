# Lab 04 – Web Scraping

## Overview

This lab focuses on collecting structured data from web pages using Python web-scraping techniques.

The practical work progresses from the IBM hands-on lab to a custom practice program and a validation-focused challenge. The implementations demonstrate how to request a web page, parse HTML content, extract structured information, clean the resulting data, validate data quality, perform basic analysis, and export the final dataset.

---

## Learning Objectives

- Send HTTP requests to a web page using `requests`
- Parse HTML using `BeautifulSoup`
- Locate and extract HTML elements
- Extract structured records from web pages
- Convert scraped data into a Pandas DataFrame
- Clean and transform scraped data
- Validate missing values and duplicate records
- Perform basic data analysis
- Export cleaned data to CSV
- Handle encoding and extraction issues
- Apply practical web-scraping debugging techniques
- Follow responsible and ethical scraping practices

---

## Lab Structure

```text
04_Web_Scraping/
│
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 03_Challenge.py
├── 04_Debug_Notes.md
├── README.md
│
└── practice_output/
    ├── color_codes.csv
    └── challenge_books.csv
Programs
01_IBM_Lab.py

Implementation of the IBM hands-on web-scraping exercises.

Key activities include:

HTML page retrieval
BeautifulSoup parsing
HTML table extraction
HTML link extraction
Pandas read_html()
Data extraction and inspection
02_My_Practice.py

A custom web-scraping practice program based on an online color-code dataset.

Key activities include:

HTTP request handling
BeautifulSoup
HTML table extraction
Pandas DataFrame creation
Data cleaning
Data validation
Duplicate detection
Missing-value checking
CSV export

Final dataset:

practice_output/color_codes.csv

Validation result:

32 records × 4 columns
Missing Values = 0
Duplicate Rows = 0
03_Challenge.py

A custom challenge using the Books to Scrape practice website.

The program extracts travel-book information and performs a complete mini data pipeline:

HTTP Request
      ↓
HTML Response
      ↓
BeautifulSoup Parsing
      ↓
Product Extraction
      ↓
Pandas DataFrame
      ↓
Data Cleaning
      ↓
Data Validation
      ↓
Basic Analysis
      ↓
CSV Export

Extracted fields:

Title
Price
Availability

Final validation:

Records = 11
Missing Values = 0
Duplicate Rows = 0
Invalid Titles = 0
Invalid Prices = 0
Invalid Availability = 0

Basic analysis:

Average Price = £39.79
Minimum Price = £23.21
Maximum Price = £56.88

Final output:

practice_output/challenge_books.csv

Challenge status:

PASSED

Debugging Highlights

The challenge initially produced incorrect price data even though the website returned:

HTTP Status Code: 200

The first execution created a CSV successfully, but all price values became NaN.

Root Cause

The initial extraction logic did not reliably separate the title and price from the returned HTML structure.

An encoding issue was also identified, producing text such as:

Noahâs

instead of:

Noah’s
Resolution

The challenge was improved by:

Using more reliable CSS selectors
Adding fallback price extraction
Explicitly setting UTF-8 encoding
Adding stronger data-quality validation
Validating critical fields before declaring success

The corrected program completed with:

Challenge validation: PASSED

Detailed debugging information is maintained in:

04_Debug_Notes.md
Tools & Technologies
Python
Requests
BeautifulSoup
Pandas
pathlib
Regular Expressions
HTML
CSV
Responsible Web Scraping

Web scraping should be performed responsibly.

Practical considerations include:

Respect website terms and policies
Check robots.txt where appropriate
Avoid excessive requests
Use reasonable timeouts
Identify requests appropriately
Do not collect sensitive or private information
Prefer public and permitted data sources

For learning and portfolio development, public practice websites are preferred.

Key Practical Takeaways

This lab reinforced an important data-engineering principle:

A successful HTTP request does not guarantee correct data extraction.

Therefore, a reliable scraping workflow should include:

Request
→ Extract
→ Clean
→ Validate
→ Analyze
→ Export

Data validation is essential even when the HTTP request itself succeeds.

Status

Lab 04 – Web Scraping: COMPLETED

IBM Lab: ✅
My Practice: ✅
Challenge: ✅
Debugging: ✅
Data Validation: ✅
CSV Outputs: ✅
README: ✅


Boss, **this README is sufficient for the lab level**—professional, concise, and not overloaded with theory. It also records the important debugging experience from our actual execution rather than pretending everything worked on the first attempt.


### Next → Lab 05


Now we can move directly to:


**`05_Working_with_Different_File_Formats`**


We will follow the same locked workflow:


**Folder Structure → IBM Lab → Run → My Practice → Challenge → Debug Notes → README → Git**


Let's proceed with **Lab 05 – Working with Different File Formats**
```
