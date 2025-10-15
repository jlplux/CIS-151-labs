def test_if_true(p1: bool) -> bool:
    if p1 is True:
        return True
    else:
        return False


def test_if_empty(p1: str) -> bool:
    if len(p1) == 0:
        return True
    else:
        return False

def return_smaller_int(p1, p2: int) -> int:
    if p1 < p2:
        return p1
    else:
        return p2

def return_shorter_param(p1, p2: str) -> int:
    if len(p1) < len(p2):
        return p1
    else:
        return p2

def either_or_true(p1, p2: bool) -> bool:
    if p1 == p2:
        return False
    else:
        return True

