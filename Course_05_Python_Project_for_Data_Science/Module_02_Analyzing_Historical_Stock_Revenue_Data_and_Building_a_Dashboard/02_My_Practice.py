"""
Course 05 - Module 02
My Practice: Historical Stock & Revenue Analysis

Purpose:
    Practice stock-data extraction, web scraping, data cleaning,
    and visualization using Tesla and GameStop.
"""

import pandas as pd
import requests
import yfinance as yf
import matplotlib.pyplot as plt
from io import StringIO

# ============================================================
# 1. EXTRACT STOCK DATA USING YFINANCE
# ============================================================


def get_stock_data(ticker_symbol):
    """Download maximum available historical stock data."""

    ticker = yf.Ticker(ticker_symbol)
    stock_data = ticker.history(period="max")

    stock_data.reset_index(inplace=True)

    return stock_data


# ============================================================
# 2. EXTRACT REVENUE DATA FROM WEB PAGE
# ============================================================

def get_revenue_data(url, table_index=1):
    """Extract and prepare the revenue table from an HTML webpage."""

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    html_data = response.text

    tables = pd.read_html(StringIO(html_data))

    print(f"Number of tables found: {len(tables)}")

    # Select the revenue table
    revenue_data = tables[table_index].copy()

    # The HTML table does not provide useful column names,
    # so assign the expected names manually.
    revenue_data.columns = ["Date", "Revenue"]

    return revenue_data


# ============================================================
# 3. CLEAN REVENUE DATA
# ============================================================


def clean_revenue_data(revenue_data):
    """Clean revenue values and remove invalid records."""

    revenue_data["Revenue"] = (
        revenue_data["Revenue"]
        .astype(str)
        .str.replace(r"[$,]", "", regex=True)
        .str.strip()
    )

    revenue_data["Revenue"] = pd.to_numeric(revenue_data["Revenue"], errors="coerce")

    revenue_data.dropna(subset=["Revenue"], inplace=True)

    revenue_data["Date"] = pd.to_datetime(revenue_data["Date"], errors="coerce")

    revenue_data.dropna(subset=["Date"], inplace=True)

    revenue_data.reset_index(drop=True, inplace=True)

    return revenue_data


# ============================================================
# 4. LOAD TESLA DATA
# ============================================================

print("=" * 60)
print("TESLA STOCK & REVENUE ANALYSIS")
print("=" * 60)

tesla_data = get_stock_data("TSLA")

tesla_revenue_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage."
    "appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/"
    "labs/project/revenue.htm"
)

tesla_revenue = get_revenue_data(tesla_revenue_url)
tesla_revenue = clean_revenue_data(tesla_revenue)


print("\nTesla Stock Data:")
print(tesla_data.head())

print("\nTesla Revenue Data:")
print(tesla_revenue.head())

print("\nTesla Revenue Data Types:")
print(tesla_revenue.dtypes)


# ============================================================
# 5. LOAD GAMESTOP DATA
# ============================================================

print("\n" + "=" * 60)
print("GAMESTOP STOCK & REVENUE ANALYSIS")
print("=" * 60)

gme_data = get_stock_data("GME")

gme_revenue_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage."
    "appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/"
    "labs/project/stock.html"
)

gme_revenue = get_revenue_data(gme_revenue_url)
gme_revenue = clean_revenue_data(gme_revenue)


print("\nGameStop Stock Data:")
print(gme_data.head())

print("\nGameStop Revenue Data:")
print(gme_revenue.head())

print("\nGameStop Revenue Data Types:")
print(gme_revenue.dtypes)


# ============================================================
# 6. BASIC DATA ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("BASIC ANALYSIS")
print("=" * 60)

print("\nTesla:")
print(f"Highest closing price: ${tesla_data['Close'].max():.2f}")
print(f"Lowest closing price: ${tesla_data['Close'].min():.2f}")
print(f"Latest closing price: ${tesla_data['Close'].iloc[-1]:.2f}")

print("\nGameStop:")
print(f"Highest closing price: ${gme_data['Close'].max():.2f}")
print(f"Lowest closing price: ${gme_data['Close'].min():.2f}")
print(f"Latest closing price: ${gme_data['Close'].iloc[-1]:.2f}")


# ============================================================
# 7. TESLA VISUALIZATION
# ============================================================

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(tesla_data["Date"], tesla_data["Close"])

axes[0].set_title("Tesla Historical Closing Price")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Price (USD)")
axes[0].grid(True)


axes[1].plot(tesla_revenue["Date"], tesla_revenue["Revenue"])

axes[1].set_title("Tesla Historical Revenue")
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Revenue (USD Million)")
axes[1].grid(True)

plt.tight_layout()
plt.show()


# ============================================================
# 8. GAMESTOP VISUALIZATION
# ============================================================

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(gme_data["Date"], gme_data["Close"])

axes[0].set_title("GameStop Historical Closing Price")
axes[0].set_xlabel("Date")
axes[0].set_ylabel("Price (USD)")
axes[0].grid(True)


axes[1].plot(gme_revenue["Date"], gme_revenue["Revenue"])

axes[1].set_title("GameStop Historical Revenue")
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Revenue (USD Million)")
axes[1].grid(True)

plt.tight_layout()
plt.show()


# ============================================================
# 9. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("PRACTICE COMPLETE")
print("=" * 60)

print("✓ Stock data extracted using yfinance")
print("✓ Revenue data extracted from HTML")
print("✓ Revenue data cleaned")
print("✓ Data types converted")
print("✓ Basic analysis completed")
print("✓ Tesla charts generated")
print("✓ GameStop charts generated")
