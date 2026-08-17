"""
IBM DAPC - Course 04
Module 05 - APIs and Data Collection

Lab 04 - Web Scraping

02_My_Practice.py

Purpose:
Build a professional web-scraping workflow using:

- Requests
- User-Agent
- BeautifulSoup
- find()
- find_all()
- HTML table extraction
- Pandas read_html()
- Data validation
- CSV export
- pathlib
- Error handling
"""

# =========================================================
# 1. IMPORT LIBRARIES
# =========================================================

from io import StringIO
from pathlib import Path

import pandas as pd
import requests

from bs4 import BeautifulSoup

# =========================================================
# 2. CONFIGURATION
# =========================================================

URL = (
    "https://cf-courses-data.s3.us.cloud-object-storage."
    "appdomain.cloud/IBM-DA0321EN-SkillsNetwork/"
    "labs/datasets/HTMLColorCodes.html"
)

OUTPUT_DIR = Path("practice_output")

OUTPUT_FILE = OUTPUT_DIR / "color_codes.csv"

TIMEOUT = 15

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/151.0 Safari/537.36"
    )
}


# =========================================================
# 3. PROJECT HEADER
# =========================================================

print("=" * 60)
print("WEB SCRAPING - PROFESSIONAL PRACTICE")
print("=" * 60)


# =========================================================
# 4. SEND HTTP REQUEST
# =========================================================

print("\nRequesting Web Page...")

try:

    response = requests.get(URL, headers=HEADERS, timeout=TIMEOUT)

    print("\nHTTP Status Code:")
    print(response.status_code)

    response.raise_for_status()

    print("\nRequest successful.")

except requests.exceptions.Timeout:

    print("\nRequest timed out.")
    raise SystemExit

except requests.exceptions.RequestException as error:

    print("\nRequest failed:")
    print(error)
    raise SystemExit


# =========================================================
# 5. RESPONSE INFORMATION
# =========================================================

print("\n" + "=" * 60)
print("RESPONSE INFORMATION")
print("=" * 60)

print("\nContent Type:")
print(response.headers.get("Content-Type"))

print("\nEncoding:")
print(response.encoding)

print("\nResponse Size:")
print(len(response.text), "characters")


# =========================================================
# 6. CREATE BEAUTIFULSOUP OBJECT
# =========================================================

soup = BeautifulSoup(response.text, "html.parser")

print("\n" + "=" * 60)
print("BEAUTIFULSOUP ANALYSIS")
print("=" * 60)


# =========================================================
# 7. FIND PAGE TITLE
# =========================================================

title = soup.find("title")

print("\nPage Title:")

if title:

    print(title.get_text(strip=True))

else:

    print("No title found.")


# =========================================================
# 8. FIND ALL HTML TABLES
# =========================================================

tables = soup.find_all("table")

print("\nNumber of HTML Tables:")
print(len(tables))


# =========================================================
# 9. CHECK TABLE AVAILABILITY
# =========================================================

if not tables:

    print("\nNo HTML table found.")
    raise SystemExit


# =========================================================
# 10. INSPECT FIRST TABLE
# =========================================================

first_table = tables[0]

rows = first_table.find_all("tr")

print("\nRows in First Table:")
print(len(rows))


# =========================================================
# 11. EXTRACT TABLE HEADER
# =========================================================

print("\nTable Header:")

header_row = rows[0]

header_cells = header_row.find_all(["th", "td"])

headers_found = []

for cell in header_cells:

    headers_found.append(cell.get_text(" ", strip=True))

print(headers_found)


# =========================================================
# 12. EXTRACT FIRST FIVE DATA ROWS
# =========================================================

print("\nFirst Five Data Rows:")

for row in rows[1:6]:

    cells = row.find_all(["th", "td"])

    row_data = []

    for cell in cells:

        row_data.append(cell.get_text(" ", strip=True))

    print(row_data)


# =========================================================
# 13. EXTRACT TABLE USING PANDAS
# =========================================================

print("\n" + "=" * 60)
print("PANDAS TABLE EXTRACTION")
print("=" * 60)

try:

    dataframes = pd.read_html(StringIO(response.text), header=0)

except ValueError as error:

    print("\nNo HTML tables could be extracted.")

    print(error)

    raise SystemExit


print("\nTables Extracted:")
print(len(dataframes))


# =========================================================
# 14. SELECT FIRST DATAFRAME
# =========================================================

df = dataframes[0].copy()


# =========================================================
# 15. CLEAN COLUMN NAMES
# =========================================================

df.columns = [str(column).strip() for column in df.columns]


# =========================================================
# 16. REMOVE COMPLETELY EMPTY COLUMNS
# =========================================================

df = df.dropna(axis=1, how="all")


# =========================================================
# 17. DISPLAY CLEAN DATAFRAME
# =========================================================

print("\nCleaned DataFrame:")

print(df.head())


# =========================================================
# 18. DATASET SHAPE
# =========================================================

print("\nDataset Shape:")

print(df.shape)


# =========================================================
# 19. COLUMN NAMES
# =========================================================

print("\nColumn Names:")

print(df.columns.tolist())


# =========================================================
# 20. DATA VALIDATION
# =========================================================

print("\n" + "=" * 60)
print("DATA VALIDATION")
print("=" * 60)


# ---------------------------------------------------------
# Missing Values
# ---------------------------------------------------------

print("\nMissing Values:")

print(df.isnull().sum())


# ---------------------------------------------------------
# Duplicate Rows
# ---------------------------------------------------------

print("\nDuplicate Rows:")

print(df.duplicated().sum())


# =========================================================
# 21. DATA TYPES
# =========================================================

print("\nData Types:")

print(df.dtypes)


# =========================================================
# 22. DATA SAMPLE
# =========================================================

print("\n" + "=" * 60)
print("DATA SAMPLE")
print("=" * 60)

print("\nFirst Five Records:")

print(df.head())


# =========================================================
# 23. BASIC ANALYSIS
# =========================================================

print("\n" + "=" * 60)
print("BASIC ANALYSIS")
print("=" * 60)

print("\nNumber of Records:")

print(len(df))


# ---------------------------------------------------------
# Color Names
# ---------------------------------------------------------

if "Color Name" in df.columns:

    print("\nFirst Ten Color Names:")

    print(df["Color Name"].head(10).tolist())


# ---------------------------------------------------------
# Hex Codes
# ---------------------------------------------------------

if "Hex Code #RRGGBB" in df.columns:

    print("\nFirst Ten Hex Codes:")

    print(df["Hex Code #RRGGBB"].head(10).tolist())


# =========================================================
# 24. CREATE OUTPUT DIRECTORY
# =========================================================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# =========================================================
# 25. EXPORT DATA TO CSV
# =========================================================

print("\n" + "=" * 60)
print("CSV EXPORT")
print("=" * 60)

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print("\nData saved successfully.")

print("Output File:")
print(OUTPUT_FILE)


# =========================================================
# 26. VERIFY OUTPUT FILE
# =========================================================

output_path = OUTPUT_FILE.resolve()

print("\nOutput Path:")
print(output_path)

print("\nFile Exists:")
print(output_path.exists())


if output_path.exists():

    print("\nFile Size:")
    print(output_path.stat().st_size, "bytes")


# =========================================================
# 27. PROFESSIONAL SCRAPING CHECK
# =========================================================

print("\n" + "=" * 60)
print("SCRAPING PRACTICE CHECK")
print("=" * 60)

print("\nUser-Agent:")
print("Configured")

print("\nTimeout:")
print("Configured")

print("\nHTTP Status Validation:")
print("Enabled")

print("\nData Validation:")
print("Enabled")

print("\nCSV Export:")
print("Enabled")

print("\nEthical Scraping Reminder:")

print(
    "Always check robots.txt, terms of service, "
    "rate limits, and website policies before scraping."
)


# =========================================================
# 28. FINAL SUMMARY
# =========================================================

print("\n" + "=" * 60)
print("WEB SCRAPING PRACTICE COMPLETED")
print("=" * 60)

print("\nRecords Processed:")
print(len(df))

print("\nColumns:")
print(df.columns.tolist())

print("\nOutput:")
print(output_path)
