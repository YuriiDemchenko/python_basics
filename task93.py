wheels_count = int(input("Введіть кількість коліс "))
sits = int(input("Введіть кількість місць "))
guns_count = int(input("Введіть кількість зброї "))


class Banderomobil:
    # your code goes here
    wheels = wheels_count
    sit = sits
    guns = guns_count
    cars_count = 0

    def __init__(self, wheels, sit, guns):
        self.wheels_count = wheels
        self.sits = sit
        self.guns_count = guns
        Banderomobil.cars_count += 1

    def print_info(self):
        print(
            "Бандеромобіль на {} колесах, призначений для {} людей і {} стволів".format(
                self.wheels_count, self.sits, self.guns_count
            )
        )


car1 = Banderomobil(wheels_count, sits, guns_count)
car1.print_info()
print(car1.cars_count)

car2 = Banderomobil(wheels_count + 1, sits + 1, guns_count + 1)
car2.print_info()
print(car2.cars_count)
