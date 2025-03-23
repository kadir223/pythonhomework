import os


class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w") as f:
                pass

    def add_employee(self, employee):
        if self.search_employee(employee.employee_id):
            print("Error: Employee ID already exists.")
            return
        with open(self.FILE_NAME, "a") as f:
            f.write(str(employee) + "\n")
        print("Employee added successfully!")

    def view_all_employees(self):
        with open(self.FILE_NAME, "r") as f:
            records = f.readlines()
        if not records:
            print("No employee records found.")
        else:
            print("Employee Records:")
            for record in records:
                print(record.strip())

    def search_employee(self, employee_id):
        with open(self.FILE_NAME, "r") as f:
            for line in f:
                if line.startswith(employee_id + ","):
                    return line.strip()
        return None

    def update_employee(self, employee_id, new_name=None, new_position=None, new_salary=None):
        updated = False
        with open(self.FILE_NAME, "r") as f:
            records = f.readlines()
        with open(self.FILE_NAME, "w") as f:
            for line in records:
                if line.startswith(employee_id + ","):
                    parts = line.strip().split(", ")
                    name = new_name if new_name else parts[1]
                    position = new_position if new_position else parts[2]
                    salary = new_salary if new_salary else parts[3]
                    f.write(f"{employee_id}, {name}, {position}, {salary}\n")
                    updated = True
                else:
                    f.write(line)
        print("Employee updated successfully!" if updated else "Employee not found.")

    def delete_employee(self, employee_id):
        deleted = False
        with open(self.FILE_NAME, "r") as f:
            records = f.readlines()
        with open(self.FILE_NAME, "w") as f:
            for line in records:
                if line.startswith(employee_id + ","):
                    deleted = True
                    continue
                f.write(line)
        print("Employee deleted successfully!" if deleted else "Employee not found.")

    def menu(self):
        while True:
            print("""
Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit

Enter your choice: """, end="")
            choice = input().strip()

            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter Salary: ")
                self.add_employee(Employee(employee_id, name, position, salary))
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                employee_id = input("Enter Employee ID to search: ")
                record = self.search_employee(employee_id)
                print("Employee Found:\n" + record if record else "Employee not found.")
            elif choice == "4":
                employee_id = input("Enter Employee ID to update: ")
                new_name = input("Enter new name (leave blank to keep current): ") or None
                new_position = input("Enter new position (leave blank to keep current): ") or None
                new_salary = input("Enter new salary (leave blank to keep current): ") or None
                self.update_employee(employee_id, new_name, new_position, new_salary)
            elif choice == "5":
                employee_id = input("Enter Employee ID to delete: ")
                self.delete_employee(employee_id)
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    manager = EmployeeManager()
    manager.menu()
