# 1. Implement a function called 'sum_range' which:
#
#
#
# takes three input parameters plist, beg, and end
#
# plist is a list of ints, and beg and end are ints
#
# returns the sum of the items in plist from index = beg to index = end-1
#
# returns 0 if list_param is empty
#
# returns 0 if start is equal to end
#
# returns 0 if start is greater than end

def sum_range(plist: list, beg: int, end: int) -> int:
    if not plist:
        return 0
    if beg >= end:
        return 0
    return sum(plist[beg:end])


def every_other_item(plist: list) -> list:
    result = []
    for x in range(0,len(plist),2):
        result.append(plist[x])
    return result





def last_half(plist: list) -> list:
    n = len(plist)
    if n == 0:
        return []

    start_index = n // 2
    return plist[start_index:]


def last_half_backwards(plist: list) -> list:
    start = len(plist) // 2
    result = []
    for i in range(len(plist) - 1, start - 1, -1):
        result.append(plist[i])
    del plist[start:]
    return result


def selection_sort(plist: list) -> list:
    result = []
    while plist:
        smallest = min(plist)
        plist.remove(smallest)
        result.append(smallest)
    return result
