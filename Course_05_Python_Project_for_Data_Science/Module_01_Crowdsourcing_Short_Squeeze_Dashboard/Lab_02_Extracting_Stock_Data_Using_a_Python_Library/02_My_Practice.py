"""
Lab 02 - My Practice
Stock Data Explorer using yfinance
"""

import yfinance as yf
import pandas as pd

# Create a Ticker object for Apple
apple = yf.Ticker("AAPL")

print("Ticker Object:")
print(apple)
# Extract selected stock information
apple_info = apple.info

print("\nApple Stock Information:")
print("Company:", apple_info["longName"])
print("Country:", apple_info["country"])
print("Sector:", apple_info["sector"])

# Extract historical price data
apple_history = apple.history(period="1y")

print("\nHistorical Data Type:")
print(type(apple_history))

print("\nLast Five Trading Days:")
print(apple_history.tail())

# Calculate the average closing price
average_close = apple_history["Close"].mean()

print("\nAverage Closing Price - Last 1 Year:")
print(round(average_close, 2))

# Calculate total trading volume
total_volume = apple_history["Volume"].sum()

print("\nTotal Trading Volume - Last 1 Year:")
print(f"{total_volume:,.0f}")

# Find the highest-volume trading day
highest_volume_index = apple_history["Volume"].idxmax()
highest_volume = apple_history.loc[highest_volume_index, "Volume"]

print("\nHighest Trading Volume Day:")
print("Date:", highest_volume_index)
print("Volume:", f"{highest_volume:,.0f}")

# Create a summary DataFrame
stock_summary = pd.DataFrame(
    {
        "Company": [apple_info["longName"]],
        "Ticker": ["AAPL"],
        "Country": [apple_info["country"]],
        "Sector": [apple_info["sector"]],
        "Average Close (1Y)": [round(average_close, 2)],
        "Total Volume (1Y)": [total_volume],
        "Highest Volume": [highest_volume],
        "Highest Volume Date": [highest_volume_index],
    }
)

print("\nStock Summary:")
print(stock_summary)


# Stock symbols for multi-stock analysis
tickers = ["AAPL", "MSFT", "NVDA"]

print("\nStocks to Analyze:")
print(tickers)

# Extract company information and historical data
stock_results = []

for ticker in tickers:
    stock = yf.Ticker(ticker)
    stock_info = stock.info

    print("\nTicker:", ticker)
    print("Company:", stock_info["longName"])
    print("Country:", stock_info["country"])
    print("Sector:", stock_info["sector"])

    # Extract one year of historical data
    stock_history = stock.history(period="1y")

    print("Historical Data Type:", type(stock_history))
    print("Number of Trading Days:", len(stock_history))

    # Calculate stock metrics
    average_close = stock_history["Close"].mean()
    total_volume = stock_history["Volume"].sum()
    # Find the highest-volume trading day
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

    print("Average Closing Price:", round(average_close, 2))
    print("Total Trading Volume:", f"{total_volume:,.0f}")


# Create a DataFrame from the collected results
multi_stock_summary = pd.DataFrame(stock_results)

print("\nMulti-Stock Summary:")
print(multi_stock_summary)

# Find the stock with the highest total trading volume
highest_volume_stock_index = multi_stock_summary["Total Volume"].idxmax()

highest_volume_stock = multi_stock_summary.loc[highest_volume_stock_index, "Ticker"]

highest_total_volume = multi_stock_summary.loc[
    highest_volume_stock_index, "Total Volume"
]

print("\nHighest Total Volume Stock:")
print("Ticker:", highest_volume_stock)
print("Total Volume:", f"{highest_total_volume:,.0f}")
