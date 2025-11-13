from time import time

if __name__ == '__main__':
    rounds = 1000
    n = 10 ** 5
    add_avg = 0
    remove_avg = 0
    numbers = []

    for r in range(rounds):
        start_time = time()
        for i in range(n):
            numbers.append(n)
        add_avg += time()-start_time

        start_time = time()
        for i in range(n):
            del numbers[-1]
        remove_avg += time()-start_time

    add_avg /= rounds
    remove_avg /= rounds
    print('Average time to append:', add_avg)
    print('Average time to remove:', remove_avg)


