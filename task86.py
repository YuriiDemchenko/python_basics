str_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

# your code goes here
user_input = input("What to delete? ")
str_set.discard(user_input)
print(str_set)
