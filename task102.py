input_qa_name = "тестувальник андрій"
input_pm_name = "менеджер тарас"
input_qa_expected_action = "Знаходити помилки"
input_pm_expected_action = "Відправляти листи"
input_qa_task = "Протестувати нову функціональність"

# your code goes here


class User:
    def __init__(self, username, expected_action):
        self._username = username
        self._expected_action = expected_action

    def perform_action(self):
        self.search_words = ["Степан", "Нищити русню"]
        if any(x in self._expected_action for x in self.search_words):
            print("Степан виконує дію: 'Нищити русню'")
        else:
            print(f"{self._username} виконує дію: '{self._expected_action}'")

    def get_username(self):
        return self._username

    def set_username(self, value):
        self._username = value.title()


class QA(User):
    def __init__(self, username, expected_action):
        super().__init__(username, expected_action)
        self.tasks = []

    def set_task(self, task):
        self.tasks.append(task)


class Manager(User):
    def perform_action(self):
        print("Зайнятий. Напишіть мені листа з Вашим питанням")


qa = QA(input_qa_name, input_qa_expected_action)
print(qa.get_username())
qa.set_username(input_qa_name)
print(qa.get_username())
qa.perform_action()
print(qa.tasks)
qa.set_task(input_qa_task)
print(qa.tasks)

pm = Manager(input_pm_name, input_pm_expected_action)
print(pm.get_username())
pm.set_username(input_pm_name)
print(pm.get_username())
pm.perform_action()
