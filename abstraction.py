from abc import ABC, abstractmethod


class Parent:
    @abstractmethod
    def operation(self):
        pass


class Addition(Parent):
    def __init__(self):
        self.x = 5
        self.y = 10

    def operation(self):
        return self.x + self.y


sum = Addition()
sum.x = 7
sum.y = 1
# print(sum.operation())
print('{} + {} = 12'.format(Addition().x, sum.x))
