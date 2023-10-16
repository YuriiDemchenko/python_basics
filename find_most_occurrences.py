names = [
    "Igor",
    "Vasya",
    "Vania",
    "Sasha",
    "Valentin",
    "Vadik",
    "Vania",
    "Sasha",
    "Mykola",
    "Vania",
    "Sasha",
    "Sasha",
    "Igor",
    "Igor",
    "Vadik",
    "Vadik",
    "Vadik",
    "Vadik",
]
data = {}
for i in names:
    data[i] = names.count(i)

max_key = max(data, key=data.get)

print(
    f"Ім'я з найбільшою кількістю входжень: {max_key}, кількість входжень: {data[max_key]}"
)
