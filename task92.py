car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")


class Cars:
    # your code goes here
    list_of_cars = []

    def __init__(self, car1, car2, car3):
        self.list_of_cars.append(car1)
        self.list_of_cars.append(car2)
        self.list_of_cars.append(car3)


cars = Cars(car_1, car_2, car_3)
list_of_cars = cars.list_of_cars
separator = " та ".join(list_of_cars)
print("Список авто: {}".format(separator))
