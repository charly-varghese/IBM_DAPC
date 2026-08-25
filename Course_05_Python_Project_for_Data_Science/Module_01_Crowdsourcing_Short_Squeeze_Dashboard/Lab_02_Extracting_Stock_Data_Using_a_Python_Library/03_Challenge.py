"""
Lab 02 - Challenge
Multi-Stock Market Analysis using yfinance
"""

import yfinance as yf
import pandas as pd

# Stocks for analysis
tickers = ["AAPL", "MSFT", "NVDA", "AMD"]

stock_results = []


# Extract and analyze each stock
for ticker in tickers:
    stock = yf.Ticker(ticker)
    stock_info = stock.info

    stock_history = stock.history(period="1y")

    average_close = stock_history["Close"].mean()
    total_volume = stock_history["Volume"].sum()

    highest_volume_index = stock_history["Volume"].idxmax()
    highest_volume = stock_history.loc[highest_volume_index, "Volume"]

    stock_results.append(
        {
            "Ticker": ticker,
            "Company": stock_info["longName"],
            "Country": stock_info["country"],
            "Sector": stock_info["sector"],
            "Trading Days": len(stock_history),
            "Average Close": round(average_close, 2),
            "Total Volume": total_volume,
            "Highest Volume": highest_volume,
            "Highest Volume Date": highest_volume_index,
        }
    )


# Create summary DataFrame
challenge_summary = pd.DataFrame(stock_results)


print("\nChallenge Stock Summary:")
print(challenge_summary)


# Highest average closing price
highest_average_index = challenge_summary["Average Close"].idxmax()

highest_average_stock = challenge_summary.loc[highest_average_index, "Ticker"]

highest_average_price = challenge_summary.loc[highest_average_index, "Average Close"]


# Highest total trading volume
highest_total_volume_index = challenge_summary["Total Volume"].idxmax()

highest_total_volume_stock = challenge_summary.loc[highest_total_volume_index, "Ticker"]

highest_total_volume = challenge_summary.loc[highest_total_volume_index, "Total Volume"]


# Highest single-day trading volume
highest_single_day_index = challenge_summary["Highest Volume"].idxmax()

highest_single_day_stock = challenge_summary.loc[highest_single_day_index, "Ticker"]

highest_single_day_volume = challenge_summary.loc[
    highest_single_day_index, "Highest Volume"
]

highest_single_day_date = challenge_summary.loc[
    highest_single_day_index, "Highest Volume Date"
]


# Display challenge results
print("\nChallenge Results:")

print("\n1. Highest Average Closing Price:")
print("Ticker:", highest_average_stock)
print("Average Close:", highest_average_price)

print("\n2. Highest Total Trading Volume:")
print("Ticker:", highest_total_volume_stock)
print("Total Volume:", f"{highest_total_volume:,.0f}")

print("\n3. Highest Single-Day Trading Volume:")
print("Ticker:", highest_single_day_stock)
print("Volume:", f"{highest_single_day_volume:,.0f}")
print("Date:", highest_single_day_date)
