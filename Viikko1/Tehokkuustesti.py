from random import randint
from time import time

# toteutus 1
def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# toteutus 2
def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__ == '__main__':
    test_list = [randint(1, 101) for x in range(10**7)]

    start_time = time()
    count_even1(test_list)
    print('Time for first implementation:', time() - start_time)

    start_time = time()
    count_even2(test_list)
    print('Time for second implementation:', time() - start_time)

