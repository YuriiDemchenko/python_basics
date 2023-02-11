input_database_name = "Зарплата"
input_command_to_execute = "Видати 100500ГРН Кожному"


class Database:
    # your code goes here
    executed_commands = []

    def __init__(self, database_name):
        self.database_name = database_name
        self.connected_to_database = False

    @staticmethod
    def to_lower(str):
        prepared_str = str.lower()
        return prepared_str

    @classmethod
    def add_to_executed_commands(cls, command):
        cls.command = command
        cls.executed_commands.append(command)

    def connect_to_database(self):
        self.connected_to_database = True
        print("Під'єднано до бази даних")

    def execute_command(self, command):
        self.command = command
        print(self.command)
        self.executed_commands.append(command)


db = Database(input_database_name)
print(db.database_name)
print(db.connected_to_database)

db.connect_to_database()
print(db.connected_to_database)
print(Database.executed_commands)

lower_command = Database.to_lower(input_command_to_execute)
db.execute_command(lower_command)
print(Database.executed_commands)
