"""
===============================================================================
Employee Analytics & Business Intelligence System

Report Generation Module

IBM Data Analyst Professional Certificate (IBM DAPC)

Author : Varghese
Version : 2.0
===============================================================================
"""

from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font

from config import (
    CSV_DIR,
    EXCEL_DIR,
    REPORT_DIR,
)

from utils import (
    print_header,
    print_success,
)

# =============================================================================
# Export Excel Workbook
# =============================================================================


def export_excel(report_dict):
    """
    Export all report DataFrames into a single Excel workbook.
    """

    print_header("GENERATING EXCEL WORKBOOK")

    workbook = Workbook()

    # Remove default sheet
    workbook.remove(workbook.active)

    for report_name, dataframe in report_dict.items():

        sheet_name = report_name.replace("_", " ").title()

        worksheet = workbook.create_sheet(title=sheet_name[:31])

        # Write Header
        worksheet.append(list(dataframe.columns))

        # Bold Header
        for cell in worksheet[1]:
            cell.font = Font(bold=True)

        # Write Data
        for row in dataframe.itertuples(index=False):
            worksheet.append(list(row))

        # Auto Column Width
        for column_cells in worksheet.columns:

            max_length = max(
                len(str(cell.value)) if cell.value is not None else 0
                for cell in column_cells
            )

            worksheet.column_dimensions[column_cells[0].column_letter].width = (
                max_length + 3
            )

    excel_file = EXCEL_DIR / "Employee_Analytics_Report.xlsx"

    workbook.save(excel_file)

    print_success("Excel workbook generated successfully.")

    return excel_file


# =============================================================================
# Executive Markdown Report
# =============================================================================


def generate_markdown_report(df):
    """
    Generate Executive Markdown Report.
    """

    print_header("GENERATING EXECUTIVE REPORT")

    report = f"""# Employee Analytics Report

## Executive Summary

- Total Employees : {len(df)}
- Departments : {df['Department'].nunique()}
- Cities : {df['City'].nunique()}
- Projects : {df['Project'].nunique()}

## Salary Summary

- Average Salary : ₹ {df['Salary'].mean():,.2f}
- Highest Salary : ₹ {df['Salary'].max():,.2f}
- Lowest Salary : ₹ {df['Salary'].min():,.2f}

---

Generated Automatically

Employee Analytics & Business Intelligence System
"""

    report_file = REPORT_DIR / "Executive_Report.md"

    with open(report_file, "w", encoding="utf-8") as file:
        file.write(report)

    print_success("Executive markdown report generated.")

    return report_file


# =============================================================================
# Project Log
# =============================================================================


def generate_project_log():
    """
    Generate Project Log.
    """

    print_header("GENERATING PROJECT LOG")

    now = datetime.now()

    log = f"""Employee Analytics & Business Intelligence System

Execution Date : {now.strftime("%d-%m-%Y")}

Execution Time : {now.strftime("%H:%M:%S")}

Status : SUCCESS

Project Version : 2.0
"""

    log_file = REPORT_DIR / "Project_Log.txt"

    with open(log_file, "w", encoding="utf-8") as file:
        file.write(log)

    print_success("Project log generated.")

    return log_file


# =============================================================================
# List Generated Reports
# =============================================================================


def list_generated_reports():
    """
    Display all generated CSV reports.
    """

    print_header("GENERATED CSV REPORTS")

    csv_files = sorted(CSV_DIR.glob("*.csv"))

    if not csv_files:

        print("No CSV reports found.")

        return

    for file in csv_files:

        print_success(file.name)
