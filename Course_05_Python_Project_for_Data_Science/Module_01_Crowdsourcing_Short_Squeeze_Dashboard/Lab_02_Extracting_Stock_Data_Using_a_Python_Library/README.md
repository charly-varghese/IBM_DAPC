# Lab 02 — Extracting Stock Data Using a Python Library

## Course

**Course 05 — Python Project for Data Science*

## Module

**Module 01 — Crowdsourcing Short Squeeze Dashboard*

## Lab Objective

This lab demonstrates how to extract and analyze stock market data using the
`yfinance` Python library.

The lab progresses from analyzing a single stock to building a reusable
multi-stock analysis workflow using Python and Pandas.

---

## Technologies Used

- Python
- yfinance
- Pandas
- VS Code
- Git / GitHub

---

## Learning Objectives

By completing this lab, the following practical skills were implemented:

- Create a `yfinance.Ticker` object.
- Extract company information.
- Retrieve historical stock price data.
- Retrieve historical dividend data.
- Work with Pandas DataFrames and Series.
- Calculate average closing prices.
- Calculate total trading volume.
- Identify the highest-volume trading day.
- Build a multi-stock analysis workflow.
- Store analytical results using a list of dictionaries.
- Convert collected results into a Pandas DataFrame.
- Compare multiple stocks using Pandas.
- Identify stocks with the highest trading activity.

---

## Lab Structure

```text
Lab_02_Extracting_Stock_Data_Using_a_Python_Library/
│
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 03_Challenge.py
├── 04_Debug_Notes.md
└── README.md
1. IBM Lab Implementation
File

01_IBM_Lab.py

The IBM implementation covers:

Creating an Apple (AAPL) ticker object.
Extracting Apple company information.
Retrieving maximum available historical share-price data.
Resetting the DataFrame index.
Plotting historical opening prices.
Extracting historical dividend data.
Plotting historical dividends.
Completing the AMD exercise.
AMD Exercise

The implementation extracts:

Country
Sector
First-day trading volume
2. My Practice
File

02_My_Practice.py

The My Practice program extends the IBM lab from single-stock analysis
to reusable multi-stock analysis.

Stocks Analyzed
AAPL
MSFT
NVDA
Metrics Calculated

For each stock:

Company
Country
Sector
Number of trading days
Average closing price
Total trading volume
Highest trading volume
Highest trading-volume date

The results are collected as dictionaries and converted into a Pandas
DataFrame.

Example Analysis

The program identifies the stock with the highest total trading volume.

For the retrieved dataset:

Highest Total Volume Stock: NVDA
Total Volume: 42,398,709,700
3. Challenge
File

03_Challenge.py

The Challenge extends the multi-stock analysis by adding AMD:

AAPL
MSFT
NVDA
AMD

The program identifies:

Stock with the highest average closing price.
Stock with the highest total trading volume.
Stock with the highest single-day trading volume.
Challenge Results

For the retrieved dataset:

Highest Average Closing Price:
MSFT — 445.74

Highest Total Trading Volume:
NVDA — 42,398,709,700

Highest Single-Day Trading Volume:
NVDA — 360,807,900
4. Key Python and Pandas Techniques
yfinance
stock = yf.Ticker("AAPL")
stock_info = stock.info
stock_history = stock.history(period="1y")
Selecting a DataFrame Column
stock_history["Close"]
Calculating an Average
stock_history["Close"].mean()
Calculating Total Volume
stock_history["Volume"].sum()
Finding the Maximum Value
stock_history["Volume"].idxmax()
Retrieving a Value Using .loc
stock_history.loc[highest_volume_index, "Volume"]
Creating a DataFrame from Collected Results
pd.DataFrame(stock_results)
5. Data Processing Workflow

The practical workflow developed in this lab is:

yfinance
    ↓
Ticker Object
    ↓
Company Information
    ↓
Historical Market Data
    ↓
Pandas Analysis
    ↓
Calculated Metrics
    ↓
List of Dictionaries
    ↓
Pandas DataFrame
    ↓
Cross-Stock Comparison

This workflow provides a foundation for more advanced financial-data
analysis and the Short Squeeze Dashboard developed later in the module.

6. Debugging
File

04_Debug_Notes.md

The main debugging issues addressed during the lab included:

Using stock_history before it was created.
Incorrect indentation and execution order inside the multi-stock loop.

These were resolved and documented.

Final Validation
01_IBM_Lab.py        → PASS
02_My_Practice.py    → PASS
03_Challenge.py     → PASS
Markdownlint         → PASS
7. Professional Learning Outcome

This lab moved beyond simply extracting stock data.

The final implementation demonstrates a reusable analytical pattern:

Single Stock Analysis
        ↓
Reusable Multi-Stock Analysis
        ↓
Metric Calculation
        ↓
Structured Results
        ↓
Comparative Analysis

This pattern will be reused in later financial-data projects and in the
development of the Crowdsourcing Short Squeeze Dashboard.

Status

Lab 02 — COMPLETED ✅

Course 05 — Module 01 practical portfolio: In Progress


