# 📘 Pandas Mastery Series

## Chapter 03 – loc()

---

## 🎯 Objective

Learn how to retrieve data using **row labels** and **column names** with the `loc()` function.

---

## 📚 Topics Covered

- loc()
- Select one row
- Select one value
- Select multiple rows
- Select multiple columns
- Select rows and columns
- Label slicing
- set_index()
- Access using custom labels

---

## 🧠 Syntax

```python
df.loc[row_label, column_label]
```

---

## Examples

### One Row

```python
df.loc[0]
```

---

### One Value

```python
df.loc[1,"Salary"]
```

---

### Multiple Columns

```python
df.loc[:,["Name","Salary"]]
```

---

### Multiple Rows

```python
df.loc[1:3]
```

---

### Rows and Columns

```python
df.loc[1:3,["Name","Department"]]
```

---

### Label Slicing

```python
df.loc[0:2,"Employee_ID":"Salary"]
```

---

### After set_index()

```python
df2 = df.set_index("Name")

df2.loc["John"]
```

---

## 💡 Memory Trick

``

loc

L = Label

Uses Row Labels
Uses Column Names
``

---

## Difference

| loc | iloc |

|------|-----|
| Label Based | Integer Position Based |
| Uses Names | Uses Numbers |

---

## Real-World Usage

- Employee Database
- Banking
- Sales Reports
- Financial Analysis
- Customer Data
- HR Analytics

---

## Practice Questions

1. Print the second row.
2. Print David's Salary.
3. Print Rose's Department.
4. Print rows 1–4.
5. Print Name and Salary.
6. Print Employee_ID to Salary.
7. Set Name as index.
8. Print Mary's Experience.

---

## Interview Questions

- What is loc()?
- Difference between loc() and iloc()?
- Why use set_index()?
- Does loc() use labels or positions?

---

## Next Chapter

\*_CV_04_iloc_

Learn:

- Integer Position Indexing
- Selecting rows by position
- Selecting columns by position
- Slicing using iloc()

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
