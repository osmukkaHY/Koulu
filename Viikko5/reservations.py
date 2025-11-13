import random

def check_overlapping(reservations):
    ordered = sorted(reservations, key=lambda x: x[0])
    previous_pair = (0, 0)

    for pair in ordered:
        if previous_pair[1] >= pair[0]:
            return True
        previous_pair = pair

    return False

