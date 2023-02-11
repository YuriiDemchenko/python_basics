number = int(input("Введіть число "))
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# your code goes here
for i in a:
    if number == i:
        result = "Введене число - існує"
        break
    else:
        result = "Введене число - не існує"
print(result)
