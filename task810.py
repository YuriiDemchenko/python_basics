last_name = input("Введіть прізвище ")
name = input("Введіть ім'я ")
second_name = input("Введіть по батькові ")

# your code goes here
if len(last_name) < 1 or len(name) < 1 or len(second_name) < 1:
    print("Не введений ключовий параметр")
else:
    formatted_name = name[0:1]
    formatted_second_name = second_name[0:1]
    print(f"{last_name} {formatted_name}.{formatted_second_name}.")
