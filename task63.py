number = int(input("Введіть число "))
i = 0
while i <= number:
    pair_check = i % 2
    if pair_check == 0:         
        print(i ** 2)
    else:   
        print(i)
    i=i+1