def count_rounds(numbers):
    rounds = 0
    gathered_numbers = set()

    for n in numbers:
        if n-1 not in gathered_numbers:
            rounds += 1
        gathered_numbers.add(n)

    return rounds

