"""
=========================================================
IBM Data Analyst Professional Certificate (IBM DAPC)

Course 04 – Python for Data Science, AI & Development

CV_04 – Array Attributes

File : 01_IBM_Lab.py

Objective:
Understand the important attributes of NumPy arrays.

Author : Charly Varghese
=========================================================
"""

import numpy as np

print("=" * 60)
print("NUMPY ARRAY ATTRIBUTES")
print("=" * 60)

arr = np.array([[10, 20, 30], [40, 50, 60]])

print("\nArray")
print(arr)

print("\nShape")
print(arr.shape)

print("\nDimensions")
print(arr.ndim)

print("\nSize")
print(arr.size)

print("\nData Type")
print(arr.dtype)

print("\nItem Size (Bytes)")
print(arr.itemsize)

print("\nTotal Memory (Bytes)")
print(arr.nbytes)

print("\nConvert Data Type")

new_arr = arr.astype(float)

print(new_arr)
print(new_arr.dtype)

print("\nLab Completed Successfully.")
