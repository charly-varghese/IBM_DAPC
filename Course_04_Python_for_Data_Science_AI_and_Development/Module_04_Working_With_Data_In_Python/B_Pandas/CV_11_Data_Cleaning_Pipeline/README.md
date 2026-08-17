# 📘 Pandas Mastery Series

## Chapter 11 – Data Cleaning Pipeline

---

## 🎯 Objective

Build a complete data cleaning pipeline using Pandas.

This chapter combines multiple Pandas concepts into a practical workflow that prepares raw data for analysis.

---

## 📂 Dataset

`../datasets/employees_missing.csv`

---

## 📂 Output

`../output/employees_cleaned.csv`

---

## 📚 Pipeline Steps

1. Load the dataset
2. Explore the dataset
3. Check missing values
4. Clean missing values
5. Validate cleaned data
6. Export cleaned dataset
7. Reload the cleaned dataset
8. Generate a summary report

---

## 🧠 Pandas Functions Used

### Reading Data

```python
pd.read_csv()
```

### Exploring Data

```python
shape
columns
info()
describe()
```

### Missing Values

```python
isnull()
fillna()
```

### Export

```python
to_csv()
```

---

## Cleaning Strategy

| Column | Method |
| ------ | ------ |

| Salary | Mean |
| Experience | Median |
| Department | "Unknown" |
| City | "Not Available" |

---

## Expected Output

- Clean dataset with no missing values.
- `employees_cleaned.csv` created in the common `output` folder.
- Console report showing before/after cleaning statistics.

---

## Real-World Applications

- ETL Pipelines
- HR Data Preparation
- Financial Data Cleaning
- Machine Learning Preprocessing
- Business Intelligence

---

## Practice Challenges

1. Save the cleaned dataset with a different file name.
2. Replace missing departments with `"Unassigned"` instead of `"Unknown"`.
3. Round the average salary to two decimal places before filling.
4. Display only rows that originally contained missing values.
5. Add a timestamp column indicating when the dataset was cleaned.

---

## Interview Questions

1. What is a data cleaning pipeline?
2. Why should data be cleaned before analysis?
3. Why is median often used for missing numeric values?
4. What is the difference between `read_csv()` and `to_csv()`?
5. How do you verify that all missing values have been handled?

---

## Next Chapter

\*_CV_12_Data_Integration_

Topics:

- Merging DataFrames
- Joining DataFrames
- Concatenation
- Keys
- Inner Join
- Left Join
- Right Join
- Outer Join

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
