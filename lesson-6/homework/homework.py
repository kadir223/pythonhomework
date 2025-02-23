import os
import collections
import string

def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# ================== Employee Records Manager ==================
class EmployeeManager:
    FILE_NAME = "employees.txt"

    @staticmethod
    def add_employee(employee_id, name, position, salary):
        with open(EmployeeManager.FILE_NAME, "a") as file:
            file.write(f"{employee_id},{name},{position},{salary}\n")

    @staticmethod
    def view_employees():
        if not os.path.exists(EmployeeManager.FILE_NAME):
            print("No records found.")
            return
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                print(line.strip())

    @staticmethod
    def search_employee(employee_id):
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(str(employee_id) + ","):
                    print(line.strip())
                    return
        print("Employee not found.")

    @staticmethod
    def update_employee(employee_id, name=None, position=None, salary=None):
        updated = False
        employees = []
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                emp_data = line.strip().split(",")
                if emp_data[0] == str(employee_id):
                    if name:
                        emp_data[1] = name
                    if position:
                        emp_data[2] = position
                    if salary:
                        emp_data[3] = str(salary)
                    updated = True
                employees.append(",".join(emp_data))
        with open(EmployeeManager.FILE_NAME, "w") as file:
            file.write("\n".join(employees) + "\n")
        print("Employee updated." if updated else "Employee not found.")

    @staticmethod
    def delete_employee(employee_id):
        employees = []
        deleted = False
        with open(EmployeeManager.FILE_NAME, "r") as file:
            for line in file:
                if not line.startswith(str(employee_id) + ","):
                    employees.append(line.strip())
                else:
                    deleted = True
        with open(EmployeeManager.FILE_NAME, "w") as file:
            file.write("\n".join(employees) + "\n")
        print("Employee deleted." if deleted else "Employee not found.")

# ================== Word Frequency Counter ==================
def word_frequency_counter(file_name="sample.txt", top_n=5):
    if not os.path.exists(file_name):
        text = input("Enter text to create the file: ")
        with open(file_name, "w") as file:
            file.write(text)
    with open(file_name, "r") as file:
        text = file.read().lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_counts = collections.Counter(words)
    total_words = sum(word_counts.values())
    top_words = word_counts.most_common(top_n)
    print(f"Total words: {total_words}")
    print("Top words:")
    for word, count in top_words:
        print(f"{word} - {count} times")
    with open("word_count_report.txt", "w") as report:
        report.write(f"Word Count Report\nTotal Words: {total_words}\nTop {top_n} Words:\n")
        for word, count in top_words:
            report.write(f"{word} - {count}\n")

# ================== Menu System ==================
def main():
    while True:
        print("\nEmployee Manager Menu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Word Frequency Counter")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = input("Enter Salary: ")
            EmployeeManager.add_employee(emp_id, name, position, salary)
        elif choice == "2":
            EmployeeManager.view_employees()
        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            EmployeeManager.search_employee(emp_id)
        elif choice == "4":
            emp_id = input("Enter Employee ID: ")
            name = input("New Name (press enter to keep unchanged): ") or None
            position = input("New Position (press enter to keep unchanged): ") or None
            salary = input("New Salary (press enter to keep unchanged): ") or None
            EmployeeManager.update_employee(emp_id, name, position, salary)
        elif choice == "5":
            emp_id = input("Enter Employee ID: ")
            EmployeeManager.delete_employee(emp_id)
        elif choice == "6":
            top_n = int(input("Enter number of top words to display: "))
            word_frequency_counter(top_n=top_n)
        elif choice == "7":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
