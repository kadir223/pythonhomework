import json
import csv
import os
from abc import ABC, abstractmethod



class TaskStorage(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass



class JSONStorage(TaskStorage):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return [Task(**data) for data in json.load(f)]



class CSVStorage(TaskStorage):
    def __init__(self, filename="tasks.csv"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["task_id", "title", "description", "due_date", "status"])
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date, task.status])

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            return [Task(**row) for row in reader]



class Task:
    def __init__(self, task_id, title, description, due_date=None, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date}, {self.status}"


# Task Manager
class TaskManager:
    def __init__(self, storage: TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def update_task(self, task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title or task.title
                task.description = description or task.description
                task.due_date = due_date or task.due_date
                task.status = status or task.status
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        filtered = [task for task in self.tasks if task.status.lower() == status.lower()]
        if not filtered:
            print("No tasks found with that status.")
        else:
            for task in filtered:
                print(task)

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved successfully!")



if __name__ == "__main__":
    storage_type = input("Choose storage format (json/csv): ").strip().lower()
    storage = JSONStorage() if storage_type == "json" else CSVStorage()
    manager = TaskManager(storage)

    while True:
        print("""
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD, optional): ") or None
            status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
            manager.add_task(Task(task_id, title, description, due_date, status))
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new title (leave blank to keep current): ") or None
            description = input("Enter new description (leave blank to keep current): ") or None
            due_date = input("Enter new due date (leave blank to keep current): ") or None
            status = input("Enter new status (Pending/In Progress/Completed, leave blank to keep current): ") or None
            manager.update_task(task_id, title, description, due_date, status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            manager.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter by (Pending/In Progress/Completed): ")
            manager.filter_tasks(status)
        elif choice == "6":
            manager.save_tasks()
        elif choice == "7":
            manager = TaskManager(storage)
            print("Tasks loaded successfully!")
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
