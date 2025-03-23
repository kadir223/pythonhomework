import math
import json
import csv
import os



class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        elif isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions")
            return sum(a * b for a, b in zip(self.components, other.components))
        else:
            raise TypeError("Unsupported operation")

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(a / mag for a in self.components))


# Employee Management System (OOP)
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee.employee_id},{employee.name},{employee.position},{employee.salary}\n")

    @staticmethod
    def view_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            return "No records found."
        with open(EmployeeManager.FILE_NAME, "r") as file:
            return file.read()


# To-Do Application
class ToDoManager:
    def __init__(self, file_format='json'):
        self.tasks = []
        self.file_format = file_format
        self.file_name = f"tasks.{file_format}"

    def add_task(self, task_id, title, desc, due_date, status):
        self.tasks.append(
            {"Task ID": task_id, "Title": title, "Description": desc, "Due Date": due_date, "Status": status})

    def save_tasks(self):
        if self.file_format == 'json':
            with open(self.file_name, 'w') as file:
                json.dump(self.tasks, file, indent=4)
        elif self.file_format == 'csv':
            with open(self.file_name, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.tasks[0].keys())
                writer.writeheader()
                writer.writerows(self.tasks)

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return "No tasks found."
        if self.file_format == 'json':
            with open(self.file_name, 'r') as file:
                self.tasks = json.load(file)
        elif self.file_format == 'csv':
            with open(self.file_name, 'r') as file:
                reader = csv.DictReader(file)
                self.tasks = list(reader)


# Example Usage
if __name__ == "__main__":
    # Vector Class Example
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    print(v1 + v2)
    print(v1 * v2)
    print(v1.normalize())

    # Employee Manager Example
    emp1 = Employee(1001, "John Doe", "Engineer", 75000)
    EmployeeManager.add_employee(emp1)
    print(EmployeeManager.view_employees())

    # To-Do Manager Example
    todo = ToDoManager("json")
    todo.add_task(101, "Finish Homework", "Math and Science", "2024-12-31", "Pending")
    todo.save_tasks()
    todo.load_tasks()
    print(todo.tasks)
