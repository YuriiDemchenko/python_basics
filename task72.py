number = int(input("Введіть число"))

# your code goes here
def is_even_or_odd(x):
    number = x % 2
    if number == 0: 
        x = str(x)
        result = "число "+ x + " парне"
    else:
        x = str(x)
        result = "число "+ x +" непарне"
    return result
print(is_even_or_odd(number))