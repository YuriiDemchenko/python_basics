number = int(input("Enter the number: "))
dict = {}
for i in range(0, number + 1):
    dict.update({i: i**2})

print(dict)
