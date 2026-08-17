# 📘 Pandas Mastery Series

## Chapter 06 – Filtering

---

## 🎯 Objective

Learn how to retrieve rows from a DataFrame based on conditions.

Filtering is one of the most frequently used operations in data analysis.

---

## 📚 Topics Covered

- Boolean Indexing
- Comparison Operators
- Multiple Conditions
- AND (&)
- OR (|)
- NOT (!=)
- isin()
- between()
- String Filtering

---

## 🧠 Syntax

### Greater Than

```python
df[df["Salary"] > 50000]
```

### Less Than

```python
df[df["Salary"] < 50000]
```

### Equal To

```python
df[df["Department"] == "IT"]
```

### Not Equal

```python
df[df["Department"] != "IT"]
```

### AND

```python
df[(df["Department"]=="IT") & (df["Salary"]>60000)]
```

### OR

```python
df[(df["Department"]=="IT") | (df["Department"]=="HR")]
```

### isin()

```python
df[df["Department"].isin(["IT","Sales"])]
```

### between()

```python
df[df["Salary"].between(50000,65000)]
```

### String Filtering

```python
df[df["Name"].str.startswith("J")]
```

---

## 💡 Memory Trick

Filtering is similar to SQL:

```sql
SELECT *
FROM Employee
WHERE Salary > 50000;
```

Equivalent Pandas:

```python
df[df["Salary"] > 50000]
```

---

## Real-World Applications

- Employee Reports
- Customer Segmentation
- Banking Transactions
- Sales Analysis
- Inventory Filtering
- HR Analytics

---

## Practice Questions

1. Employees earning more than 60,000.
2. Employees with less than 3 years experience.
3. Employees in Sales.
4. Employees in HR or Finance.
5. Employees not in IT.
6. Employees whose names begin with M.
7. Salary between 45,000 and 60,000.
8. Employees in IT with more than 3 years experience.

---

## Interview Questions

- What is Boolean Indexing?
- Difference between AND and OR filtering?
- What does `isin()` do?
- What is `between()` used for?
- How do you filter string values?

---

## Next Chapter

CV_07_Sorting

Topics:

- sort_values()
- sort_index()
- Ascending
- Descending
- Multiple Columns

---

Author: Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
