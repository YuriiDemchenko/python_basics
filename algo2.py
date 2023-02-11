count = float(input("Бажана кількість електро: "))
tarrif = 7.8
price = count * tarrif
print("Ціна заряджання: " , round(price, 2))

cash = float(input("Сума готівки: "))
if cash >= price:
    rest = cash - price
    print("Решта: ", round(rest, 2))
else:
    print("Not enough cash!")
if not(5>7 and 2>3):
    print("True")
else:
    print("False")