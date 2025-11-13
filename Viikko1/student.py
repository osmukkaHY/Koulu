def check_number(number):
    if number[0] != '0' or len(number) == 1 or len(number) > 9: return False

    number = list(number)
    coefficients    = [3, 7, 1]
    check_num       = int(number.pop(-1))
    raw_sum         = 0

    for i in range(len(number)):
        digit = int(number[i])
        raw_sum += coefficients[i % 3] * digit
    return False if (raw_sum + check_num) % 10 else True

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False
