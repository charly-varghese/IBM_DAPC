# 📘 Pandas Mastery Series

## Chapter 10 – Handling Missing Data

---

## 🎯 Objective

Learn how to identify, analyze, and handle missing values in a Pandas DataFrame.

Handling missing data is a critical step in real-world data cleaning and preprocessing.

---

## 📂 Dataset

`../datasets/employees_missing.csv`

---

## 📚 Topics Covered

- isnull()
- notnull()
- dropna()
- fillna()
- mean()
- median()
- Forward Fill (ffill)
- Backward Fill (bfill)

---

## 🧠 Functions

### Check Missing Values

```python
df.isnull()
```

---

### Count Missing Values

```python
df.isnull().sum()
```

---

### Check Non-Missing Values

```python
df.notnull()
```

---

### Remove Missing Rows

```python
df.dropna()
```

---

### Fill Missing Values

```python
df["Salary"].fillna(mean_salary)
```

---

### Forward Fill

```python
df.fillna(method="ffill")
```

---

### Backward Fill

```python
df.fillna(method="bfill")
```

---

## 💡 When to Use

| Situation | Recommended Method |
| --------- | ------------------ |

| Remove incomplete rows | dropna() |
| Replace numeric values | mean() or median() |
| Replace text values | fillna("Unknown") |
| Continue previous value | ffill |
| Use next available value | bfill |

---

## Real-World Applications

- HR Data Cleaning
- Banking Transactions
- Sales Data Preparation
- Customer Analytics
- Machine Learning Preprocessing
- ETL Pipelines

---

## Practice Questions

1. Count missing values in each column.
2. Remove rows with missing values.
3. Fill missing salaries using the average salary.
4. Fill missing experience using the median.
5. Replace missing departments with "Unknown".
6. Replace missing cities with "Not Available".
7. Apply forward fill.
8. Apply backward fill.

---

## Interview Questions

- What are missing values?
- Difference between `isnull()` and `notnull()`?
- When should you use `dropna()`?
- When is `fillna()` a better choice?
- Why is the median often preferred over the mean for skewed data?

---

## Next Chapter

\*_CV_11_Reading_and_Writing_Files_

Topics:

- read_csv()
- to_csv()
- read_excel()
- to_excel()
- Saving cleaned datasets

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
