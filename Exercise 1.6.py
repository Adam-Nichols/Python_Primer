interest_rate = float(input("Please enter your banks interest rate (as a percent): "))
initial_amount = float(input("Please enter your initial investment: "))
years = float(input("Please  enter the number of years you plan to save: "))

result = round(initial_amount*((1+(interest_rate/100))**years),1)

print("{:,}".format(result))