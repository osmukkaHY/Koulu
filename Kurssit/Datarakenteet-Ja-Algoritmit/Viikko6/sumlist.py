class SumList:
    def __init__(self):
        self.previous_sums = [0]

    def append(self, number):
        self.previous_sums.append(self.previous_sums[-1]+number)

    def sum(self, a, b):
        return self.previous_sums[b+1] - self.previous_sums[a]

