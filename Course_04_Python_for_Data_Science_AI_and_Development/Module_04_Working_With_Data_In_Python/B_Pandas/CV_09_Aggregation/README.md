# 📘 Pandas Mastery Series

## Chapter 09 – Aggregation

---

## 🎯 Objective

Learn how to summarize numerical data using Pandas aggregation functions.

Aggregation converts raw data into meaningful statistics for analysis and reporting.

---

## 📚 Topics Covered

- sum()
- mean()
- median()
- min()
- max()
- count()
- std()
- var()
- describe()
- agg()

---

## Dataset

`datasets/employees.csv`

---

## Functions Learned

### Sum

```python
df["Salary"].sum()
```

---

### Mean

```python
df["Salary"].mean()
```

---

### Median

```python
df["Salary"].median()
```

---

### Minimum

```python
df["Salary"].min()
```

---

### Maximum

```python
df["Salary"].max()
```

---

### Count

```python
df["Employee_ID"].count()
```

---

### Standard Deviation

```python
df["Salary"].std()
```

---

### Variance

```python
df["Salary"].var()
```

---

### Describe

```python
df.describe()
```

---

### Multiple Aggregations

```python
df["Salary"].agg([
    "count",
    "sum",
    "mean",
    "median",
    "min",
    "max",
    "std",
    "var"
])
```

---

## 💡 Memory Trick

Aggregation answers questions like:

- How many?
- What is the total?
- What is the average?
- What is the highest?
- What is the lowest?
- How much variation exists?

---

## Real-World Applications

- Sales Reports
- Financial Statements
- Payroll Analysis
- Business Intelligence Dashboards
- Banking Analytics
- Customer Analytics

---

## Practice Questions

1. Calculate the total salary.
2. Find the average experience.
3. Find the highest salary.
4. Find the lowest salary.
5. Count employees.
6. Display summary statistics using `describe()`.
7. Use `agg()` to display multiple statistics.

---

## Interview Questions

- What is aggregation?
- Difference between `mean()` and `median()`?
- What is `describe()`?
- What is `agg()`?
- What is standard deviation?

---

## Next Chapter

\*_CV_10_Handling_Missing_Data_

Topics:

- isnull()
- notnull()
- fillna()
- dropna()
- replace()
- interpolate()

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
