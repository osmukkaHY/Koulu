def min_steps(x):
    if x == 1:
        return 0
    counts = [(0, -1), (1, 0)]

    for i in range(2, x+1):
        multiplication = counts[i // 2][1] if not i % 2 else -1
        addition = counts[i - 3][1] if x > 3 else -1
        if multiplication == -1 and addition == -1:
            counts.append((i, -1))
        elif multiplication == -1:
            counts.append((i, addition+1))
        elif addition == -1:
            counts.append((i, multiplication+1))
        else:
            counts.append((i, min(multiplication, addition)+1))
    return counts[-1][1]
                
