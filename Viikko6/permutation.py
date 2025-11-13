class PermutationTracker:
    def __init__(self):
        self.numbers = set()
        self.sum = 0
        self.max_number = 0
        self.number_count = 0
        self.has_duplicates = False

    def append(self, number):
        self.number_count += 1
        if number in self.numbers:
            self.has_duplicates = True
            return

        self.numbers.add(number)
        self.sum += number
        if number > self.max_number:
            self.max_number = number

    def check(self):
        if self.has_duplicates or self.max_number != self.number_count:
            return False

        expected_sum = self.number_count * (self.number_count + 1) / 2
        return self.sum == expected_sum

