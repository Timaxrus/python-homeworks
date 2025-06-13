# 1. 

from datetime import datetime

class Task:
    """
    A class representing a single task in the ToDo list.
    Attributes include title, description, due date, and status.
    """
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        # Validate that the due_date is in the future
        if not self._is_future_date(due_date):
            raise ValueError("Due date must be in the future.")
        self.due_date = due_date  # Expected format: YYYY-MM-DD
        self.status = "Incomplete"  # Default status

    def _is_future_date(self, date_str):
        """Helper method to check if a date is in the future."""
        try:
            due_date = datetime.strptime(date_str, "%Y-%m-%d").date()
            return due_date > datetime.now().date()
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

    def mark_complete(self):
        """Marks the task as complete."""
        self.status = "Complete"

    def __str__(self):
        """Returns a string representation of the task."""
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}\n")


class ToDoList:
    """
    A class to manage a list of tasks.
    Includes methods to add tasks, mark tasks as complete, list all tasks,
    and display incomplete tasks.
    """
    def __init__(self):
        self.tasks = []  # List to store Task objects

    def add_task(self, task):
        """Adds a new task to the ToDo list."""
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully.")

    def mark_task_complete(self, title):
        """
        Marks a task as complete by its title.
        If the task is not found, prints an error message.
        """
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{task.title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        """Lists all tasks in the list."""
        if not self.tasks:
            print("No tasks available.")
            return
        print("All Tasks:")
        for task in self.tasks:
            print("-" * 40)
            print(task)

    def display_incomplete_tasks(self):
        """Displays only the incomplete tasks."""
        incomplete_tasks = [task for task in self.tasks if task.status == "Incomplete"]
        if not incomplete_tasks:
            print("No incomplete tasks available.")
            return
        print("Incomplete Tasks:")
        for task in incomplete_tasks:
            print("-" * 40)
            print(task)


def main():
    """
    Main program to interact with the ToDoList through a CLI.
    """
    todo_list = ToDoList()

    while True:
        print("\n--- ToDo List Application ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Task
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task = Task(title, description, due_date)
                todo_list.add_task(task)
            except ValueError as e:
                print(e)

        elif choice == "2":
            # Mark Task as Complete
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)

        elif choice == "3":
            # List All Tasks
            todo_list.list_all_tasks()

        elif choice == "4":
            # Display Incomplete Tasks
            todo_list.display_incomplete_tasks()

        elif choice == "5":
            # Exit
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# 2.

class Post:
    """
    A class representing a single blog post.
    Attributes include title, content, and author.
    """
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        """Returns a string representation of the post."""
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content: {self.content}\n")


class Blog:
    """
    A class to manage a list of blog posts.
    Includes methods to add, delete, edit, and display posts.
    """
    def __init__(self):
        self.posts = []  # List to store Post objects

    def add_post(self, post):
        """Adds a new post to the blog."""
        self.posts.append(post)
        print(f"Post '{post.title}' added successfully.")

    def list_all_posts(self):
        """Lists all posts in the blog."""
        if not self.posts:
            print("No posts available.")
            return
        print("All Posts:")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}. {post}")

    def display_posts_by_author(self, author):
        """Displays posts written by a specific author."""
        author_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        if not author_posts:
            print(f"No posts found by author '{author}'.")
            return
        print(f"Posts by {author}:")
        for post in author_posts:
            print("-" * 40)
            print(post)

    def delete_post(self, title):
        """
        Deletes a post by its title.
        If the post is not found, prints an error message.
        """
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{post.title}' deleted successfully.")
                return
        print(f"Post '{title}' not found.")

    def edit_post(self, title, new_content):
        """
        Edits the content of a post by its title.
        If the post is not found, prints an error message.
        """
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.content = new_content
                print(f"Post '{post.title}' updated successfully.")
                return
        print(f"Post '{title}' not found.")

    def display_latest_posts(self, count=3):
        """Displays the latest 'count' posts."""
        if not self.posts:
            print("No posts available.")
            return
        print(f"Latest {count} Posts:")
        for post in self.posts[-count:]:
            print("-" * 40)
            print(post)


def main():
    """
    Main program to interact with the Blog system through a CLI.
    """
    blog = Blog()

    while True:
        print("\n--- Simple Blog System ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Post
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter post author: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            # List All Posts
            blog.list_all_posts()

        elif choice == "3":
            # Display Posts by Author
            author = input("Enter the author's name: ")
            blog.display_posts_by_author(author)

        elif choice == "4":
            # Delete Post
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            # Edit Post
            title = input("Enter the title of the post to edit: ")
            new_content = input("Enter the new content: ")
            blog.edit_post(title, new_content)

        elif choice == "6":
            # Display Latest Posts
            try:
                count = int(input("How many latest posts would you like to see? "))
                blog.display_latest_posts(count)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "7":
            # Exit
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


# 3.

class Account:
    """
    A class representing a bank account.
    Attributes include account number, account holder name, and balance.
    """
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def transfer(self, amount, target_account):
        """Transfers money to another account."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                target_account.deposit(amount)
                print(f"Transferred ${amount:.2f} to account {target_account.account_number}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid transfer amount.")

    def display_details(self):
        """Displays account details."""
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder_name}\n"
                f"Balance: ${self.balance:.2f}")


class Bank:
    """
    A class to manage a list of bank accounts.
    Includes methods to add accounts, check balance, deposit, withdraw, and transfer money.
    """
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts by account number

    def add_account(self, account):
        """Adds a new account to the bank."""
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} added successfully.")

    def get_account(self, account_number):
        """Retrieves an account by its account number."""
        return self.accounts.get(account_number)

    def check_balance(self, account_number):
        """Checks the balance of an account."""
        account = self.get_account(account_number)
        if account:
            print(f"Balance for account {account_number}: ${account.balance:.2f}")
        else:
            print(f"Account {account_number} not found.")

    def deposit_money(self, account_number, amount):
        """Deposits money into an account."""
        account = self.get_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(f"Account {account_number} not found.")

    def withdraw_money(self, account_number, amount):
        """Withdraws money from an account."""
        account = self.get_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(f"Account {account_number} not found.")

    def transfer_money(self, from_account_number, to_account_number, amount):
        """Transfers money between two accounts."""
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account and to_account:
            from_account.transfer(amount, to_account)
        else:
            print("One or both accounts not found.")

    def display_account_details(self, account_number):
        """Displays details of an account."""
        account = self.get_account(account_number)
        if account:
            print(account.display_details())
        else:
            print(f"Account {account_number} not found.")


def main():
    """
    Main program to interact with the Banking system through a CLI.
    """
    bank = Bank()

    while True:
        print("\n--- Simple Banking System ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Account
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            account = Account(account_number, account_holder_name, initial_balance)
            bank.add_account(account)

        elif choice == "2":
            # Check Balance
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)

        elif choice == "3":
            # Deposit Money
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit_money(account_number, amount)

        elif choice == "4":
            # Withdraw Money
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw_money(account_number, amount)

        elif choice == "5":
            # Transfer Money
            from_account_number = input("Enter source account number: ")
            to_account_number = input("Enter target account number: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer_money(from_account_number, to_account_number, amount)

        elif choice == "6":
            # Display Account Details
            account_number = input("Enter account number: ")
            bank.display_account_details(account_number)

        elif choice == "7":
            # Exit
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
