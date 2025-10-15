def is_vowel(param: str) -> bool:

   if (len(param) == 1):

       if param in "aeiou":

           return True

   return False



def filter_vowels(p1: str) -> str:
    result = ""
    for i in p1:
        if is_vowel(i) == True:
            result += i
        else:
            result += ""
    return result

def contains(plist: list, p2: int):
    for item in plist:
        if item == p2:
            return True
    return False




def index_of(plist: list, p2: int) -> int:
    for i in range(len(plist)):
        if plist[i] == p2:
            return i
    return -1



def get_login(first_name: str, last_name: str) -> str:
    return first_name[0] + last_name[:5]



def get_padded_login(first_name: str, last_name: str) -> str:
    login = get_login(first_name, last_name)
    if len(login) < 6:
        login = login + "0" * (6 - len(login))
    return login
