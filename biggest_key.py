# find 3 biggest keys
find_the_biggest = {"a": 1500, "b": 58374, "c": 560, "d": 1400, "e": 51874, "f": 20}
sorted_numbers = sorted(find_the_biggest.items(), key=lambda x: x[1], reverse=True)
for i in sorted_numbers[0:3]:
    print(i[0])
