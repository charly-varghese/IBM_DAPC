"""
Lab 03 - My Practice

Course 05 - Python Project for Data Science
Module 01 - Crowdsourcing Short Squeeze Dashboard

Purpose:
    Build a reusable web-scraping workflow for extracting
    historical stock data from HTML tables.
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

# -------------------------------------------------------------------
# 1. Stock URLs
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
# 2. Reusable scraping function
# -------------------------------------------------------------------


def scrape_stock_table(url):
    """Extract the first HTML table from a stock-data webpage."""

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")

    if table is None:
        raise ValueError("No HTML table found on the webpage.")

    rows = table.find_all("tr")

    headers = [cell.get_text(strip=True) for cell in rows[0].find_all(["th", "td"])]

    records = []

    for row in rows[1:]:
        cells = row.find_all("td")

        if len(cells) == len(headers):
            records.append([cell.get_text(strip=True) for cell in cells])

    return pd.DataFrame(records, columns=headers)


# -------------------------------------------------------------------
# 3. Scrape Netflix data
# -------------------------------------------------------------------

netflix_data = scrape_stock_table(STOCK_URLS["NFLX"])

print("=" * 70)
print("NETFLIX STOCK DATA")
print("=" * 70)

print(netflix_data.head())


# -------------------------------------------------------------------
# 4. Scrape Amazon data
# -------------------------------------------------------------------

amazon_data = scrape_stock_table(STOCK_URLS["AMZN"])

print("\n" + "=" * 70)
print("AMAZON STOCK DATA")
print("=" * 70)

print(amazon_data.head())


# -------------------------------------------------------------------
# 5. Normalize scraped column names
# -------------------------------------------------------------------


def normalize_stock_columns(dataframe):
    """Normalize Yahoo Finance column names."""

    dataframe = dataframe.rename(
        columns={
            "Close*": "Close",
            "Adj Close**": "Adj Close",
        }
    )

    return dataframe


netflix_data = normalize_stock_columns(netflix_data)
amazon_data = normalize_stock_columns(amazon_data)


# -------------------------------------------------------------------
# 6. Clean financial columns
# -------------------------------------------------------------------


def clean_numeric_columns(dataframe):
    """Convert scraped financial columns into numeric values."""

    numeric_columns = [column for column in dataframe.columns if column != "Date"]

    for column in numeric_columns:
        dataframe[column] = (
            dataframe[column].str.replace(",", "", regex=False).astype(float)
        )

    return dataframe


netflix_data = clean_numeric_columns(netflix_data)
amazon_data = clean_numeric_columns(amazon_data)


# -------------------------------------------------------------------
# 7. Validate the extracted data
# -------------------------------------------------------------------

print("\n" + "=" * 70)
print("DATA VALIDATION")
print("=" * 70)

print("\nNetflix:")
print("Rows:", len(netflix_data))
print("Columns:", netflix_data.columns.tolist())

print("\nAmazon:")
print("Rows:", len(amazon_data))
print("Columns:", amazon_data.columns.tolist())


# -------------------------------------------------------------------
# 8. Basic stock comparison
# -------------------------------------------------------------------

netflix_average_close = netflix_data["Close"].mean()
amazon_average_close = amazon_data["Close"].mean()

netflix_highest_close = netflix_data["Close"].max()
amazon_highest_close = amazon_data["Close"].max()

print("\n" + "=" * 70)
print("STOCK COMPARISON")
print("=" * 70)

print(f"\nNetflix average close: ${netflix_average_close:.2f}")
print(f"Amazon average close: ${amazon_average_close:.2f}")

print(f"\nNetflix highest close: ${netflix_highest_close:.2f}")
print(f"Amazon highest close: ${amazon_highest_close:.2f}")


# -------------------------------------------------------------------
# 9. Highest-volume trading period
# -------------------------------------------------------------------

netflix_highest_volume = netflix_data.loc[netflix_data["Volume"].idxmax()]

amazon_highest_volume = amazon_data.loc[amazon_data["Volume"].idxmax()]

print("\n" + "=" * 70)
print("HIGHEST TRADING VOLUME")
print("=" * 70)

print("\nNetflix:")
print(netflix_highest_volume[["Date", "Volume"]])

print("\nAmazon:")
print(amazon_highest_volume[["Date", "Volume"]])
