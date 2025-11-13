def create_distribution(string):
    substrings = set()
    lengths = {}

    for start in range(len(string)):
        for end in range(start,len(string)):
            substrings.add(string[start:end+1])

    for sl in [len(x) for x in substrings]:
        if sl in lengths:
            lengths[sl] += 1
        else:
            lengths[sl] = 1
    return lengths

