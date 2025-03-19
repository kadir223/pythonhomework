def convert_cel_to_far(c):
    return round((c*9/5) + 32, 2)
def convert_far_to_cel(F):
    return round((F - 32) * 5/9,2)
F=int(input("Enter temperature in Fahrenheit: "))
print(f"{F} Fahnerheit is equal to {convert_far_to_cel(F) } celcius")
C=int(input("Enter temperature in Celsius: "))
print(f"{C} celcius is equal to {convert_cel_to_far(C)} fahrenheit")

