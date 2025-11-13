def count_steps(numbers):
    steps = 0
    previous_index = 0

    for index in [x[0] for x in sorted([pair for pair in enumerate(numbers)], key=lambda x: x[1])]:
        steps += abs(index-previous_index)
        previous_index = index

    return steps

