def max_list(mas):
    max = mas[0]

    for i in mas:
        if max < i:
            max = i

    return max


def positive_count(mas):
    number = 0
    for i in mas:
        if i > 0:
            number += i

    return number


def average_temp(mas):
    s = 0
    for i in mas:
        s = s + i

    return s / len(mas)


tempterature = [3, 1, 2, 55, -3, -10, 5, -25]
print(max_list(tempterature))
