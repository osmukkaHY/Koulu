def can_create(coins, target):
    if 1 in coins:
        return True
    results = {0: True, 1: False}

    for s in range(2, target+1):
        if s in coins:
            results[s] = True
            continue

        results[s] = False
        for coin in coins:
            if coin < s and results[s-coin]:
                results[s] = True
                break
    return results[target]

print(can_create([2, 4, 9], 30))
