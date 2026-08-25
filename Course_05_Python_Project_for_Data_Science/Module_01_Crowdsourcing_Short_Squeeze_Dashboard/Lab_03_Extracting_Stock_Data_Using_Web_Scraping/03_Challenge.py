"""
Lab 03 - Challenge

Course 05 - Python Project for Data Science
Module 01 - Crowdsourcing Short Squeeze Dashboard

Challenge:
    Build a reusable multi-stock web-scraping pipeline and
    generate a stock-level summary DataFrame.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup


# -------------------------------------------------------------------
# 1. Stock Configuration
# -------------------------------------------------------------------

STOCK_URLS = {
    "NFLX": (
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/"
        "netflix_data_webpage.html"
    ),
    "AMZN": (
        "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
        "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/"
        "amazon_data_webpage.html"
    ),
}


# -------------------------------------------------------------------
# 2. Web Scraping Function
# -------------------------------------------------------------------

def scrape_stock_table(url):
    """Extract the first HTML table from a stock webpage."""

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")

    if table is None:
        raise ValueError("No HTML table found on the webpage.")

    rows = table.find_all("tr")

    headers = [
        cell.get_text(strip=True)
        for cell in rows[0].find_all(["th", "td"])
    ]

    records = []

    for row in rows[1:]:
        cells = row.find_all("td")

        if len(cells) == len(headers):
            records.append(
                [cell.get_text(strip=True) for cell in cells]
            )

    return pd.DataFrame(records, columns=headers)


# -------------------------------------------------------------------
# 3. Normalize Column Names
# -------------------------------------------------------------------

def normalize_stock_columns(dataframe):
    """Standardize Yahoo Finance column names."""

    dataframe = dataframe.rename(
        columns={
            "Close*": "Close",
            "Adj Close**": "Adj Close",
        }
    )

    return dataframe


# -------------------------------------------------------------------
# 4. Clean Numeric Columns
# -------------------------------------------------------------------

def clean_numeric_columns(dataframe):
    """Convert financial columns from strings to numeric values."""

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


# -------------------------------------------------------------------
# 5. Scrape and Prepare One Stock
# -------------------------------------------------------------------

def prepare_stock_data(ticker, url):
    """Scrape, normalize, clean, and label one stock dataset."""

    dataframe = scrape_stock_table(url)

    dataframe = normalize_stock_columns(dataframe)

    dataframe = clean_numeric_columns(dataframe)

    dataframe.insert(0, "Ticker", ticker)

    return dataframe


# -------------------------------------------------------------------
# 6. Process All Stocks
# -------------------------------------------------------------------

stock_dataframes = []

for ticker, url in STOCK_URLS.items():
    print(f"Scraping {ticker}...")

    stock_dataframe = prepare_stock_data(ticker, url)

    stock_dataframes.append(stock_dataframe)


# -------------------------------------------------------------------
# 7. Combine Stock Data
# -------------------------------------------------------------------

all_stock_data = pd.concat(
    stock_dataframes,
    ignore_index=True,
)


print("\n" + "=" * 70)
print("COMBINED STOCK DATA")
print("=" * 70)

print(all_stock_data.head())

print("\nTotal records:", len(all_stock_data))

print("\nRecords by stock:")
print(all_stock_data["Ticker"].value_counts())


# -------------------------------------------------------------------
# 8. Generate Stock Summary
# -------------------------------------------------------------------

stock_summary = (
    all_stock_data
    .groupby("Ticker")
    .agg(
        Records=("Date", "count"),
        Average_Close=("Close", "mean"),
        Highest_Close=("Close", "max"),
        Lowest_Close=("Close", "min"),
        Average_Volume=("Volume", "mean"),
        Highest_Volume=("Volume", "max"),
    )
    .reset_index()
)


# -------------------------------------------------------------------
# 9. Display Summary
# -------------------------------------------------------------------

print("\n" + "=" * 70)
print("STOCK SUMMARY")
print("=" * 70)

print(stock_summary.to_string(index=False))


# -------------------------------------------------------------------
# 10. Identify Highest-Volume Stock
# -------------------------------------------------------------------

highest_volume_index = stock_summary["Highest_Volume"].idxmax()

highest_volume_stock = stock_summary.loc[
    highest_volume_index
]

print("\n" + "=" * 70)
print("HIGHEST-VOLUME STOCK")
print("=" * 70)

print(
    f"Stock: {highest_volume_stock['Ticker']}"
)

print(
    f"Highest Volume: "
    f"{highest_volume_stock['Highest_Volume']:,.0f}"
)


# -------------------------------------------------------------------
# 11. Identify Highest Average Closing Price
# -------------------------------------------------------------------

highest_average_close_index = stock_summary[
    "Average_Close"
].idxmax()

highest_average_close_stock = stock_summary.loc[
    highest_average_close_index
]

print("\n" + "=" * 70)
print("HIGHEST AVERAGE CLOSING PRICE")
print("=" * 70)

print(
    f"Stock: "
    f"{highest_average_close_stock['Ticker']}"
)

print(
    f"Average Close: "
    f"${highest_average_close_stock['Average_Close']:.2f}"
)
