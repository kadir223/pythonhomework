def factor(num):
    for i in range(1,num+1):
        if num % i == 0:
            print(f"{i} is factor of {num}")
number=int(input("Enter number to find factor: "))
if number<0:
    print("Factor cannot be negative")
else:

    factor(number)
