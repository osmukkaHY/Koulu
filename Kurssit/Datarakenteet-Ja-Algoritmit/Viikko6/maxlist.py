class MaxList:
    def __init__(self):
        self._list = []
        self._max_number = 0

    def append(self, number):
        self._list.append(number)
        self._max_number = max(self._max_number, number)

    def max(self):
        return self._max_number

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8
