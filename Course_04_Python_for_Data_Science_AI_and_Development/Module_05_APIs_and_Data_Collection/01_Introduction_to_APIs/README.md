# Lab 01 - Introduction to APIs

## IBM Data Analyst Professional Certificate

**Course:** Python for Data Science, AI & Development

**Module:** APIs and Data Collection

**Lab:** Introduction to APIs

---

## Objective

Learn the fundamentals of APIs and understand how Python programs communicate with software components and REST APIs.

By completing this lab, I learned how to:

- Understand the concept of an API.
- Use Pandas as a Python API.
- Create and work with Pandas DataFrames.
- Understand REST API communication.
- Send HTTP requests using Python.
- Process JSON responses.
- Work with the NBA API.
- Download data from a remote URL.
- Load downloaded data into Pandas.
- Perform basic analysis on API-related datasets.

---

## IBM Hands-On Lab

This practical implementation is based on the IBM Hands-On Lab:

\*_Introduction to API_

The original IBM notebook introduces APIs through two main concepts:

1. Pandas as an API
2. REST APIs

The IBM lab also demonstrates retrieving NBA team information, identifying the Golden State Warriors, downloading a dataset, and analyzing game performance.

---

## Learning Approach

The original IBM notebook was reorganized into a professional VS Code structure instead of following the Jupyter Notebook cell by cell.

The workflow used in this practical implementation is:

```text
IBM Hands-On Lab
       |
       v
Concept Understanding
       |
       v
Professional Python Implementation
       |
       v
Independent Practice
       |
       v
Challenge Exercises
       |
       v
Debugging
       |
       v
GitHub Documentation
```

---

## Project Structure

```text
01_Introduction_to_APIs/
│
├── 01_IBM_Lab.py
├── 02_My_Practice.py
├── 03_Challenge.py
├── 04_Debug_Notes.md
├── README.md
│
├── Golden_State.pkl
├── users_data.csv
├── users_data.xlsx
├── challenge_users.csv
└── challenge_users.xlsx
```

> `Golden_State.pkl`, CSV files, and Excel files are generated or downloaded during practice. They are included only when required for the completed practical implementation.

---

## File Description

| File | Purpose |
| ---- | ------- |

| `01_IBM_Lab.py` | Professional implementation of the IBM Hands-On Lab |
| `02_My_Practice.py` | Additional REST API practice |
| `03_Challenge.py` | Independent API exercises |
| `04_Debug_Notes.md` | API troubleshooting and debugging reference |
| `README.md` | Lab documentation |

---

## Concepts Covered

### API Fundamentals

An API, or Application Programming Interface, allows different software components to communicate with each other.

A simple conceptual model is:

```text
Python Program
      |
      | Request
      v
     API
      |
      | Response
      v
Python Program
```

---

### Pandas as an API

The IBM lab demonstrates that Pandas provides an API through which Python programs can communicate with the Pandas library.

Example:

```python
import pandas as pd

data = {
    "Math": [11, 21, 31],
    "Science": [12, 22, 32]
}

df = pd.DataFrame(data)

print(df.head())
print(df.mean())
```

Methods such as `head()` and `mean()` provide an interface through which the Python program interacts with the Pandas library.

---

### REST APIs

REST APIs allow applications to communicate over the internet using HTTP requests.

A simplified workflow is:

```text
Python Application
       |
       | HTTP Request
       v
REST API Server
       |
       | HTTP Response
       v
JSON / Data
```

---

## HTTP Requests

The `requests` library is used to communicate with web APIs.

Example:

```python
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(
    url,
    timeout=30
)

response.raise_for_status()

data = response.json()

print(data)
```

---

## HTTP Status Codes

HTTP status codes provide information about the result of an API request.

| Status Code | Meaning               |
| ----------- | --------------------- |
| `200`       | Request successful    |
| `201`       | Resource created      |
| `204`       | No content            |
| `400`       | Bad request           |
| `401`       | Unauthorized          |
| `403`       | Forbidden             |
| `404`       | Resource not found    |
| `429`       | Too many requests     |
| `500`       | Internal server error |
| `503`       | Service unavailable   |

---

## JSON Data

Many REST APIs return data in JSON format.

Example:

```json
{
  "id": 1,
  "name": "Example User",
  "email": "user@example.com"
}
```

Python can convert the JSON response into Python objects using:

```python
data = response.json()
```

---

## NBA API Practice

The IBM Hands-On Lab uses the `nba_api` package.

The package can be installed with:

```bash
pip install nba_api
```

Example:

```python
from nba_api.stats.static import teams

nba_teams = teams.get_teams()

print(nba_teams[:3])
```

The lab then converts the returned team information into a Pandas DataFrame.

---

## Finding the Golden State Warriors

The NBA team dataset can be converted into a DataFrame:

```python
df_teams = pd.DataFrame(dict_nba_team)
```

The Warriors can then be identified using their nickname:

```python
df_warriors = df_teams[
    df_teams["nickname"] == "Warriors"
]
```

The team ID can be extracted with:

```python
id_warriors = df_warriors["id"].values[0]
```

---

## Downloading Data

The IBM lab provides a Golden State Warriors dataset in Pickle format.

The dataset is downloaded using the `requests` library.

A professional implementation uses:

```python
import requests

try:
    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    with open("Golden_State.pkl", "wb") as file:
        file.write(response.content)

    print("Download completed successfully.")

except requests.exceptions.RequestException as error:
    print(f"Download failed: {error}")
```

---

## Reading the Pickle Dataset

Pandas can read the downloaded dataset:

```python
import pandas as pd

games = pd.read_pickle("Golden_State.pkl")

print(games.head())
```

---

## Home and Away Analysis

The IBM dataset contains game matchup information.

Home games:

```python
games_home = games[
    games["MATCHUP"] == "GSW vs. TOR"
]
```

Away games:

```python
games_away = games[
    games["MATCHUP"] == "GSW @ TOR"
]
```

The `PLUS_MINUS` column can then be analyzed:

```python
home_average = games_home["PLUS_MINUS"].mean()

away_average = games_away["PLUS_MINUS"].mean()

print("Home Average:", home_average)
print("Away Average:", away_average)
```

---

## IBM Quiz

The original IBM lab asks learners to calculate the mean of the `PTS` column for the home and away game DataFrames.

The implementation is:

```python
print(games_home["PTS"].mean())
print(games_away["PTS"].mean())
```

This reinforces the use of Pandas aggregation methods on data obtained through an API or downloaded dataset.

---

## My Practice

`02_My_Practice.py` extends the IBM concepts using the JSONPlaceholder REST API.

The practice includes:

- Sending a GET request.
- Checking the HTTP response.
- Converting JSON into Python data.
- Creating a Pandas DataFrame.
- Selecting relevant columns.
- Inspecting the dataset.
- Generating summary information.
- Exporting API data to CSV.
- Exporting API data to Excel.

Example:

```python
response = requests.get(
    url,
    timeout=30
)

response.raise_for_status()

users = response.json()

df = pd.DataFrame(users)
```

---

## Challenge Exercises

`03_Challenge.py` reinforces the API concepts through independent exercises.

The challenges include:

- Checking HTTP status codes.
- Converting JSON responses.
- Extracting user names.
- Extracting email addresses.
- Creating DataFrames.
- Filtering records.
- Sorting records.
- Exporting API data.
- Working with nested JSON data.

---

## Professional Enhancements

The following improvements were added beyond the basic IBM notebook implementation:

- Professional Python file structure.
- Clear code sections.
- Exception handling.
- HTTP response validation.
- Request timeout handling.
- JSON processing.
- REST API practice using JSONPlaceholder.
- CSV export.
- Excel export.
- Independent challenge exercises.
- Debugging documentation.
- GitHub-oriented documentation.

---

## Packages Used

The main Python packages used in this lab are:

```text
requests
pandas
matplotlib
nba_api
openpyxl
```

Install the required packages with:

```bash
pip install requests pandas matplotlib nba_api openpyxl
```

---

## Environment Verification

The project uses the existing Python virtual environment:

```text
.venv
```

Verify the active environment:

```bash
python --version
```

Verify Requests:

```bash
pip show requests
```

Verify NBA API:

```bash
pip show nba_api
```

Verify Pandas:

```bash
pip show pandas
```

---

## Debugging

Common problems encountered during API development include:

- Missing Python packages.
- Incorrect API URLs.
- HTTP errors.
- Network connection failures.
- Request timeouts.
- Invalid JSON responses.
- Missing JSON keys.
- Missing DataFrame columns.
- File-not-found errors.
- API rate limits.

Detailed troubleshooting information is documented in:

```text
04_Debug_Notes.md
```

---

## Best Practices Demonstrated

### Use Timeouts

```python
requests.get(
    url,
    timeout=30
)
```

### Validate HTTP Responses

```python
response.raise_for_status()
```

### Handle Exceptions

```python
try:
    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

except requests.exceptions.RequestException as error:
    print(error)
```

### Inspect API Data

```python
print(response.status_code)
print(response.text)
```

### Validate DataFrames

```python
print(df.head())
print(df.shape)
print(df.columns)
```

---

## Business Applications

API data collection is widely used in real-world analytics workflows.

Examples include:

- Financial market data collection.
- Sales system integration.
- CRM data collection.
- ERP system integration.
- Weather data collection.
- E-commerce analytics.
- Business intelligence dashboards.
- Automated reporting.
- Data engineering pipelines.
- Machine learning data preparation.

---

## Interview Questions

### Beginner

1. What is an API?
2. What is a REST API?
3. What is JSON?
4. What does `requests.get()` do?
5. What does HTTP status code `200` mean?
6. What does `response.json()` do?
7. What is the purpose of Pandas?

### Intermediate

1. What is the difference between an API request and an API response?
2. Why should API requests use a timeout?
3. What does `raise_for_status()` do?
4. How do you handle API errors in Python?
5. How do you convert JSON data into a Pandas DataFrame?
6. What is the difference between HTTP 401 and HTTP 403?
7. How would you debug an API returning unexpected data?
8. How can API data be exported into CSV or Excel?

### Practical Question

**Question:** An API returns HTTP 200, but your Python program fails while processing the response. What would you check?

**Answer approach:**

1. Inspect the response content.
2. Verify that the response contains valid JSON.
3. Inspect the JSON structure.
4. Check whether the expected keys exist.
5. Validate the data types.
6. Create the DataFrame.
7. Check DataFrame columns and shape.

---

## Key Takeaways

After completing this lab, I can:

- Explain the purpose of an API.
- Understand the basic REST API workflow.
- Make HTTP GET requests using Python.
- Process JSON responses.
- Work with API-generated datasets.
- Use Pandas to organize API data.
- Download remote files using Python.
- Handle common API errors.
- Perform basic analysis on collected data.
- Export collected data to common file formats.

---

## Skills Demonstrated

```text
Python
   |
   +-- requests
   |
   +-- REST APIs
   |
   +-- HTTP Requests
   |
   +-- JSON
   |
   +-- Pandas
   |
   +-- Data Collection
   |
   +-- Data Processing
   |
   +-- Error Handling
   |
   +-- File Handling
   |
   +-- Data Export
```

---

## Lab Completion Checklist

- [x] Understand API fundamentals.
- [x] Understand Pandas as an API.
- [x] Understand REST APIs.
- [x] Install and use `requests`.
- [x] Make an HTTP GET request.
- [x] Check an HTTP response.
- [x] Process JSON data.
- [x] Work with `nba_api`.
- [x] Identify the Golden State Warriors.
- [x] Download the IBM dataset.
- [x] Load the Pickle dataset with Pandas.
- [x] Analyze home and away games.
- [x] Calculate mean values.
- [x] Create API practice programs.
- [x] Complete challenge exercises.
- [x] Create debugging documentation.

---

## Lab Outcome

This lab established the foundation for working with APIs and external data sources in Python.

The skills developed here will be used in the remaining Module 05 labs:

```text
Lab 01
Introduction to APIs
        |
        v
Lab 02
REST APIs and HTTP Requests
        |
        v
Lab 03
API Examples
        |
        v
Lab 04
Web Scraping
        |
        v
Lab 05
Different File Formats
        |
        v
Lab 06
GDP Data Extraction and Processing Project
```

---

## Next Lab

### Lab 02 - Access REST APIs and HTTP Requests

The next practical lab will focus more deeply on:

- HTTP requests.
- REST API endpoints.
- GET requests.
- API responses.
- JSON data.
- Query parameters.
- Request handling.
- Practical API data collection
