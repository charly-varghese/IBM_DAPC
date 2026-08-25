from bs4 import BeautifulSoup
from io import StringIO

html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

soup = BeautifulSoup(html, "html.parser")

print(soup)
print(soup.title)
print(soup.h3)
print(soup.h3.name)
print(soup.h3.parent.name)
print(soup.h3.b["id"])
print(soup.h3.b.attrs)
print(soup.h3.b.string)
print(soup.find_all("h3"))
print(soup.find_all(["h3", "p"]))
for tag in soup.find_all(["h3", "p"]):
    print(tag.get_text(strip=True))
print(soup.find_all(id="boldest"))
print(soup.find_all(string=" Stephen Curry"))
print(soup.find("h3"))
print(soup.find("b", id="boldest"))
for child in soup.h3.children:
    print(repr(child))
print(soup.h3.next_sibling)
print(soup.h3.next_sibling.next_sibling)

# ============================================================
# REAL WEB SCRAPING — REQUESTS
# ============================================================

import requests

url = "https://example.com"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)
print("Content Type:", response.headers.get("Content-Type"))

html_content = response.text

print("HTML Length:", len(html_content))

from bs4 import BeautifulSoup

web_soup = BeautifulSoup(html_content, "html.parser")

print("Page Title:", web_soup.title.get_text(strip=True))

# Extract links
links = web_soup.find_all("a")

print("Number of links:", len(links))

for link in links:
    print("Link text:", link.get_text(strip=True))
    print("URL:", link.get("href"))
# Extract images from a controlled HTML example
image_html = """
<html>
    <body>
        <img src="stock_chart.png" alt="Stock Chart">
        <img src="volume_chart.png" alt="Trading Volume">
    </body>
</html>
"""

image_soup = BeautifulSoup(image_html, "html.parser")

images = image_soup.find_all("img")

print("Number of images:", len(images))

for image in images:
    print("Image source:", image.get("src"))
    print("Alt text:", image.get("alt"))


# ============================================================
# SECTION: SCRAPE HTML TABLE USING BEAUTIFULSOUP
# ============================================================

import pandas as pd

population_url = "https://en.wikipedia.org/wiki/World_population"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
}

population_response = requests.get(population_url, headers=headers, timeout=20)

print("Population Page Status Code:", population_response.status_code)

population_soup = BeautifulSoup(population_response.text, "html.parser")

# Find all HTML tables
tables = population_soup.find_all("table")

print("Number of tables:", len(tables))

# Find the table containing
# "10 most densely populated countries"

table_index = None

for index, table in enumerate(tables):
    if "10 most densely populated countries" in str(table):
        table_index = index
        break

print("Selected table index:", table_index)

if table_index is not None:
    print(tables[table_index].prettify())
else:
    print("Target table was not found.")


# ============================================================
# HTML TABLE → PANDAS DATAFRAME
# ============================================================

html_table = """
<table>
<tr>
    <th>Rank</th>
    <th>Country</th>
    <th>Population</th>
    <th>Area</th>
    <th>Density</th>
</tr>
<tr>
    <td>1</td>
    <td>Country A</td>
    <td>1000000</td>
    <td>1000</td>
    <td>1000</td>
</tr>
<tr>
    <td>2</td>
    <td>Country B</td>
    <td>800000</td>
    <td>1200</td>
    <td>667</td>
</tr>
</table>
"""

table_soup = BeautifulSoup(html_table, "html.parser")

table = table_soup.find("table")

rows = table.find_all("tr")

population_data = []

for row in rows[1:]:
    cells = row.find_all("td")

    population_data.append({
        "Rank": cells[0].text.strip(),
        "Country": cells[1].text.strip(),
        "Population": cells[2].text.strip(),
        "Area": cells[3].text.strip(),
        "Density": cells[4].text.strip()
    })

population_df = pd.DataFrame(population_data)

print("\nPopulation DataFrame:")
print(population_df)
