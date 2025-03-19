def invest(amount,rate,year):
    for i in range(1,year+1):
        amount = amount * (1+rate)
        print(f"year {i}: ${amount:.2f}")
amount = float(input("Enter initial amount: "))
rate = float(input("Enter annual rate (as decimal): "))
years = int(input("Enter number of years: "))
invest(amount,rate,years)

