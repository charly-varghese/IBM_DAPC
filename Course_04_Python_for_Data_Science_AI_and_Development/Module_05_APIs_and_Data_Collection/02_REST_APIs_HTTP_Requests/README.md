# REST APIs & HTTP Requests

## IBM DAPC – Course 04

### Python for Data Science, AI & Development

---

## 1. Module Information

**Course:** Course 04 – Python for Data Science, AI & Development  
**Module:** Module 05 – APIs and Data Collection  
**Lab:** REST APIs & HTTP Requests  
**Folder:** `02_REST_APIs_HTTP_Requests`

---

## 2. Learning Objective

This lab focuses on using Python to communicate with web services through HTTP requests and REST APIs.

The practical work covers:

- HTTP requests
- REST API concepts
- GET requests
- POST requests
- Query parameters
- Request headers
- Response headers
- HTTP status codes
- JSON responses
- Error handling
- Timeout handling
- File downloads
- JSON data extraction
- Pandas DataFrame creation
- CSV data export

The goal is to understand how Python can collect data from APIs and transform the collected data into a structured format suitable for analysis.

---

## 3. IBM Hands-on Lab

### `01_IBM_Lab.py`

The IBM lab demonstrates practical HTTP request operations using Python's `requests` library.

### Main Concepts Practiced

```text
Python
   ↓
requests
   ↓
HTTP Request
   ↓
API / Web Server
   ↓
HTTP Response
   ↓
Status Code + Headers + Content
   ↓
JSON / Text / File

Operations Practiced
GET request
Query parameters
POST request
Request headers
Response headers
JSON response
File download
HTTP status code handling
Timeout handling

## 4. GET Request
A GET request is used to retrieve data from a server.
Example:
import requests
response = requests.get(
    "https://example.com",
    timeout=10
)
print(response.status_code)

## Important response attributes:
response.status_code
response.url
response.headers
response.text
response.encoding

## 5. HTTP Status Codes
### HTTP status codes indicate the result of an HTTP request.

| Status Code | Meaning                 |
| ----------: | ----------------------- |
|         200 | OK / Request successful |
|         201 | Created                 |
|         400 | Bad Request             |
|         401 | Unauthorized            |
|         403 | Forbidden               |
|         404 | Not Found               |
|         500 | Internal Server Error   |
|         503 | Service Unavailable     |

During this lab, IBM's website successfully returned:
Status Code: 200

## 6. Query Parameters

Query parameters can be sent using the params argument.

Example:
payload = {
    "name": "Varghese",
    "ID": 123
}

response = requests.get(
    "https://httpbin.org/get",
    params=payload,
    timeout=10
)
The generated URL becomes conceptually:

https://httpbin.org/get?name=Varghese&ID=123

The server can then return the supplied parameters as JSON.

## 7. JSON Response
Many REST APIs return data in JSON format.
Example:
data = response.json()
print(type(data))
print(data)

A JSON response can become a Python object such as:

dict
list

Example:

{
    "ID": "123",
    "name": "Varghese"
}

Python representation:

<class 'dict'>

## 8. POST Request

POST requests are commonly used to send data to a server.

Example:

payload = {
    "name": "Varghese",
    "ID": 123
}


response = requests.post(
    "https://httpbin.org/post",
    data=payload,
    timeout=10
)

The server can return the submitted form data.

Example:

POST Request Body:
name=Varghese&ID=123
## 9. Request Headers

Request headers provide additional information about the HTTP request.

Example:

print(response.request.headers)

Typical request headers include:

User-Agent
Accept
Accept-Encoding
Connection

The lab demonstrated the Python Requests user agent:

python-requests/2.34.2
## 10. Response Headers

Response headers provide information about the server response.

Example:

print(response.headers)

Common response headers include:

Content-Type
Content-Encoding
Date
Cache-Control
ETag
Strict-Transport-Security

The IBM website response during the lab included:

Content-Type: text/html;charset=utf-8
Content-Encoding: gzip
## 11. Error Handling

API requests can fail for many reasons.

Professional Python code should handle request failures safely.

Example:

try:


    response = requests.get(
        API_URL,
        timeout=15
    )


    response.raise_for_status()


except requests.exceptions.Timeout:


    print("Request timed out.")


except requests.exceptions.RequestException as error:


    print("API request failed:")
    print(error)

This prevents unexpected network problems from crashing the complete workflow.

## 12. Timeout Handling

During the IBM lab, httpbin.org occasionally returned timeout errors.

Observed error:

requests.exceptions.ReadTimeout

Example message:

Request timed out.
The server did not respond within 10 seconds.

This demonstrated an important real-world API concept:

A Python program can be correct even when the remote API server is temporarily slow, unavailable, or overloaded.
The timeout should therefore be treated as a network/API condition rather than automatically as a Python programming error.
13. HTTP 503 Service Unavailable

During repeated testing, httpbin.org also returned:

503 Service Temporarily Unavailable

This demonstrated why code should not blindly execute:

response.json()

without first checking the response.

A safer pattern is:

if response.ok:
    data = response.json()
else:
    print("Request failed.")
    print("Status:", response.status_code)

Important lesson:

503 ≠ Python Error

It is an HTTP response from the remote service.

14. JSONDecodeError

When a failed HTTP response was processed using:

response.json()

the program produced:
requests.exceptions.JSONDecodeError
This happened because the server response was not valid JSON.

A safer approach is:

if response.ok:


    data = response.json()


else:


    print("Request failed.")
    print("Status:", response.status_code)

Professional API workflow:

Request
   ↓
Check Status
   ↓
Validate Response
   ↓
Parse JSON

Do not assume every HTTP response contains valid JSON.

15. My Practice
02_My_Practice.py

A professional API data collection workflow was created using:

REST API
   ↓
GET Request
   ↓
JSON Response
   ↓
Python List
   ↓
Selected Fields
   ↓
Pandas DataFrame
   ↓
Data Analysis
   ↓
CSV Export

The practice project uses:

https://jsonplaceholder.typicode.com/users

The objective was to collect API data, extract useful fields, convert the result into a Pandas DataFrame, perform basic analysis, and save the result as a CSV file.

16. API Data Collection

The API returned:

10 users

The selected fields were:

ID
Name
Username
Email
City
Company

The resulting DataFrame contains:

10 rows
6 columns

DataFrame shape:

(10, 6)
17. Nested JSON Extraction

The API response contains nested objects.

For example:

user["address"]["city"]

extracts the city from the nested address object.

Similarly:

user["company"]["name"]

extracts the company name from the nested company object.

This is an important skill when working with real-world REST API responses because API data is frequently hierarchical and nested.

18. Pandas DataFrame

The extracted records were converted into a Pandas DataFrame:

df = pd.DataFrame(selected_users)

Result:

Shape: (10, 6)

Columns:

[
    'ID',
    'Name',
    'Username',
    'Email',
    'City',
    'Company'
]

The DataFrame provides a structured tabular representation of the API response.

19. Data Inspection

The following Pandas operations were practiced:

df.shape
df.columns.tolist()
df.dtypes

These operations provide basic information about the collected dataset.

Example result:

ID          int64
Name        str
Username    str
Email       str
City        str
Company     str
20. Basic Data Analysis

User distribution by city was calculated using:

df["City"].value_counts()

The result demonstrated that each returned user belonged to a different city in the sample dataset.

This demonstrates the transition:

Data Collection
      ↓
Data Structuring
      ↓
Data Analysis

API data can therefore be immediately transformed into a dataset suitable for analysis.

21. CSV Export

The final DataFrame was exported using:

df.to_csv(
    OUTPUT_FILE,
    index=False
)

Output file:

api_users.csv

The output path was also verified using pathlib:

from pathlib import Path


output_path = Path(OUTPUT_FILE).resolve()


df.to_csv(
    OUTPUT_FILE,
    index=False
)


print("Data saved successfully.")
print("Output File:", OUTPUT_FILE)
print("Output Path:", output_path)

The final output was successfully generated inside the lab folder.

22. Challenge
03_Challenge.py

The challenge section is used to reinforce the REST API concepts learned in the IBM lab and the My Practice exercise.

The challenge focuses on independently applying:

API requests
JSON processing
Error handling
Data extraction
Pandas
Data analysis
CSV export

The challenge is intended to move the learner from guided IBM exercises toward independent problem solving.

23. Debug Notes
04_Debug_Notes.md

This file records important problems encountered during the practical work.

Issue 1 – Requests Module Not Found

Initial error:

ModuleNotFoundError: No module named 'requests'

The environment was checked using:

python -m pip show requests

Installed package:

requests 2.34.2

Python interpreter verification:

python -c "import sys; print(sys.executable)"

Confirmed interpreter:

D:\MASTER\_BRAIN\_ENV_2025\IBM\_DAPC\.venv\Scripts\python.exe

Import test:

python -c "import requests; print('Requests OK:', requests.__version__)"

Result:

Requests OK: 2.34.2
Issue 2 – HTTPBin Timeout

Observed:

requests.exceptions.ReadTimeout

Cause:

The remote httpbin.org server did not respond within the configured timeout.

Solution:

Use timeout handling:

try:


    response = requests.get(
        URL,
        timeout=10
    )


except requests.exceptions.Timeout:


    print("Request timed out.")
Issue 3 – HTTP 503

Observed:

503 Service Temporarily Unavailable

Cause:

The remote server was temporarily unavailable.

Important lesson:

503 ≠ Python Error

It is an HTTP response from the remote service.

Issue 4 – JSONDecodeError

When a failed HTTP response was processed using:

response.json()

the program produced:

requests.exceptions.JSONDecodeError

Lesson:

Always validate the response before assuming that the server returned JSON.

Example:

if response.ok:


    data = response.json()


else:


    print("Request failed.")
    print(response.status_code)
24. Files and Technologies
Files in This Lab
02_REST_APIs_HTTP_Requests/
│
├── challenge_output/
│
├── 01_IBM_Lab.py
│
├── 02_My_Practice.py
│
├── 03_Challenge.py
│
├── 04_Debug_Notes.md
│
├── api_users.csv
│
├── httpbin_image.png
│
└── README.md

Technologies Used
Technology_Purpose

Python - Programming language
Requests - HTTP/API communication
Pandas - Data processing
JSON - API data format
REST - API architecture
HTTP - Communication protocol
pathlib - File path management
CSV - Data export format
VS Code - Development environment
Git/GitHub _Version control and portfolio

## 25. Skills, Data Engineering Connection & Lab Status
Key Skills Acquired

After completing this lab, I can:

Send HTTP GET requests using Python.
Send POST requests using Python.
Work with REST APIs.
Pass query parameters.
Inspect request headers.
Inspect response headers.
Read HTTP status codes.
Parse JSON responses.
Handle nested JSON structures.
Handle API errors.
Handle network timeouts.
Convert API data into Pandas DataFrames.
Perform basic DataFrame analysis.
Export API data to CSV.
Verify generated file paths.
Diagnose server-side API failures.
Build a basic API-to-DataFrame-to-CSV workflow.
Data Engineering Connection

This lab represents a practical introduction to the Extract, Transform, Load pattern.

              API / Web Service
                     │
                     ▼
              ┌─────────────┐
              │   EXTRACT   │
              └─────────────┘
                     │
                     ▼
                 JSON Data
                     │
                     ▼
              ┌─────────────┐
              │  TRANSFORM  │
              └─────────────┘
                     │
              Pandas DataFrame
                     │
                     ▼
              ┌─────────────┐
              │    LOAD     │
              └─────────────┘
                     │
                     ▼
                 CSV File

This is a simplified example of an ETL workflow.

Professional API Workflow
1. Identify API
       ↓
2. Send HTTP Request
       ↓
3. Check Status Code
       ↓
4. Handle Errors / Timeout
       ↓
5. Validate Response
       ↓
6. Parse JSON
       ↓
7. Extract Required Fields
       ↓
8. Create DataFrame
       ↓
9. Inspect / Analyze Data
       ↓
10. Export Data
Lab Status

Status: COMPLETED ✅

Completed components:

 IBM REST API Lab
 GET requests
 POST requests
 Query parameters
 Request headers
 Response headers
 JSON responses
 HTTP status codes
 Timeout handling
 Error handling
 API data extraction
 Nested JSON extraction
 Pandas DataFrame
 Basic analysis
 CSV export
 Output path verification
 Debug documentation

```

IBM DAPC – Course 04
Module 05 – APIs and Data Collection
Core Data Engineering Pattern
EXTRACT → TRANSFORM → LOAD

This lab establishes the foundation for programmatic data collection from REST APIs and prepares for advanced API usage, web scraping, and data engineering workflows.

Repository: IBM_DAPC
Course: 04 – Python for Data Science, AI & Development
Module: 05 – APIs and Data Collection
Lab: 02 – REST APIs & HTTP Requests
Status: ✅ COMPLETED
