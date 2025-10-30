import itertools
import re

def create_words(word):
    words = []
    letters = set(list(word))

    for permutation in set(itertools.permutations(word)):
        duplicates = False
        for i in range(len(permutation)-1):
            if permutation[i] == permutation[i+1]:
                duplicates = True
                break
        if duplicates: continue
        words.append(''.join(permutation))
    return sorted(words)

if __name__ == "__main__":
    print(create_words("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create_words("aab")) # ['aba']
    print(create_words("aaab")) # []

    print(create_words("kala"))
    # ['akal', 'akla', 'alak', 'alka', 'kala', 'laka']

    print(create_words("syksy"))
    # ['ksysy', 'kysys', 'skysy', 'syksy', 'sykys', 'sysky', 
    #  'sysyk', 'yksys', 'ysksy', 'yskys', 'ysyks', 'ysysk']

    print(len(create_words("aybabtu"))) # 660
    print(len(create_words("abcdefgh"))) # 40320
