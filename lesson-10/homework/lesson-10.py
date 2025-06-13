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
