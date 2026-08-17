"""
===============================================================================
Employee Analytics & Business Intelligence System

Utility Functions

IBM Data Analyst Professional Certificate (IBM DAPC)

Author : Varghese
Version : 2.0
===============================================================================
"""

from datetime import datetime
from pathlib import Path
import time
import pandas as pd

# =============================================================================
# Console Formatting
# =============================================================================


def print_header(title: str) -> None:
    """Print a formatted section header."""

    print("\n" + "=" * 80)
    print(title.center(80))
    print("=" * 80)


def print_section(title: str) -> None:
    """Print a subsection heading."""

    print("\n" + "-" * 80)
    print(title)
    print("-" * 80)


def print_success(message: str) -> None:
    """Display a success message."""

    print(f"✓ {message}")


def print_warning(message: str) -> None:
    """Display a warning message."""

    print(f"⚠ {message}")


def print_error(message: str) -> None:
    """Display an error message."""

    print(f"✗ {message}")


# =============================================================================
# Dataset Validation
# =============================================================================


def validate_dataset(df: pd.DataFrame) -> bool:
    """
    Validate whether the DataFrame is empty.
    """

    if df.empty:
        print_error("Dataset is empty.")
        return False

    print_success("Dataset validation completed.")
    return True


def check_required_columns(df: pd.DataFrame, required_columns: list) -> bool:
    """
    Check whether all required columns exist.
    """

    missing = [column for column in required_columns if column not in df.columns]

    if missing:

        print_error("Missing Columns:")

        for column in missing:
            print(f"   - {column}")

        return False

    print_success("All required columns are available.")

    return True


# =============================================================================
# Logging
# =============================================================================


def save_log(message: str, log_file: Path) -> None:
    """
    Append messages to project log.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as file:

        file.write(f"[{timestamp}] {message}\n")


# =============================================================================
# Execution Timer
# =============================================================================


def execution_timer(start_time: float) -> None:
    """
    Display execution time.
    """

    elapsed = time.time() - start_time

    print_success(f"Execution Time : {elapsed:.2f} seconds")


# =============================================================================
# Project Banner
# =============================================================================


def project_banner(project_name: str, version: str) -> None:
    """
    Display application banner.
    """

    print("\n" + "=" * 80)

    print(project_name.center(80))

    print(f"Version {version}".center(80))

    print("=" * 80)
