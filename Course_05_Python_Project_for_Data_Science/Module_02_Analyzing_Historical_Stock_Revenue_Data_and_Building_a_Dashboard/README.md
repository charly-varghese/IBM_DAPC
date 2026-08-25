# Module 02 — Analyzing Historical Stock/Revenue Data and Building a Dashboard

## Course 05 — Python Project for Data Science

This module is the final project for **Course 05 — Python Project for Data Science**.

The project applies Python-based data extraction, web scraping, data cleaning, analysis, and visualization to historical stock and revenue data.

The implementation follows a practical workflow:

```text
Extract
  ↓
Clean
  ↓
Transform
  ↓
Analyze
  ↓
Visualize
  ↓
Interpret

1. Project Objective

The objective of this project is to analyze historical stock-price and quarterly-revenue data and present the results through visualizations.

The project demonstrates how Python can be used to combine:

Financial market data
Web-scraped revenue data
Pandas DataFrames
Data cleaning
Statistical analysis
Time-series visualization
Interactive/dashboard-oriented analysis
2. Companies Analyzed

The final project focuses on:

Tesla
Amazon
AMD
GameStop

The practical exercises in this module additionally use Tesla and GameStop for stock/revenue analysis and comparison.

3. Technologies Used
Programming Language
Python
Development Environment
VS Code
Jupyter Notebook
Python Virtual Environment (.venv)
Python Libraries
pandas
yfinance
requests
beautifulsoup4
matplotlib
plotly
Data Sources
Historical stock data through yfinance
Revenue data extracted from HTML tables using pandas.read_html()
4. Project Structure
Module_02_Analyzing_Historical_Stock_Revenue_Data_and_Building_a_Dashboard/
│
├── Analyzing_Historical_Stock_Revenue_Data.ipynb
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 03_Challenge.py
├── 04_Debug_Notes.md
└── README.md
5. IBM Final Project Notebook
Analyzing_Historical_Stock_Revenue_Data.ipynb

The Jupyter Notebook contains the main IBM final-project implementation.

The notebook demonstrates the complete project workflow, including:

Importing Python libraries
Extracting historical stock data
Extracting quarterly revenue data
Cleaning revenue data
Preparing DataFrames
Creating stock/revenue visualizations
Building dashboard-style visualizations
Comparing historical stock performance and revenue

The notebook is also the primary artifact used for the official IBM project submission.

6. IBM Lab Implementation
01_IBM_Lab.py

This file contains the practical Python implementation of the IBM project workflow.

It demonstrates the core techniques required by the assignment:

Stock-data extraction
Revenue-data extraction
HTML-table processing
Data cleaning
DataFrame manipulation
Visualization

The implementation was executed successfully in VS Code.

7. My Practice
02_My_Practice.py

The My Practice program extends the IBM workflow into a reusable analysis structure.

Stock Data

Historical stock data is extracted using:

ticker = yf.Ticker(ticker_symbol)

stock_data = ticker.history(
    period="max"
)
Revenue Data

Revenue data is extracted from HTML using:

tables = pd.read_html(StringIO(response.text))

The required revenue table is then normalized:

revenue_data.columns = ["Date", "Revenue"]
Data Cleaning

Revenue values are converted into numeric values after removing currency symbols and thousands separators.

Raw Revenue
    ↓
Remove $
    ↓
Remove commas
    ↓
Convert to numeric
    ↓
Clean Revenue DataFrame
Analysis

The practice program calculates:

Highest closing price
Lowest closing price
Latest closing price
Revenue statistics

It also generates stock/revenue visualizations for:

Tesla
GameStop
8. Challenge
03_Challenge.py

The Challenge program extends the practice implementation into a comparative analysis between Tesla and GameStop.

The program performs:

Tesla stock extraction
Tesla revenue extraction
GameStop stock extraction
GameStop revenue extraction
Revenue cleaning
Statistical analysis
Company comparison
Visualization
Challenge Results

The executed Challenge produced the following results:

Metric Tesla GameStop
Highest Closing Price $489.88 $86.88
Lowest Closing Price $1.05 $0.64
Average Closing Price $110.81 $9.37
Highest Revenue $21,454M $3,693M
Lowest Revenue $21M  $416M
Average Revenue $4,101.23M  $1,967.69M
Key Findings
Tesla reached the higher maximum closing price.
Tesla recorded the higher maximum revenue.

These results were generated directly from the executed Python program.

9. Data Extraction Workflow

The project combines two major approaches.

Historical Stock Data
Company Ticker
      ↓
yfinance
      ↓
Historical Stock Data
      ↓
Pandas DataFrame
      ↓
Analysis
Revenue Data
Revenue Webpage
      ↓
requests
      ↓
HTML
      ↓
pandas.read_html()
      ↓
Revenue DataFrame
      ↓
Cleaning
      ↓
Analysis
10. Important Web-Scraping Technique

One important debugging lesson from this project was that HTML tables do not always provide the expected column names.

Initially, the code assumed that the extracted table already contained:

Date
Revenue

However, the extracted table structure did not expose those names directly.

The solution was to select the required table and explicitly normalize its columns:

revenue_data = tables[1].copy()

revenue_data.columns = ["Date", "Revenue"]

This made the revenue-processing workflow reliable.

11. Revenue Data Cleaning

Financial data frequently contains formatting characters.

For example:

$21,454
$16,934

The project removes these formatting characters before numerical analysis.

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

This produces numeric revenue values suitable for:

Statistical calculations
Comparisons
Plotting
Time-series analysis
12. Data Validation

The project validates the extracted data before performing analysis.

Important checks include:

print(dataframe.columns)
print(dataframe.dtypes)
print(dataframe.head())

and checking for invalid values.

This ensures that the extraction and cleaning stages produce usable DataFrames.

13. Visualization

Visualization is used to identify historical relationships and trends between stock performance and revenue.

The project uses:

Matplotlib for practical analysis visualizations
Plotly for interactive dashboard-oriented visualizations in the final notebook

The visualizations focus on:

Historical stock prices
Quarterly revenue
Stock/revenue relationships
Company comparisons
14. Debugging Highlights

Several real implementation issues were encountered and resolved during development.

Issue 1 — Revenue Column KeyError
KeyError: 'Revenue'
Cause

The extracted HTML table did not initially expose the expected column names.

Solution

The selected revenue table was explicitly normalized:

revenue_data.columns = ["Date", "Revenue"]
Issue 2 — Revenue Table Detection

An initial implementation attempted to detect the revenue table by searching for:

Date
Revenue

in the extracted column names.

This failed because the source table structure did not provide those names directly.

The solution was to inspect the extracted tables and select the correct revenue table before assigning normalized column names.

Issue 3 — Financial Data Conversion

Revenue values containing:

$
,

cannot be directly used for numerical analysis.

They were cleaned before conversion using Pandas string operations and pd.to_numeric().

15. Final Validation

The practical implementation was successfully executed in VS Code.

02_My_Practice.py
PRACTICE COMPLETE

Confirmed:

Stock data extraction
Revenue extraction
Revenue cleaning
Data-type conversion
Basic analysis
Tesla visualization
GameStop visualization
03_Challenge.py
CHALLENGE COMPLETE

Confirmed:

Tesla stock extraction
Tesla revenue extraction
GameStop stock extraction
GameStop revenue extraction
Revenue cleaning
Statistical analysis
Company comparison
Tesla visualization
GameStop visualization
16. Learning Outcomes

This project strengthened practical skills in:

Python financial-data extraction
yfinance
HTTP requests
HTML table extraction
pandas.read_html()
BeautifulSoup
Pandas DataFrames
Data cleaning
Numeric conversion
Datetime conversion
Statistical analysis
Time-series analysis
Matplotlib visualization
Plotly visualization
Dashboard-oriented thinking
Debugging
Reusable Python functions
17. Professional Data Workflow

The complete project demonstrates the following data workflow:

                    DATA SOURCES
                         │
             ┌───────────┴───────────┐
             │                       │
       Stock Data              Revenue Data
             │                       │
         yfinance              Web Scraping
             │                       │
             └───────────┬───────────┘
                         │
                   Pandas DataFrames
                         │
                    Data Cleaning
                         │
                   Data Validation
                         │
                     Analysis
                         │
                  Visualization
                         │
                 Dashboard Insights
18. Portfolio Significance

This project represents a complete practical data-analysis workflow rather than a collection of isolated exercises.

It combines:

Data Extraction
      +
Web Scraping
      +
Data Cleaning
      +
Data Analysis
      +
Visualization
      +
Debugging
      +
Documentation

The project therefore serves as a practical portfolio example of using Python to transform raw financial data into meaningful analytical insights.

19. Final Status
Component Status
IBM Final Project Notebook ✅ Completed
IBM Lab Implementation ✅ Completed
My Practice ✅ Completed
Challenge ✅ Completed
Revenue Web Scraping ✅ Completed
Stock Data Extraction ✅ Completed
Data Cleaning ✅ Completed
Data Analysis ✅ Completed
Visualization ✅ Completed
Debug Notes ✅ Completed
README Documentation ✅ Completed
VS Code Validation ✅ Completed
Git/GitHub Ready ✅ Ready
Course 05 — Module 02

Status: COMPLETED

This module completes the practical implementation of the Course 05 final project:

Analyzing Historical Stock/Revenue Data and Building a Dashboard
```
