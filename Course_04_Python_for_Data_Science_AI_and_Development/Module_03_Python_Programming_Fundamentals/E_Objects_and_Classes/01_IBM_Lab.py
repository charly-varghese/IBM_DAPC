"""
IBM Data Analyst Professional Certificate
Course 04 - Python for Data Science, AI & Development

Module 03 - Python Programming Fundamentals
Lab 05 - Objects and Classes

Author : Charly Varghese
"""

# --------------------------------------------------
# Import Library
# --------------------------------------------------

import matplotlib.pyplot as plt 


# ==================================================
# Circle Class
# ==================================================

class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

    # Method
    def drawCircle(self):
        plt.gca().add_patch(
            plt.Circle((0, 0), radius=self.radius, fc=self.color)
        )
        plt.axis('scaled')
        plt.show()


# ==================================================
# Create Red Circle
# ==================================================

print("\nCreating RedCircle...")

RedCircle = Circle(10, "red")

print("Radius :", RedCircle.radius)
print("Color  :", RedCircle.color)

print("\nAvailable Methods:")
print(dir(RedCircle))

# Change radius

RedCircle.radius = 1

print("\nUpdated Radius :", RedCircle.radius)

print("\nDrawing Red Circle...")
RedCircle.drawCircle()

print("\nIncreasing Radius")

print("Radius :", RedCircle.radius)

RedCircle.add_radius(2)

print("After add_radius(2) :", RedCircle.radius)

RedCircle.add_radius(5)

print("After add_radius(5) :", RedCircle.radius)

print("\nDrawing Updated Red Circle...")
RedCircle.drawCircle()

# ==================================================
# Blue Circle
# ==================================================

print("\nCreating BlueCircle...")

BlueCircle = Circle(radius=100)

print("Radius :", BlueCircle.radius)
print("Color  :", BlueCircle.color)

print("\nDrawing Blue Circle...")
BlueCircle.drawCircle()

# ==================================================
# Rectangle Class
# ==================================================

class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(
            plt.Rectangle(
                (0, 0),
                self.width,
                self.height,
                fc=self.color
            )
        )

        plt.axis('scaled')
        plt.show()


# ==================================================
# Skinny Blue Rectangle
# ==================================================

print("\nCreating SkinnyBlueRectangle...")

SkinnyBlueRectangle = Rectangle(2, 3, "blue")

print("Height :", SkinnyBlueRectangle.height)
print("Width  :", SkinnyBlueRectangle.width)
print("Color  :", SkinnyBlueRectangle.color)

print("\nDrawing Skinny Blue Rectangle...")
SkinnyBlueRectangle.drawRectangle()

# ==================================================
# Fat Yellow Rectangle
# ==================================================

print("\nCreating FatYellowRectangle...")

FatYellowRectangle = Rectangle(20, 5, "yellow")

print("Height :", FatYellowRectangle.height)
print("Width  :", FatYellowRectangle.width)
print("Color  :", FatYellowRectangle.color)

print("\nDrawing Fat Yellow Rectangle...")
FatYellowRectangle.drawRectangle()

# ==================================================
# Vehicle Class Scenario
# ==================================================

print("\nVehicle Class Scenario")


class Vehicle:

    # Constructor
    def __init__(self, max_speed, mileage, color="White"):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        self.seating_capacity = None

    # Method
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    # Method
    def display_properties(self):
        print("-" * 40)
        print("Maximum Speed    :", self.max_speed)
        print("Mileage          :", self.mileage)
        print("Color            :", self.color)
        print("Seating Capacity :", self.seating_capacity)


# --------------------------------------------------
# Task 1
# --------------------------------------------------

print("\nTask 1")

vehicle = Vehicle(180, 20)

print(vehicle.max_speed)
print(vehicle.mileage)

# --------------------------------------------------
# Task 2
# --------------------------------------------------

print("\nTask 2")

print("Default Color :", vehicle.color)

# --------------------------------------------------
# Task 3
# --------------------------------------------------

print("\nTask 3")

vehicle.assign_seating_capacity(5)

print("Seating Capacity :", vehicle.seating_capacity)

# --------------------------------------------------
# Task 4
# --------------------------------------------------

print("\nTask 4")

vehicle.display_properties()

# --------------------------------------------------
# Task 5
# --------------------------------------------------

print("\nTask 5")

Vehicle1 = Vehicle(200, 20)

Vehicle1.assign_seating_capacity(5)

Vehicle2 = Vehicle(180, 25)

Vehicle2.assign_seating_capacity(4)

Vehicle1.display_properties()

Vehicle2.display_properties()