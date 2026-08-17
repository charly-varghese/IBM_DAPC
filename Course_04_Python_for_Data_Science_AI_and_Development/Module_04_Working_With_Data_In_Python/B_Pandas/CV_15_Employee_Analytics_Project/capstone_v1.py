"""
===============================================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 : Python for Data Science, AI & Development
Module 04 : Working with Data in Python

CAPSTONE PROJECT

Employee Analytics & Business Intelligence System

Part 01
Project Initialization
Data Validation
Executive KPI Dashboard

Author : Varghese

===============================================================================
"""

# =============================================================================
# Import Libraries
# =============================================================================

import pandas as pd

from pathlib import Path

from openpyxl import Workbook

import matplotlib.pyplot as plt

from datetime import datetime

# =============================================================================
# Project Configuration
# =============================================================================

# =============================================================================
# Project Configuration
# =============================================================================

PROJECT_NAME = "Employee Analytics & Business Intelligence System"

# Current Project Folder
BASE_DIR = Path(__file__).resolve().parent

# Common Dataset Folder
DATASET = BASE_DIR.parent / "datasets" / "processed" / "employee_database.csv"

# Project Output Folders
OUTPUT_CSV = BASE_DIR / "output" / "csv"
OUTPUT_EXCEL = BASE_DIR / "output" / "excel"
OUTPUT_CHARTS = BASE_DIR / "output" / "charts"
OUTPUT_REPORTS = BASE_DIR / "output" / "reports"

# Common Reports Folder
REPORT_FOLDER = BASE_DIR.parent / "reports"

# Create folders automatically
OUTPUT_CSV.mkdir(parents=True, exist_ok=True)
OUTPUT_EXCEL.mkdir(parents=True, exist_ok=True)
OUTPUT_CHARTS.mkdir(parents=True, exist_ok=True)
OUTPUT_REPORTS.mkdir(parents=True, exist_ok=True)
REPORT_FOLDER.mkdir(parents=True, exist_ok=True)

# =============================================================================
# Helper Functions
# =============================================================================


def print_header(title: str):
    """Print a formatted section header."""
    print("\n" + "=" * 75)
    print(title.center(75))
    print("=" * 75)


def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Load dataset from CSV.
    """

    print_header("STEP 1 : LOADING DATASET")

    if not file_path.exists():
        raise FileNotFoundError(f"\nDataset not found:\n{file_path}")

    df = pd.read_csv(file_path)

    print("Dataset Loaded Successfully.")

    return df


def validate_dataset(df: pd.DataFrame):
    """
    Validate dataset structure.
    """

    print_header("STEP 2 : DATASET VALIDATION")

    print(f"Rows             : {df.shape[0]}")
    print(f"Columns          : {df.shape[1]}")

    print("\nColumn Names")

    for column in df.columns:
        print(f"• {column}")

    print("\nData Types")

    print(df.dtypes)


def explore_dataset(df: pd.DataFrame):
    """
    Explore dataset.
    """

    print_header("STEP 3 : DATASET EXPLORATION")

    print("\nFirst Five Records")

    print(df.head())

    print("\nLast Five Records")

    print(df.tail())

    print("\nSummary Statistics")

    print(df.describe(include="all"))


def executive_dashboard(df: pd.DataFrame):
    """
    Display Executive KPI Dashboard.
    """

    print_header("EXECUTIVE KPI DASHBOARD")

    total_employees = len(df)

    total_departments = df["Department"].nunique()

    total_projects = df["Project"].nunique()

    total_cities = df["City"].nunique()

    total_salary = df["Salary"].sum()

    average_salary = df["Salary"].mean()

    highest_salary = df["Salary"].max()

    lowest_salary = df["Salary"].min()

    average_experience = df["Experience"].mean()

    print(f"Total Employees          : {total_employees}")

    print(f"Departments              : {total_departments}")

    print(f"Cities                   : {total_cities}")

    print(f"Projects                 : {total_projects}")

    print("-" * 75)

    print(f"Total Salary             : ₹ {total_salary:,.2f}")

    print(f"Average Salary           : ₹ {average_salary:,.2f}")

    print(f"Highest Salary           : ₹ {highest_salary:,.2f}")

    print(f"Lowest Salary            : ₹ {lowest_salary:,.2f}")

    print(f"Average Experience       : {average_experience:.2f} Years")

    # Join_Date may not exist if CV_14 was skipped
    if "Join_Date" in df.columns:

        join_dates = pd.to_datetime(df["Join_Date"])

        print("-" * 75)

        print(f"First Join Date          : {join_dates.min().date()}")

        print(f"Latest Join Date         : {join_dates.max().date()}")

        print(f"Years Covered            : {join_dates.dt.year.nunique()}")


def department_analytics(df: pd.DataFrame):

    print_header("DEPARTMENT ANALYTICS")

    department_report = (
        df.groupby("Department")
        .agg(
            Employees=("Employee_ID", "count"),
            Total_Salary=("Salary", "sum"),
            Average_Salary=("Salary", "mean"),
            Highest_Salary=("Salary", "max"),
            Lowest_Salary=("Salary", "min"),
            Average_Experience=("Experience", "mean"),
        )
        .round(2)
        .sort_values("Average_Salary", ascending=False)
    )

    print(department_report)

    department_report.to_csv(OUTPUT_CSV / "department_summary.csv")

    return department_report


def city_analytics(df):

    print_header("CITY ANALYTICS")

    city_report = (
        df.groupby("City")
        .agg(Employees=("Employee_ID", "count"), Average_Salary=("Salary", "mean"))
        .round(2)
        .sort_values("Employees", ascending=False)
    )

    print(city_report)

    city_report.to_csv(OUTPUT_CSV / "city_summary.csv")

    return city_report


def salary_analytics(df):

    print_header("SALARY ANALYTICS")

    salary_summary = pd.DataFrame(
        {
            "Metric": [
                "Total Salary",
                "Average Salary",
                "Median Salary",
                "Highest Salary",
                "Lowest Salary",
                "Salary Std Dev",
            ],
            "Value": [
                df["Salary"].sum(),
                df["Salary"].mean(),
                df["Salary"].median(),
                df["Salary"].max(),
                df["Salary"].min(),
                df["Salary"].std(),
            ],
        }
    )

    print(salary_summary)

    salary_summary.to_csv(OUTPUT_CSV / "salary_summary.csv", index=False)
    return salary_summary


def project_analytics(df):

    print_header("PROJECT ANALYTICS")

    project_report = (
        df.groupby("Project").agg(Employees=("Employee_ID", "count")).sort_index()
    )

    print(project_report)

    project_report.to_csv(OUTPUT_CSV / "project_summary.csv")

    return project_report


def hiring_trend(df):

    if "Join_Date" not in df.columns:
        print("\nJoin_Date column not available.")
        return

    print_header("HIRING TREND")

    temp = df.copy()

    temp["Join_Date"] = pd.to_datetime(temp["Join_Date"])

    temp["Year"] = temp["Join_Date"].dt.year

    report = temp.groupby("Year").agg(Employees=("Employee_ID", "count"))

    print(report)

    report.to_csv(OUTPUT_CSV / "hiring_trend.csv")

    return report


def top_salary_report(df):

    print_header("TOP 5 HIGHEST PAID EMPLOYEES")

    top = df.sort_values("Salary", ascending=False)[
        ["Employee_ID", "Name", "Department", "Salary", "Project"]
    ].head(5)

    print(top)

    top.to_csv(OUTPUT_CSV / "top_salary_report.csv", index=False)

    return top


def employee_summary(df):

    print_header("EMPLOYEE SUMMARY")

    summary = df.copy()

    print(summary.head())

    summary.to_csv(OUTPUT_CSV / "employee_summary.csv", index=False)

    return summary

    from openpyxl import Workbook


def export_to_excel():

    print_header("EXPORTING EXCEL REPORT")

    wb = Workbook()

    # Remove default sheet
    wb.remove(wb.active)

    reports = {
        "Employee Summary": "employee_summary.csv",
        "Department Summary": "department_summary.csv",
        "City Summary": "city_summary.csv",
        "Salary Summary": "salary_summary.csv",
        "Project Summary": "project_summary.csv",
        "Hiring Trend": "hiring_trend.csv",
        "Top Salary": "top_salary_report.csv",
    }

    for sheet_name, filename in reports.items():

        csv_file = OUTPUT_CSV / filename

        if csv_file.exists():

            ws = wb.create_sheet(title=sheet_name[:31])

            df = pd.read_csv(csv_file)

            ws.append(list(df.columns))

            for row in df.itertuples(index=False):
                ws.append(list(row))

    excel_file = OUTPUT_EXCEL / "Employee_Analytics_Report.xlsx"

    wb.save(excel_file)

    print("Excel Report Created")

    print(excel_file)


def executive_report(df):

    print_header("EXECUTIVE REPORT")

    report = f"""
# Employee Analytics Report

## Company Summary

Total Employees : {len(df)}

Departments : {df['Department'].nunique()}

Cities : {df['City'].nunique()}

Projects : {df['Project'].nunique()}

## Salary Summary

Average Salary : ₹ {df['Salary'].mean():,.2f}

Highest Salary : ₹ {df['Salary'].max():,.2f}

Lowest Salary : ₹ {df['Salary'].min():,.2f}

## Conclusion

The employee analytics pipeline completed successfully.

Reports have been generated in CSV and Excel formats.
"""

    file = OUTPUT_REPORTS / "Executive_Report.md"

    with open(file, "w", encoding="utf-8") as f:
        f.write(report)

    print("Executive Report Created")


from datetime import datetime


def project_log():

    print_header("PROJECT LOG")

    now = datetime.now()

    log = f"""
Project Completed Successfully

Date : {now.strftime('%d-%m-%Y')}

Time : {now.strftime('%H:%M:%S')}
"""

    file = OUTPUT_REPORTS / "Project_Log.txt"

    with open(file, "w") as f:

        f.write(log)

    print("Project Log Created")


import matplotlib.pyplot as plt


def department_salary_chart(df):

    print_header("DEPARTMENT SALARY CHART")

    salary = df.groupby("Department")["Salary"].mean().sort_values()

    plt.figure(figsize=(8, 5))

    plt.bar(salary.index, salary.values)

    plt.title("Average Salary by Department")

    plt.xticks(rotation=30)

    plt.tight_layout()

    file = OUTPUT_CHARTS / "department_salary_chart.png"

    plt.savefig(file)

    plt.close()

    print(file)


def hiring_trend_chart(df):

    if "Join_Date" not in df.columns:

        return

    temp = df.copy()

    temp["Join_Date"] = pd.to_datetime(temp["Join_Date"])

    temp["Year"] = temp["Join_Date"].dt.year

    yearly = temp.groupby("Year").size()

    plt.figure(figsize=(8, 5))

    plt.plot(yearly.index, yearly.values, marker="o")

    plt.title("Hiring Trend")

    plt.grid(True)

    plt.tight_layout()

    file = OUTPUT_CHARTS / "hiring_trend.png"

    plt.savefig(file)

    plt.close()

    print(file)


def final_dashboard():

    print("\n")

    print("=" * 75)

    print("EMPLOYEE ANALYTICS & BUSINESS INTELLIGENCE SYSTEM".center(75))

    print("=" * 75)

    print()

    print("✓ CSV Reports Generated")

    print("✓ Excel Report Generated")

    print("✓ Charts Generated")

    print("✓ Executive Report Generated")

    print("✓ Project Log Generated")

    print()

    print("Project Completed Successfully")

    print()

    print("=" * 75)


# =============================================================================
# Main Program
# =============================================================================


def main():

    print("\n" + "=" * 75)
    print(PROJECT_NAME.center(75))
    print("=" * 75)

    df = load_dataset(DATASET)

    validate_dataset(df)

    explore_dataset(df)

    executive_dashboard(df)

    # Analytics Reports

    employee_summary(df)

    department_analytics(df)

    city_analytics(df)

    salary_analytics(df)

    project_analytics(df)

    hiring_trend(df)

    top_salary_report(df)

    export_to_excel()

    department_salary_chart(df)

    hiring_trend_chart(df)

    executive_report(df)

    project_log()

    final_dashboard()

    print_header("CSV REPORTS GENERATED")

    print("employee_summary.csv")

    print("department_summary.csv")

    print("city_summary.csv")

    print("salary_summary.csv")

    print("project_summary.csv")

    print("top_salary_report.csv")

    print("hiring_trend.csv")

    print("\nReports saved successfully.")

    print("\n" + "=" * 75)
    print("PART 02 COMPLETED SUCCESSFULLY".center(75))
    print("=" * 75)


# =============================================================================

if __name__ == "__main__":
    main()
