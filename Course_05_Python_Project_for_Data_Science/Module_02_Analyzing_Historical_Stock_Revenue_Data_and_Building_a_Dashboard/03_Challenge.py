"""
Course 05 - Module 02
Challenge: Stock & Revenue Comparison

Companies:
- Tesla (TSLA)
- GameStop (GME)

Workflow:
Extract → Clean → Analyze → Compare → Visualize
"""

import pandas as pd
import yfinance as yf
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from io import StringIO

# ============================================================
# CONFIGURATION
# ============================================================

TESLA_REVENUE_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
)

GAMESTOP_REVENUE_URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
)


# ============================================================
# REVENUE EXTRACTION
# ============================================================
def get_revenue_data(url, table_index=1):
    """
    Extract and clean revenue data from an HTML webpage.
    """

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    # Read HTML tables
    tables = pd.read_html(StringIO(response.text))

    print(f"Number of tables found: {len(tables)}")

    # Select the revenue table used by the IBM project
    revenue_data = tables[table_index].copy()

    # The source table does not provide useful column names.
    revenue_data.columns = ["Date", "Revenue"]

    # Clean revenue values
    revenue_data["Revenue"] = (
        revenue_data["Revenue"]
        .astype(str)
        .str.replace(r"[$,]", "", regex=True)
        .str.strip()
    )

    # Convert data types
    revenue_data["Date"] = pd.to_datetime(revenue_data["Date"], errors="coerce")

    revenue_data["Revenue"] = pd.to_numeric(revenue_data["Revenue"], errors="coerce")

    # Remove invalid rows
    revenue_data.dropna(subset=["Date", "Revenue"], inplace=True)

    revenue_data.reset_index(drop=True, inplace=True)

    return revenue_data


# ============================================================
# STOCK DATA EXTRACTION
# ============================================================


def get_stock_data(ticker_symbol):
    """
    Extract maximum available historical stock data.
    """

    stock = yf.Ticker(ticker_symbol)

    stock_data = stock.history(period="max")

    stock_data.reset_index(inplace=True)

    return stock_data


# ============================================================
# ANALYSIS
# ============================================================


def analyze_company(stock_data, revenue_data, company):
    """
    Calculate important stock and revenue statistics.
    """

    results = {
        "Company": company,
        "Highest Closing Price": stock_data["Close"].max(),
        "Lowest Closing Price": stock_data["Close"].min(),
        "Average Closing Price": stock_data["Close"].mean(),
        "Highest Revenue": revenue_data["Revenue"].max(),
        "Lowest Revenue": revenue_data["Revenue"].min(),
        "Average Revenue": revenue_data["Revenue"].mean(),
    }

    return results


# ============================================================
# VISUALIZATION
# ============================================================


def make_graph(stock_data, revenue_data, company):
    """
    Create stock price and revenue graphs.
    """

    stock_data = stock_data.copy()
    revenue_data = revenue_data.copy()

    # Ensure dates are datetime
    stock_data["Date"] = pd.to_datetime(stock_data["Date"])
    revenue_data["Date"] = pd.to_datetime(revenue_data["Date"])

    # Create figure
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    # Stock price
    axes[0].plot(stock_data["Date"], stock_data["Close"], label="Closing Price")

    axes[0].set_title(f"{company} - Historical Stock Price")

    axes[0].set_xlabel("Date")
    axes[0].set_ylabel("Price (USD)")
    axes[0].grid(True)

    # Revenue
    axes[1].plot(revenue_data["Date"], revenue_data["Revenue"], label="Revenue")

    axes[1].set_title(f"{company} - Historical Revenue")

    axes[1].set_xlabel("Date")
    axes[1].set_ylabel("Revenue (USD Millions)")
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()


# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 60)
print("STOCK & REVENUE COMPARISON CHALLENGE")
print("=" * 60)


# ------------------------------------------------------------
# TESLA
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TESLA ANALYSIS")
print("=" * 60)

tesla_data = get_stock_data("TSLA")
tesla_revenue = get_revenue_data(TESLA_REVENUE_URL)

print("\nTesla Stock Data:")
print(tesla_data.head())

print("\nTesla Revenue Data:")
print(tesla_revenue.head())


tesla_results = analyze_company(tesla_data, tesla_revenue, "Tesla")


# ------------------------------------------------------------
# GAMESTOP
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("GAMESTOP ANALYSIS")
print("=" * 60)

gme_data = get_stock_data("GME")
gme_revenue = get_revenue_data(GAMESTOP_REVENUE_URL)

print("\nGameStop Stock Data:")
print(gme_data.head())

print("\nGameStop Revenue Data:")
print(gme_revenue.head())


gme_results = analyze_company(gme_data, gme_revenue, "GameStop")


# ============================================================
# COMPARISON
# ============================================================

comparison = pd.DataFrame([tesla_results, gme_results])

print("\n" + "=" * 60)
print("COMPANY COMPARISON")
print("=" * 60)

print(
    comparison.to_string(
        index=False,
        formatters={
            "Highest Closing Price": "${:,.2f}".format,
            "Lowest Closing Price": "${:,.2f}".format,
            "Average Closing Price": "${:,.2f}".format,
            "Highest Revenue": "${:,.2f}M".format,
            "Lowest Revenue": "${:,.2f}M".format,
            "Average Revenue": "${:,.2f}M".format,
        },
    )
)


# ============================================================
# WINNER ANALYSIS
# ============================================================

print("\n" + "=" * 60)
print("FINAL COMPARISON")
print("=" * 60)


if tesla_results["Highest Closing Price"] > gme_results["Highest Closing Price"]:
    print("✓ Tesla reached the higher maximum closing price.")
else:
    print("✓ GameStop reached the higher maximum closing price.")


if tesla_results["Highest Revenue"] > gme_results["Highest Revenue"]:
    print("✓ Tesla recorded the higher maximum revenue.")
else:
    print("✓ GameStop recorded the higher maximum revenue.")


# ============================================================
# VISUALIZATION
# ============================================================

print("\nGenerating Tesla graph...")

make_graph(tesla_data, tesla_revenue, "Tesla")


print("\nGenerating GameStop graph...")

make_graph(gme_data, gme_revenue, "GameStop")


# ============================================================
# COMPLETION
# ============================================================

print("\n" + "=" * 60)
print("CHALLENGE COMPLETE")
print("=" * 60)

print("✓ Tesla stock data extracted")
print("✓ Tesla revenue extracted")
print("✓ GameStop stock data extracted")
print("✓ GameStop revenue extracted")
print("✓ Revenue data cleaned")
print("✓ Statistical analysis completed")
print("✓ Company comparison completed")
print("✓ Tesla visualization generated")
print("✓ GameStop visualization generated")
