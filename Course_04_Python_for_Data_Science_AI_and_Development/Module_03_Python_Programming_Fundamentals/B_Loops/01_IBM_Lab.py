"""
IBM Data Analyst Professional Certificate
Course 04 - Python for Data Science, AI & Development

Module 03 - Python Programming Fundamentals
Lab 02 - Loops

Author : Charly Varghese
"""

# --------------------------------------------------
# Exercise 1
# Print numbers from -5 to 5 using range()
# --------------------------------------------------

print("Exercise 1")

for number in range(-5, 6):
    print(number)

print("-" * 40)


# --------------------------------------------------
# Exercise 2
# Print all genres in the list
# --------------------------------------------------

Genres = ["rock", "R&B", "Soundtrack", "R&B", "soul", "pop"]

print("Exercise 2")

for genre in Genres:
    print(genre)

print("-" * 40)


# --------------------------------------------------
# Exercise 3
# Print all colours in the list
# --------------------------------------------------

squares = ["red", "yellow", "green", "purple", "blue"]

print("Exercise 3")

for colour in squares:
    print(colour)

print("-" * 40)


# --------------------------------------------------
# Exercise 4
# Display playlist ratings using while loop
# Stop when rating becomes less than 6
# --------------------------------------------------

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]

print("Exercise 4")

index = 0

while index < len(PlayListRatings):

    rating = PlayListRatings[index]

    if rating < 6:
        break

    print(rating)

    index += 1

print("-" * 40)


# --------------------------------------------------
# Exercise 5
# Copy only consecutive 'orange' values
# Stop when a different colour is found
# --------------------------------------------------

squares = ["orange", "orange", "purple", "blue", "orange"]
new_squares = []

print("Exercise 5")

index = 0

while index < len(squares):

    if squares[index] != "orange":
        break

    new_squares.append(squares[index])

    index += 1

print("Original List :", squares)
print("New List      :", new_squares)

print("-" * 40)


# --------------------------------------------------
# Exercise 6
# Print numbers from 1 to 15
# Skip multiples of 3
# Stop when number becomes greater than 12
# --------------------------------------------------

print("Exercise 6")

for i in range(1, 16):

    if i % 3 == 0:
        continue

    if i > 12:
        break

    print(i)
