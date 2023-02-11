class shopWorker:
    _count_workers = 0

    def __init__(self, name="", age=0):
        self.name = name
        self.__age = age
        self.setting_id()

    def setting_id(self):
        shopWorker._count_workers += 1
        self._id = shopWorker._count_workers

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


shopWorker.info()

worker_one = shopWorker("Ivan", 25)
print(worker_one.get_age())
worker_one.set_age(-44)
print(worker_one.get_age())
