# ============================================================
# IBM DAPC - Course 04
# Module 05 - APIs and Data Collection
# Lab 04 - Web Scraping
# Challenge Program
# ============================================================

from pathlib import Path
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

URL = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

OUTPUT_DIR = Path(__file__).parent / "practice_output"
OUTPUT_FILE = OUTPUT_DIR / "challenge_books.csv"


# ------------------------------------------------------------
# Step 1 - Send HTTP Request
# ------------------------------------------------------------

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

try:
    response = requests.get(URL, headers=headers, timeout=15)

    response.raise_for_status()

except requests.exceptions.RequestException as error:
    print("ERROR: Unable to access the website.")
    print(f"Details: {error}")
    raise SystemExit(1)


# Explicit UTF-8 decoding
response.encoding = "utf-8"


print("=" * 60)
print("WEB SCRAPING CHALLENGE")
print("=" * 60)
print(f"HTTP Status Code: {response.status_code}")
print(f"Page Size: {len(response.text):,} characters")


# ------------------------------------------------------------
# Step 2 - Parse HTML with BeautifulSoup
# ------------------------------------------------------------

soup = BeautifulSoup(response.text, "html.parser")

page_title = soup.find("h1")

if page_title:
    print(f"Page Title: {page_title.get_text(strip=True)}")
else:
    print("Page Title: Not Found")


# ------------------------------------------------------------
# Step 3 - Find Product Records
# ------------------------------------------------------------

products = soup.select("article.product_pod")

print(f"Product Elements Found: {len(products)}")


if not products:
    print("ERROR: No product elements were found.")
    raise SystemExit(1)


# ------------------------------------------------------------
# Step 4 - Extract Book Information
# ------------------------------------------------------------

books = []

for product in products:

    # -------------------------
    # Extract title
    # -------------------------

    title_tag = product.select_one("h3 a")

    if title_tag:
        title = title_tag.get("title", "").strip()

        if not title:
            title = title_tag.get_text(strip=True)

    else:
        title = ""

    # -------------------------
    # Extract price
    # -------------------------

    price_tag = product.select_one("p.price_color")

    if price_tag:
        price_text = price_tag.get_text(strip=True)

    else:
        price_text = ""

    # -------------------------
    # Fallback price extraction
    # -------------------------

    if not price_text and title:

        price_match = re.search(r"£\s*\d+\.\d{2}", title)

        if price_match:
            price_text = price_match.group()

            title = title[: price_match.start()].strip()

    # -------------------------
    # Clean accidental price
    # from title
    # -------------------------

    price_match = re.search(r"£\s*\d+\.\d{2}", title)

    if price_match:

        if not price_text:
            price_text = price_match.group()

        title = title[: price_match.start()].strip()

    # -------------------------
    # Extract availability
    # -------------------------

    availability_tag = product.select_one("p.availability")

    if availability_tag:
        availability = availability_tag.get_text(" ", strip=True)
    else:
        availability = ""

    books.append({"Title": title, "Price": price_text, "Availability": availability})


# ------------------------------------------------------------
# Step 5 - Create DataFrame
# ------------------------------------------------------------

df = pd.DataFrame(books)

print(f"\nExtracted Records: {len(df)}")

if df.empty:
    print("ERROR: DataFrame is empty.")
    raise SystemExit(1)


print("\nRaw Extracted Data:")
print(df.to_string(index=False))


# ------------------------------------------------------------
# Step 6 - Clean Data
# ------------------------------------------------------------

df["Title"] = df["Title"].str.strip()

df["Price"] = df["Price"].str.replace("£", "", regex=False).str.strip()

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

df["Availability"] = df["Availability"].str.strip()


# ------------------------------------------------------------
# Step 7 - Data Validation
# ------------------------------------------------------------

missing_values = df.isnull().sum().sum()

duplicate_rows = df.duplicated().sum()


print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)

print(f"Missing Values: {missing_values}")
print(f"Duplicate Rows: {duplicate_rows}")


# ------------------------------------------------------------
# Step 8 - Validate Critical Columns
# ------------------------------------------------------------

invalid_titles = df["Title"].eq("").sum()

invalid_prices = df["Price"].isna().sum()

invalid_availability = df["Availability"].eq("").sum()

print(f"Invalid Titles: {invalid_titles}")
print(f"Invalid Prices: {invalid_prices}")
print(f"Invalid Availability: {invalid_availability}")


# ------------------------------------------------------------
# Step 9 - Basic Analysis
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("BASIC ANALYSIS")
print("=" * 60)

print(f"Total Books: {len(df)}")
print(f'Average Price: £{df["Price"].mean():.2f}')
print(f'Minimum Price: £{df["Price"].min():.2f}')
print(f'Maximum Price: £{df["Price"].max():.2f}')


print("\nAvailability Distribution:")

print(df["Availability"].value_counts())


# ------------------------------------------------------------
# Step 10 - Sort Books by Price
# ------------------------------------------------------------

df_sorted = df.sort_values(by="Price", ascending=False)


print("\n" + "=" * 60)
print("BOOKS SORTED BY PRICE")
print("=" * 60)

print(df_sorted.to_string(index=False))


# ------------------------------------------------------------
# Step 11 - Save Clean Dataset
# ------------------------------------------------------------

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")


# ------------------------------------------------------------
# Step 12 - Verify Output
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("OUTPUT VERIFICATION")
print("=" * 60)

print(f"Output File: {OUTPUT_FILE}")
print(f"File Exists: {OUTPUT_FILE.exists()}")

if OUTPUT_FILE.exists():

    print(f"File Size: " f"{OUTPUT_FILE.stat().st_size:,} bytes")


# ------------------------------------------------------------
# Final Validation
# ------------------------------------------------------------

if len(df) > 0 and missing_values == 0 and duplicate_rows == 0 and invalid_prices == 0:

    print("\nChallenge validation: PASSED")
    print("Challenge completed successfully.")

else:

    print("\nChallenge validation: REVIEW REQUIRED")
    print("Some data-quality issues remain.")


print("=" * 60)
