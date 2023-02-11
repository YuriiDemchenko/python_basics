t = int(input("Enter temp: "))
if t <= 0:
    print("Лід")
elif t > 0 and t < 100:
    print("Вода")
else:
    print("Пара")