countries = {"Ukraine", "USA", "Poland", "Norway", "Dutch"}
add_countries = {"Poland", "Germany", "Dutch"}
countries.add("UK")
countries.add("China")
countries.discard("China")
new_list = countries - add_countries
for i in new_list:
    print(i)
