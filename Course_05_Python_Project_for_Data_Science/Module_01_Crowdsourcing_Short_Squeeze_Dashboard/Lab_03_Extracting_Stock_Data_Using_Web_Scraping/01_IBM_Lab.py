"""
Lab 03 - Extracting Stock Data Using Web Scraping

IBM Data Analyst Professional Certificate
Course 05 - Python Project for Data Science
Module 01 - Crowdsourcing Short Squeeze Dashboard

Purpose:
    Extract historical stock data from HTML web pages using
    Requests, BeautifulSoup, and Pandas.
"""

import warnings

import pandas as pd
import requests
from bs4 import BeautifulSoup

# -------------------------------------------------------------------
# 1. Setup
# -------------------------------------------------------------------

warnings.filterwarnings("ignore", category=FutureWarning)


# -------------------------------------------------------------------
# 2. Example: Extract Netflix stock data using BeautifulSoup
# -------------------------------------------------------------------

netflix_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/"
    "netflix_data_webpage.html"
)

response = requests.get(netflix_url, timeout=30)
response.raise_for_status()

html_data = response.text

print("HTTP Status Code:", response.status_code)
print("HTML content downloaded:", len(html_data), "characters")


# Parse the HTML content.
soup = BeautifulSoup(html_data, "html.parser")


# Check the page title.
print("\nPage Title:")
print(soup.title.string)


# Create an empty DataFrame.
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])


# Locate the table body.
table_body = soup.find("tbody")


# Extract each table row.
for row in table_body.find_all("tr"):
    columns = row.find_all("td")

    if len(columns) == 7:
        date = columns[0].text.strip()
        open_price = columns[1].text.strip()
        high_price = columns[2].text.strip()
        low_price = columns[3].text.strip()
        close_price = columns[4].text.strip()
        volume = columns[6].text.strip()

        netflix_data.loc[len(netflix_data)] = [
            date,
            open_price,
            high_price,
            low_price,
            close_price,
            volume,
        ]


print("\nNetflix Stock Data:")
print(netflix_data.head())


# -------------------------------------------------------------------
# 3. Extract the same table using Pandas read_html()
# -------------------------------------------------------------------

read_html_data = pd.read_html(netflix_url)

netflix_dataframe = read_html_data[0]

print("\nData extracted using pandas.read_html():")
print(netflix_dataframe.head())


# -------------------------------------------------------------------
# 4. Exercise: Extract Amazon stock data using BeautifulSoup
# -------------------------------------------------------------------

amazon_url = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/"
    "amazon_data_webpage.html"
)

response = requests.get(amazon_url, timeout=30)
response.raise_for_status()

html_data = response.text


# Parse Amazon HTML.
beautiful_soup = BeautifulSoup(html_data, "html.parser")


# Question 1:
# What is the content of the title tag?
print("\nAmazon Page Title:")
print(beautiful_soup.title.string)


# Create the Amazon DataFrame.
amazon_data = pd.DataFrame(
    columns=[
        "Date",
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume",
    ]
)


# Locate the table body.
table_body = beautiful_soup.find("tbody")


# Extract the historical stock data.
for row in table_body.find_all("tr"):
    columns = row.find_all("td")

    if len(columns) == 7:
        date = columns[0].text.strip()
        open_price = columns[1].text.strip()
        high_price = columns[2].text.strip()
        low_price = columns[3].text.strip()
        close_price = columns[4].text.strip()
        adj_close = columns[5].text.strip()
        volume = columns[6].text.strip()

        amazon_data.loc[len(amazon_data)] = [
            date,
            open_price,
            high_price,
            low_price,
            close_price,
            adj_close,
            volume,
        ]


# Question 2:
# What are the names of the columns?
print("\nAmazon DataFrame Columns:")
print(amazon_data.columns.tolist())


# Print the first five rows.
print("\nAmazon Stock Data:")
print(amazon_data.head())


# Question 3:
# What is the Open price of the last row?
print("\nOpen Price of the Last Row:")
print(amazon_data.iloc[-1]["Open"])
