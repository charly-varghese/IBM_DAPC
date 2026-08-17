"""
IBM DAPC - Course 04
Module 05 - APIs and Data Collection

Lab 04 - Web Scraping

01_IBM_Lab.py

Purpose:
Practice HTML parsing and web scraping using
BeautifulSoup and Pandas.
"""

# =========================================================
# 1. Import Libraries
# =========================================================

import requests
import pandas as pd

from bs4 import BeautifulSoup
from io import StringIO

# =========================================================
# 2. Basic HTML Document
# =========================================================

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>

<h3>
    <b id='boldest'>Lebron James</b>
</h3>

<p>Salary: $ 92,000,000</p>

<h3>Stephen Curry</h3>

<p>Salary: $85,000,000</p>

<h3>Kevin Durant</h3>

<p>Salary: $73,200,000</p>

</body>
</html>
"""


# =========================================================
# 3. Create BeautifulSoup Object
# =========================================================

soup = BeautifulSoup(html, "html.parser")

print("=" * 60)
print("BASIC HTML PARSING")
print("=" * 60)


# =========================================================
# 4. Display HTML Title
# =========================================================

print("\nPage Title:")

print(soup.title)


# =========================================================
# 5. Extract Bold Text
# =========================================================

boldest = soup.find(id="boldest")

print("\nBoldest Text:")

print(boldest)


# =========================================================
# 6. Extract All H3 Tags
# =========================================================

print("\nAll H3 Tags:")

for heading in soup.find_all("h3"):

    print(heading)


# =========================================================
# 7. Extract All Paragraphs
# =========================================================

print("\nAll Paragraphs:")

for paragraph in soup.find_all("p"):

    print(paragraph)


# =========================================================
# 8. Extract Text from Paragraphs
# =========================================================

print("\nParagraph Text:")

for paragraph in soup.find_all("p"):

    print(paragraph.get_text())


# =========================================================
# 9. HTML Table Example
# =========================================================

table = """
<table>
<tr>
    <td id='flight'>Flight No</td>
    <td>Launch site</td>
    <td>Payload mass</td>
</tr>

<tr>
    <td>1</td>
    <td>
        <a href='https://en.wikipedia.org/wiki/Florida'>
            Florida
        </a>
    </td>
    <td>300 kg</td>
</tr>

<tr>
    <td>2</td>
    <td>
        <a href='https://en.wikipedia.org/wiki/Texas'>
            Texas
        </a>
    </td>
    <td>94 kg</td>
</tr>

<tr>
    <td>3</td>
    <td>
        <a href='https://en.wikipedia.org/wiki/Florida'>
            Florida
        </a>
    </td>
    <td>80 kg</td>
</tr>

</table>
"""


# =========================================================
# 10. Parse Table
# =========================================================

table_soup = BeautifulSoup(table, "html.parser")

print("\n" + "=" * 60)
print("HTML TABLE")
print("=" * 60)


# =========================================================
# 11. Find Table
# =========================================================

table_tag = table_soup.find("table")

print("\nTable:")

print(table_tag)


# =========================================================
# 12. Find All Table Rows
# =========================================================

rows = table_soup.find_all("tr")

print("\nNumber of Rows:")

print(len(rows))


# =========================================================
# 13. Extract Table Cells
# =========================================================

print("\nTable Data:")

for row in rows:

    cells = row.find_all("td")

    row_data = []

    for cell in cells:

        row_data.append(cell.get_text(strip=True))

    print(row_data)


# =========================================================
# 14. Extract Links
# =========================================================

print("\nLinks:")

links = table_soup.find_all("a")

for link in links:

    print(link.get_text(strip=True), "->", link.get("href"))


# =========================================================
# 15. Multiple HTML Tables
# =========================================================

two_tables = """
<h3>Rocket Launch</h3>

<table class='rocket'>

<tr>
    <td>Flight No</td>
    <td>Launch site</td>
    <td>Payload mass</td>
</tr>

<tr>
    <td>1</td>
    <td>Florida</td>
    <td>300 kg</td>
</tr>

<tr>
    <td>2</td>
    <td>Texas</td>
    <td>94 kg</td>
</tr>

<tr>
    <td>3</td>
    <td>Florida</td>
    <td>80 kg</td>
</tr>

</table>


<h3>Pizza Party</h3>

<table class='pizza'>

<tr>
    <td>Pizza Place</td>
    <td>Orders</td>
    <td>Slices</td>
</tr>

<tr>
    <td>Domino's Pizza</td>
    <td>10</td>
    <td>100</td>
</tr>

<tr>
    <td>Little Caesars</td>
    <td>12</td>
    <td>144</td>
</tr>

<tr>
    <td>Papa John's</td>
    <td>15</td>
    <td>165</td>
</tr>

</table>
"""


# =========================================================
# 16. Parse Multiple Tables
# =========================================================

multi_soup = BeautifulSoup(two_tables, "html.parser")

print("\n" + "=" * 60)
print("MULTIPLE HTML TABLES")
print("=" * 60)


tables = multi_soup.find_all("table")

print("\nNumber of Tables:")

print(len(tables))


# =========================================================
# 17. Display Table Classes
# =========================================================

print("\nTable Classes:")

for table in tables:

    print(table.get("class"))


# =========================================================
# 18. Pandas read_html()
# =========================================================

print("\n" + "=" * 60)
print("PANDAS read_html()")
print("=" * 60)

dataframes = pd.read_html(StringIO(two_tables))

print("\nNumber of DataFrames:")

print(len(dataframes))


# =========================================================
# 19. Display First Table
# =========================================================

print("\nRocket Launch DataFrame:")

print(dataframes[0])


# =========================================================
# 20. Display Second Table
# =========================================================

print("\nPizza Party DataFrame:")

print(dataframes[1])


# =========================================================
# 21. Remote HTML Table
# =========================================================

url = (
    "https://cf-courses-data.s3.us.cloud-object-storage."
    "appdomain.cloud/IBM-DA0321EN-SkillsNetwork/"
    "labs/datasets/HTMLColorCodes.html"
)


print("\n" + "=" * 60)
print("REMOTE HTML TABLE")
print("=" * 60)

try:

    response = requests.get(url, timeout=15)

    print("\nHTTP Status Code:")

    print(response.status_code)

    response.raise_for_status()

    color_tables = pd.read_html(StringIO(response.text))

    print("\nNumber of Tables Found:")

    print(len(color_tables))

    if color_tables:

        print("\nFirst Table:")

        print(color_tables[0].head())

except requests.exceptions.RequestException as error:

    print("\nRequest failed:")

    print(error)


# =========================================================
# 22. Final Summary
# =========================================================

print("\n" + "=" * 60)
print("IBM WEB SCRAPING LAB COMPLETED")
print("=" * 60)
