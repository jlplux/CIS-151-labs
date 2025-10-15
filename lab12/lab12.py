
# takes one input parameter string_param
#
# string_param consists of words seperated by a space
#
# returns a list of strings, each item in the list is a word from string_param
#
# for example
#
# string_param = 'one two three' returns ['one', 'two', 'three']
#
# string_param = 'word' returns ['word']

def get_list_of_words(string_param: str):
    return string_param.split()


# takes one input parameter, list_param
#
# list_param is a list of strings
#
# returns a string which is all the items in list_param concatenated together, with a space in between
#
# for example
#
# list_param = ['one', 'two', 'three'] returns 'one two three'
#
# list_param = ['word'] returns 'word'

def make_sentence(list_param: list[str]):
    return " ".join(list_param)



# takes one input parameter string_param
#
# string param is a series of words separated by spaces
#
# returns a string with all the words from string_param but with the order reversed
#
# for example:
#
# string_param = 'alice loves bob' returns 'bob loves alice'
#
# string_param = 'one two three four' returns 'four three two one'

def reverse_words(string_param: str) -> str:
    l2 = string_param.split()
    l3 = (l2[::-1])
    return ' '.join(l3)

# takes one input parameter p1, an int
#
# returns how many times p1 can be integer divided by 2 before the result is 0
#
# for example, if p1=4, 5, 6, or 7, the answer should be 2.
#
# if p1=8, 9, 10, 11, 12, 13, 14, or 15, the answer should be 3.
def floor_log_base_2(p1: int) -> int:
    count = 0
    while p1 >= 1:
        p1 //= 2
        if p1 > 0:
            count += 1
    return count





def next_char(p1: str) -> str:
    if len(p1) != 1 or not p1.islower():
        return p1

    val = ord(p1) + 1
    if val > ord("z"):
        val -= 26
    return chr(val)

# takes one input param p1, a lowercase, one character string from a-z
#
# returns the next vowel in the alphabet
#
# In other words:
#
#    if p1 is a, returns a
#
#    if p1 is b, c, d or e, returns e
#
#    if p1 is e, f, g, h or i, returns i
#
#    if p1 is j, k, l, m, n or o, returns o
#
#    if p1 is p, q, r, s, t, or u, returns u
#
#    if p1 is v, w, x, y, or z, returns a
#
# hint: try using the included function next_char in a while loop


def next_vowel(p1: str) -> str:
    vowels = "aeiou"
    while p1 not in vowels:
        p1 = next_char(p1)
    return p1