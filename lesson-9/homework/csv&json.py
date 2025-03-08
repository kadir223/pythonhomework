import csv
import json


# Task 1: Library Management System
class BookNotFoundException(Exception):
    pass


class BookAlreadyBorrowedException(Exception):
    pass


class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("This book is already borrowed.")
        book.is_borrowed = True
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if not book:
            raise BookNotFoundException("Book not found in library.")

        member.borrow_book(book)

    def return_book(self, member_name, book_title):
        member = next((m for m in self.members if m.name == member_name), None)
        book = next((b for b in self.books if b.title == book_title), None)

        if book and member:
            member.return_book(book)


# Task 2: Student Grades Management
def calculate_average_grades(input_file, output_file):
    grades = {}
    counts = {}

    with open(input_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row['Subject']
            grade = int(row['Grade'])
            if subject not in grades:
                grades[subject] = 0
                counts[subject] = 0
            grades[subject] += grade
            counts[subject] += 1

    averages = {subject: grades[subject] / counts[subject] for subject in grades}

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, avg in averages.items():
            writer.writerow([subject, avg])


# Task 3: JSON Handling
def load_tasks(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def save_tasks(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")


def task_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task['completed'])
    pending = total - completed
    avg_priority = sum(task['priority'] for task in tasks) / total
    print(f"Total Tasks: {total}, Completed: {completed}, Pending: {pending}, Avg Priority: {avg_priority:.2f}")


def convert_json_to_csv(json_file, csv_file):
    tasks = load_tasks(json_file)
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task['id'], task['task'], task['completed'], task['priority']])
