class TaskScheduler:
    tasks = []

    @staticmethod
    def addTask(task):
        TaskScheduler.tasks.append(task)
    
    @staticmethod
    def displayList():
        for task in TaskScheduler.tasks:
            print(task)