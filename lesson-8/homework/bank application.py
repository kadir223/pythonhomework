import json
import random


class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}


class Bank:
    FILE_NAME = "accounts.json"

    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = random.randint(1000, 9999)
        while account_number in self.accounts:
            account_number = random.randint(1000, 9999)
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(f"Account Number: {account.account_number}\nName: {account.name}\nBalance: {account.balance}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
            self.save_to_file()
        else:
            print("Account not found.")

    def save_to_file(self):
        with open(self.FILE_NAME, "w") as file:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, file)

    def load_from_file(self):
        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)
                self.accounts = {int(acc_num): Account(**details) for acc_num, details in data.items()}
        except FileNotFoundError:
            self.accounts = {}


# Interactive Menu
def main():
    bank = Bank()

    while True:
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            acc_num = int(input("Enter your account number: "))
            bank.view_account(acc_num)

        elif choice == "3":
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)

        elif choice == "4":
            acc_num = int(input("Enter your account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
