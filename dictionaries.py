countries = {"country": "Ukraine", "age": "100500", "proffesion": "tester"}
# for key in countries:
#    print(key, countries.get(key))

# key_list = countries.keys()
# print("age" in countries)
# print(key_list)
print(countries.get("age"))

countries["age"] = "505"
print(countries.get("age"))
