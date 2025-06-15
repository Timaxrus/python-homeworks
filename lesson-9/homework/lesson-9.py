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
    # Defining a properties of class Person
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.DOB = datetime.strptime(DOB, '%Y-%m-%d').date()
        
    # Defining a method that calculates the age of Class
    def age(self):
        today = datetime.today().date()
        age = today.year - self.DOB.year    # Current year - year of birth
        if (today.month, today.day) < (self.DOB.month, self.DOB.day):
            age -= 1
        return age
    
    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.DOB}"
        
        
# Example usage
if __name__ == "__main__":
    try:
        # Create an object person
        person = Person("John", "USA", "1981-01-01")

        # Calculate and display age of person
        print(person.age())
    except ValueError as e:
        print(e)

# 3.

class Calculator:
    # Adding methods for basic arithmetic operations
    # such as addition, subtraction, multiplication, and division.
    def add(self, a, b):
        return a + b
        
    def substract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        # Check if b is zero to avoid division by zero error
        if b == 0:
            # Raise an error if division by zero is attempted
            raise ValueError("Cannot divide by zero.")
        return a / b
        
        
# Example usage
if __name__ == "__main__":
   calc = Calculator()
   
   print("Addition: ", calc.add(10, 5))
   print("Substraction: ", calc.substract(10, 4))
   print("Multiplication: ", calc.multiply(5, 2))
   print("Division: ", calc.divide(10, 0))


# 4.

import math
# Defining a base class Shape

class Shape:
    def __init__ (self, name):
        self.name = name
    # Defining a method that calculates the area of the shape
    def area(self):
        # This method should be implemented by subclasses
        raise NotImplementedError("Subclasses must implement this method")
    
    # Defining a method that calculates the perimeter of the shape
    def perimeter(self):
        # This method should be implemented by subclasses
        raise NotImplementedError("Subclasses must implement this method")
    
class Square(Shape):
    # Defining a properties of class Square
    def __init__ (self, name, side_length):
        # Call the parent class constructor
        super().__init__(name)
        # Width and height should be positive numbers
        self.side_length = side_length

    # Defining a method that calculates the area of the square  
    def area(self):
        # Check if side_length is a positive number
        if self.side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        
        return self.side_length ** 2     # Area = side_length^2

    # Defining a method that calculates the perimeter of the square
    def perimeter(self):
        # Check if side_length is a positive number
        if self.side_length <= 0:
            raise ValueError("Side length must be a positive number.")
        
        return 4 * self.side_length     # Perimeter = 4 * side_length
    
class Circle(Shape):
    # Defining a properties of class Circle
    def __init__ (self, name, radius):
        # Call the parent class constructor
        super().__init__(name)
        # Radius should be a positive number
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
        
    # Defining a method that calculates the area of the circle
    def area(self):
        return math.pi * self.radius ** 2     # Area = π × r2
        
    # Defining a method that calculates the perimeter of the circle
    def perimeter(self):
        return 2 * math.pi * self.radius      # Perimeter = 2×π × r
    

class Triangle(Shape):
    # Defining a properties of class Triangle
    def __init__ (self, name, base, height):
        # Call the parent class constructor
        super().__init__(name)
        # Base and height should be positive numbers
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height
        
    # Defining a method that calculates the area of the triangle
    def area(self):
        return 0.5 * self.base * self.height     # Area = 1/2 * base * height
    
    # Defining a method that calculates the perimeter of the triangle
    def perimeter(self):
        return self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.height ** 2)  # Perimeter = base + 2 * side_length
    

# Example usage
if __name__ == "__main__":
    try:
        # Create a Square object with side length 4
        square = Square("Square", 4)
        print(f"{square.name} - Area: {square.area()}, Perimeter: {square.perimeter()}")

        # Create a Circle object with radius 3
        circle = Circle("Circle", 3)
        print(f"{circle.name} - Area: {circle.area()}, Perimeter: {circle.perimeter()}")

        # Create a Triangle object with base 5 and height 3
        triangle = Triangle("Triangle", 5, 3)
        print(f"{triangle.name} - Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")
        
    except ValueError as e:
        print(e)



# 5.

class Node:
    """
    A class representing a single node in the binary search tree.
    Each node contains a value, a left child, and a right child.
    """
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.left = None    # Pointer to the left child (smaller values)
        self.right = None   # Pointer to the right child (larger values)


class BinarySearchTree:
    """
    A class representing a binary search tree (BST).
    Includes methods for inserting and searching for elements.
    """
    def __init__(self):
        self.root = None  # The root node of the BST

    def insert(self, value):
        """
        Inserts a new value into the binary search tree.
        
        Args:
            value: The value to be inserted.
        """
        if self.root is None:
            # If the tree is empty, create a new root node
            self.root = Node(value)
        else:
            # Otherwise, call the helper function to find the correct position
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        """
        Recursively finds the correct position to insert a value in the BST.
        
        Args:
            current_node: The current node being checked.
            value: The value to be inserted.
        """
        if value < current_node.value:
            # If the value is smaller, go to the left subtree
            if current_node.left is None:
                current_node.left = Node(value)  # Insert as the left child
            else:
                self._insert_recursive(current_node.left, value)  # Continue recursion
        elif value > current_node.value:
            # If the value is larger, go to the right subtree
            if current_node.right is None:
                current_node.right = Node(value)  # Insert as the right child
            else:
                self._insert_recursive(current_node.right, value)  # Continue recursion
        # If the value is equal to the current node's value, do nothing (no duplicates allowed)

    def search(self, value):
        """
        Searches for a value in the binary search tree.
        
        Args:
            value: The value to search for.
        
        Returns:
            bool: True if the value is found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        """
        Recursively searches for a value in the BST.
        
        Args:
            current_node: The current node being checked.
            value: The value to search for.
        
        Returns:
            bool: True if the value is found, False otherwise.
        """
        if current_node is None:
            # If we reach a None node, the value is not in the tree
            return False
        if value == current_node.value:
            # If the value matches the current node's value, it is found
            return True
        elif value < current_node.value:
            # If the value is smaller, search in the left subtree
            return self._search_recursive(current_node.left, value)
        else:
            # If the value is larger, search in the right subtree
            return self._search_recursive(current_node.right, value)

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the binary search tree.
        
        Returns:
            list: A list of values in ascending order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        """
        Recursively performs an in-order traversal of the BST.
        
        Args:
            current_node: The current node being visited.
            result: The list to store the traversal results.
        """
        if current_node is not None:
            self._inorder_recursive(current_node.left, result)  # Visit left subtree
            result.append(current_node.value)                  # Visit current node
            self._inorder_recursive(current_node.right, result)  # Visit right subtree


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()

    # Insert elements into the BST
    elements = [10, 5, 15, 3, 7, 12, 18]
    for element in elements:
        bst.insert(element)

    # Perform an in-order traversal to display the tree contents
    print("In-order traversal:", bst.inorder_traversal())

    # Search for elements in the BST
    search_values = [7, 20, 15, 1]
    for value in search_values:
        print(f"Search for {value}: {'Found' if bst.search(value) else 'Not Found'}")

# 6.

class Stack:
    """
    A class representing a stack data structure.
    Includes methods for pushing, popping, and checking if the stack is empty.
    """
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.items = []  # List to store stack elements

    def push(self, item):
        """
        Push an item onto the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        """
        Pop an item from the stack.

        Returns:
            The top item of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop from an empty stack.")
        popped_item = self.items.pop()
        print(f"Popped: {popped_item}")
        return popped_item

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def peek(self):
        """
        Peek at the top item of the stack without removing it.

        Returns:
            The top item of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek into an empty stack.")
        return self.items[-1]

    def size(self):
        """
        Get the number of items in the stack.

        Returns:
            int: The size of the stack.
        """
        return len(self.items)

    def __str__(self):
        """
        Return a string representation of the stack.
        """
        return f"Stack({self.items})"


# Example usage
if __name__ == "__main__":
    stack = Stack()  # Create a new stack

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)

    # Print the stack
    print(f"Current stack: {stack}")

    # Peek at the top element
    print(f"Top element: {stack.peek()}")

    # Pop elements from the stack
    stack.pop()
    stack.pop()

    # Check if the stack is empty
    print(f"Is the stack empty? {stack.is_empty()}")

    # Get the size of the stack
    print(f"Size of the stack: {stack.size()}")

    # Print the final state of the stack
    print(f"Final stack: {stack}")


