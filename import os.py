import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_index):
        if task_index >= 0 and task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")
        else:
            print("Your to-do list is empty.")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    todo_list = TodoList()

    while True:
        clear_screen()
        print("To-Do List App")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    # Other methods...

    def display_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. Priority: {task.priority}, {task.description}")
        else:
            print("Your to-do list is empty.")

# Usage:
task = Task("Complete project", "High")
todo_list.add_task(task)
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date

# Usage:
task = Task("Complete project", "2024-04-30")
class Task:
    def __init__(self, description, category):
        self.description = description
        self.category = category

# Usage:
task = Task("Buy groceries", "Personal")
