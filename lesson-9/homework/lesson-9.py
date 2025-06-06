# 1. Circle Class

# Importing math module to calculate the area and perimeter of a circle.
import math

class Circle:
    # Defining a property radius.
    def __init__(self, radius):
        # Radius should be positive number
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
        
    # Defining a method that calculates the area of the circle
    def area(self):
        return math.pi * self.radius ** 2     # Area = π × r2
        
    # Defining a method that calculates the perimeter af the circle
    def perimeter(self):
        return 2 * math.pi * self.radius      # Perimeter = 2×π × r
        
# Example usage
if __name__ == "__main__":
    try:
        # Create a Circle object with radius 5
        circle = Circle(5)

        # Calculate and display the area and perimeter
        print(f"Area: {circle.area():.2f}")
        print(f"Perimeter: {circle.perimeter():.2f}")
    except ValueError as e:
        print(e)


# 2. 

from datetime import datetime

class Person:
    # Defining a property radius.
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.DOB = DOB
        
    # Defining a method that calculates the area of the circle
    def age(self):
        return math.pi * self.radius ** 2     # Area = π × r2
        
    # Defining a method that calculates the perimeter af the circle
    def perimeter(self):
        return 2 * math.pi * self.radius      # Perimeter = 2×π × r
        
# Example usage
if __name__ == "__main__":
    try:
        # Create a Circle object with radius 5
        circle = Circle(5)

        # Calculate and display the area and perimeter
        print(f"Area: {circle.area():.2f}")
        print(f"Perimeter: {circle.perimeter():.2f}")
    except ValueError as e:
        print(e)
