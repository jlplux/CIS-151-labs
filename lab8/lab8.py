def magic_index(p1: list) -> int:
    for item in range(len(p1)):
        value = p1[item]
        if value == item:
            return item
    return -1


    return -1



def longer_than(plist: list, p2: str):
    for x in plist:
        if len(x) > len(p2):
            return x
    return ""


def num_longer_than(plist: list, p2: str):
    count = 0
    for item in plist:
        if len(item) > len(p2):
            count = count + 1
    return count


def get_second_index(p1: str, p2: str) -> int:
    if p1.count(p2) > 1:
        first_index = p1.find(p2)
        second_index = p1.find(p2, first_index + 1)
        return second_index
    return -1


def get_third_index(p1: str, p2: str):
    if p1.count(p2) < 3:
        return -1
    first = p1.index(p2)
    second = p1.index(p2, first + 1)
    third = p1.index(p2, second + 1)
    return third
