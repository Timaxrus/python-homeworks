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


# 7.

class Node:
    """Node class represents a single node in the linked list"""
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Reference to next node (initially None)

class LinkedList:
    """Linked list implementation with core operations"""
    
    def __init__(self):
        self.head = None  # Head pointer (empty list initially)
    
    def display(self):
        """Display the complete linked list"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty list")
    
    def insert_at_start(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)
        
        if not self.head:  # If list is empty
            self.head = new_node
            return
        
        current = self.head
        while current.next:  # Traverse to last node
            current = current.next
        current.next = new_node
    
    def insert_after(self, target_data, new_data):
        """Insert a new node after a node with specific data"""
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Error: Target data {target_data} not found")
    
    def delete_node(self, data):
        """Delete the first occurrence of a node with specific data"""
        if not self.head:
            print("Error: List is empty")
            return
        
        if self.head.data == data:  # If head needs to be deleted
            self.head = self.head.next
            return
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        print(f"Error: Data {data} not found in list")
    
    def length(self):
        """Return the number of nodes in the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Demonstration
if __name__ == "__main__":
    ll = LinkedList()
    
    print("Initial list:")
    ll.display()  # Empty list
    
    print("\nInserting elements:")
    ll.insert_at_end(10)
    ll.insert_at_start(5)
    ll.insert_at_end(20)
    ll.insert_after(10, 15)
    ll.display()  # 5 -> 10 -> 15 -> 20
    
    print("\nDeleting elements:")
    ll.delete_node(15)
    ll.display()  # 5 -> 10 -> 20
    
    print("\nAttempt invalid operations:")
    ll.delete_node(100)  # Error message
    ll.insert_after(99, 100)  # Error message
    
    print("\nFinal list length:", ll.length())  # 3

# 8.


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Dictionary to store items and their quantities
    
    def add_item(self, item_name, price, quantity=1):
        """Add an item to the cart or update its quantity if already present"""
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}
    
    def remove_item(self, item_name, quantity=1):
        """Remove an item from the cart or reduce its quantity"""
        if item_name not in self.items:
            print(f"Item '{item_name}' not found in cart.")
            return
        
        if self.items[item_name]['quantity'] <= quantity:
            del self.items[item_name]
        else:
            self.items[item_name]['quantity'] -= quantity
    
    def calculate_total(self):
        """Calculate the total price of all items in the cart"""
        return sum(item['price'] * item['quantity'] for item in self.items.values())
    
    def display_cart(self):
        """Display all items in the cart with their details"""
        if not self.items:
            print("Your shopping cart is empty.")
            return
        
        print("\nShopping Cart:")
        print("-" * 30)
        for item_name, details in self.items.items():
            print(f"{item_name}: {details['quantity']} x ${details['price']:.2f} = ${details['price'] * details['quantity']:.2f}")
        print("-" * 30)
        print(f"TOTAL: ${self.calculate_total():.2f}\n")

# Demonstration
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Add items to cart
    cart.add_item("Apple", 0.99, 3)
    cart.add_item("Banana", 0.59, 5)
    cart.add_item("Milk", 3.49)
    cart.add_item("Bread", 2.99)
    
    # Display initial cart
    cart.display_cart()
    
    # Remove some items
    cart.remove_item("Banana", 2)
    cart.remove_item("Milk")
    
    # Try to remove non-existent item
    cart.remove_item("Eggs")
    
    # Display updated cart
    cart.display_cart()


# 9.

class Stack:
    def __init__(self):
        self.items = []  # Using a list to store stack elements
    
    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0
    
    def push(self, item):
        """Push an element onto the stack"""
        self.items.append(item)
        print(f"Pushed: {item}")
    
    def pop(self):
        """Pop an element from the stack"""
        if self.is_empty():
            print("Stack Underflow - Cannot pop from empty stack")
            return None
        item = self.items.pop()
        print(f"Popped: {item}")
        return item
    
    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.items[-1]
    
    def display(self):
        """Display all elements in the stack (top to bottom)"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("\nStack Contents (Top to Bottom):")
        print("-----")
        for item in reversed(self.items):
            print(f"| {item} |")
            print("-----")
    
    def size(self):
        """Return the number of elements in the stack"""
        return len(self.items)

# Demonstration
if __name__ == "__main__":
    stack = Stack()
    
    print("Stack Operations:")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    stack.display()
    
    print("\nTop element:", stack.peek())
    print("Stack size:", stack.size())
    
    stack.pop()
    stack.pop()
    stack.display()
    
    stack.pop()
    stack.pop()  # Attempt to pop from empty stack

# 10.

class Queue:
    def __init__(self):
        self.items = []  # Using a list to store queue elements
    
    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0
    
    def enqueue(self, item):
        """Add an element to the end of the queue"""
        self.items.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):
        """Remove and return the element from the front of the queue"""
        if self.is_empty():
            print("Queue Underflow - Cannot dequeue from empty queue")
            return None
        item = self.items.pop(0)
        print(f"Dequeued: {item}")
        return item
    
    def front(self):
        """Return the front element without removing it"""
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items[0]
    
    def display(self):
        """Display all elements in the queue (front to rear)"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("\nQueue Contents (Front → Rear):")
        print(" ← ".join(map(str, self.items)))
    
    def size(self):
        """Return the number of elements in the queue"""
        return len(self.items)

# Demonstration
if __name__ == "__main__":
    q = Queue()
    
    print("Queue Operations:")
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    q.display()
    
    print("\nFront element:", q.front())
    print("Queue size:", q.size())
    
    q.dequeue()
    q.dequeue()
    q.display()
    
    q.dequeue()
    q.dequeue()  # Attempt to dequeue from empty queue

# 11.

from typing import Dict, List, Optional
import uuid
from datetime import datetime

class BankAccount:
    """Represents a customer's bank account with transaction history."""
    
    def __init__(self, customer_name: str, initial_balance: float = 0.0):
        self.account_id = str(uuid.uuid4())[:8]  # Unique 8-digit ID
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transactions: List[Dict[str, any]] = []
        self._record_transaction("Account Created", initial_balance)

    def _record_transaction(self, description: str, amount: float) -> None:
        """Private method to record transactions."""
        self.transactions.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "description": description,
            "amount": amount,
            "balance": self.balance
        })

    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self._record_transaction("Deposit", amount)
        print(f"✓ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float) -> None:
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record_transaction("Withdrawal", -amount)
        print(f"✓ Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_transaction_history(self) -> List[Dict[str, any]]:
        """Return the transaction history."""
        return self.transactions

    def __str__(self) -> str:
        return f"Account {self.account_id} ({self.customer_name}): Balance ${self.balance:.2f}"


class Bank:
    """Represents a bank with customer account management."""
    
    def __init__(self, name: str):
        self.name = name
        self.accounts: Dict[str, BankAccount] = {}  # account_id → BankAccount

    def create_account(self, customer_name: str, initial_deposit: float = 0.0) -> BankAccount:
        """Create a new bank account."""
        new_account = BankAccount(customer_name, initial_deposit)
        self.accounts[new_account.account_id] = new_account
        print(f"✓ Created account {new_account.account_id} for {customer_name}")
        return new_account

    def get_account(self, account_id: str) -> Optional[BankAccount]:
        """Retrieve an account by ID."""
        return self.accounts.get(account_id)

    def transfer(self, from_account_id: str, to_account_id: str, amount: float) -> None:
        """Transfer money between accounts."""
        from_account = self.accounts.get(from_account_id)
        to_account = self.accounts.get(to_account_id)
        
        if not from_account or not to_account:
            raise ValueError("One or both accounts not found")
        
        if from_account.balance < amount:
            raise ValueError("Insufficient funds for transfer")
        
        from_account.withdraw(amount)
        to_account.deposit(amount)
        print(f"✓ Transferred ${amount:.2f} from {from_account_id} to {to_account_id}")

    def generate_bank_statement(self, account_id: str) -> str:
        """Generate a formatted bank statement."""
        account = self.accounts.get(account_id)
        if not account:
            return "Account not found"
        
        statement = [
            f"\n{' BANK STATEMENT '.center(50, '=')}",
            f"Bank: {self.name}",
            f"Account: {account_id}",
            f"Customer: {account.customer_name}",
            f"Current Balance: ${account.balance:.2f}",
            "\nTRANSACTION HISTORY:",
            f"{'Date':<20} {'Description':<15} {'Amount':>10} {'Balance':>10}"
        ]
        
        for tx in account.transactions:
            statement.append(
                f"{tx['date']:<20} {tx['description']:<15} {tx['amount']:>10.2f} {tx['balance']:>10.2f}"
            )
        
        return "\n".join(statement)


# **Demo Usage**
if __name__ == "__main__":
    # Initialize the bank
    my_bank = Bank("Python Trust Bank")

    # Create accounts
    alice = my_bank.create_account("Alice Smith", 1000.0)
    bob = my_bank.create_account("Bob Johnson", 500.0)

    # Perform transactions
    alice.deposit(200.0)
    bob.withdraw(100.0)
    my_bank.transfer(alice.account_id, bob.account_id, 300.0)

    # Generate a statement
    print(my_bank.generate_bank_statement(alice.account_id))
