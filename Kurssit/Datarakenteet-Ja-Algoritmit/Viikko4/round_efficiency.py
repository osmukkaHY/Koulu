import time
import random

l = [x+1 for x in range(10**7)]
random.shuffle(l)
print('Shuffled list 1')

def find_rounds(numbers):
    final_list = []
    number = 1

    while len(numbers):
        index = 0
        sublist = []
        while index < len(numbers):
            if numbers[index] == number:
                sublist.append(numbers.pop(index))
                number += 1
            else:
                index += 1
        final_list.append(sublist)

    return final_list

def count_rounds(numbers):
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

t = time.time()
find_rounds(l)
print('List implementation:', time.time()-t)

l = [x+1 for x in range(10**7)]
random.shuffle(l)
print('Shuffled list again')

t = time.time()
count_rounds(l)
print('Dictionary implementation:', time.time()-t)


