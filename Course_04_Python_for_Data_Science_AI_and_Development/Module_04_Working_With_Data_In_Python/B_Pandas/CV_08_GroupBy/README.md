# 📘 Pandas Mastery Series

## Chapter 08 – GroupBy

---

## 🎯 Objective

Learn how to group data and generate summaries using Pandas `groupby()`.

This is one of the most important functions in Data Analytics.

---

## 📚 Topics Covered

- groupby()
- count()
- mean()
- sum()
- min()
- max()
- agg()
- get_group()
- Group Iteration

---

## 🧠 Syntax

### Create Groups

```python
group = df.groupby("Department")
```

---

### Count

```python
group["Name"].count()
```

---

### Mean

```python
group["Salary"].mean()
```

---

### Sum

```python
group["Salary"].sum()
```

---

### Maximum

```python
group["Salary"].max()
```

---

### Minimum

```python
group["Salary"].min()
```

---

### Multiple Statistics

```python
group["Salary"].agg(
    ["count","sum","mean","min","max"]
)
```

---

### Display One Group

```python
group.get_group("Finance")
```

---

## 💡 Memory Trick

``
groupby()

Split

↓

Apply

↓

Combine
``

1. Split data into groups.
2. Apply calculations.
3. Combine results.

---

## SQL Comparison

SQL

```sql
SELECT Department,
AVG(Salary)
FROM Employee
GROUP BY Department;
```

Pandas

```python
df.groupby("Department")["Salary"].mean()
```

---

## Real-World Applications

- Department salary reports
- Monthly sales reports
- Customer segmentation
- Banking analytics
- Inventory summaries
- Business Intelligence dashboards

---

## Practice Questions

1. Count employees in each department.
2. Average salary by department.
3. Maximum salary by department.
4. Minimum salary by department.
5. Total salary by department.
6. Average experience by department.
7. Display only IT employees.
8. Create a report using multiple aggregations.

---

## Interview Questions

- What is `groupby()`?
- Explain Split-Apply-Combine.
- Difference between SQL `GROUP BY` and Pandas `groupby()`.
- What is `agg()`?
- How do you display a single group?

---

## Next Chapter

CV_09_Aggregation

Topics:

- sum()
- mean()
- median()
- mode()
- std()
- var()
- describe()

---

**Author:** Varghese

IBM Data Analyst Professional Certificate (IBM DAPC)
