# 📘 Pandas Mastery Series

## Chapter 12 – Data Integration (Merge & Join)

---

## 🎯 Objective

Learn how to combine multiple datasets into a single business-ready dataset using Pandas.

This chapter introduces one of the most important real-world data engineering tasks: **data integration**.

---

## 📂 Input Datasets

``
datasets/

employees_cleaned.csv
departments.csv
cities.csv
projects.csv
``

---

## 📂 Output Dataset

``
output/

employee_database.csv
``

---

## 📚 Topics Covered

- `pd.merge()`
- Left Join
- Inner Join (concept)
- Right Join (concept)
- Outer Join (concept)
- Joining multiple datasets
- Exporting merged data

---

## Merge Operations

### Employees + Departments

```python
pd.merge(employees, departments, on="Department", how="left")
```

---

### Employees + Cities

```python
pd.merge(employees, cities, on="City", how="left")
```

---

### Employees + Projects

```python
pd.merge(employees, projects, on="Employee_ID", how="left")
```

---

## Business Workflow

`Employees
      +
Departments
      +
Cities
      +
Projects
      ↓
Employee Database`

---

## Real-World Applications

- HR Management Systems
- ERP Systems
- CRM Platforms
- Banking Data Integration
- Data Warehousing
- ETL Pipelines

---

## Practice Challenges

1. Perform an **inner join** between Employees and Departments.
2. Try a **right join** with Projects.
3. Perform an **outer join** and observe the results.
4. Count the total number of merged records.
5. Save the merged dataset with a new filename.

---

## Interview Questions

1. What is the purpose of `pd.merge()`?
2. What is the difference between **inner**, **left**, **right**, and **outer** joins?
3. What does the `on` parameter specify?
4. Why is data integration important in analytics projects?

---

## Next Chapter

\*_CV_13_Business_Reporting_

Topics:

- Pivot Tables
- Crosstabs
- Business Reports
- KPI Summaries
- Department-wise Analysis
- Salary Dashboards

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
