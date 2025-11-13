def count_substrings(string):
    substrings = set()

    for start in range(len(string)):
        for end in range(start,len(string)):
            substrings.add(string[start:end+1])
    return len(substrings)

