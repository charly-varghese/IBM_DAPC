from bs4 import BeautifulSoup
import pandas as pd

# ============================================================
# CHALLENGE – STOCK DATA ANALYSIS
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

# Find the table
table = soup.find("table")

# Find rows
rows = table.find_all("tr")

print("Number of rows:", len(rows))
# Skip the header row
data_rows = rows[1:]

print("\nData rows:", len(data_rows))

# Extract cells from each data row

for row in data_rows:
    cells = row.find_all("td")
    ticker = cells[0].get_text(strip=True)
    company = cells[1].get_text(strip=True)
    price = cells[2].get_text(strip=True)
    volume = cells[3].get_text(strip=True)
    stock_data = []

for row in data_rows:
    cells = row.find_all("td")

    ticker = cells[0].get_text(strip=True)
    company = cells[1].get_text(strip=True)
    price = cells[2].get_text(strip=True)
    volume = cells[3].get_text(strip=True)

    stock_data.append(
        {"Ticker": ticker, "Company": company, "Price": price, "Volume": volume}
    )

print("\nExtracted Records:")
print(stock_data)

# ============================================================
# CONVERT TO PANDAS DATAFRAME
# ============================================================

stock_df = pd.DataFrame(stock_data)

print("\nStock DataFrame:")
print(stock_df)

# ============================================================
# MARKET ANALYSIS
# ============================================================

average_price = stock_df["Price"].astype(int).mean()

total_volume = stock_df["Volume"].astype(int).sum()

highest_volume_stock = stock_df.loc[stock_df["Volume"].astype(int).idxmax()]

highest_price_stock = stock_df.loc[stock_df["Price"].astype(int).idxmax()]

print("\nAverage Price:", round(average_price, 2))

print("Total Trading Volume:", total_volume)

print("\nHighest Volume Stock:")
print(highest_volume_stock["Ticker"])

print("\nHighest Price Stock:")
print(highest_price_stock["Ticker"])
