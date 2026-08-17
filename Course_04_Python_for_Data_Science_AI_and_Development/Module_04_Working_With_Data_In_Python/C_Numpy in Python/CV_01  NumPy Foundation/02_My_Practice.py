import numpy as np

# Company monthly profit (₹ Lakhs)
profit = np.array([12, 15, 18, 20, 17, 22])

print("Monthly Profit")
print(profit)

# Dummy inventory
inventory = np.zeros(6)

print("\nInventory")
print(inventory)

# Employee IDs
employee_ids = np.arange(1001, 1007)

print("\nEmployee IDs")
print(employee_ids)

# Random customer ratings
np.random.seed(42)

ratings = np.random.randint(1, 6, 10)

print("\nCustomer Ratings")
print(ratings)
