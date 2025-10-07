class PermutationTracker:
    def __init__(self):
        self._numbers_set       = set()
        self._numbers           = []
        self._is_permutation    = True

    def append(self, number):
        if number in self._numbers_set:
            self._is_permutation = False
            return

        self._numbers += [0 for x in range(number-len(self._numbers))]
        self._numbers[number-1] = number
        self._numbers_set.add(number)
        self._is_permutation = True if 0 not in self._numbers else False

    def check(self):
        return self._is_permutation


if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False


    tracker = PermutationTracker()
    total = 0
    for i in range(10**5):
        if i%2 == 0:
            tracker.append(i + 2)
        else:
            tracker.append(i)
        if tracker.check():
            total += 1
    print(total) # 50000
