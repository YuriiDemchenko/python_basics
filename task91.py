windows_count = int(input("Введіть кількість вікон "))
flors_count = int(input("Введіть кількість поверхів "))


class Building:
    windows_count
    flors_count

    def __init__(self, windows_count, flors_count):
        self.windows_count = windows_count
        self.flors_count = flors_count

    def __str__(self):
        str_out = str(self.total)
        return str_out


building = Building(windows_count, flors_count)
total = building.windows_count * building.flors_count
print("Загальна кількість вікон {}".format(total))
