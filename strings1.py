user = {"name": "Shiroki", "surname": "Mirukami", "age": "1050", "prof": "dumb"}

formatted_string = "His name is {} {} and he's {} old working {}"
print(formatted_string.format(user["name"], user["surname"], user["age"], user["prof"]))
test_text = "TEST here"
mes = f"test message {test_text}"
print(mes)
