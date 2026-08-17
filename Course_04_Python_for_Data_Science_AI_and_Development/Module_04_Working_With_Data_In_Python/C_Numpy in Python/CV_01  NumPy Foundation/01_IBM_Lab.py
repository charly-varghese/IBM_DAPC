"""
=================================================
IBM DAPC
Course 04 – Python for Data Science, AI & Development

CV_01 – NumPy Foundation
01_IBM_Lab.py
=================================================
"""

# Import NumPy
import numpy as np

# Create a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("Array:")
print(numbers)

print("\nType:")
print(type(numbers))

np.random.seed(10)
sales = np.random.randint(100, 500, 10)
print(sales)