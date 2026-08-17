"""
===============================================================================
Employee Analytics & Business Intelligence System

Charts Module

IBM Data Analyst Professional Certificate (IBM DAPC)

Author : Varghese
Version : 2.0
===============================================================================
"""

import matplotlib.pyplot as plt

from config import CHART_DIR

from utils import (
    print_header,
    print_success,
)

# =============================================================================
# Average Salary by Department
# =============================================================================


def department_salary_chart(df):

    print_header("DEPARTMENT SALARY CHART")

    salary = df.groupby("Department")["Salary"].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))

    plt.bar(salary.index, salary.values)

    plt.title("Average Salary by Department")

    plt.xlabel("Department")

    plt.ylabel("Average Salary")

    plt.xticks(rotation=20)

    plt.tight_layout()

    file = CHART_DIR / "average_salary_by_department.png"

    plt.savefig(file, dpi=300)

    plt.close()

    print_success(file.name)


# =============================================================================
# Employee Distribution by Department
# =============================================================================


def employee_distribution_chart(df):

    print_header("EMPLOYEE DISTRIBUTION")

    distribution = df["Department"].value_counts()

    plt.figure(figsize=(8, 8))

    plt.pie(
        distribution,
        labels=distribution.index,
        autopct="%1.1f%%",
        startangle=90,
    )

    plt.title("Employee Distribution by Department")

    plt.tight_layout()

    file = CHART_DIR / "employee_distribution.png"

    plt.savefig(file, dpi=300)

    plt.close()

    print_success(file.name)


# =============================================================================
# Employee Count by City
# =============================================================================


def city_employee_chart(df):

    print_header("CITY EMPLOYEE COUNT")

    city = df["City"].value_counts()

    plt.figure(figsize=(10, 6))

    plt.bar(city.index, city.values)

    plt.title("Employees by City")

    plt.xlabel("City")

    plt.ylabel("Employee Count")

    plt.xticks(rotation=20)

    plt.tight_layout()

    file = CHART_DIR / "employee_by_city.png"

    plt.savefig(file, dpi=300)

    plt.close()

    print_success(file.name)


# =============================================================================
# Hiring Trend
# =============================================================================


def hiring_trend_chart(df):

    if "Join_Date" not in df.columns:
        return

    print_header("HIRING TREND")

    temp = df.copy()

    temp["Join_Date"] = temp["Join_Date"].astype("datetime64[ns]")

    temp["Year"] = temp["Join_Date"].dt.year

    trend = temp.groupby("Year").size()

    plt.figure(figsize=(10, 5))

    plt.plot(
        trend.index,
        trend.values,
        marker="o",
    )

    plt.title("Hiring Trend")

    plt.xlabel("Year")

    plt.ylabel("Employees")

    plt.grid(True)

    plt.tight_layout()

    file = CHART_DIR / "hiring_trend.png"

    plt.savefig(file, dpi=300)

    plt.close()

    print_success(file.name)


# =============================================================================
# Salary Distribution
# =============================================================================


def salary_distribution_chart(df):

    print_header("SALARY DISTRIBUTION")

    plt.figure(figsize=(10, 6))

    plt.hist(
        df["Salary"],
        bins=10,
    )

    plt.title("Salary Distribution")

    plt.xlabel("Salary")

    plt.ylabel("Frequency")

    plt.tight_layout()

    file = CHART_DIR / "salary_distribution.png"

    plt.savefig(file, dpi=300)

    plt.close()

    print_success(file.name)


# =============================================================================
# Generate All Charts
# =============================================================================


def generate_all_charts(df):

    print_header("GENERATING ALL CHARTS")

    department_salary_chart(df)

    employee_distribution_chart(df)

    city_employee_chart(df)

    hiring_trend_chart(df)

    salary_distribution_chart(df)

    print_success("All charts generated successfully.")
