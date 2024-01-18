from math import ceil
import random

# Creating a list of lists
numbers = [[1, 2, 3], [4, 5, 6]]
# Concatenating the two lists in 'numbers'
# and storing the result in 'new_numbers'
new_numbers = numbers[0] + numbers[1]
print(new_numbers)

# Printing numbers from 2 to 20, five times
for i in range(5):
    print(" ".join(str(j) for j in range(2, 21)))

# Printing decreasing number of asterisks starting from 6
for i in range(6, 1, -1):
    print("* " * i)

# Printing numbers from 10 to 50, with each number repeated 'i' times
for i in range(1, 6):
    print((str(i * 10) + " ") * i)

# Printing numbers from 101 to 165 in groups of 5
for i in range(0, ceil((165 - 101) / 5)):
    for j in range(1, 6):
        print(101 + 5 * i + j, end=" ")
    print()

# Printing 10 random numbers between 100 and 200, three times
for i in range(0, 3):
    for j in range(1, 11):
        cost = random.randint(100, 200)
        print(cost, end=" ")
    print()

# Creating a list of 20 unique random numbers between 1 and 20
array = []
i = random.sample(range(1, 21), 20)
array.append(i)
print(array)

# Counting the number of positive and negative numbers in a list
result = {"Positive": 0, "Negative": 0}
numbers = [1, 3, -2, -4, 3, -5, 0, -1, 10, 4, -5, 6]
for num in numbers:
    if num < 0:
        result["Negative"] += 1
    if num > 0:
        result["Positive"] += 1
print(result)

# Creating a list of 10 random numbers between -5 and 10
# and filtering out the negative numbers
i = random.sample(range(-5, 10), 10)
print("Random numbers with negative values", i)
j = [x for x in i if x >= 0]
print("Positives only", j)
