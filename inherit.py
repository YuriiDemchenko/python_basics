class shopWorker:
    _count_workers = 0

    def __init__(self, name="", age=0):
        self.name = name
        self.__age = age
        self.setting_id()

    def setting_id(self):
        shopWorker._count_workers += 1
        self._id = shopWorker._count_workers

    def working(self):
        print("Working")

    def add_year(self):
        self.__age += 1

    def __str__(self):
        str_out = "Worker " + str(self._id) + ": " + self.name + " " + str(self.__age)
        str_out += " Total workers: " + str(shopWorker._count_workers)
        return str_out

    @staticmethod
    def info():
        print("Total workers", shopWorker._count_workers)

    @classmethod
    def naming_shop(cls, name):
        cls.name_shop = name
        return cls.name_shop

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age
        if new_age < 0:
            new_age = -new_age
        self.__age = new_age


class Seller(shopWorker):
    def __init__(self, name="", age=0, cash=0):
        super().__init__(name, age)
        self.cash = cash

    def __str__(self):
        return super().__str__() + " Working with cash " + str(self.cash)

    def working(self):
        print("Serving customers")


# shopWorker.info()
worker_one = shopWorker("Ivan", 25)
print(worker_one)
print(worker_one.working())

print(worker_one.get_age())
worker_one.set_age(-44)
print(worker_one.get_age())

seller1 = Seller("Oksana", 42, 45556.5)
print(seller1)
print(seller1.working())

seller2 = Seller("Marusya", 33, 5552.0)
print(seller2)
print(seller2.working())

print(Seller._count_workers)
