class OccurrenceTracker:
    def __init__(self):
        self.numbers = {}
        self.number_counts = {}

    def append(self, number):
        # Handle old count.
        old_number_count = self.numbers[number] if number in self.numbers
        self.number_counts[old_number_count] -= 1
        if self.number_counts[old_number_count] == 0:
            del self.number_counts[old_number_count]

        # Add number to numbers.
        self.numbers[number] = 1 if number not in self.numbers else self.numbers[number] + 1

        # Handle new count.
        new_number_count = self.numbers[number]
        self.number_counts[new_number_count] = 1 if new_number_count not in self.number_counts else self.number_counts[new_number_count] + 1

    def count(self):
        return len(self.number_counts)

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3
