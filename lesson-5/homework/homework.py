import statistics

def convert_cel_to_far(celsius):
    return round(celsius * 9/5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

# Task 1 Execution
def temperature_conversion():
    f = float(input("Enter a temperature in degrees F: "))
    print(f"{f} degrees F = {convert_far_to_cel(f)} degrees C")
    c = float(input("Enter a temperature in degrees C: "))
    print(f"{c} degrees C = {convert_cel_to_far(c)} degrees F")

def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

# Task 2 Execution
def investment_calculator():
    amount = float(input("Enter initial amount: "))
    rate = float(input("Enter annual rate (as decimal): "))
    years = int(input("Enter number of years: "))
    invest(amount, rate, years)

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

# Task 3 Execution
def factor_finder():
    num = int(input("Enter a positive integer: "))
    factors(num)

def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuition = [uni[2] for uni in universities]
    return students, tuition

def mean(values):
    return sum(values) / len(values)

def median(values):
    return statistics.median(values)

# Task 4 Execution
def university_stats():
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
    students, tuition = enrollment_stats(universities)
    print("******************************")
    print(f"Total students: {sum(students):,}")
    print(f"Total tuition: $ {sum(tuition):,}")
    print("")
    print(f"Student mean: {mean(students):,.2f}")
    print(f"Student median: {median(students):,.0f}")
    print("")
    print(f"Tuition mean: $ {mean(tuition):,.2f}")
    print(f"Tuition median: $ {median(tuition):,.0f}")
    print("******************************")

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Task 5 Execution
def prime_checker():
    num = int(input("Enter a number: "))
    print(f"{num} is prime: {is_prime(num)}")

