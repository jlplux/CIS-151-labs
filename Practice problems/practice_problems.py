# practice_problems.py

# -------------------------------
# Problem 1 – Count Vowels
# -------------------------------
def count_vowels(s: str) -> int:
    """
    Returns the number of vowels (a, e, i, o, u) in the string s.
    """
    y = 0
    for x in s:
        if x in "aeiouAEIOU":
            y += 1
    return y



# -------------------------------
# Problem 2 – Sum of Integers in a List
# -------------------------------
def sum_integers(lst: list) -> int:
    """
    Returns the sum of all integers in lst.
    """
    y = 0
    for x in lst:
        y += x
    return y




# -------------------------------
# Problem 3 – Remove Vowels from a String
# -------------------------------
def remove_vowels(s: str) -> str:
    """
    Returns the string s with all vowels removed.
    """
    y = ""
    for x in s:
        if x not in "aeiouAEIOU":
            y += x
    return y






# -------------------------------
# Problem 4 – Count Frequency of Words
# -------------------------------
def word_frequency(lst: list) -> dict:
    """
    Returns a dictionary with the count of each word in lst.
    """
    freq = {}
    for word in lst:
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq






# -------------------------------
# Problem 5 – Filter Even Numbers
# -------------------------------
def filter_even(lst: list) -> list:
    """
    Returns a list of all even numbers in lst.
    """
    new = []
    for x in lst:
        if x % 2 == 0:
            new.append(x)
    return new

