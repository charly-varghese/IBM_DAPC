# 📘 Pandas Mastery Series

## Chapter 01 – DataFrame vs Series

---

## 🎯 Objective

Understand the two fundamental Pandas data structures:

- DataFrame
- Series

This chapter builds the foundation required for learning all advanced Pandas topics.

---

## 📚 Topics Covered

- Import Pandas
- Python Dictionary
- Create DataFrame
- Print DataFrame
- Check Data Type
- Select One Column
- Series
- DataFrame
- Single Bracket []
- Double Bracket [[]]
- Multiple Column Selection
- shape
- columns

---

## 📂 Files

```text
CV_01_DataFrame_vs_Series/

│
├── 01_My_Practice.py
├── README.md
├── datasets/
└── output/
```

---

## 🧠 Important Concepts

## DataFrame

A DataFrame is a two-dimensional table consisting of rows and columns.

Example:

| Name | Age | Department |
| ---- | --: | ---------- |

| Rose | 25 | Finance |

| John | 30 | IT |

---

## Series

A Series is a single column extracted from a DataFrame.

Example:

| Name  |
| ----- |
| Rose  |
| John  |
| James |

---

## ⭐ Memory Trick

`DataFrame
│
├── Name
├── Age
├── Department
└── Salary`

Each column is a **Series**.

---

## 📌 Rules

| Code | Returns |

|------|---------|
| df | DataFrame |
| df["Name"] | Series |
| df[["Name"]] | DataFrame |
| df[["Name","Salary"]] | DataFrame |

---

## 💼 Real-World Use Cases

- Employee Data
- Student Records
- Sales Reports
- Financial Data
- Banking
- Data Analytics
- Machine Learning

---

## 🎯 Learning Outcome

After completing this chapter you should be able to:

- Understand DataFrame
- Understand Series
- Select single columns
- Select multiple columns
- Differentiate between [] and [[]]

---

## 🚀 Next Chapter

CV_02_Column_Selection

Learn:

- Selecting one column
- Selecting multiple columns
- Column properties
- Practical exercises

---

**Author:** Varghese

\*_IBM Data Analyst Professional Certificate (IBM DAPC)_
