# 📘 Pandas Mastery Series

## Chapter 04 – iloc()

---

## 🎯 Objective

Learn how to retrieve data using **integer row positions** and **integer column positions** with the `iloc()` function.

---

## 📚 Topics Covered

- iloc()
- Select one row
- Select one value
- Select one column
- Select multiple columns
- Select multiple rows
- Select rows and columns
- Row slicing
- Negative indexing
- Position-based selection

---

## 🧠 Syntax

```python
df.iloc[row_position, column_position]
```

---

## Examples

### First Row

```python
df.iloc[0]
```

---

### One Value

```python
df.iloc[1,3]
```

---

### First Column

```python
df.iloc[:,0]
```

---

### Multiple Columns

```python
df.iloc[:,[1,3]]
```

---

### Multiple Rows

```python
df.iloc[1:4]
```

---

### Rows and Columns

```python
df.iloc[1:4,1:4]
```

---

### Last Two Rows

```python
df.iloc[-2:]
```

---

### Specific Rows

```python
df.iloc[[0,2,4]]
```

---

## 💡 Memory Trick

``
iloc

I = Integer Position

Uses Numbers
Never Uses Labels
``

---

## Difference

| loc | iloc |
| --- | ---- |

| Uses Labels | Uses Integer Positions |
| Row Labels | Row Numbers |
| Column Names | Column Numbers |
| End label included in label slicing | End position excluded in slicing |

---

## Real-World Applications

- Dataset sampling
- Selecting records by position
- Data preprocessing
- Machine Learning pipelines
- Exploratory Data Analysis (EDA)

---

## Practice Questions

1. Print the first row.
2. Print the third row.
3. Print the second column.
4. Print rows 2–4.
5. Print rows 1–3 and columns 2–4.
6. Print the last row.
7. Print rows 1, 3 and 5.
8. Print Name and Salary for rows 1, 3 and 5.

---

## Interview Questions

- What is iloc()?
- Difference between loc() and iloc()?
- Can iloc() use column names?
- Does iloc() use integer positions?

---

## Next Chapter

\*_CV_05_Slicing_

Topics:

- Row slicing
- Column slicing
- loc() slicing
- iloc() slicing
- Combined slicing
- Practical exercises

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
