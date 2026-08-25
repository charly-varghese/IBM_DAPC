"""
Lab 02 - Extracting Stock Data Using a Python Library

IBM Lab Implementation
"""

import yfinance as yf
import matplotlib.pyplot as plt

# ============================================================
# 1. Using yfinance to Extract Stock Information
# ============================================================

# Create a Ticker object for Apple
apple = yf.Ticker("AAPL")

print("Ticker Object:")
print(apple)

# Extract stock information
apple_info = apple.info

print("\nStock Information Type:")
print(type(apple_info))

# Extract Apple's country
print("\nApple Country:")
print(apple_info["country"])

# ============================================================
# 2. Using yfinance to Extract Historical Share Price Data
# ============================================================

# Extract maximum available historical share-price data
apple_share_price_data = apple.history(period="max")

print("\nHistorical Share Price Data Type:")
print(type(apple_share_price_data))

print("\nFirst Five Rows - Before Resetting Index:")
print(apple_share_price_data.head())

# Reset the DataFrame index
apple_share_price_data.reset_index(inplace=True)

print("\nFirst Five Rows - After Resetting Index:")
print(apple_share_price_data.head())

# ============================================================
# 3. Plot Apple's Historical Opening Share Price
# ============================================================
apple_share_price_data.plot(x="Date", y="Open")
plt.title("Apple Historical Opening Share Price")
plt.xlabel("Date")
plt.ylabel("Opening Price")
plt.show()

# ============================================================
# 4. Using yfinance to Extract Historical Dividend Data
# ============================================================

# Extract historical dividend data
apple_dividends = apple.dividends

print("\nHistorical Dividend Data Type:")
print(type(apple_dividends))

print("\nFirst Five Dividend Records:")
print(apple_dividends.head())

# Plot historical dividends
apple_dividends.plot()

plt.title("Apple Historical Dividends")
plt.xlabel("Date")
plt.ylabel("Dividend")

plt.show()

# ============================================================
# 5. IBM Exercise - AMD
# ============================================================

# Create a Ticker object for AMD
amd = yf.Ticker("AMD")

# Extract AMD stock information
amd_info = amd.info

# Question 1: Country
amd_country = amd_info["country"]
print("\nQuestion 1 - AMD Country:")
print(amd_country)

# Question 2: Sector
amd_sector = amd_info["sector"]
print("\nQuestion 2 - AMD Sector:")
print(amd_sector)

# Question 3: First-day trading volume
amd_share_price_data = amd.history(period="max")

first_day_volume = amd_share_price_data.iloc[0]["Volume"]

print("\nQuestion 3 - First Day Volume:")
print(first_day_volume)
