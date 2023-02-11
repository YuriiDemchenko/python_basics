number = int(input("Введіть число "))

for i in range(1, number + 1):
    is_even_or_odd = i % 2
    if is_even_or_odd == 0:
        number = i**2
        print(number)
