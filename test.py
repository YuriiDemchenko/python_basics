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

# Creating a list of 20 unique random numbers between 1 and 100
i = random.sample(range(1, 101), 20)
print(i)

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

lst = [1, 3, 15, -2, -9, 3, -5, -10, 0, -1, 10, 4, -7, 6, -12]
mx = max(lst)
mn = min(lst)
print(f"{lst},max:{mx}, min:{mn} ")
lst.remove(mx)
lst.remove(mn)
print(lst)


pupil_list = [180, 159, 162, 171, 169, 165, 172]
del pupil_list[1]
pupil_list.remove(165)
print(pupil_list)

# This code modifies each number in the list by subtracting 20
# from it and then multiplying it by the last number in the list.
random_list = [180, 159, 162, 171, 169, 165, 172]
for num in random_list:
    random_list[random_list.index(num)] = (num - 20) * random_list[-1]
print(random_list)

arr = [180, 159, 162, 171, 169, 165, 172]
max_index = arr.index(max(arr))
arr[1], arr[4] = arr[4], arr[1]
arr[2], arr[max_index] = arr[max_index], arr[2]
print(arr)


word = "Appreciative"
half_word = word[: len(word) // 2]
print(half_word)

word = "информатика"
print(word[2:7], word[7:10], word[::-1])

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
sentences = text.split(". ")
print(len(sentences), sentences)


text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
print(text.replace("o", "a"))


# palindrome check
def isPalindrome(s):
    return s == s[::-1]


s1 = "АРГЕНТИНА МАНИТ НЕГРА"
s2 = "ПОТ КАК ПОТОП"
s3 = "А РОЗА УПАЛА НА ЛАПУ АЗОРА"

print(
    isPalindrome(s1.replace(" ", "")),
    isPalindrome(s2.replace(" ", "")),
    isPalindrome(s3.replace(" ", "")),
)
