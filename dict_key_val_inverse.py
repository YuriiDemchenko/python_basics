# swapping places of keys and values
d1 = {1: "value1", 2: "value2"}
print("Before: ", d1)
inv_map = {}
for key in d1.keys():
    val = d1[key]
    inv_map[val] = key
d1 = inv_map
print("After: ", d1)
