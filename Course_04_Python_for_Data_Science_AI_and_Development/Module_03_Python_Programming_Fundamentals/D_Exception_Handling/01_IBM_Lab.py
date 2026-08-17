"""
IBM Data Analyst Professional Certificate
Course 04 - Python for Data Science, AI & Development

Module 03 - Python Programming Fundamentals
Lab 04 - Exception Handling

Exercise 1
"""

# ----------------------------------------
# Exercise 1
# Handling ZeroDivisionError
# ----------------------------------------

#def safe_divide(numerator, denominator):
 #   try:
 #       result = numerator / denominator
 #       return result

 #   except ZeroDivisionError:
 #       print("Error: Cannot divide by zero.")
 #       return None


# Test Case

#numerator = int(input("20 : "))
#denominator = int(input("0 : "))

# print("Result :", safe_divide(numerator, denominator))

"""
IBM Data Analyst Professional Certificate
Course 04 - Python for Data Science, AI & Development

Module 03 - Python Programming Fundamentals
Lab 04 - Exception Handling

Exercise 2
"""

#import math

# ----------------------------------------
# Exercise 2
# Handling ValueError
# ----------------------------------------

# def perform_calculation(number1):
 #   try:
#        result = math.sqrt(number1)
#        print("Result :", result)

#    except ValueError:
#         print ("Error: Invalid input! Please enter a positive integer or a float value.")


# Test Case

#number1 = float(input(" 25 : "))

#perform_calculation(number1)

"""
Module 03 - Python Programming Fundamentals
Lab 04 - Exception Handling
Exercise 3
"""

# ----------------------------------------
# Exercise 3
# Handling Generic Exceptions
# ----------------------------------------

def complex_calculation(num):
    try:
        result = num / (num - 5)
        print("Result :", result)

    except Exception as e:
        print("An error occurred during calculation.")


# Test Case

user_input = float(input("Enter a number : "))

complex_calculation(user_input)