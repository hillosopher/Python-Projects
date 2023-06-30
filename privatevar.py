

class Private():
    def __init__(self):
        self._protected = 5
        self.__private = 10

    def getPrivate(self):
        print(self.__private)

    def setPrivate(self, int):
        self.__private = int


Private1 = Private()
Private1.getPrivate()
Private1.setPrivate(7)
Private1.getPrivate()
