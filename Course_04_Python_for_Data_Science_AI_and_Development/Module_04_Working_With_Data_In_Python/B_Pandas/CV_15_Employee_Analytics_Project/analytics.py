"""
===============================================================================
Employee Analytics & Business Intelligence System

Business Analytics Module

IBM Data Analyst Professional Certificate (IBM DAPC)

Author : Varghese
Version : 2.0
===============================================================================
"""

import pandas as pd

from config import (
    EMPLOYEE_DATABASE,
    CSV_DIR,
)

from utils import (
    print_header,
    print_success,
    validate_dataset,
    check_required_columns,
)

# =============================================================================
# Load Dataset
# =============================================================================


def load_dataset():

    print_header("LOADING DATASET")

    df = pd.read_csv(EMPLOYEE_DATABASE)

    validate_dataset(df)

    print_success("Employee database loaded successfully.")

    return df


# =============================================================================
# Dataset Overview
# =============================================================================


def dataset_overview(df):

    print_header("DATASET OVERVIEW")

    print(df.info())

    print(df.head())


# =============================================================================
# Executive KPI
# =============================================================================


def executive_kpi(df):

    print_header("EXECUTIVE KPI")

    kpi = pd.DataFrame(
        {
            "Metric": [
                "Total Employees",
                "Departments",
                "Cities",
                "Projects",
                "Average Salary",
                "Highest Salary",
                "Lowest Salary",
            ],
            "Value": [
                len(df),
                df["Department"].nunique(),
                df["City"].nunique(),
                df["Project"].nunique(),
                df["Salary"].mean(),
                df["Salary"].max(),
                df["Salary"].min(),
            ],
        }
    )

    return kpi


# =============================================================================
# Employee Summary
# =============================================================================


def employee_summary(df):

    return df.copy()


# =============================================================================
# Department Summary
# =============================================================================


def department_summary(df):

    return (
        df.groupby("Department")
        .agg(
            Employees=("Employee_ID", "count"),
            Average_Salary=("Salary", "mean"),
            Highest_Salary=("Salary", "max"),
            Lowest_Salary=("Salary", "min"),
            Total_Salary=("Salary", "sum"),
            Average_Experience=("Experience", "mean"),
        )
        .round(2)
        .sort_values(by="Average_Salary", ascending=False)
    )


# =============================================================================
# City Summary
# =============================================================================


def city_summary(df):

    return (
        df.groupby("City")
        .agg(Employees=("Employee_ID", "count"), Average_Salary=("Salary", "mean"))
        .round(2)
    )


# =============================================================================
# Salary Summary
# =============================================================================


def salary_summary(df):

    salary = pd.DataFrame(
        {
            "Metric": [
                "Total Salary",
                "Average Salary",
                "Median Salary",
                "Highest Salary",
                "Lowest Salary",
                "Standard Deviation",
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

    return salary


# =============================================================================
# Project Summary
# =============================================================================


def project_summary(df):

    return df.groupby("Project").agg(Employees=("Employee_ID", "count"))


# =============================================================================
# Hiring Trend
# =============================================================================


def hiring_trend(df):

    temp = df.copy()

    temp["Join_Date"] = pd.to_datetime(temp["Join_Date"])

    temp["Year"] = temp["Join_Date"].dt.year

    return temp.groupby("Year").agg(Employees=("Employee_ID", "count"))


# =============================================================================
# Top Salary Report
# =============================================================================


def top_salary_report(df):

    return df.sort_values(by="Salary", ascending=False)[
        ["Employee_ID", "Name", "Department", "Salary", "Project"]
    ].head(5)


# =============================================================================
# Generate All Reports
# =============================================================================


def generate_reports(df):
    """
    Generate all analytics reports and return them as a dictionary.
    """

    print_header("GENERATING ANALYTICS REPORTS")

    reports = {
        "employee_summary": employee_summary(df),
        "department_summary": department_summary(df),
        "city_summary": city_summary(df),
        "salary_summary": salary_summary(df),
        "project_summary": project_summary(df),
        "hiring_trend": hiring_trend(df),
        "top_salary_report": top_salary_report(df),
        "kpi_dashboard": executive_kpi(df),
    }

    print_success("Analytics completed successfully.")

    return reports


# =============================================================================
# Save CSV Reports
# =============================================================================


def save_csv_reports(report_dict):
    """
    Save all reports to CSV files.
    """

    print_header("SAVING CSV REPORTS")

    for report_name, dataframe in report_dict.items():

        output_file = CSV_DIR / f"{report_name}.csv"

        dataframe.to_csv(output_file, index=False)

        print_success(f"{report_name}.csv created")

    print_success("All CSV reports generated successfully.")
