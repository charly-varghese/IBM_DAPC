"""
=====================================================
IBM DAPC
Course 04 - Python for Data Science, AI & Development

Module 04
Lab 01 - Reading Files with open()

Author : Varghese
=====================================================
"""

# ---------------------------------------------------
# Import Libraries
# ---------------------------------------------------

from pathlib import Path

# ---------------------------------------------------
# File Path
# ---------------------------------------------------

file_path = Path("datasets/example1.txt")

# ---------------------------------------------------
# Open File
# ---------------------------------------------------

file1 = open(file_path, "r")

print("=" * 50)
print("FILE INFORMATION")
print("=" * 50)

print("File Name :", file1.name)
print("Mode      :", file1.mode)

print()

# ---------------------------------------------------
# Read Entire File
# ---------------------------------------------------

file_content = file1.read()

print("=" * 50)
print("FILE CONTENT")
print("=" * 50)

print(file_content)

print()

print("Data Type :", type(file_content))

print()

# ---------------------------------------------------
# Close File
# ---------------------------------------------------

file1.close()

print("File Closed :", file1.closed)
