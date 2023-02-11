miles = float(input("Введіть кількість миль"))

# your code goes here
def convert_miles_to_km(x):
    result = x * 1.6
    return round(result, 2)

print(convert_miles_to_km(miles))