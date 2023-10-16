from math import ceil

# numbers = [[1, 2, 3], [4, 5, 6]]
# new_numbers = numbers[0] + numbers[1]
# print(new_numbers)

# for i in range(5):
#     print(" ".join(str(j) for j in range(2, 21)))

# for i in range(6, 1, -1):
#     print("* " * i)

# for i in range(1, 6):
#     print((str(i * 10) + " ") * i)

for i in range(0, ceil((165 - 101) / 5)):
    for j in range(1, 6):
        print(101 + 5 * i + j, end=" ")
    print()
