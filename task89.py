user = {"name": "sergii", "age": 100500, "country": "Ukraine"}

key = input("Введіть ім'я ключа ")
new_key = input("Введіть нове ім'я ключа ")

# your code goes here

if user.get(key) is None:
    print("Шуканого ключа немає")
else:
    user[new_key] = user[key]
    del user[key]
    print(user)
