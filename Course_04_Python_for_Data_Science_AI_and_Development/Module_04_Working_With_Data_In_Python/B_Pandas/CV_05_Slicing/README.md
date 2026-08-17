# 📘 Pandas Mastery Series

## Chapter 05 – Slicing

---

## 🎯 Objective

Learn how to retrieve a range of rows and columns using slicing in Pandas.

---

## 📚 Topics Covered

- Row Slicing
- Column Slicing
- loc() Slicing
- iloc() Slicing
- Combined Slicing
- head()
- tail()
- Step Slicing
- Reverse Slicing

---

## 🧠 Slicing Syntax

### iloc()

```python
df.iloc[row_start:row_end, column_start:column_end]
```

- Uses integer positions.
- End position is **excluded**.

---

### loc()

```python
df.loc[row_label:row_label, column_name:column_name]
```

- Uses labels.
- End label is **included**.

---

## Examples

iloc()

```python
df.iloc[1:4]
```

Returns rows 1, 2 and 3.

---

loc()

```python
df.loc[1:4]
```

Returns rows 1, 2, 3 and 4.

---

### Column Slicing

```python
df.loc[:, "Name":"Salary"]
```

Returns columns from **Name** to **Salary**.

---

### Reverse

```python
df.iloc[::-1]
```

Displays the DataFrame in reverse order.

---

### Every Second Row

```python
df.iloc[::2]
```

Returns alternate rows.

---

## 💡 Memory Trick

``
iloc

0:3

Returns

0
1
2
``

``
loc

0:3

Returns

0
1
2
3
``

---

## Difference

| iloc | loc |
| ---- | --- |

| Integer Positions | Labels |

| End Excluded | End Included|

---

## Real-World Applications

- Extracting subsets of data
- Preparing training datasets
- Exploratory Data Analysis
- Sampling records
- Report generation

---

## Practice Questions

1. Display rows 2–5 using `iloc`.
2. Display rows 2–5 using `loc`.
3. Display Name to Salary columns.
4. Display the first four rows.
5. Display the last two rows.
6. Display alternate rows.
7. Reverse the DataFrame.
8. Display rows 1–4 and columns Name to Department.

---

## Interview Questions

- What is slicing?
- Difference between `loc` slicing and `iloc` slicing?
- Why does `loc` include the last row?
- How do you reverse a DataFrame?

---

## Next Chapter

\*_CV_06_Filtering_

Topics:

- Comparison Operators
- Boolean Indexing
- Multiple Conditions
- `isin()`
- `between()`
- String Filtering

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
