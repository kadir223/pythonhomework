#Question 1
number=float(input("enter a number: "))
print("rounded number is: ", round(number,2))

#Question 2
num1=float(input("enter a number: "))
num2=float(input("enter a number: "))
num3=float(input("enter a number: "))
print("the largest number is: ", max(num1,num2,num3))
print("the smallest number is: ", min(num1,num2,num3))
#Question 3
km=float(input("Enter kilometers: "))
m=km*1000
cm=m*100
print(f"The {km} kilometers is equal to {m} meters and {cm} centimeters.")
#Question 4
num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
devision=num1/num2
remainder=num1%num2
print("the remainder is: ", remainder)
print("the remainder is: ", devision)
#Question 5
celcius=float(input("Enter celcius: "))
F=celcius*1.8+32
print(f" The {celcius} celcius is equal to {F} Faranheit.")
#Question 6
num1=int(input("enter a number:"))
print("the last digit is:",num1%10)
#Question 7
num1=int(input())
if num1%2==0:
    print('even')
else:
    print('odd')