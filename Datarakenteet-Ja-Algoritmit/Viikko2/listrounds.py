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

