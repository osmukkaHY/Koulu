class RepeatList:
    def __init__(self):
        self._numbers = {}
        self._multiple_flag = False

    def append(self, number):
        self._numbers[number] = self._numbers[number] + 1 \
                                    if number in self._numbers \
                                    else 1
        if self._numbers[number] > 1:
            self._multiple_flag = True

    def repeat(self):
        return self._multiple_flag

