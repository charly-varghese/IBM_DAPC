# Module 05 – APIs and Data Collection

## Overview

Module 05 introduces practical techniques for collecting data from external sources using APIs, HTTP requests, and web-scraping methods.

The practical implementation was completed in VS Code using Python, with a focus on reliable data collection, validation, cleaning, analysis, and export. Each completed lab includes IBM-based implementation, custom practice, debugging, and professional documentation.

This module forms an important bridge between Python programming and real-world data acquisition workflows used in Data Analytics and Data Engineering.

---

## Practical Scope

The practical portfolio implementation covers:

- Introduction to APIs
- REST APIs and HTTP Requests
- API-based data collection
- JSON response handling
- Random user data generation
- Web scraping
- HTML parsing
- HTML table extraction
- Data cleaning and validation
- CSV data export
- Error handling and debugging

### Practical Labs Completed

| Lab | Topic                                    | Status       |
| --- | ---------------------------------------- | ------------ |
| 01  | Introduction to APIs                     | ✅ Completed |
| 02  | REST APIs & HTTP Requests                | ✅ Completed |
| 03  | API Examples                             | ✅ Completed |
| 04  | Web Scraping                             | ✅ Completed |
| 05  | Working with Different File Formats      | ⏭️ Skipped   |
| 06  | GDP Data Extraction & Processing Project | ⏭️ Skipped   |

Labs 05 and 06 were intentionally excluded from the hands-on portfolio implementation to maintain a focused and manageable Course 04 practical scope. Their concepts remain part of the overall IBM course learning and can be revisited when required.

---

## Folder Structure

```text
Module_05_APIs_and_Data_Collection/
│
├── 01_Introduction_to_APIs/
│   ├── 01_IBM_Lab.py
│   ├── 02_My_Practice.py
│   ├── 03_Challenge.py
│   ├── 04_Debug_Notes.md
│   └── README.md
│
├── 02_REST_APIs_HTTP_Requests/
│   ├── 01_IBM_Lab.py
│   ├── 02_My_Practice.py
│   ├── 03_Challenge.py
│   └── README.md
│
├── 03_API_Examples/
│   ├── 01_IBM_Lab.py
│   ├── 02_My_Practice.py
│   └── README.md
│
├── 04_Web_Scraping/
│   ├── 01_IBM_Lab.py
│   ├── 02_My_Practice.py
│   ├── 03_Challenge.py
│   ├── 04_Debug_Notes.md
│   ├── README.md
│   └── practice_output/
│
└── README.md
```

---

## Lab 01 – Introduction to APIs

## Practical Focus

The lab introduced the basic concept of obtaining data through programmatic interfaces.

The implementation included:

- Simple API interaction
- Response inspection
- Pickle-based data handling
- Dataset exploration
- Working with structured data

The practice program and challenge extended the IBM exercise into custom Python implementations.

\*_Status: Completed_

---

## Lab 02 – REST APIs & HTTP Requests

This lab provided hands-on experience with HTTP-based APIs and Python's `requests` library.

Key implementation areas included:

- `requests.get()`
- HTTP status codes
- JSON responses
- Dictionaries and lists
- Pandas DataFrames
- Data extraction
- `value_counts()`
- CSV export
- `pathlib.Path`
- Output-file verification

### Environment Verification

The Requests library was verified inside the project virtual environment.

```text
Requests version: 2.34.2
```

### Debugging Experience

The IBM exercise used external services including `httpbin.org`.

Some requests returned:

- `503 Service Unavailable`
- `ReadTimeout`
- `JSONDecodeError`

These were correctly identified as external service/server-response issues rather than Python syntax errors.

The practice implementation successfully used JSONPlaceholder as a stable API source for structured data collection.

\*_Status: Completed_

---

## Lab 03 – API Examples

Practical Focus

This lab demonstrated practical API-based generation and collection of user information.

The IBM exercise generated:

```text
10 Random Users
```

The custom practice implementation generated:

```text
20 Random Users
```

The implementation included:

- Random user API/package usage
- Pandas
- Data validation
- Missing-value checking
- Duplicate checking
- Gender distribution
- State analysis
- City analysis
- CSV export
- Output verification

Final practice output:

```text
practice_output/random_users.csv
```

\*_Status: Completed_

---

## Lab 04 – Web Scraping

Practical Focus

Lab 04 expanded the data-collection workflow from APIs to HTML-based web scraping.

Technologies and techniques included:

- `requests`
- `BeautifulSoup`
- HTML parsing
- `find()`
- `find_all()`
- CSS selectors
- HTML tables
- Pandas `read_html()`
- `StringIO`
- HTTP status validation
- User-Agent headers
- Timeout handling
- Data cleaning
- Data validation
- CSV export
- Encoding handling
- Responsible scraping

### Practice Dataset

The custom practice program extracted an online color-code dataset.

Final cleaned dataset:

```text
32 records × 4 columns
Missing Values = 0
Duplicate Rows = 0
```

Output:

```text
04_Web_Scraping/practice_output/color_codes.csv
```

### Challenge Dataset

The custom challenge extracted travel-book information from the Books to Scrape practice website.

Fields collected:

- Title
- Price
- Availability

Final validation:

```text
Records = 11
Missing Values = 0
Duplicate Rows = 0
Invalid Titles = 0
Invalid Prices = 0
Invalid Availability = 0
```

Analysis results:

```text
Average Price = £39.79
Minimum Price = £23.21
Maximum Price = £56.88
```

Output:

```text
04_Web_Scraping/practice_output/challenge_books.csv
```

Challenge status:

\*_PASSED_

---

## Key Debugging Lessons

Module 05 provided several important real-world debugging experiences.

## 1. HTTP 200 Does Not Guarantee Correct Data

A successful HTTP request only confirms that the server responded successfully.

It does **not** guarantee that the extracted dataset is correct.

Therefore:

```text
Request Success
        ↓
Extraction Validation
        ↓
Data Quality Validation
```

must be treated as separate steps.

---

## 2. External API Failures Are Not Always Python Errors

External services may return:

- Timeout errors
- HTTP 503
- Invalid/non-JSON responses
- Temporary service failures

These should be distinguished from actual Python programming errors.

---

## 3. HTML Parsing Requires Flexible Extraction

Web pages can contain unexpected structures or encoding behaviour.

The Web Scraping challenge initially produced:

```text
Price = NaN
```

for all records even though the HTTP request returned:

```text
HTTP Status Code: 200
```

The issue was identified through validation and corrected using more reliable selectors, fallback extraction, and explicit UTF-8 handling.

---

## 4. Pandas HTML Parsing

Modern Pandas requires HTML strings to be wrapped using `StringIO` when passed to `read_html()`.

Example:

```python
from io import StringIO

pd.read_html(
    StringIO(html_content)
)
```

This was an important compatibility lesson during the Web Scraping practice.

---

## Tools & Technologies

- Python 3.14
- Requests
- BeautifulSoup
- Pandas
- pathlib
- JSON
- HTML
- REST APIs
- HTTP
- CSV
- StringIO
- Regular Expressions
- VS Code
- Git
- GitHub
- Python Virtual Environment

---

## Practical Data Collection Workflow

The completed work demonstrates the following general workflow:

```text
External Source
      ↓
HTTP/API Request
      ↓
Response Validation
      ↓
Data Extraction
      ↓
Data Cleaning
      ↓
Data Validation
      ↓
Data Analysis
      ↓
CSV / Dataset Export
      ↓
Output Verification
```

This workflow is directly applicable to real-world Data Analyst and Data Engineering projects.

---

## Professional Practices Applied

Throughout the module, the practical work emphasized:

- Virtual-environment usage
- Error handling
- HTTP status validation
- Timeout handling
- Data-quality checks
- Missing-value detection
- Duplicate detection
- Output verification
- Clean folder organization
- Reusable Python structure
- Debug documentation
- Git/GitHub portfolio preparation

---

## Practical Scope Decision

Labs 05 and 06 were intentionally skipped from the hands-on implementation.

This was a deliberate scope decision because the completed practical work already provides substantial coverage of:

- API interaction
- REST APIs
- HTTP requests
- JSON
- structured data collection
- Pandas integration
- web scraping
- HTML parsing
- data cleaning
- validation
- analysis
- CSV export
- debugging

The skipped labs remain available for future targeted study if a project requires those specific file-format or GDP-processing techniques.

---

## Module Status

\*_Module 05 – APIs and Data Collection: PRACTICAL SCOPE COMPLETED_

### Completed

- Lab 01 – Introduction to APIs ✅
- Lab 02 – REST APIs & HTTP Requests ✅
- Lab 03 – API Examples ✅
- Lab 04 – Web Scraping ✅
- Debugging & validation ✅
- Lab-level README documentation ✅
- Module-level documentation ✅

### Intentionally Skipped

- Lab 05 – Working with Different File Formats ⏭️
- Lab 06 – GDP Data Extraction & Processing Project ⏭️

---

## Portfolio Outcome

Module 05 demonstrates practical experience in acquiring external data, transforming it into analysis-ready structures, validating data quality, and producing reusable datasets.

This completes the practical API and data-collection component of **IBM DAPC Course 04**.
