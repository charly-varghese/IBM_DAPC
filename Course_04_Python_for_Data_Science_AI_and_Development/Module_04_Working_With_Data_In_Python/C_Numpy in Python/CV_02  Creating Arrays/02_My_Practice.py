"""
=========================================================
CV_02 – My Practice

Practice creating different types of NumPy arrays
using business-oriented examples.
=========================================================
"""

import numpy as np

print("=" * 60)
print("MY NUMPY PRACTICE")
print("=" * 60)

# Employee IDs
employee_ids = np.arange(1001, 1011)

print("\nEmployee IDs")
print(employee_ids)

# Monthly Profit (Lakhs)
profit = np.array([15, 18, 20, 24, 30, 28])

print("\nMonthly Profit")
print(profit)

# Warehouse Inventory
inventory = np.zeros(8)

print("\nInventory Before Stock Arrival")
print(inventory)

# Machine Status
machine_status = np.ones(6)

print("\nMachine Status")
print(machine_status)

# Customer Ratings
np.random.seed(42)

ratings = np.random.randint(1, 6, 20)

print("\nCustomer Ratings")
print(ratings)

# Daily Orders
orders = np.random.randint(100, 500, 15)

print("\nDaily Orders")
print(orders)

print("\nPractice Completed Successfully.")
S