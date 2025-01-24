#compound interest calculation

principal = 0
rate = 0
time = 0

while True:
    principal = float(input("Enter the principal amount: "))
    if principal < 0:
        print("The principal amount must be greater than zero.")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("The rate of interest must be greater than zero.")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("The time in years must be greater than zero.")
    else:
        break

amount = principal * pow((1 + rate / 100), time)

print(f'Balance after {time} yrs : {amount:.2f} $')

