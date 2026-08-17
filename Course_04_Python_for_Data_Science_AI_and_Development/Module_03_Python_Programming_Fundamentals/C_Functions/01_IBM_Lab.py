# Question 1

def divide(a, b):
    return a / b

print(divide(20, 5))

# Question 2

def con(a, b):
    return a + b

print(con(2, 3))
print(con("Data", "Analytics"))

# Question 3

def con(a, b):
    return a + b

# Integers
print(con(10, 20))

# Strings
print(con("Hello ", "World"))

# Question 4

text = """Mary had a little lamb
Little lamb, little lamb
Mary had a little lamb.
Its fleece was white as snow
And everywhere that Mary went
Mary went, Mary went
Everywhere that Mary went
The lamb was sure to go"""


def count_little(sentence):
    words = sentence.lower().split()
    return words.count("little")


print("Total count:", count_little(text))