def hash_value(string):
    A, M, D = 23, 2**32, 97
    hash = 0
    n = len(string)-1

    for i in string.encode('ascii'):
        hash += (i-D)*A**n
        n -= 1
    return hash % M

