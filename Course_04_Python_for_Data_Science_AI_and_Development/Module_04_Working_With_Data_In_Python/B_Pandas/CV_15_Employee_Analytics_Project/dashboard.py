"""
===============================================================================
Employee Analytics & Business Intelligence System

Dashboard Module

IBM Data Analyst Professional Certificate (IBM DAPC)

Author : Varghese
Version : 2.0
===============================================================================
"""

from datetime import datetime

from utils import (
    print_header,
    print_success,
)

# =============================================================================
# Project Banner
# =============================================================================


def show_banner():

    print("\n" + "=" * 80)

    print("EMPLOYEE ANALYTICS & BUSINESS INTELLIGENCE SYSTEM".center(80))

    print("Professional Capstone Project".center(80))

    print("IBM Data Analyst Professional Certificate".center(80))

    print("=" * 80)


# =============================================================================
# Dataset Summary
# =============================================================================


def dataset_summary(df):

    print_header("DATASET SUMMARY")

    print(f"Total Employees     : {len(df)}")

    print(f"Departments         : {df['Department'].nunique()}")

    print(f"Cities              : {df['City'].nunique()}")

    print(f"Projects            : {df['Project'].nunique()}")

    print(f"Average Salary      : ₹ {df['Salary'].mean():,.2f}")

    print(f"Highest Salary      : ₹ {df['Salary'].max():,.2f}")

    print(f"Lowest Salary       : ₹ {df['Salary'].min():,.2f}")


# =============================================================================
# Output Summary
# =============================================================================


def output_summary():

    print_header("OUTPUT GENERATED")

    outputs = [
        "CSV Reports",
        "Excel Workbook",
        "Charts",
        "Executive Markdown Report",
        "Project Log",
    ]

    for item in outputs:

        print_success(item)


# =============================================================================
# Project Information
# =============================================================================


def project_information():

    print_header("PROJECT INFORMATION")

    print("Project Name : Employee Analytics & Business Intelligence System")

    print("Version      : 2.0")

    print("Author       : Varghese")

    print("Platform     : IBM Data Analyst Professional Certificate")

    print("Language     : Python")

    print("Library      : Pandas, Matplotlib, OpenPyXL")


# =============================================================================
# Execution Summary
# =============================================================================


def execution_summary():

    print_header("EXECUTION SUMMARY")

    print_success("Dataset Loaded")

    print_success("Analytics Completed")

    print_success("Reports Generated")

    print_success("Charts Generated")

    print_success("Excel Workbook Created")

    print_success("Markdown Report Created")

    print_success("Project Log Created")


# =============================================================================
# Completion Banner
# =============================================================================


def completion_banner():

    print("\n" + "=" * 80)

    print("PROJECT COMPLETED SUCCESSFULLY".center(80))

    print("=" * 80)

    print()

    print(f"Execution Time : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")

    print()

    print("Thank you for using")

    print("Employee Analytics & Business Intelligence System")

    print()

    print("=" * 80)


# =============================================================================
# Display Complete Dashboard
# =============================================================================


def display_dashboard(df):

    show_banner()

    dataset_summary(df)

    output_summary()

    project_information()

    execution_summary()

    completion_banner()
