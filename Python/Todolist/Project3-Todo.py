import os
class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r') as file:
                    self.tasks = [line.strip() for line in file.readlines()]
        except Exception as e:
            print(f"An error occured while loading tasks: {e}")

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as file:
                for task in self.tasks:
                    file.write(task + "\n")
        except Exception as e:
            print(f"An error occured while saving tasks: {e}")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task):
        try:
            self.tasks.remove(task)
            self.save_tasks()
        except ValueError:
            print(f"Task '{task}' not found in the list.")
    
    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to do list")
        else:
            print("To-Do list:")
            for index, task in enumerate(self.tasks, start = 1):
                print(f"{index}. {task}")

if __name__ == "__main__":
    todo_list = ToDoList('tasks.txt')

    while True:
        print("\n Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.display_tasks()
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")