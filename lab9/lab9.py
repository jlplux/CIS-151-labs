def filter_strings(plist: list, pstr: str) -> list:
    result = []
    for string in plist:
        if string.startswith(pstr):
            result.append(string)
    return result




def first_name_first(p1: str) -> str:
    parts = p1.split(', ')
    last_name = parts[0]
    first_name = parts[1]
    return f"{first_name} {last_name}"





def last_name_first(p1: str) -> str:
    parts = p1.split()
    if len(parts) == 2:
        first, last = parts
        return last + ", " + first
    elif len(parts) == 3:
        first, middle, last = parts
        return last + ", " + first + " " + middle

def find_min(plist: list) -> int:
    smallest = plist[0]
    for num in plist:
        if num < smallest:
            smallest = num
    return smallest


#def



def two_smallest_ints(plist: int) -> int:
    plist.sort()
    return [plist[0], plist[1]]
