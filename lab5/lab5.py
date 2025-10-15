def right_justify(p1: str) -> str:
    if len(p1) > 3:
        return "---"
    elif len(p1) == 3:
        return p1
    elif len(p1) == 2:
        return " " + p1
    elif len(p1) == 1:
        return "  " + p1
    elif len(p1) == 0:
        return "   "



def is_vowel(p1: str) -> bool:
    if len(p1) > 1:
        return False
    if p1 not in ["a", "e", "i", "o", "u"]:
        return False
    if p1 in ["a", "e", "i", "o", "u"] and len(p1) == 1:
        return True
    return False


def fizzbuzz(p1: int) -> str:
    if (p1 % 5 == 0) and (p1 % 3 == 0):
        return "fizzbuzz"
    elif p1 % 3 == 0:
        return "fizz"
    elif p1 % 5 == 0:
        return "buzz"
    return ""



