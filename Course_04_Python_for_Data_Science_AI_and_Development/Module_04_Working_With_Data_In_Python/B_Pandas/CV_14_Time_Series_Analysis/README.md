# 📘 Pandas Mastery Series

## Chapter 14 – Time Series Analysis

---

## 🎯 Objective

Learn how to analyze time-based data using Pandas.

This chapter focuses on converting date columns, extracting date components, filtering by time, and creating monthly and yearly reports.

---

## 📂 Input Dataset

`datasets/processed/employee_database.csv`

---

## 📂 Output Reports

``
output/csv/

monthly_joining_report.csv

yearly_joining_report.csv
``

---

## 📚 Topics Covered

- `pd.to_datetime()`
- `.dt.year`
- `.dt.month`
- `.dt.month_name()`
- `.dt.day`
- Date filtering
- Monthly reports
- Yearly reports

---

## Workflow

1. Load employee database.
2. Convert `Join_Date` to datetime.
3. Extract year, month, month name, and day.
4. Generate monthly joining report.
5. Generate yearly joining report.
6. Filter employees by joining date.
7. Export reports to CSV.

---

## Real-World Applications

- HR Hiring Trends
- Employee Joining Analysis
- Monthly Recruitment Reports
- Workforce Planning
- Time-Based Business Intelligence

---

## Practice Challenges

1. Display employees who joined in 2023.
2. Find the month with the highest number of new employees.
3. Sort employees by `Join_Date`.
4. Display the first and last employee to join.
5. Export the filtered 2024 employee list to a CSV file.

---

## Interview Questions

1. Why is `pd.to_datetime()` important?
2. How do you extract the year from a date column?
3. How do you filter rows after a specific date?
4. What are common business uses of time series data?

---

## Next Chapter

\*_CV_15_Employee_Analytics_Project_

Topics:

- End-to-End Employee Analytics
- KPI Dashboard
- Multi-Report Generation
- Professional Portfolio Project

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
