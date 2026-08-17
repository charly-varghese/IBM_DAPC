# 📘 Pandas Mastery Series

## Chapter 02 – Column Selection

---

## 🎯 Objective

Learn how to access, inspect, and understand DataFrame columns using Pandas.

This chapter focuses on selecting one or more columns and understanding the structure of a DataFrame.

---

## 📚 Topics Covered

- Single Column Selection
- Multiple Column Selection
- Series vs DataFrame
- Column Names
- DataFrame Shape
- head()
- tail()
- info()
- dtypes

---

## 📂 Folder Structure

```text
CV_02_Column_Selection/

│
├── 01_My_Practice.py
├── README.md
├── datasets/
└── output/
```

---

## 🧠 Key Concepts

### Single Column

```python
df["Name"]
```

Returns a **Series**.

---

### Single Column as DataFrame

```python
df[["Name"]]
```

Returns a **DataFrame**.

---

### Multiple Columns

```python
df[["Name", "Salary"]]
```

Returns a DataFrame containing only the selected columns.

---

### Column Names

```python
df.columns
```

Displays all column names.

---

### Shape

```python
df.shape
```

Returns:

```text
(rows, columns)
```

Example:

```text
(5, 5)
```

---

### Head

```python
df.head()
```

Displays the first five rows.

---

### Tail

```python
df.tail()
```

Displays the last five rows.

---

### Info

```python
df.info()
```

Displays:

- Number of rows
- Number of columns
- Data types
- Memory usage

---

### dtypes

```python
df.dtypes
```

Displays the data type of every column.

---

## 💼 Real-World Applications

These operations are commonly used in:

- Employee databases
- Banking systems
- Financial reports
- Sales dashboards
- Customer analytics
- Business Intelligence
- Data Engineering

---

## 🎯 Learning Outcome

After completing this chapter you will be able to:

- Select one column
- Select multiple columns
- Understand DataFrame structure
- Inspect datasets
- Identify column data types
- Explore datasets before analysis

---

## 📝 Practice Challenges

Try the following without referring to the solution:

1. Print only the Department column.
2. Print Employee_ID and Name together.
3. Display the first four rows.
4. Display the last three rows.
5. Print only the column names.
6. Find the total number of rows and columns.
7. Check the data type of every column.

---

## 🚀 Next Chapter

CV_03_loc

Topics:

- loc[]
- Label-based indexing
- Selecting rows
- Selecting rows and columns
- Selecting multiple rows
- Practical exercises

---

**Author:** Varghese

\*_IBM Data Analyst Professional Certificate (IBM DAPC)_
