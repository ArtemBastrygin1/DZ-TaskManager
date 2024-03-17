class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

    def info(self):
        return f'Title: {self.title}\nDescription: {self.description}'


class TaskManager:
    def __init__(self):
        self.__tasks = []

    def add_task(self, title, description):
        self.object = f'Title - {title}: Description - {description}'
        self.__tasks.append(self.object)

    @property
    def get_task(self):
        for i in self.__tasks:
            print(i)



obj1 = TaskManager()

obj1.add_task("Задача 1", "Описание задачи 1")
obj1.add_task("Задача 2", "Описание задачи 2")






