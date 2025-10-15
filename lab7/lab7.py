def get_item_at(p1: list, p2: int) -> int:
        if 0 <= p2 < len(p1):
            return p1[p2]
        else:
            return -1


def get_first_digit(p1: str) -> str:
    x = ""
    for index in range(len(p1)):
        char = p1[index]
        if char.isdigit():
            return char
    return x






def first_two_items(p1: list) -> list:
    if len(p1) >= 2:
        return p1[0:2]
    if len(p1) == 1:
        return p1
    if len(p1) == 0:
        return p1




def last_n_items(p1: list, p2: int) -> list:
    # p1 = [a,b,c,d,e,f,g]
    #p2=1
    # len(p1) = 7
    #
    if len(p1) >= p2:

        return p1[-p2:]
    else:
        return (p1)



