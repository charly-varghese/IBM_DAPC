# 📘 Pandas Mastery Series

## Chapter 07 – Sorting

---

## 🎯 Objective

Learn how to arrange data in ascending and descending order using Pandas.

Sorting helps organize datasets for reporting, dashboards, and business analysis.

---

## 📚 Topics Covered

- sort_values()
- sort_index()
- Ascending Order
- Descending Order
- Multiple Column Sorting
- Mixed Sorting
- Top Records
- Bottom Records

---

## 🧠 Syntax

### Sort by One Column

```python
df.sort_values(by="Salary")
```

---

### Descending Order

```python
df.sort_values(by="Salary", ascending=False)
```

---

### Multiple Columns

```python
df.sort_values(by=["Department","Salary"])
```

---

### Mixed Sorting

```python
df.sort_values(
    by=["Department","Salary"],
    ascending=[True,False]
)
```

---

### Sort Index

```python
df.sort_index()
```

---

## 💡 Memory Trick

``
sort_values()

Sorts the DATA
``

``
sort_index()

Sorts the ROW NUMBERS
``

---

## Real-World Applications

- Highest salary report
- Lowest sales report
- Employee ranking
- Student merit list
- Product ranking
- Customer segmentation

---

## Practice Questions

1. Sort employees by Name.
2. Sort Salary in descending order.
3. Sort Experience in ascending order.
4. Sort Department then Name.
5. Sort Department ascending and Salary descending.
6. Display the Top 5 highest salaries.
7. Display the Lowest 3 salaries.
8. Sort by index in reverse order.

---

## Interview Questions

- What is `sort_values()`?
- Difference between `sort_values()` and `sort_index()`?
- How do you sort descending?
- How do you sort multiple columns?

---

## Next Chapter

CV_08_GroupBy

Topics:

- groupby()
- mean()
- sum()
- count()
- min()
- max()

---

Author: Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
