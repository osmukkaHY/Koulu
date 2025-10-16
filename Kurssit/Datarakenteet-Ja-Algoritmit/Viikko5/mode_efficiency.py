import random
import time

def find_mode(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode

def find_mode_sorted(numbers):
    ordered = sorted(numbers)
    max_count = 0
    current_number = ordered[0]
    count = 0

    for n in ordered:
        if n == current_number:
            count += 1
        else:
            max_count = max(count, max_count)
            current_number = 1
            count = 1

    return max(count, max_count)


l = [random.randint(1, 1001) for x in range(10**7)]

t = time.time()
find_mode(l)
print(time.time()-t)

t = time.time()
find_mode_sorted(l)
print(time.time()-t)



