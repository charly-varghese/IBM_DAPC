"""
=========================================================
Configuration File

Employee Analytics & Business Intelligence System

IBM Data Analyst Professional Certificate
=========================================================
"""

from pathlib import Path

# --------------------------------------------------------
# Project Information
# --------------------------------------------------------

PROJECT_NAME = "Employee Analytics & Business Intelligence System"

VERSION = "2.0"

AUTHOR = "Varghese"

# --------------------------------------------------------
# Base Directories
# --------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATASET_DIR = BASE_DIR.parent / "datasets"

RAW_DATA = DATASET_DIR / "raw"

PROCESSED_DATA = DATASET_DIR / "processed"

# Main Dataset

EMPLOYEE_DATABASE = PROCESSED_DATA / "employee_database.csv"

# --------------------------------------------------------
# Output Directories
# --------------------------------------------------------

OUTPUT_DIR = BASE_DIR / "output"

CSV_DIR = OUTPUT_DIR / "csv"

EXCEL_DIR = OUTPUT_DIR / "excel"

CHART_DIR = OUTPUT_DIR / "charts"

REPORT_DIR = OUTPUT_DIR / "reports"

# --------------------------------------------------------
# Create Folders Automatically
# --------------------------------------------------------

CSV_DIR.mkdir(parents=True, exist_ok=True)

EXCEL_DIR.mkdir(parents=True, exist_ok=True)

CHART_DIR.mkdir(parents=True, exist_ok=True)

REPORT_DIR.mkdir(parents=True, exist_ok=True)
