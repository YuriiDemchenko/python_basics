deposit_amount = float(input("Deposit sum: "))
annual_rate = float(input("Annual rate: "))
desired_amount = float(input("Desired amount: "))

deposit_period = 0

while deposit_amount < desired_amount:
    deposit_period = deposit_period + 1
    deposit_amount = deposit_amount + deposit_amount * (annual_rate / 100)
print("Expected deposit time: ", deposit_period, " years")