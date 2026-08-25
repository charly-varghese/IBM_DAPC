# Lab 01 – Introduction to Web Scraping Using BeautifulSoup

## Course 05 – Python Project for Data Science

### Module 01 – Crowdsourcing Short Squeeze Dashboard

---

## 1. Lab Overview

This lab introduces the fundamentals of **Web Scraping using Python and BeautifulSoup**.

The practical work covers how to:

- Parse HTML content
- Navigate HTML elements
- Find tags and attributes
- Extract text from HTML
- Extract links and images
- Extract tabular data
- Convert scraped data into a Pandas DataFrame
- Clean scraped data
- Perform basic analysis on extracted market-style data

The lab establishes the foundation for later stages of the **Crowdsourcing Short Squeeze Dashboard** project.

---

## 2. Learning Objectives

By completing this lab, I practiced how to:

1. Import and use BeautifulSoup
2. Parse HTML using `html.parser`
3. Use `find()` and `find_all()`
4. Access HTML tags and attributes
5. Extract text using `get_text()`
6. Extract hyperlinks and image information
7. Identify HTML tables
8. Extract rows using `<tr>`
9. Extract cells using `<td>`
10. Build Python dictionaries from scraped data
11. Build a list of dictionaries
12. Convert scraped data into a Pandas DataFrame
13. Convert text-based numeric data into numeric types
14. Perform basic DataFrame analysis

---

## 3. Technologies Used

- Python
- BeautifulSoup4
- Requests
- Pandas
- VS Code
- Python Virtual Environment (`.venv`)

---

## 4. Environment Verification

The practical work was completed inside the project virtual environment.

Verified packages:

```text
requests: 2.34.2
BeautifulSoup: OK
pandas: 3.0.5
``
5. IBM Lab Practice
5.1 HTML Parsing

A sample HTML document was parsed using BeautifulSoup:

soup = BeautifulSoup(html, "html.parser")

This allowed the HTML document to be navigated programmatically.

5.2 Finding HTML Elements

The lab practiced:

soup.find()

and:

soup.find_all()

Examples included finding:

title
h3
body
elements with specific IDs
multiple HTML elements
5.3 HTML Attributes

Attributes were inspected using:

tag.attrs

Example:

{'id': 'boldest'}

Specific attributes can also be accessed directly.

5.4 Extracting Text

Text content was extracted from HTML elements.

Example:

tag.get_text()

This converts HTML such as:

<b id="boldest">Lebron James</b>

into:

Lebron James
6. Links and Images

The lab also practiced extracting hyperlinks and images from HTML pages.

Links

Important fields:

Link text
URL
Images

Important fields:

Image source
Alt text

This demonstrates how web pages can be converted from unstructured HTML into structured information.

7. HTML Table Extraction

The most important practical section was extracting tabular data.

The basic structure of an HTML table is:

<table>
    <tr>
        <td>...</td>
        <td>...</td>
    </tr>
</table>

The scraping process used:

table = soup.find("table")

Then:

rows = table.find_all("tr")

And individual cells were extracted using:

cells = row.find_all("td")
8. From HTML to Structured Data

The extracted cell values were converted into Python dictionaries.

Example structure:

{
    "Ticker": ticker,
    "Company": company,
    "Price": price,
    "Volume": volume
}

Multiple records were stored in a list:

HTML
 ↓
BeautifulSoup
 ↓
Rows
 ↓
Cells
 ↓
Dictionary
 ↓
List of Dictionaries
9. HTML → Pandas DataFrame

The extracted records were converted into a Pandas DataFrame:

stock_df = pd.DataFrame(stock_data)

Result:

  Ticker    Company Price   Volume
0   AAPL      Apple   220  5000000
1   MSFT  Microsoft   510  3200000
2   TSLA      Tesla   340  7100000

This is an important transition from web scraping to data analysis.

10. Data Cleaning

Scraped numerical values initially existed as text.

They were converted to numeric values using:

stock_df["Price"] = pd.to_numeric(stock_df["Price"])
stock_df["Volume"] = pd.to_numeric(stock_df["Volume"])

This produced numeric data types suitable for analysis.

11. My Practice

A stock-market style HTML table was created and scraped independently.

The dataset contained:

| Ticker | Company   | Price | Volume    |
|--------|-----------|------:|----------:|
| AAPL   | Apple     | 220   | 5,000,000 |
| MSFT   | Microsoft | 510   | 3,200,000 |
| TSLA   | Tesla     | 340   | 7,100,000 |

The extracted data was converted into a Pandas DataFrame and cleaned for analysis.

12. Challenge

The challenge extended the My Practice exercise.

The following metrics were calculated:

Average Price
356.67
Total Trading Volume
15,300,000
Highest Volume Stock
TSLA
Highest Price Stock
MSFT
13. Debugging Experience

Several practical debugging situations were encountered during the lab.

Case 1 – Variable Name / Case Sensitivity

Python variable names are case-sensitive.

For example:

table_index

and:

table_Index

are different variables.

Case 2 – Undefined Variable

A NameError occurred when table_index was referenced before a matching table had been found.

The solution was to initialize and validate the variable:

table_index = None

and then:

if table_index is not None:
    ...
Case 3 – HTTP 403

A live webpage request returned:

Status Code: 403

This demonstrated that web scraping can fail because of server-side access restrictions.

Instead of spending excessive time fighting the website, the practical exercise continued using controlled HTML data so that the actual BeautifulSoup learning objectives could be completed.

Case 4 – Duplicate Output

During the Challenge, records were accidentally printed multiple times.

The cause was duplicate loop/code blocks rather than incorrect data extraction.

After removing the duplicate block, the expected three records were produced.

This reinforced the importance of checking both:

program logic
duplicated code
14. Key Concepts Learned
BeautifulSoup
     ↓
Parse HTML
     ↓
Find elements
     ↓
Extract attributes/text
     ↓
Extract tables
     ↓
Create structured records
     ↓
Pandas DataFrame
     ↓
Clean data
     ↓
Analyze data

This workflow is highly relevant to real-world data collection pipelines.

15. Connection to the Short Squeeze Dashboard

The skills learned in this lab form the foundation for collecting market-related information.

The same pipeline can later be extended to datasets containing fields such as:

Ticker
Price
Volume
Short Interest
Float
Short Ratio
Market Capitalization

These fields can eventually be combined to support short squeeze analysis and dashboard development.

16. Files in This Lab
Lab_01_Intro_to_Web_Scraping_Using_BeautifulSoup/
│
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 03_Challenge.py
├── 04_Debug_Notes.md
└── README.md
17. Practical Workflow
This lab followed the portfolio learning workflow:

EXPLAIN
   ↓
SHOW
   ↓
DO
   ↓
FIX
   ↓
MASTER
   ↓
DOCUMENT
   ↓
GIT

The objective was not simply to complete the IBM exercise, but to convert the concepts into reusable Python and data-analysis skills.

Status

Lab 01 – COMPLETED

IBM Lab       ✅
My Practice   ✅
Challenge     ✅
Debugging     ✅
Documentation 🔄
Git Review    ⬜
Git Commit    ⬜
```
