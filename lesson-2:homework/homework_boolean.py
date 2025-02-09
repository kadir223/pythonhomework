
# Q1
username = input("Enter your username: ")
password = input("Enter your password: ")

if username and password:
    print("Both are provided.")
else:
    print("cannot be empty.")

# Q2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("not equal.")

# Q3
num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("The number is positive and even.")
else:
    print("The number is negative or odd ")

# Q4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 != num2 and num2 != num3 and num1 != num3:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

# Q5
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2):
    print("Both strings have the same length.")
else:
    print("The strings have different lengths.")

# Q6
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")

# Q7
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 + num2 > 50.8:
    print("The sum is greater than 50.8.")
else:
    print("The sum is not greater than 50.8.")

# Q8
num = int(input("Enter a number: "))

if 10 <= num <= 20:
    print(f"{num} is between 10 and 20 (inclusive).")
else:
    print(f"{num} is not between 10 and 20.")
