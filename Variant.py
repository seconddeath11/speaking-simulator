class Variant(object):
    def __init__(self, num, task1, task2, task3, task4):
        self.num = num
        self.task1 = task1
        self.task2 = task2
        self.task3 = task3
        self.task4 = task4

    def get_task(self, num):
        return {
            1: self.task1,
            2: self.task2,
            3: self.task3,
            4: self.task4
        }.get(num, 1)
