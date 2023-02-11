class shopWorker:
    count_workers = 0

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        shopWorker.count_workers += 1
        self.id = shopWorker.count_workers

    def add_year(self, year):
        self.age += year

    def __str__(self):
        str_out = "Worker " + str(self.id) + ": " + self.name + " " + str(self.age)
        str_out += " Total workers: " + str(shopWorker.count_workers)
        return str_out

    @staticmethod
    def info():
        print("Total workers", shopWorker.count_workers)

    @classmethod
    def naming_shop(cls, name):
        cls.name_shop = name
        return cls.name_shop


shopWorker.info()

# print(shopWorker.count_workers)

worker_one = shopWorker("ivan", 25)
print(worker_one)

worker_two = shopWorker("Petro", 32)
print(worker_two)

shopWorker.info()
print(worker_one.naming_shop("Vasya"))
print(shopWorker.name_shop)

# print("Worker1: ", worker_one.name, " Age: ", worker_one.age)
# print("Total workers: ", worker_one.count_workers)
# worker_one.add_year(25)
# print("Worker1: ", worker_one.name, " Age: ", worker_one.age)
# print("Total workers: ", worker_one.count_workers)

# worker_two = shopWorker("Petro", 42)

# print("Worker2: ", worker_two.name, " Age: ", worker_two.age)
# print("Total workers: ", worker_two.count_workers)

# worker_three = shopWorker()

# print(worker_three.name, worker_three.age)
# print(worker_three.count_workers)
