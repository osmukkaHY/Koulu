class ChangeList:
    def __init__(self):
        self._numbers = []
        self._change = 0

    def append(self, number):
        self._numbers.append((number, self._change))

    def get(self, index):
        return self._numbers[index][0] + (self._change - self._numbers[index][1])

    def change_all(self, amount):
        self._change += amount

