from bs4 import BeautifulSoup
import pandas as pd

# ============================================================
# MY PRACTICE – STOCK MARKET HTML SCRAPING
# ============================================================

stock_html = """
<table>
    <tr>
        <th>Ticker</th>
        <th>Company</th>
        <th>Price</th>
        <th>Volume</th>
    </tr>
    <tr>
        <td>AAPL</td>
        <td>Apple</td>
        <td>220</td>
        <td>5000000</td>
    </tr>
    <tr>
        <td>MSFT</td>
        <td>Microsoft</td>
        <td>510</td>
        <td>3200000</td>
    </tr>
    <tr>
        <td>TSLA</td>
        <td>Tesla</td>
        <td>340</td>
        <td>7100000</td>
    </tr>
</table>
"""

# Parse HTML
soup = BeautifulSoup(stock_html, "html.parser")

# Find table
table = soup.find("table")

# Find all rows
rows = table.find_all("tr")

# Store extracted records
stock_data = []

for row in rows[1:]:
    cells = row.find_all("td")

    stock_data.append(
        {
            "Ticker": cells[0].get_text(strip=True),
            "Company": cells[1].get_text(strip=True),
            "Price": cells[2].get_text(strip=True),
            "Volume": cells[3].get_text(strip=True),
        }
    )

# Convert to DataFrame
stock_df = pd.DataFrame(stock_data)

print("\nStock Market Data:")
print(stock_df)

# ============================================================
# DATA CLEANING
# ============================================================

stock_df["Price"] = pd.to_numeric(stock_df["Price"])
stock_df["Volume"] = pd.to_numeric(stock_df["Volume"])

print("\nData Types:")
print(stock_df.dtypes)


# ============================================================
# SIMPLE MARKET ANALYSIS
# ============================================================

# Stock with the highest trading volume
highest_volume_stock = stock_df.loc[
    stock_df["Volume"].idxmax()
]

print("\nHighest Volume Stock:")
print(highest_volume_stock)

# Stock with the highest price
highest_price_stock = stock_df.loc[
    stock_df["Price"].idxmax()
]

print("\nHighest Price Stock:")
print(highest_price_stock)

