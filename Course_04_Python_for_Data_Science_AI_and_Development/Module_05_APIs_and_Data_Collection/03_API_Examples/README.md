# API Examples

## IBM DAPC – Course 04

### Python for Data Science, AI & Development

---

## 1. Module Information

**Course:** Course 04 – Python for Data Science, AI & Development  
**Module:** Module 05 – APIs and Data Collection  
**Lab:** API Examples  
**Folder:** `03_API_Examples`

---

## 2. Learning Objective

This lab focuses on working with API-generated data and converting the collected information into a structured Pandas DataFrame.

The practical work demonstrates how Python can:

- Connect to an API-based data source.
- Generate user records.
- Access API-generated user objects.
- Extract selected fields.
- Convert API data into Python dictionaries.
- Store records in a list.
- Create a Pandas DataFrame.
- Inspect structured API data.
- Validate collected data.
- Perform basic data analysis.
- Export the dataset to CSV.
- Handle multilingual and Unicode data.

The main objective is to understand the complete transition from API data collection to structured data analysis.

---

## 3. IBM Hands-on Lab

### `01_IBM_Lab.py`

The IBM lab demonstrates the use of the `RandomUser` package to generate user data.

The main IBM workflow is:

```text
RandomUser
    ↓
Generate Users
    ↓
Python Objects
    ↓
Extract User Information
    ↓
Dictionary
    ↓
List
    ↓
Pandas DataFrame

The lab uses:

from randomuser import RandomUser
import pandas as pd
4. Random User Data Generation

The IBM lab generates multiple user records using:

users = RandomUser.generate_users(10)

The number of generated users in the IBM practice was:

10 users

The generated data is dynamic.

Therefore, each execution can produce different:

Names
Gender
Cities
States
Email addresses
Dates of birth
Profile pictures

This is expected behavior because the Random User source generates random user records.

5. RandomUser Object

When printing a generated user directly:

print(users[0])

the output appears similar to:

<randomuser.RandomUser object at 0x...>

This is not an error.

It is the Python representation of a RandomUser object.

The actual user information is accessed through methods such as:

user.get_full_name()
user.get_gender()
user.get_city()
user.get_state()
user.get_email()
user.get_dob()
user.get_picture()
6. User Data Extraction

The IBM lab extracts selected fields from each generated user.

The main fields are:

Name
Gender
City
State
Email
DOB
Picture

The extracted information is stored as a Python dictionary.

Example structure:

{
    "Name": user.get_full_name(),
    "Gender": user.get_gender(),
    "City": user.get_city(),
    "State": user.get_state(),
    "Email": user.get_email(),
    "DOB": user.get_dob(),
    "Picture": user.get_picture()
}

Multiple dictionaries are stored inside a list.

7. Creating the Pandas DataFrame

The extracted records are converted into a Pandas DataFrame:

df = pd.DataFrame(user_data)

The IBM lab successfully produced:

Shape: (10, 7)

The seven columns were:

Name
Gender
City
State
Email
DOB
Picture

This converts API-generated object data into a tabular format suitable for data analysis.

8. IBM Function – get_users()

The IBM lab also introduces a reusable function:

def get_users():


    users = []


    for user in RandomUser.generate_users(10):


        users.append(
            {
                "Name": user.get_full_name(),
                "Gender": user.get_gender(),
                "City": user.get_city(),
                "State": user.get_state(),
                "Email": user.get_email(),
                "DOB": user.get_dob(),
                "Picture": user.get_picture()
            }
        )


    return pd.DataFrame(users)

The function combines:

Data Generation
       ↓
Data Extraction
       ↓
Dictionary Creation
       ↓
List Construction
       ↓
DataFrame Creation

This is an important step toward reusable Python data-collection functions.

9. My Practice
02_My_Practice.py

The IBM concept was extended into a more professional API data collection workflow.

Instead of generating only 10 users, the practice program generates:

20 users

The professional workflow is:

Random User API
       ↓
20 Records
       ↓
Data Extraction
       ↓
Pandas DataFrame
       ↓
Data Validation
       ↓
Data Quality Checks
       ↓
Business Analysis
       ↓
CSV Export
       ↓
Output Verification
10. Data Validation

The professional practice performs several validation checks.

Dataset Shape
df.shape

The verified result was:

(20, 7)

This means:

20 records
7 columns
Column Validation

The program checks:

df.columns.tolist()

Expected columns:

Name
Gender
City
State
Email
DOB
Picture
Missing Value Check

The program uses:

df.isnull().sum()

Verified result:

0 missing values

for all seven columns.

Duplicate Check

The program uses:

df.duplicated().sum()

Verified result:

0 duplicate rows

This provides a basic data quality check before analysis.

11. Sample Data Inspection

The practice program displays sample records using:

df.head()

This allows the analyst to quickly inspect the first five records.

Example data may contain multilingual names such as:

رونیکا حسینی
کوروش پارسا
احسان مرادی

and multilingual geographic information.

This demonstrates that API-generated datasets can contain Unicode and non-English text.

12. Unicode Data Handling

The practice project intentionally uses:

encoding="utf-8-sig"

during CSV export.

Example:

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig"
)

This helps preserve multilingual text when the CSV is opened in applications such as Excel.

The practical run successfully handled multilingual records without data corruption.

13. Gender Analysis

The practice project calculates gender distribution using:

df["Gender"].value_counts()

One verified run produced:

male      11
female     9

The result can change in future runs because the Random User data is dynamically generated.

The important concept is the use of:

value_counts()

for categorical data analysis.

14. State Analysis

State distribution is calculated using:

df["State"].value_counts()

The practice project displays the top states using:

state_distribution.head(10)

This provides a quick geographic distribution analysis.

The exact results can change on every execution because the user records are randomly generated.

15. City Analysis

City distribution is calculated using:

df["City"].value_counts()

The top cities are displayed using:

city_distribution.head(10)

This demonstrates how categorical geographic information can be summarized using Pandas.

16. Data Quality Check

The professional practice checks whether all required columns exist.

Required columns:

required_columns = [
    "Name",
    "Gender",
    "City",
    "State",
    "Email",
    "DOB",
    "Picture",
]

The program compares the required columns against the DataFrame.

If all required columns are present:

All required columns are present.

This is a simple but useful validation step in a real-world data pipeline.

17. CSV Export

The final dataset is exported to:

practice_output/random_users.csv

The program creates the output directory automatically:

OUTPUT_DIR.mkdir(exist_ok=True)

The DataFrame is exported using:

df.to_csv(
    OUTPUT_FILE,
    index=False,
    encoding="utf-8-sig",
)
18. Output Path Verification

The practice program verifies the generated file using pathlib.

Example:

output_path = OUTPUT_FILE.resolve()


print("Output Path:")
print(output_path)


print("File Exists:")
print(output_path.exists())

The verified result was:

File Exists:
True

The generated CSV file size in the tested run was:

2965 bytes

The exact size may vary depending on the randomly generated data.

19. Project Structure

The current project structure is:

03_API_Examples/
│
├── 01_IBM_Lab.py
│
├── 02_My_Practice.py
│
├── practice_output/
│   └── random_users.csv
│
├── 03_Challenge.py
│
├── 04_Debug_Notes.md
│
└── README.md

The challenge, debug notes, and final documentation will complete the full lab portfolio structure.

20. Technologies Used
Technology-Purpose
Python-Programming language
RandomUser-API-generated user data
Pandas-Data processing and analysis
JSON/API Objects-Data source representation
pathlib - File and directory management
CSV - Data export
VS Code - Development environment
Git - Version control
GitHub - Portfolio publishing
21. Key Functions and Methods
RandomUser
RandomUser.generate_users()

Generates user objects.

User Information Methods
user.get_full_name()
user.get_gender()
user.get_city()
user.get_state()
user.get_email()
user.get_dob()
user.get_picture()

These methods extract individual user attributes.

Pandas
pd.DataFrame()

Creates a DataFrame.

df.shape

Returns the number of rows and columns.

df.columns.tolist()

Returns column names.

df.isnull().sum()

Checks missing values.

df.duplicated().sum()

Checks duplicate rows.

df["Gender"].value_counts()

Counts categorical values.

df.head()

Displays sample records.

df.to_csv()

Exports the DataFrame to CSV.

22. Business Applications

The techniques practiced in this lab are applicable to many real-world data workflows.

Examples include:

Customer Data Collection
API
 ↓
Customer Records
 ↓
DataFrame
 ↓
Customer Analysis
Market Research
API
 ↓
Market Data
 ↓
Structured Dataset
 ↓
Business Insights
HR Analytics
Employee API
 ↓
Employee Dataset
 ↓
Gender / Location Analysis
 ↓
HR Insights
Customer Segmentation
Customer Data
 ↓
Location
 ↓
Category
 ↓
Frequency
 ↓
Segmentation
Data Engineering
API
 ↓
Extract
 ↓
Transform
 ↓
Validate
 ↓
Load
23. Common Mistakes
Mistake 1 – Treating RandomUser object output as an error

Output:

<randomuser.RandomUser object at 0x...>

This is normal Python object representation.

Use the appropriate methods:

user.get_full_name()
user.get_email()
user.get_city()
Mistake 2 – Expecting identical data every run

Random User data changes every time the program runs.

Therefore:

Run 1 ≠ Run 2

This is expected behavior.

Mistake 3 – Ignoring Unicode

API data may contain non-English characters.

Use UTF-8 compatible export:

encoding="utf-8-sig"
Mistake 4 – Skipping validation

Before analysis, always check:

df.shape
df.columns
df.isnull().sum()
df.duplicated().sum()
Mistake 5 – Hard-coding output directories

Using pathlib provides a cleaner approach:

from pathlib import Path


OUTPUT_DIR = Path("practice_output")
24. Key Takeaways

After completing this lab, I can:

Generate API-based user data.
Work with API-generated Python objects.
Extract individual fields from API objects.
Build dictionaries from API records.
Store records in Python lists.
Convert API data into Pandas DataFrames.
Validate dataset structure.
Detect missing values.
Detect duplicate rows.
Analyze categorical data.
Analyze gender distribution.
Analyze state distribution.
Analyze city distribution.
Handle multilingual Unicode data.
Export structured API data to CSV.
Verify generated files and paths.
Build a reusable API data collection workflow.
25. Lab Status and Next Step
Current Status

API Examples – Practical Lab: IN PROGRESS

Completed:

 01_IBM_Lab.py
 RandomUser data generation
 User field extraction
 Pandas DataFrame creation
 IBM get_users() function
 02_My_Practice.py
 20-user dataset
 Data validation
 Missing value analysis
 Duplicate analysis
 Gender analysis
 State analysis
 City analysis
 Unicode handling
 CSV export
 Output path verification
```

IBM DAPC – Course 04
Module 05 – APIs and Data Collection
Lab 03 – API Examples

The central learning pattern is:

API DATA
↓
EXTRACT
↓
STRUCTURE
↓
VALIDATE
↓
ANALYZE
↓
EXPORT

This lab strengthens the connection between Python programming, API data collection, Pandas data analysis, and practical data engineering workflows.

Repository: IBM_DAPC
Course: 04 – Python for Data Science, AI & Development
Module: 05 – APIs and Data Collection
Lab: 03 – API Examples
Status: 🔄 IN PROGRESS
